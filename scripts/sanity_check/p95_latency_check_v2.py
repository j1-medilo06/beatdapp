#!/usr/bin/env python3
##################################################################################################################
# How to run:  ./p95_latency_check.py [path]/[filename.ext] [p95_target_ms]                                      #
#   ie. ./p95_latency_check.py /logs/2024/06/15/10.0.10.10_app_0001.log 400                                      #
##################################################################################################################

import re
import math
import argparse

# Regular Expression (RegEx) for extracting timestamp, user_id, latency, and status.
LOG_PATTERN = re.compile(
    r"^(?P<timestamp>\S+)\s+.*user_id=(?P<user_id>\d+)\s+"
    r"latency_ms=(?P<latency>\d+)\s+status=(?P<status>\d+)"
)

def calculate_p95(latencies):
    if not latencies:
        return None
    latencies.sort()
    index = math.ceil(0.95 * len(latencies)) - 1
    return latencies[index]

def main():
    # Parse arguments
    parser = argparse.ArgumentParser(description="Calculate P95 latency from a log file")
    parser.add_argument("log_file", help="Path to the log file")
    parser.add_argument("p95_target", type=int, help="P95 latency target in milliseconds")
    args = parser.parse_args()

    LOG_FILE = args.log_file
    P95_TARGET_MS = args.p95_target

    requests = []

    try:
        with open(LOG_FILE, "r") as f:
            for line in f:
                match = LOG_PATTERN.search(line)
                if not match:
                    continue
                try:
                    requests.append({
                        "timestamp": match.group("timestamp"),
                        "user_id": match.group("user_id"),
                        "latency": int(match.group("latency")),
                        "status": int(match.group("status")),
                    })
                except ValueError:
                    continue
    except FileNotFoundError:
        print(f"❌ Log file not found: {LOG_FILE}")
        return

    latencies = [r["latency"] for r in requests]
    p95 = calculate_p95(latencies)

    print("\n=== Load Test Latency Sanity Report ===")
    print(f"Total requests found: {len(requests)}")

    if p95 is not None:
        print(f"P95 latency: {P95_TARGET_MS} ms")
        if p95 < P95_TARGET_MS:
            print(f"✅ P95 target met (< {P95_TARGET_MS}ms)")
        else:
            print(f"\n❌ P95 target NOT met >= {P95_TARGET_MS}ms")
    else:
        print("No valid request latencies found.")
        return

    # Report slow requests
    print(f"\n--- Requests >= {P95_TARGET_MS}ms ---")
    slow_found = False
    for r in requests:
        if r["latency"] >= P95_TARGET_MS:
            slow_found = True
            print(
                f"Time:{r['timestamp']},"
                f"user_id:{r['user_id']},"
                f"status:{r['status']},"
                f"latency:{r['latency']} ms"
            )

    if not slow_found:
        print("None")

if __name__ == "__main__":
    main()
