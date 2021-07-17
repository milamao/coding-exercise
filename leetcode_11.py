class Solution(object):

    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height) - 1
        max_area = min(height[left], height[right]) * (right - left)
        while right - left > 1:
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
            curr_area = min(height[left], height[right]) * (right - left)
            max_area = max(curr_area, max_area)

        return max_area