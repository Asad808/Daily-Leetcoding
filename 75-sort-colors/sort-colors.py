class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """


        i = 0
        l = 0
        r = len(nums) - 1

        while i<=r:


            if nums[i] == 0:
                nums[i], nums[l] = nums[l], nums[i]
                l += 1

            if nums[i] == 2:
                nums[i], nums[r] = nums[r], nums[i]
                r -= 1
                i -= 1



            i += 1