class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        Using greedy algorithm
        """

        count = [0] * 26
        for task in tasks:
            # Count how many times each task appears
            count[ord(task) - ord('A')] += 1

        count.sort()
        maxf = count[25]  # maximum frequency among all tasks

        # initial idle sloys
        idle = (maxf - 1) * n

        for i in range(24, -1, -1):
            # get idle needed for every other task apart from the last one
            idle -= min(maxf - 1, count[i])

        return max(0, idle) + len(tasks)

