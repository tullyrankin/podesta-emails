"""Podesta Emails."""

from __future__ import print_function

import lxml.html
import re
import requests


def get_twitter_description(html):
    """Return value of content attribute in meta twitter:description."""
    pattern = re.compile('<meta property="twitter:description" content="([^"]*)"')
    match = pattern.search(html)
    if match:
        return match.group(1)

def get_from_addr(s):
    """Return From Address."""
    try:
        return re.search('From: (.*)\n', s, re.MULTILINE).group(1)
    except:
        return None

def get_to_addr(s):
    """Return To Address."""
    try:
        return re.search('To: (.*)\n', s, re.MULTILINE).group(1)
    except:
        return None

def get_email_body(html):
    """Return the body of the email."""
    try:
        doc = lxml.html.fromstring(html)
        body_text = doc.xpath('//div[@class="email-content"]')[0].text_content()
        body_text = cleanup_spaces(body_text)
        return body_text
    except:
        return None

def get_html(email_id):
    """Return HTML for the given email_id."""
    url = "https://wikileaks.com/podesta-emails/emailid/{0}"
    resp = requests.get(url.format(email_id))
    return resp.text

def cleanup_spaces(s):
    """Replaces consecutive spaces with single space."""
    return "\n".join([s2.strip() for s2 in s.split('\n')])


def print_email(email):
    """Print the To, From, and Body content of email."""
    print('To:', get_to_addr(email))
    print('From:', get_from_addr(email))


class TerminalRunner(object):
    """Interactive command line email viewer."""

    def __init__(self, email_id=1):
        self._current = email_id

    def __enter__(self):
        while True:
            html = get_html(self._current)
            email = get_twitter_description(html)
            email_body = get_email_body(html)

            if email:
                print_email(email)

            if email_body:
                print("-" * 50)
                print(email_body)
                print("-" * 50)

            action = self._get_action()
            if action == 'p':
                self._current = self._current - 1
            if action == 'n':
                self._current = self._current + 1
            if action == 'x':
                break

    def _get_action(self):
        options = {
            "p": "Previous",
            "n": "Next",
            "x": "Exit"
        }
        while True:
            action = input('>>>')
            if action in options:
                return action
            else:
                print("Invalid Option. Options {0}".format(options))

    def __exit__(self, *args):
        print('Exiting...')


def main():
    """Run the application."""
    import sys
    email_ids = sys.argv[1:]
    for email_id in email_ids:
        html = get_html(email_id)
        email = get_twitter_description(html)
        email_body = get_email_body(html)
        if email:
            print_email(email)
            print(email_body)

if __name__ == '__main__':
    main()
