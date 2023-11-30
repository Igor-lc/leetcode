'''Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
Input: nums = [3,2,3]
Output: 3
Input: nums = [2,2,1,1,1,2,2]
Output: 2
Follow-up: Could you solve the problem in linear time and in O(1) space?'''

from collections import Counter, defaultdict

# ver_4 space complexity O(1)
class Solution4:
    def majorityElement(self, nums):
        count = 1
        prev = nums[0]

        for el in nums[1:]:
            if count == 0:
                prev = el

            count += 1 if prev == el else -1
            print(prev, count, el)

        return prev


class Solution3:
    def majorityElement(self, nums):
        elements = defaultdict(int)

        for el in nums:
            elements[el] += 1

        return max(elements, key=elements.get)


class Solution2:
    def majorityElement(self, nums):
        counts = Counter(nums)
        return max(counts, key=counts.get)


class Solution:
    def majorityElement(self, nums):
        elements = {}
        max_ = (0, 0)

        for el in nums:
            try:
                elements[el] += 1
            except:
                elements[el] = 1

        for el in elements:
            if elements[el] > max_[1]:
                max_ = (el, elements[el])
        return max_[0]


print(Solution4().majorityElement([3,2,6,3,6,4,6,5,6]))
print(Solution4().majorityElement([6,5,5]))
print(Solution4().majorityElement([8,9,8,9,8]))
print(Solution3().majorityElement([8,8,7,7,7]))
print(Solution2().majorityElement([6,6,6,7,7]))
print(Solution().majorityElement([2,2,1,1,1,2,2]))
