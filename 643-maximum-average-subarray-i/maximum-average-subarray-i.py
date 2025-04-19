class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        cur_Sum = 0
        # cur_Sum = sum(nums[:k])
        for i in range(k):
            cur_Sum += nums[i]


        n = len(nums)

        max_avg = cur_Sum/k

        for i in range(k,n):
            cur_Sum += nums[i]
            cur_Sum -= nums[i-k]
            avg = cur_Sum/k

            max_avg = max(max_avg, avg)
        return max_avg
