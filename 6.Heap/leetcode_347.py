from queue import PriorityQueue
class Solution:
    def topKFrequent(self, nums, k):
        count = {}

        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

        pq = PriorityQueue()

        for num, freq in count.items():
            pq.put((freq, num))

            if pq.qsize() > k:
                pq.get()

        result = []
        while not pq.empty():
            result.append(pq.get()[1])
        return result[::-1]

# Driven code
nums = [1,1,1,2,2,3]
k = 2
s = Solution()
print(s.topKFrequent(nums, k))