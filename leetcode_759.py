"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    # Solution 2: Time complexity: O(nlogk)
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        # translate each employee's time slots to list of lists
        # use a heap to sort the time slots, O(nlogk)
        # merge intervals: [(1, 3), (4, 10)]
        # get gaps: [(3, 4)]
        intervals = self.get_sorted_inervals(schedule)
        merged_intervals = self.merge_intervals(intervals)

        res = []
        for i in range(0, len(merged_intervals) - 1):
            res.append(Interval(merged_intervals[i][1], merged_intervals[i + 1][0]))
        return res

    def get_sorted_inervals(self, schedule):
        heap = []
        positions = []
        for i in range(len(schedule)):
            positions.append(0)
            heapq.heappush(heap, (schedule[i][0].start, schedule[i][0].end, i))

        intervals = []
        while heap:
            start, end, index = heapq.heappop(heap)
            pos = positions[index]
            if pos < len(schedule[index]) - 1:
                pos += 1
                positions[index] = pos
                heapq.heappush(heap, (schedule[index][pos].start, schedule[index][pos].end, index))
            intervals.append((start, end))

        return intervals

    # Solution 1: Time complexity: O(nlogn)
    def employeeFreeTimeV1(self, schedule: '[[Interval]]') -> '[Interval]':
        # get all work intervals
        # sort them
        # merge intervals: [(1, 3), (4, 10)]
        # get gaps: [(3, 4)]

        intervals = self.get_intervals(schedule)  # [(1, 2), (5, 6), (1, 3), (4, 10)]
        intervals.sort()  # [(1, 2), (1, 3), (4, 10), (5, 6)]

        merged_intervals = self.merge_intervals(intervals)

        res = []
        for i in range(0, len(merged_intervals) - 1):
            res.append(Interval(merged_intervals[i][1], merged_intervals[i + 1][0]))
        return res

    def get_intervals(self, schedule):
        intervals = []
        for i in range(len(schedule)):
            for interval in schedule[i]:
                intervals.append((interval.start, interval.end))

        return intervals

    def merge_intervals(self, intervals):
        merged_intervals = [(intervals[0])]
        for i in range(1, len(intervals)):
            if merged_intervals[-1][1] < intervals[i][0]:
                merged_intervals.append(intervals[i])
            else:
                end = max(merged_intervals[-1][1], intervals[i][1])
                merged_intervals[-1] = (merged_intervals[-1][0], end)  # !!! update the last interval

        return merged_intervals