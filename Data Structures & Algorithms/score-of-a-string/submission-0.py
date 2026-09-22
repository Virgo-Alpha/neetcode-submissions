class Solution:
    def scoreOfString(self, s: str) -> int:
        
        first, second = 0, 1
        sums = 0

        while second < len(s):
            local_sum = abs(ord(s[second]) - ord(s[first]))
            sums += local_sum

            first += 1
            second += 1

        return sums