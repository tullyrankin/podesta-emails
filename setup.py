from setuptools import setup

setup(
    name="Podesta Emails",
    version="0.0.1",
    description="WikiLeaks Podesta Emails",
    author="Tully Rankin",
    author_email="tullyrankin@gmail.com",
    url="https://github.com/tullyrankin/podesta-emails",
    packages=[
        'podesta_emails',
    ],
    package_dir={'podesta_emails': 'podesta_emails'},
    include_package_data=True,
    entry_points={"console_scripts": [
        "podesta-emails = podesta_emails.cli:main",
    ]},
    install_requires=[
        "lxml==3.6.4",
        "requests==2.11.1"
    ],
    license='BSD',
    zip_safe=False,
    keywords="podesta emails wikileaks",
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
)
