#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import traceback


def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "octofit_tracker.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    try:
        print("Executing command:", sys.argv)
        execute_from_command_line(sys.argv)
    except SystemExit as e:
        print("SystemExit occurred with code:", e.code)
        traceback.print_exc()
        raise
    except Exception as e:
        print("An unexpected error occurred:", str(e))
        traceback.print_exc()
        raise


if __name__ == "__main__":
    main()
