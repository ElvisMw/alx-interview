#!/usr/bin/python3

"""
Script to summarize an Nginx access log file.

It reads from stdin and prints a summary of the data to stdout.

The summary includes the total file size and the number of requests for each
HTTP response code.

Usage:

    python3 summary.py < access.log
"""

import sys
import signal
import re


def print_summary(response_counts, total_size):
    """Print a summary of the data.

    Args:
        response_counts: A dictionary of HTTP response counts.
        total_size: The total file size.
    """
    print(f"File size: {total_size}")
    for code, count in sorted(response_counts.items(),
                              key=lambda x: int(x[0])):
        if count:
            print(f"{code}: {count}")


def handle_interrupt(signum, frame):
    """Handle interrupt signal (CTRL + C)."""
    print_summary(response_counts, total_size)
    sys.exit(0)


""" Initialize variables """
response_counts = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}
total_size = 0
line_count = 0

""" Set up signal handler for interrupt (CTRL + C) """
signal.signal(signal.SIGINT, handle_interrupt)

try:
    for line in sys.stdin:
        line_count += 1
        if line_count % 10 == 0:
            print_summary(response_counts, total_size)

        """ Parse the line using regex """
        match = re.match(
            r'^\S+ - \[\S+\] "GET /projects/260 HTTP/1.1" (\d+) (\d+)$', line
        )
        if match:
            status_code, file_size = match.groups()
            total_size += int(file_size)
            if status_code in response_counts:
                response_counts[status_code] += 1

    """ Print the final summary """
    print_summary(response_counts, total_size)

except KeyboardInterrupt:
    """ Handle keyboard interruption (CTRL + C) """
    print_summary(response_counts, total_size)
    sys.exit(0)
