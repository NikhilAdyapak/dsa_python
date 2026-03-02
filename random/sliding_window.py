def longest_stable_connection(stream, k):
    left = 0
    max_length = 0
    zero_count = 0
    
    for right in range(len(stream)):
        if stream[right] == 0:
            zero_count += 1
            
        while zero_count > k:
            if stream[left] == 0:
                zero_count -= 1
            left += 1
            
        max_length = max(max_length, right - left + 1)
        
    return max_length

stream = [1, 1, 0, 0, 1, 1, 1, 0, 1]
k = 1
print(longest_stable_connection(stream, k))