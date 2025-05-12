class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        su = 0
        mi = []


        for i, n in enumerate(nums):
            su += n
            

            while su >= target:
                mi.append(len(nums[l:i+1]))
                su -= nums[l]
                l += 1
        if mi:
            return min(mi) 
        else:
            return 0
                