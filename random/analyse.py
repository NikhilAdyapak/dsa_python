def analyze_server_logs(logs):
    error_counts = {}
    
    for log in logs:
        # Example log: "ERROR 2026-03-19 Data pipeline failed"
        parts = log.split(" ", 2) 
        
        if len(parts) < 3:
            continue
            
        log_level, timestamp, message = parts
        
        if log_level == "ERROR":
            # Use .get() for safe dictionary updates
            error_counts[message] = error_counts.get(message, 0) + 1
            
    return error_counts

# Example usage
sample_logs = [
    "INFO 2026-03-19 Server started",
    "ERROR 2026-03-19 Connection timeout",
    "ERROR 2026-03-19 Connection timeout",
    "WARNING 2026-03-19 High memory usage"
]
print(analyze_server_logs(sample_logs)) 
# Output: {'Connection timeout': 2}