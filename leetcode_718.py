class Solution:
    # Solution 1: brute force, TLE
    def findLengthV1(self, nums1: List[int], nums2: List[int]) -> int:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        nums2_map = collections.defaultdict(list)  # num: [positions]
        for i in range(len(nums2)):
            nums2_map[nums2[i]].append(i)

        max_len = 0
        for i in range(len(nums1)):
            for j in nums2_map[nums1[i]]:
                length = 0
                p1, p2 = i, j
                while p1 < len(nums1) and p2 < len(nums2):
                    if nums1[p1] == nums2[p2]:
                        length += 1
                        p1 += 1
                        p2 += 1
                    else:
                        break
                max_len = max(max_len, length)
                if max_len == len(nums1):
                    break

        return max_len

    # Solution 2: DP
    """
    Since a common subarray of A and B must start at some A[i] and B[j], 
    let dp[i][j] be the longest common prefix of A[i:] and B[j:]. 
    Whenever A[i] == B[j], we know dp[i][j] = dp[i+1][j+1] + 1. 
    Also, the answer is max(dp[i][j]) over all i, j.

    We can perform bottom-up dynamic programming to find the answer based on this recurrence. 
    Our loop invariant is that the answer is already calculated correctly and stored in dp for any larger i, j.
    """

    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        memo = [[0] * (len(nums2) + 1) for _ in range(len(nums1) + 1)]

        for i in range(len(nums1) - 1, -1, -1):
            for j in range(len(nums2) - 1, -1, -1):
                if nums1[i] == nums2[j]:
                    memo[i][j] = memo[i + 1][j + 1] + 1

        return max(max(row) for row in memo)