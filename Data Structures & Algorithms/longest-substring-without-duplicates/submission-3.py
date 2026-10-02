class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # We are supposed to use a sliding window
        # A single window is as large as when it contents start to repeat themselves
        # As such, the window should be a set for ease of look up
        # However, a hashmap also has the same lookup and can help us store the idx of the last l
        # Use a hashmap instead of a set here
        candidate_longest = 0
        longest = 0
        window = {} # hashmap - advantage is in storing the idx
        
        l = 0

        # We need to loop over s
        # If char is in window then we pop the left most element from the set
        # Else, we add char to window

        for r in range(len(s)):
            if s[r] in window:
                # window.pop(s[l])
                # Instead of deleting keys, you can leave them in the hashmap. 
                # When you see a character again (if s[r] in window:), you check if its last recorded index is greater than or equal to l. 
                # If it is, it's inside your current window, and you can instantly update l to window[s[r]] + 1.
                l = max(l, window[s[r]] + 1)
            window[s[r]] = r
            candidate_longest = r - l + 1
            longest = max(longest, candidate_longest)

        return longest
        