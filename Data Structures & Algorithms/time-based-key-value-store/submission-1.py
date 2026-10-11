class TimeMap:
    """
    Knowing that each insert has a bigger timestamp than the previous one, 
    we can go through the dict in reverse order and return the first associated value with the same key and inferior timestamp."""
    def __init__(self):
        self.h = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.h[(key, timestamp)] = value

    def get(self, key: str, timestamp: int) -> str:
        if (key, timestamp) in self.h:
            return self.h[(key, timestamp)]

        for keyMap, value in reversed(self.h.items()):
            if key == keyMap[0] and keyMap[1] < timestamp:
                return value

        return ""