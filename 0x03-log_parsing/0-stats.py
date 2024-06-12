#!/usr/bin/python3
"""Script that reads stdin line by line and computes metrics."""

import sys
import signal

file_size = 0
status_counts = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0
    }
line_count = 0


def print_stats():
    """Prints the statistics collected so far."""
    print("File size: {}".format(file_size))
    for status_code in sorted(status_counts.keys()):
        if status_counts[status_code] > 0:
            print("{}: {}".format(status_code, status_counts[status_code]))


def signal_handler(sig, frame):
    """Handles the keyboard interruption signal to print stats."""
    print_stats()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        line_count += 1
        parts = line.split()

        if len(parts) < 7:
            continue

        try:
            file_size += int(parts[-1])
        except ValueError:
            continue

        try:
            status_code = int(parts[-2])
            if status_code in status_counts:
                status_counts[status_code] += 1
        except ValueError:
            continue

        if line_count % 10 == 0:
            print_stats()
except Exception:
    pass
finally:
    print_stats()
