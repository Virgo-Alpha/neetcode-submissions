class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # get s1 frequency
        freq = Counter(s1)
        # default dict to count in s2, also default dict is just neater
        count = defaultdict(int)
        # left of the window
        l = 0

        for r in range(len(s2)):
            # count the characters in s2 and add to the map
            count[s2[r]] += 1
            
            # when the current length is greater than s1 time to shrink
            if (r - l + 1) > len(s1):
                count[s2[l]] -= 1
                # when shrinking if the freq of a character is 0 remove from the map
                if count[s2[l]] == 0:
                    del count[s2[l]]
                l += 1
            
            # if the s2 map and s1 map lenght are same check if the values are same 
            if len(count) == len(freq):
                if count == freq:
                    return True
              
                   
        return False
