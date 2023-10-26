'''Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.
You must not use any built-in exponent function or operator.
For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.'''

class Solution:
    def mySqrt(self, x: int) -> int:
        min, max = 1, x
        while min <= max:
            middle = (max + min) // 2
            if middle * middle == x:
                return middle
            elif middle * middle < x:
                min = middle + 1
            else:
                max = middle - 1
        return max

print(Solution().mySqrt(0))