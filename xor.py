class Solution:
    def singleNumber(self, nums):
        result = 0
        for digit in nums:
            result ^= digit
        return result

nums = [2,2,1]
print(Solution().singleNumber(nums))

def xorRange(start, end):
    result = 0
    for num in range(start, end + 1):
        result ^= num
        print(result, num)
    return result

start_value = 5
end_value = 8
print(xorRange(start_value, end_value))
