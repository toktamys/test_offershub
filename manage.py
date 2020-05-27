#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

from django.conf import settings


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'asana_offershub.local_settings')
    try:
        settings.PERSONAL_ACCESS_TOKEN
    except Exception as e:
        raise ImportError(
            "PERSONAL_ACCESS_TOKEN didn't provided"
        ) from e

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
