import heapq

heap = [4, 9, 2, 6, 1, 0]
heapq.heapify(heap)
heapq.heappush(heap, 10)

print(heap)
print(heapq.heappop(heap))
print(heap)