'''Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
Example 1:

Input: rowIndex = 3
Output: [1,3,3,1]
Example 2:

Input: rowIndex = 0
Output: [1]
Example 3:

Input: rowIndex = 1
Output: [1,1]
'''
class Solution:
    def generate(self, numRows):
        lists = []

        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1,1]]
        elif numRows > 2:
            lists = [[1], [1,1]]

            for row in range(1, numRows - 1):
                last_list = lists[-1].copy()
                new_list = [1]

                for i in range(len(last_list) - 1):
                    new_list.append(last_list[i] + last_list[i + 1])
                new_list.append(1)

                lists += [new_list]
        return lists
