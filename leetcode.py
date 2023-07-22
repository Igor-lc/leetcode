class Solution:
    def arithmeticTriplets(self, nums, diff):
        c = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                for k in range(j, len(nums)):
                    if nums[j] - nums[i] == diff and nums[k] - nums[j] == diff:
                        c += 1
        return c

from collections import defaultdict

class Solution2:
    def arithmeticTriplets(self, nums, diff):
        count = 0
        num_counts = defaultdict(int)
        num_triplets = defaultdict(int)

        for num in nums:
            count += num_triplets[num - diff]
            num_triplets[num] += num_counts[num - diff]
            num_counts[num] += 1

        return count


print(Solution2().arithmeticTriplets(nums = [0,1,4,6,7,10], diff = 3))


class Solution3:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        shortest = min(strs, key=len)

        for i, char in enumerate(shortest):
            for string in strs:
                print(string)
                if string[i] != char:
                    return shortest[:i]
        return shortest


print(Solution3().longestCommonPrefix(["dog", "racecar", "car"]))
print(Solution3().longestCommonPrefix(["flower", "flow", "flight"]))
print(Solution3().longestCommonPrefix(["a"]))


class Solution4:
    def isValid(self, s):
        lst = []
        mapping = {')': '(', '}': '{', ']': '['}
        for bracket in s:
            if bracket in mapping:
                top_element = lst.pop() if lst else False
                if mapping[bracket] != top_element:
                    return False
            else:
                lst.append(bracket)
        return not lst


print(Solution4().isValid("()[]]{}"))
