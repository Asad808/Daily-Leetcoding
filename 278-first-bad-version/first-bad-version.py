# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = 0
        r = n
        output = 1
        while l<=r:
            m = (l+r)//2
            bad = isBadVersion(m)
            if bad == True:
                output = m
                r = m -1
            elif bad == False:
                l = m + 1
        return output