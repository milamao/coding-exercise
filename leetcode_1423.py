class Solution:
    # Solution 1: DFS, O(2^k), TLE
    def maxScore1(self, cardPoints: List[int], k: int) -> int:
        if k >= len(cardPoints):
            return sum(cardPoints)
        scores = []
        self.draw_card(cardPoints, 0, len(cardPoints) - 1, k, 0, scores)
        return max(scores)

    def draw_card(self, cardPoints, left, right, k, score, scores):
        if k == 0:
            scores.append(score)
            return
        self.draw_card(cardPoints, left + 1, right, k - 1, score + cardPoints[left], scores)
        self.draw_card(cardPoints, left, right - 1, k - 1, score + cardPoints[right], scores)

    # Solution 2: sliding window, O(n), window size is n-k,
    # it's effectively asking for the min sum of an n-k sub array
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        startingIndex = 0
        presentSubarrayScore = 0
        n = len(cardPoints)
        requiredSubarrayLength = n - k

        totalScore = sum(cardPoints)
        minSubarrayScore = totalScore

        if k >= n:
            return totalScore

        for i in range(n):
            presentSubarrayScore += cardPoints[i];
            presentSubarrayLength = i - startingIndex + 1;

            if presentSubarrayLength == requiredSubarrayLength:
                minSubarrayScore = min(minSubarrayScore, presentSubarrayScore)
                presentSubarrayScore -= cardPoints[startingIndex]
                startingIndex += 1

        return totalScore - minSubarrayScore
