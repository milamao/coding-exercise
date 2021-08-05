class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k == 0:
            return 0

        counter = {}
        left, right = 0, 0
        n = len(s)
        max_len = 0
        while right < n:
            char = s[right]
            counter[char] = counter.get(char, 0) + 1
            while len(counter) > k:
                char = s[left]
                counter[char] -= 1
                if not counter[char]:
                    del counter[char]
                left += 1
            max_len = max(max_len, right - left + 1)
            right += 1

        return max_len