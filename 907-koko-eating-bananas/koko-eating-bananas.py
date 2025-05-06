class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """

        n = len(piles)
        max_pile = max(piles)
        # Tighter upper bound: hi = ceil(max_pile / (h / n))
        hi = ceil(max_pile / (h / n))
        
        lo = max(1, ceil(sum(piles)/h)) 
        while lo <= hi:
            curr_guess = (lo + hi) // 2
            hours_passed = sum(ceil(pile / curr_guess) for pile in piles)
            
            if hours_passed > h:
                lo = curr_guess + 1
            else:
                hi = curr_guess - 1
                
        return int(lo)


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
            