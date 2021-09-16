class Solution:

    # Solution 1: brute force, TLE
    def maxScoreSightseeingPairV1(self, values: List[int]) -> int:
        max_score = 0
        for i in range(len(values)):
            for j in range(i + 1, len(values)):
                max_score = max(max_score, values[i] + values[j] + i - j)
        return max_score

    # Solution 2: DP
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        # formula: values[i] + i + values[j] - j
        ans = float("-inf")
        lMax = values[0]
        for i in range(1, len(values)):
            if lMax + values[i] - i > ans:
                ans = lMax + values[i] - i

            if values[i] + i > lMax:
                lMax = values[i] + i

        return ans