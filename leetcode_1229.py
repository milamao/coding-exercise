class Solution:

    # Solution 1: TLE
    def minAvailableDurationV1(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        # find the last meeting end time of slots1
        # find the last meeting end time of slots2
        # init an array to size "last meeting end time", set all values to 0
        # walk through slots 1, add 1 to elements that fall in meeting times
        # walk through slots 2, add 1 to elements that fall in meeting times
        # walk through the array, find subarray of size "duration" whose value is all 2s
        max_end_time = 0
        for start_time, end_time in slots1:
            max_end_time = max(max_end_time, end_time)

        for start_time, end_time in slots2:
            max_end_time = max(max_end_time, end_time)

        avails = [0] * (max_end_time + 1)
        for start_time, end_time in slots1:
            for i in range(start_time, end_time + 1):
                avails[i] += 1

        for start_time, end_time in slots2:
            for i in range(start_time, end_time + 1):
                avails[i] += 1

        for i in range(max_end_time):
            if avails[i] == 2:
                subarr_size = 0
                for j in range(1, duration + 1):
                    if avails[i + j] == 2:
                        subarr_size += 1
                    else:
                        break
                if subarr_size == duration:
                    return [i, i + duration]

        return []

    # Solution 2: 2 pointers
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:

        slots1.sort()
        slots2.sort()
        pointer1 = pointer2 = 0

        while pointer1 < len(slots1) and pointer2 < len(slots2):
            # find the boundaries of the intersection, or the common slot
            intersect_left = max(slots1[pointer1][0], slots2[pointer2][0])
            intersect_right = min(slots1[pointer1][1], slots2[pointer2][1])
            if intersect_right - intersect_left >= duration:
                return [intersect_left, intersect_left + duration]

            # always move the one that ends earlier
            if slots1[pointer1][1] < slots2[pointer2][1]:
                pointer1 += 1
            else:
                pointer2 += 1

        return []
