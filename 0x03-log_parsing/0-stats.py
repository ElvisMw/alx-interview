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


def print_summary(response_counts, total_size):
    """Print a summary of the data.

    Args:
        response_counts: A dictionary of HTTP response counts.
        total_size: The total  file size.
    """
    print(f"File size: {total_size}")
    print("Total: {}".format(sum(response_counts.values())))
    for x, y in sorted(response_counts.items()):
        if y != 0:
            print("{}: {}".format(x, y))


total_size = 0
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

try:
    for line in sys.stdin:
        line_data = line.split()
        size, status_code = line_data[::-1]
        total_size += int(size)

        if status_code in response_counts:
            response_counts[status_code] += 1

        if response_counts["200"] == 10:
            print_summary(response_counts, total_size)
            total_size = 0
            for x in response_counts:
                response_counts[x] = 0

finally:
    print_summary(response_counts, total_size)
