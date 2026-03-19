def analyze_server_logs(logs):
    error_counts = {}
    
    for log in logs:
        parts = log.split(" ", 2) 
        
        if len(parts) < 3:
            continue
            
        log_level, timestamp, message = parts
        
        if log_level == "ERROR":
            error_counts[message] = error_counts.get(message, 0) + 1
            
    return error_counts

sample_logs = [
    "INFO 2026-03-19 Server started",
    "ERROR 2026-03-19 Connection timeout",
    "ERROR 2026-03-19 Connection timeout",
    "WARNING 2026-03-19 High memory usage"
]
print(analyze_server_logs(sample_logs))