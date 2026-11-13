class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(i, curStr):
            # Base case when the strings are the same number as digits
            if len(curStr) == len(digits):
                res.append(curStr)
                return
            
            # loop through the values of the map digitToChar for the idx of the curr str
            for c in digitToChar[digits[i]]:
                backtrack(i + 1, curStr + c)

        # Only start the backtrack if digits is not an empty string
        if digits: backtrack(0, "")

        return res
