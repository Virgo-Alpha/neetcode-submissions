class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # We should always process the most frequent task first. 
        # After selecting the most frequent task, we must ensure that it is not 
        #   processed again until after n seconds, due to the cooldown condition.

        # We can use a Max-Heap to efficiently retrieve the most frequent task 
        #   at any given instance. 
        # However, to enforce the cooldown period, we must temporarily hold off from
        #   reinserting the processed task into the heap. 
        # This is where a queue data structure comes in handy. 
        # It helps maintain the order of processed tasks.

        # We start by calculating the frequency of each task and 
        #   initialize a variable time to track the total processing time. 
        # The task frequencies are inserted into a Max-Heap. 
        # We also use a queue to store tasks along with the time they become
        #   available after the cooldown. 
        # At each step, if the Max-Heap is empty, we update time to match the next
        #   available task in the queue, covering idle time. 
        # Otherwise, we process the most frequent task from the heap, 
        #   decrement its frequency, and if it's still valid,
        #   add it back to the queue with its next available time. 
        # If the task at the front of the queue becomes available, 
        #   we pop it and reinsert it into the heap.

        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        time = 0
        q = deque()  # pairs of [-cnt, idleTime]
        while maxHeap or q:
            time += 1

            if not maxHeap:
                time = q[0][1]
            else:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, time + n])
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time
