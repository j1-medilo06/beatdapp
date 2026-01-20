# P95 Latency Check

`p95_latency_check.py` is a Python script designed to analyze log files and calculate the **95th percentile (P95) latency** of requests. It helps in performing load test sanity checks and identifying slow requests that exceed a defined latency threshold.

---
## Features

- Parse logs to extract **timestamp**, **user ID**, **latency (ms)**, and **status code**.
- Calculate **P95 latency** from log data.
- Compare P95 latency against a **target threshold**.
- Display a report with:
  - Total number of valid requests
  - P95 latency value
  - Indicator if the target is met or not
  - List of requests exceeding the target latency
- Dynamic functionality with **command-line arguments** for log file path and target latency.

---
## Requirements

- Python 3.x
- Standard Python libraries: `re`, `math`, `argparse` (all included in Python standard library)

---
## Usage
### Command-line Usage

```bash
./p95_latency_check.py_v1 [path_to_log_file]                    # static p95 values inside the code.
./p95_latency_check.py_v2 [path_to_log_file] [p95_target_ms].   # Uses dynamic p95 value inside the code.

```

## OUTPUTS
```pgsql
=== Load Test Latency Sanity Report ===
Total requests found: 21
P95 latency: 200 ms

❌ P95 target NOT met >= 200ms

--- Requests >= 200ms ---
Time:2024-06-15T08:01:11,user_id:9902,status:200,latency:210 ms
Time:2024-06-15T08:01:12,user_id:8821,status:200,latency:850 ms
Time:2024-06-15T08:01:16,user_id:4402,status:200,latency:300 ms
Time:2024-06-15T08:01:18,user_id:5050,status:200,latency:220 ms
Time:2024-06-15T08:01:20,user_id:7070,status:200,latency:410 ms
Time:2024-06-15T08:01:25,user_id:1111,status:200,latency:900 ms
Time:2024-06-15T08:01:27,user_id:3333,status:200,latency:200 ms
Time:2024-06-15T08:01:29,user_id:5555,status:200,latency:1000 ms
Time:2024-06-15T08:01:33,user_id:9999,status:200,latency:250 ms
```
The output is exported as a CSV file with comma (,) separators, making it compatible with various tools and workflows.