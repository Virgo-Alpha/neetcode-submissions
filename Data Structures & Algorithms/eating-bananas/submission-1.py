class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Binary search so we need to somehow sort first
        # k - bananas per hour. I suspect we should sort desc
        # h - number of hours to eat all the bananas. Acts as our target

        # Hint 1: recommended time complexity is O(nlogm):n is len(piles) and m is max(piles)
        # Hint 2: h >= len(piles), what's the upper bound of the answer? max(piles)
        # Hint 3: k bananas / h == x / k time to finish a pile with x bananas. What's min(k)
        # Hint 4: Bruteforce would check linearly from 1 to max(piles) and find min(k)
        # Hint 5: lower bound = 1; upper bound = max(piles), use bin search to find min(k)

        l, r = 1, max(piles)
        res = r

        while l <= r:
            # k is the current speed we are testing
            k = (l + r) // 2
            
            # totalTime needed to eat through piles at this speed
            totalTime = 0
            for p in piles:
                totalTime += math.ceil(float(p) / k)
            if totalTime <= h:
                # record the speed because it's within h but check for a lower one too
                # k <= res every time we enter the if block
                res = k
                r = k - 1
            else:
                # Speed is too slow, so search in the right half
                l = k + 1

        return res
