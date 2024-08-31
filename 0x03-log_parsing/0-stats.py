#!/usr/bin/python3
import sys

def print_stats(total_size, status_codes):
    """Prints the accumulated metrics."""
    print(f"File size: {total_size}")
    for code in sorted(status_codes):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")

# Initialize variables
total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

try:
    for line in sys.stdin:
        parts = line.split()
        
        # Validate the format of the line
        if len(parts) > 6:
            # Extract the necessary components
            ip = parts[0]
            status_code = parts[-2]
            file_size = parts[-1]

            # Update total file size
            try:
                total_size += int(file_size)
            except ValueError:
                continue

            # Update status code counts
            try:
                if int(status_code) in status_codes:
                    status_codes[int(status_code)] += 1
            except ValueError:
                continue

            line_count += 1

            # Print stats after every 10 lines
            if line_count % 10 == 0:
                print_stats(total_size, status_codes)

except KeyboardInterrupt:
    print_stats(total_size, status_codes)
    raise

# Print final stats after EOF
print_stats(total_size, status_codes)
