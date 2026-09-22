class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        sentence = s.strip().split(" ")

        return len(sentence[-1])