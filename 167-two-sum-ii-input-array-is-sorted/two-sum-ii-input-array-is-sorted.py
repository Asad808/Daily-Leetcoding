class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        arr = []
        while l<r:
            sm = numbers[l] + numbers[r]
            if sm == target:
                arr.append(l+1)
                arr.append(r + 1)
                return arr
            elif sm > target:
                r -= 1
            else:
                l+=1