class Solution:
    def fizzBuzz(self, n: int):
        string_ = []

        for i in range(1, n + 1):
            s = ''
            if not i % 3:
                s += "Fizz"
            if not i % 5:
                s += "Buzz"
            if not s:
                s += str(i)
            string_.append(s)

        return string_

print(Solution().fizzBuzz(15))