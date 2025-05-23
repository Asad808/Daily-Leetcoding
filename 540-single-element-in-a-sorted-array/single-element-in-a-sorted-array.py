class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if (mid == 0 or nums[mid] != nums[mid - 1]) and (mid == len(nums) - 1 or nums[mid] != nums[mid + 1]):
                return nums[mid]
            if mid > 0 and nums[mid] == nums[mid - 1]:
                if mid % 2 == 1:
                    start = mid + 1
                else:
                    end = mid - 2
            else:
                if mid % 2 == 0:
                    start = mid + 2
                else:
                    end = mid - 1
        return -1