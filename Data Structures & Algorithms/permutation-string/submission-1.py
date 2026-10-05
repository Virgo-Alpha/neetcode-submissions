class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        # Fixed arrays of size 26 for lowercase English letters
        s1_counts = [0] * 26
        window_counts = [0] * 26

        # Helper lambda to map a character to an index 0-25
        get_idx = lambda char: ord(char) - ord('a')

        # 1. Populate initial frequencies for s1 and the first window of s2
        for i in range(len(s1)):
            s1_counts[get_idx(s1[i])] += 1
            window_counts[get_idx(s2[i])] += 1

        # 2. Count initial matches between the two arrays
        matches = 0
        for i in range(26):
            if s1_counts[i] == window_counts[i]:
                matches += 1

        # 3. Slide the window through s2
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            # --- Process Right Character (Entering Window) ---
            r_idx = get_idx(s2[r])
            window_counts[r_idx] += 1
            if window_counts[r_idx] == s1_counts[r_idx]:
                matches += 1
            elif window_counts[r_idx] == s1_counts[r_idx] + 1:
                # It was a match before we incremented it, so we just broke it
                matches -= 1

            # --- Process Left Character (Leaving Window) ---
            l_idx = get_idx(s2[l])
            window_counts[l_idx] -= 1
            if window_counts[l_idx] == s1_counts[l_idx]:
                matches += 1
            elif window_counts[l_idx] == s1_counts[l_idx] - 1:
                # It was a match before we decremented it, so we just broke it
                matches -= 1
            
            l += 1

        return matches == 26
