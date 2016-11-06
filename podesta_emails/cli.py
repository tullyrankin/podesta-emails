"""Command line interface."""

import podesta_emails.podesta as podesta


def main():
    """Run the application."""
    try:
        email_id = int(input('Email ID to read: '))
    except:
        email_id = 1

    with podesta.TerminalRunner(email_id=email_id) as t:
        pass


if __name__ == "__main__":
    main()
