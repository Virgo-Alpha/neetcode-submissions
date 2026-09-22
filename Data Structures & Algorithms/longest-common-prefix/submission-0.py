class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        
        for i in range(len(strs[0])):
            # loops through the chars in first str
            for s in strs:
                # loop through every str
                if i == len(s) or s[i] != strs[0][i]:
                    # if i is out of bounds (because the current string we are at is shorter than the first)
                    # Or if the prefix has ended and so char at i of current str is different from the one at i in first str
                    return res
            res += strs[0][i]

        return res
