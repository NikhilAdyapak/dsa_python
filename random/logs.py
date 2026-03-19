from datetime import datetime

def get_top_errors(logs, start_time_str, end_time_str, k):
    # 1. Define the time format for parsing
    time_format = "%Y-%m-%d %H:%M:%S"
    
    # Convert boundary strings to datetime objects for comparison
    start_time = datetime.strptime(start_time_str, time_format)
    end_time = datetime.strptime(end_time_str, time_format)
    
    error_counts = {}
    
    # 2. Process each log line
    for log in logs:
        # Safely split the log into exactly 3 parts
        parts = log.split(" | ")
        if len(parts) != 3:
            continue
            
        timestamp_str, level, message = parts
        
        # We only care about ERROR level logs
        if level != "ERROR":
            continue
            
        # 3. Check if the log is within the time window
        try:
            log_time = datetime.strptime(timestamp_str, time_format)
            if start_time <= log_time <= end_time:
                # Increment the count in our dictionary
                error_counts[message] = error_counts.get(message, 0) + 1
        except ValueError:
            # Handle malformed timestamps gracefully
            continue
    print(error_counts)
            
    # 4. Sort the dictionary by count (descending) and return top k
    # items() returns (key, value) pairs. lambda x: x[1] sorts by the count.
    sorted_errors = sorted(error_counts.items(), key=lambda x: x[1], reverse=True)
    
    return sorted_errors[:k]

# --- Test Case ---
logs = [
    "2026-03-19 10:00:00 | INFO | System startup",
    "2026-03-19 10:05:00 | ERROR | DB Connection Timeout",
    "2026-03-19 10:10:00 | ERROR | Memory Limit Exceeded",
    "2026-03-19 10:15:00 | ERROR | DB Connection Timeout",
    "2026-03-19 11:00:00 | ERROR | Kafka Queue Full",
    "2026-03-19 12:00:00 | ERROR | DB Connection Timeout" # Outside time window
]

print(get_top_errors(logs, "2026-03-19 10:00:00", "2026-03-19 11:30:00", 2))
# Expected Output: [('DB Connection Timeout', 2), ('Memory Limit Exceeded', 1)]