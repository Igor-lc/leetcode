import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-zA-Z0-9]', '', s).casefold()
        return s == s[::-1]

    def isPalindrome2(self, string):
        string = string.lower()
        string = ''.join(char for char in string if char.isalnum())
        return string == string[::-1]


print(Solution().isPalindrome("A man, a plan, a canal: Panama"))
print(Solution().isPalindrome2("A man, a plan, a canal: Panama"))