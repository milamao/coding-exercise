class Solution:
    # Solution 2: bucket sort?
    # 原理：每经过一个s里的字母就消掉一个word里的字母
    def numMatchingSubseq(self, s, words):
        ans = 0
        heads = [[] for _ in range(26)]
        for word in words:
            it = iter(word)
            heads[ord(next(it)) - ord('a')].append(it)

        for letter in s:
            letter_index = ord(letter) - ord('a')
            old_bucket = heads[letter_index]
            heads[letter_index] = []

            while old_bucket:
                it = old_bucket.pop()
                nxt = next(it, None)
                if nxt:
                    heads[ord(nxt) - ord('a')].append(it)
                else:
                    ans += 1

        return ans

    # Solution 1: 2 pointer
    def numMatchingSubseq1(self, s: str, words: List[str]) -> int:
        total = 0
        matches = set()
        non_matches = set()
        for word in words:
            if word in matches:
                total += 1
                continue
            if word in non_matches:
                continue
            if len(word) > len(s):
                continue
            if len(word) == len(s):
                if word == s:
                    total += 1
                continue
            i, j = 0, 0
            while i < len(s) and j < len(word):
                if s[i] == word[j]:
                    j += 1
                i += 1
            if j == len(word):
                total += 1
                matches.add(word)
            else:
                non_matches.add(word)

        return total