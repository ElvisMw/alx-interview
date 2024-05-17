#!/usr/bin/python3

"""Script for collecting statistics from Apache access logs.

The script reads input from stdin and collects statistics
on the file size and response status codes from the logs.
It prints the statistics every 10 lines read or upon receiving
a keyboard interruption (CTRL + C).
"""

import sys
import signal
import re

# Dictionary to store response counts
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

# Total size of all files in bytes
total_size = 0

# Total number of lines read
line_count = 0

def print_summary():
    """Print the summary of the collected metrics."""
    print(f"File size: {total_size}")
    for status_code, count in sorted(response_counts.items()):
        if count > 0:
            print(f"{status_code}: {count}")

def handle_interrupt(signum, frame):
    """Handle keyboard interruption (CTRL + C)."""
    print_summary()
    sys.exit(0)

# Register the signal handler for SIGINT (CTRL + C)
signal.signal(signal.SIGINT, handle_interrupt)

try:
    # Read the input from stdin line by line
    for line in sys.stdin:
        line_count += 1

        # Parse the log line and update the statistics
        match = re.match(
            r'^\S+ - \[\S+\] "GET /projects/260 HTTP/1.1" (\d+) (\d+)$',
            line
        )
        if match:
            status_code, file_size = match.groups()
            total_size += int(file_size)
            if status_code in response_counts:
                response_counts[status_code] += 1

        if line_count % 10 == 0:
            print_summary()

    print_summary()

except KeyboardInterrupt:
    handle_interrupt()

except Exception as e:
    print(f"Error: {e}", file=sys.stderr)
    sys.exit(1)
