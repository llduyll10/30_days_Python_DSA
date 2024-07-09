import queue

pq = queue.PriorityQueue()

h = [7, 12, 6, 10, 17, 15, 2, 4]
for i in h:
    pq.put(i)
print(pq.queue)
top = pq.queue[0]
print(top)
topValue = pq.get()
print(topValue)
