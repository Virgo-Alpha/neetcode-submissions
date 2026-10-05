class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Use freq of the chars and sliding window
        # We need 2 freq maps with that of s1 being fixed and that size being the sliding window size

        if len(s1) > len(s2):
            # we can short circuit here
            return False

        # 1. Target frequencies we need to match
        s1_counts = {}
        for char in s1:
            s1_counts[char] = 1 + s1_counts.get(char, 0)

        # 2. Tracks the frequencies of the CURRENT sliding window in s2
        window_counts = {}
        l = 0

        for r in range(len(s2)):
            # Add the current right character to the window_counts map
            right_char = s2[r]
            window_counts[right_char] = 1 + window_counts.get(right_char, 0)

            # 3. Check if window size exceeds len(s1)
            # Hint: Current size is calculated as (r - l + 1)
            if (r - l + 1) > len(s1):
                left_char = s2[l]
                # TODO: Decrement left_char from window_counts
                window_counts[s2[l]] -= 1
                # TODO: If left_char count hits 0, delete it from window_counts (keeps maps clean)
                if window_counts[left_char] == 0: 
                    del window_counts[left_char]

                # TODO: Shrink the window by moving the left pointer
                l += 1

            # 4. Where to compare frequencies:
            # If the window size matches len(s1), check if maps are identical
            if (r - l + 1) == len(s1):
                # TODO: Compare window_counts with s1_counts. If they match, what do we return?
                if s1_counts == window_counts:
                    return True 

        # 5. TODO: If the loop finishes and we never matched, what do we return?
        return False

