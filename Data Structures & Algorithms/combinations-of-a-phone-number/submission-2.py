class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Instead of using recursion, we build combinations level by level.
        # Breadth-First Expansion: Instead of going deep down one path like recursion,
        #   this builds all possible combinations one character at a time across every existing branch simultaneously.
        
        if not digits: return []

        res = [""]
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        for digit in digits:
            tmp = [] # temp strings for each digit
            
            for curStr in res:
                # Because res = [""] has a length of 1, this loop actually runs once 
                # during the first pass, using that empty string "" as a blank canvas
                for c in digitToChar[digit]:
                    # candidate c for each digit is added to temp of prev digit
                    tmp.append(curStr + c)
            
            res = tmp
        
        return res