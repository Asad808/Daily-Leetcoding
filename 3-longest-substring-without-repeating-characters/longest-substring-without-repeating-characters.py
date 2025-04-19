class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 1
        maxlen = 0
        if len(s)> 1:
            for i in range(len(s)):
                str_len = len(set(s[l:r]))
                if str_len > maxlen:
                    maxlen = str_len
                    r += 1

                elif s[l] in s[l:r]:
                    l+=1
                    r += 1
        else:
            return len(s)

        return maxlen
