def merge_sessions(intervals):
    if not intervals:
        return []

    intervals.sort(key=lambda x: x[0])
    print(intervals)

    merged = []

    for current_interval in intervals:
        current_start = current_interval[0]
        current_end = current_interval[1]

        if not merged or merged[-1][1] < current_start:
            merged.append(current_interval)
            
        else:
            merged[-1][1] = max(merged[-1][1], current_end)

    return merged

intervals = [[1, 3], [8, 10], [2, 6], [15, 18]]
print(merge_sessions(intervals))


def merge(intervals):
    intervals = sorted(intervals, key = lambda x : x[0])

    merged = []

    for inter in intervals:
        if not merged or merged[-1][1] < inter[0]:
            merged.append(inter)
        
        else:
            merged[-1][1] = max(merged[-1][1], inter[1])
    return merged
print(merge(intervals))
