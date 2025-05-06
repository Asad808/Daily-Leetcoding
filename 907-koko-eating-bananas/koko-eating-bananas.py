class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """

        l, r = 1, max(piles)
        while l < r:
            m = (l + r) // 2
            if sum((p + m - 1) // m for p in piles) > h:
                l = m + 1
            else:
                r = m
        return l


        # l, r = 1, max(piles)


        # res = r

        # while l <= r:
        #     hours = 0
        #     k = (l + r)//2
            
        #     for p in piles:
        #         hours += math.ceil(p/k)

        #     if hours <= h:
        #         res = min(res,k)
        #         r = k-1
                
        #     else:
        #         l = k + 1

        # return res
            