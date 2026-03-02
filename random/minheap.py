import heapq

# def get_min_gpus(sessions):
#     sorted_sessions = sorted(sessions, key = lambda x : x[0])
#     active_gpus = []
#     for start, end in sorted_sessions:
#         if active_gpus and active_gpus[0] <= start:
#             heapq.heappop(active_gpus)
#         heapq.heappush(active_gpus, end)
#     return len(active_gpus)

def get_min_gpus(sessions):
    sessions_sorted = sorted(sessions, key = lambda x : x[0])
    heap = []
    for st, end in sessions_sorted:
        if len(heap) > 0 and st >= heap[0]:
            heapq.heappop(heap)
        heapq.heappush(heap, end)
    return len(heap)

sessions = [[0, 30], [5, 10], [15, 20]]
print(get_min_gpus(sessions))