class Solution(object):
    # Solution 2: sliding window
    def checkInclusion(self, s1, s2):
        if len(s1) > len(s2):
            return False

        len_s1 = len(s1)

        counter_s1 = Counter(s1)  # {'a': 2, 'b': 3}
        counter_s2 = {}
        left = 0
        for i in range(0, len(s2)):
            counter_s2[s2[i]] = counter_s2.get(s2[i], 0) + 1
            if i < len_s1 - 1:
                continue
            if self.compare_counter(counter_s1, counter_s2):
                return True

            counter_s2[s2[left]] -= 1
            if counter_s2[s2[left]] == 0:
                del counter_s2[s2[left]]
            left += 1

        return False

    def compare_counter(self, counter_s1, counter_s2):
        if len(counter_s1) != len(counter_s2):
            return False

        for char in counter_s1:
            if char not in counter_s2:
                return False
            if counter_s1[char] != counter_s2[char]:
                return False

        return True

    # Solution 1: Brute Force
    def checkInclusion1(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) > len(s2):
            return False

        len_s1 = len(s1)
        # chars_s1 = list(s1) # O(n)
        chars_s1 = []
        for char in s1:
            chars_s1.append(char)
        # print(chars_s1)
        char_set_s1 = set(chars_s1)  # O(n)
        chars_s1.sort()  # O(nlogn)
        s1_sorted = "".join(chars_s1)  # O(n)

        for i in range(len(s2) - len_s1 + 1):  # O(m-n)
            if s2[i] in char_set_s1:  # O(1)
                # substr = s2[i:i+len_s1]
                # chars_s2 = substr[::]
                chars_s2 = []
                for j in range(i, i + len_s1):  # o(n)
                    chars_s2.append(s2[j])
                chars_s2.sort()  # O(nlogn)
                if "".join(chars_s2) == s1_sorted:
                    return True

        return False

    # Time Complexity: if m is really big, O(m*nlogn)