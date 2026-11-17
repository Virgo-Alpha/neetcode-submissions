class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        We initialize an empty Min-Heap. 
        We iterate through the array and add elements to the heap. 
        When the size of the heap exceeds k, we pop from the heap and continue. 
        After the iteration, the top element of the heap is the k-th largest element.
        """

        heap = []

        for num in nums:
            heapq.heappush(heap, num)

            if len(heap) > k:
                heapq.heappop(heap)

        return heapq.heappop(heap)
