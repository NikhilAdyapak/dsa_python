from datetime import datetime

def get_top_errors(logs, start_time_str, end_time_str, k):
    time_format = "%Y-%m-%d %H:%M:%S"
    
    start_time = datetime.strptime(start_time_str, time_format)
    end_time = datetime.strptime(end_time_str, time_format)
    
    error_counts = {}
    
    for log in logs:
        parts = log.split(" | ")
        if len(parts) != 3:
            continue
            
        timestamp_str, level, message = parts
        
        if level != "ERROR":
            continue
            
        try:
            log_time = datetime.strptime(timestamp_str, time_format)
            if start_time <= log_time <= end_time:
                error_counts[message] = error_counts.get(message, 0) + 1
        except ValueError:
            continue
    print(error_counts)
            
    sorted_errors = sorted(error_counts.items(), key=lambda x: x[1], reverse=True)
    
    return sorted_errors[:k]

logs = [
    "2026-03-19 10:00:00 | INFO | System startup",
    "2026-03-19 10:05:00 | ERROR | DB Connection Timeout",
    "2026-03-19 10:10:00 | ERROR | Memory Limit Exceeded",
    "2026-03-19 10:15:00 | ERROR | DB Connection Timeout",
    "2026-03-19 11:00:00 | ERROR | Kafka Queue Full",
    "2026-03-19 12:00:00 | ERROR | DB Connection Timeout" 
]

print(get_top_errors(logs, "2026-03-19 10:00:00", "2026-03-19 11:30:00", 2))