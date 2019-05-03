#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Trial.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        #THe above import my fail for some other reason. Ensure that the
        #issue really is that django is missing to avoid making other
        #exceptions in python 2.
        try:
            import django
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
