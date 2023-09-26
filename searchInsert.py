'''Given a sorted array of distinct integers and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.
You must write an algorithm with O(log n) runtime complexity.'''


class Solution:
    def searchInsert(self, nums, target):
        min_index, max_index = 0, len(nums) - 1
        while min_index <= max_index:
            middle_index = (max_index + min_index) // 2
            if target < nums[middle_index]:
                max_index = middle_index - 1
            elif target > nums[middle_index]:
                min_index = middle_index + 1
            else:
                return middle_index
        return min_index


print(Solution().searchInsert([1,3,5,6], 5))
print(Solution().searchInsert([1,3,5,6], 2))
print(Solution().searchInsert([1,3,5,6], 7))
print(Solution().searchInsert([1,3,5,6], 0))