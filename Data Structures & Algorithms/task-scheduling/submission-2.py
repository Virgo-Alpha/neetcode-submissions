class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        The task with the highest frequency determines the minimum needed structure of the schedule.
        If a task appears maxf times, these copies must be at least n units apart.
        This creates (maxf - 1) "gaps", and each gap must have a length of (n + 1) slots (the task itself + n cooldowns).

        If multiple tasks share this maximum frequency (maxCount tasks), they all occupy the final row of the structure.

        So the minimal time required to schedule all tasks without violating cooldown rules is: time = (maxf - 1) * (n + 1) + maxCount

        However, if the number of tasks is larger than this calculated time, then simply performing all tasks takes longer.
        Thus, the actual answer must be: max(len(tasks), time)
"""
        count = [0] * 26
        for task in tasks:
            # Count how many times each task appears.
            count[ord(task) - ord('A')] += 1

        maxf = max(count)  # the highest task frequency
        maxCount = 0
        for i in count:
            # Count how many tasks have this highest frequency
            maxCount += 1 if i == maxf else 0

        time = (maxf - 1) * (n + 1) + maxCount
        return max(len(tasks), time)
