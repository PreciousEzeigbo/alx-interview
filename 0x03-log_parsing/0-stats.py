#!/usr/bin/python3
import sys
import signal

# Dictionary to keep count of each status code
status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
# Total file size
total_file_size = 0
# Line counter
line_counter = 0

def print_stats():
    """Prints the current statistics."""
    print("File size:", total_file_size)
    for code in sorted(status_counts):
        if status_counts[code] > 0:
            print(f"{code}: {status_counts[code]}")

def handle_interrupt(signal, frame):
    """Handle keyboard interruption and print final stats."""
    print_stats()
    sys.exit(0)

# Register the signal handler
signal.signal(signal.SIGINT, handle_interrupt)

try:
    for line in sys.stdin:
        line = line.strip()
        # Validate format
        parts = line.split()
        if len(parts) != 7:
            continue
        
        # Extract and validate fields
        try:
            ip = parts[0]
            date = parts[3] + ' ' + parts[4]
            request = parts[5] + ' ' + parts[6]
            status_code = int(parts[6])
            file_size = int(parts[7])
        except (IndexError, ValueError):
            continue

        # Update the total file size
        total_file_size += file_size

        # Update the count of status codes
        if status_code in status_counts:
            status_counts[status_code] += 1

        # Update the line counter
        line_counter += 1

        # Print stats every 10 lines
        if line_counter % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    # Print stats when interrupted
    print_stats()
    sys.exit(0)
