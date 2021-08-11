class Solution:
    # Solution 2: quick select
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = collections.Counter(nums)  # O(n)
        vals = list(count.keys())  # O(n)
        self.sort(vals, count, 0, len(vals) - 1, k)  # O(n) ~ O(n^2)
        return vals[:k]

    def sort(self, nums, count_dict, start, end, k):
        if start == end:
            return

        i, j = start, end
        mid = (start + end) // 2
        pivot = count_dict[nums[mid]]

        while i <= j:
            while i <= j and count_dict[nums[i]] > pivot:
                i += 1
            while i <= j and count_dict[nums[j]] < pivot:
                j -= 1

            if i <= j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1

        if k <= j - start + 1:
            return self.sort(nums, count_dict, start, j, k)
        if k >= i - start + 1:
            return self.sort(nums, count_dict, i, end, k - (i - start))
        return

    # Solution 1: simply use counter
    def topKFrequent1(self, nums: List[int], k: int) -> List[int]:
        counter = collections.Counter(nums)
        elems = counter.most_common(k)
        return [elem[0] for elem in elems]