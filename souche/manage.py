#!/usr/bin/env python
import os
import sys


if __name__ == "__main__":
    project_path = os.path.abspath(
                os.path.join(os.path.dirname(__file__), os.pardir))
    if project_path not in sys.path:
        sys.path.append(project_path)
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
