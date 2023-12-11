class Solution:
    def convertToTitle(self, columnNumber):
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        excelNumber = ''

        while columnNumber > 0:
            remainder = (columnNumber - 1) % 26
            excelNumber = alphabet[remainder] + excelNumber
            columnNumber = (columnNumber - 1) // 26

        return excelNumber

Solution().convertToTitle(702)
Solution().convertToTitle(18280)


'''
1  A  27 AA  53 BA
26 Z  52 AZ  78 BZ
'''