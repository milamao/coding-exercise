class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.key_vals = collections.defaultdict(dict)  # key: key, value: {timestamp: value}
        self.key_timestamps = collections.defaultdict(list)  # key: key, value: [timestamps]

    # Time Complexity: O(1)
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.key_vals[key][timestamp] = value
        self.key_timestamps[key].append(timestamp)

    # Time Complexity: O(logn)
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.key_vals:
            return ""

        if timestamp in self.key_vals[key]:
            return self.key_vals[key][timestamp]

        ts = self.__find_next_smallest(key, timestamp)
        if ts is not None:
            return self.key_vals[key][ts]

        return ""

    def __find_next_smallest(self, key, timestamp):
        # handle edge cases
        timestamps = self.key_timestamps[key]
        if not timestamps:
            return None
        if timestamp < timestamps[0]:
            return None
        if timestamp > timestamps[-1]:
            return timestamps[-1]

        # binary search
        left, right = 0, len(timestamps) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if timestamps[mid] < timestamp:
                left = mid
            else:
                right = mid
        if timestamps[right] < timestamp:
            return timestamps[right]
        if timestamps[left] < timestamp:
            return timestamps[left]
        return None

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)