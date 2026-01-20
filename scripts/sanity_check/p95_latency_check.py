##################################################################################################################
# How to run:  ./p95_latency_check.py [path]/[filename.ext] (/logs/2024/06/15/10.0.10.10_app_0001.log)           #
##################################################################################################################

import re # Provides regular expression support for pattern matching and parsing text (used to extract fields from log lines)
import math # Provides mathematical functions such as ceil(), which is used to compute the 95th percentile index

# This code is designed to be dynamic, allowing us to run sanity checks across multiple log paths and files.

LOG_FILE = "./logs/2024/06/15/10.0.10.10_app_0001.log" # STATIC [PATH]/[FILE]. will change to dynamic functionality on version 0.2
# We should be able to dynamically adjust the value based on the acceptance criteria, or override default and standard settings whenever needed.
P95_TARGET_MS = 400 # will change to dynamic functionality on version 0.2


# Regular Expression (RegEx) for extracting timestamp, user_id, latency, and status. This approach provides flexibility for future log mapping, as log formats may vary across sources.
LOG_PATTERN = re.compile(
    r"^(?P<timestamp>\S+)\s+.*user_id=(?P<user_id>\d+)\s+"
    r"latency_ms=(?P<latency>\d+)\s+status=(?P<status>\d+)"
)

def calculate_p95(latencies):
    # latencies: list of request latencies in milliseconds
    # This function calculates the 95th percentile (P95),
    # meaning 95% of requests completed at or below this value
    if not latencies:
        return None  # No data available, cannot compute P95
    latencies.sort() # Sort latencies in ascending order
    index = math.ceil(0.95 * len(latencies)) - 1  # Compute index for the 95th percentile (ceil for conservative SRE reporting)
    return latencies[index] # Return the latency value at the P95 position

def main():
    requests = [] # Initialize an empty list to store parsed request data from the log file

    with open(LOG_FILE, "r") as f:
        for line in f:
            match = LOG_PATTERN.search(line) # Apply the regular expression pattern to extract fields from the log line
            if not match:
                continue  # Skip the line if it does not match the expected log format

            try:
                requests.append({
                    "timestamp": match.group("timestamp"),    # Extract and store the timestamp from the log line
                    "user_id": match.group("user_id"),        # Extract and store the user ID from the log line
                    "latency": int(match.group("latency")),   # Extract latency, convert it to an integer, and store it
                    "status": int(match.group("status")),     # Extract HTTP status code, convert it to an integer, and store it

                })
            except ValueError:
                continue # Skip this entry if latency or status cannot be converted to integers

    latencies = [r["latency"] for r in requests]     # Create a list of latency values from all parsed requests
    p95 = calculate_p95(latencies)                   # Calculate the 95th percentile (P95) latency from the latency list

    # This code will generate a summary report that will shows the list of important items.
    print("\n=== Load Test Latency Sanity Report ===")
    print(f"Total requests found: {len(requests)}")            # Display the total number of valid requests processed

    if p95 is not None:                                        # Check if P95 latency was successfully calculated
        print(f"P95 latency: {p95} ms")
        if p95 < P95_TARGET_MS:
            print(f"✅ P95 target met (< {P95_TARGET_MS}ms)")          # Print the computed P95 latency value. Please check {P95_TARGET_MS} in line 11 for the list of variables.

        else:
            print(f"\n❌ P95 target NOT met >= {P95_TARGET_MS}ms ---") # Indicate that performance does not meet the target. Please check {P95_TARGET_MS} in line 11 for the list of variables.
    else:
        print("No valid request latencies found.")                     # Handle the case where no valid latency data exists
        return


    # Report slow requests
    print(f"\n--- Requests >= {P95_TARGET_MS}ms ---")
    slow_found = False                                   # Flag to track whether any slow requests are detected
    for r in requests:                                   # Iterate through all recorded requests
        if r["latency"] >= P95_TARGET_MS:                # Identify requests exceeding or meeting the latency threshold
            slow_found = True                            # Mark that at least one slow request exists
            print(
                f"Time:{r['timestamp']},"
                f"user_id:{r['user_id']},"
                f"status:{r['status']},"
                f"latency:{r['latency']} ms"
                
            )                                            # Print detailed information for each slow request

    if not slow_found:
        print("None")                                    # Print 'None' if no slow requests were found

if __name__ == "__main__":
    main()
