class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l = 0
        r = num


        while l<=r:
            mid = (l+r) // 2

            if mid**2 > num:
                r = mid - 1
            elif mid**2 < num:
                l = mid + 1
            
            elif mid**2 == num:
                return True

        return False