#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    import socket
    hostname = socket.gethostname()
    SETTINGS_FILE = {
        "gongpingjia": "souche.settings.product",
        "eyelee": "souche.settings.test"
    }
    settings_file = SETTINGS_FILE.get(hostname, "souche.settings.dev")
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings_file)

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
