class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        arr = []
        arr2 = []
        combined1 = 0
        combined2 = 0

        for num in num1:
            # arr.append(ord(num) - ord("0"))
        # for a in arr:
            combined1 = combined1*10 + ord(num) - ord("0")

        
        for num in num2:
            # arr2.append(ord(num) - ord("0"))
        # for a in arr2:
            combined2 = combined2*10 + ord(num) - ord("0")

        return str(combined1*combined2)