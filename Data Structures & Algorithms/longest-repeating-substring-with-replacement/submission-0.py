class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # We should use a sliding window, l = 0, for right in ...
        # shrink the window when the number of replacements exceeds k (remove l)
        # Recommended complexity is O(n) so one loop
        longest = 0 # longest substring with a single repeating character
        left = 0
        window = {} # hashmap of char: freq

        max_freq = 0

        # If we think in respect to the freq of the characters
        # Let's create a Counter

        for r in range(len(s)):
            window[s[r]] = 1 + window.get(s[r], 0)
            max_freq = max(max_freq, window[s[r]])

            while ( r - left + 1) - max_freq > k:
                # we shrink an invalid window until it becomes valid
                window[s[left]] -= 1
                left += 1

            longest = max(longest, r - left + 1)

        return longest
