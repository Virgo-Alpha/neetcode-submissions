import heapq, math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        We initialize a Max-Heap that orders points based on their 
            distances from the origin. 
        Starting with an empty heap, we iterate through the array of points, inserting 
            each point into the heap. 
        If the size of the heap exceeds k, we remove the farthest point 
        (the maximum element in the heap). 
        After completing the iteration, the heap will contain the k closest 
            points to the origin. 
        Finally, we convert the heap into an array and return it.
        """
        # The below is actually (x - 0)^2 + (y - 0)^2
        distance_calc = lambda x, y: math.sqrt((x ** 2 + y ** 2))

        heap = []
        
        for x, y in points:
            # calculate distance here
            distance = distance_calc(x, y)

            # Push distance and co-ordinates as a tuple: (-dist, [x, y])
            heapq.heappush(heap, (-distance, [x, y]))
            if len(heap) > k:
                heapq.heappop(heap)

        # we need to return the kth closest points; an arr of arrays
        kth_closest = [point for _, point in heap]

        return kth_closest