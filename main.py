# convert integer to roman
# why i didn't use dictinary, but used nested list(array) is because i want them to be
# sorted in acsending or decending order
# when you multiply string by interger it will be more of that string
# example is M * 3 =  MMM
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        dic = [["I", 1], ["IV", 4], ["V", 5], ["IX", 9], ["X", 10],
              ["XL", 40], ["L", 50], ["XC", 90], ["C", 100], ["CD", 400],
              ["D", 500], ["CM", 900], ["M", 1000]]
        res = ""
        for key, val in reversed(dic):
            if num // val:
                count = num // val
                res += (key * count)# when you multiply string by interger it will be more of the string
                # example is M * 3 =  MMM
                num = num % val
        return res
num = 980
answer = Solution()
solution = answer.intToRoman(num)
print(solution)