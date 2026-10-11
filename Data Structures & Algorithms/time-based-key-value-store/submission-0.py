class TimeMap:

    def __init__(self):
        self.time_map = {} # k: v where v is a list [val, timestamp]
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        # binary search of the time_map for the correct timestamp
        if key not in self.time_map:
            self.time_map[key] = []
        self.time_map[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        # binary search of the time_map for the timestamp
        values = self.time_map.get(key, [])
        res = ""

        l, r = 0, len(values) - 1
        
        while l <= r:
            m = (l + r) // 2
            if values[m][1] <= timestamp:
                res = values[m][0]
                l = m + 1
            else:
                r = m - 1
        return res
