class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # We are supposed to use a sliding window
        # A single window is as large as when it contents start to repeat themselves
        # As such, the window should be a set for ease of look up
        candidate_longest = 0
        longest = 0
        window = set()
        
        l = 0

        # We need to loop over s
        # If char is in window then we pop the left most element from the set
        # Else, we add char to window

        for r in range(len(s)):
            while s[r] in window:
                window.remove(s[l])
                l += 1
            window.add(s[r])
            candidate_longest = r - l + 1
            longest = max(longest, candidate_longest)

        return longest


        