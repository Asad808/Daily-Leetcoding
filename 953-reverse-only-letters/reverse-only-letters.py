class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        l = 0
        r = len(s) - 1
        s= list(s)
        while l<r:
            if s[l].isalpha() and s[r].isalpha():
                s[l], s[r] = s[r], s[l]
                l+=1
                r-=1
            elif not s[l].isalpha():
                l+=1
            else:
                r-=1
        s= "".join(s)
        return s