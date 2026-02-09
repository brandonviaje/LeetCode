from collections import deque
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        greedy solution: choose the local greedy solution in hopes for a global optimal solution

        local greedy choice: execute the task with the highest remaining frequency that is NOT in cooldown.
        keep track of  a time variable

        need a queue: queue’s purpose is to keep track of tasks that are in their cooldown period, since we can't run same task until n intervals passed
        """
        freq = Counter(tasks)       

        # convert freq to max heap
        maxHeap = [-val for val in freq.values()]
        heapq.heapify(maxHeap)

        queue = deque() # remaining count, ready_time
        time = 0

        while maxHeap or queue:
            time += 1 # update time

            if maxHeap:
                curr_task = heapq.heappop(maxHeap) + 1 # decrement task

                if curr_task != 0:
                    queue.append((curr_task,time + n)) # add to queue the current_task number and the time it will be able to go back to CPU

            # check if any task in cooldown is ready to be scheduled
            if queue and queue[0][1] == time:
                task, _ = queue.popleft()
                heapq.heappush(maxHeap, task)

        return time

        # T O(n)
        # S O(n)