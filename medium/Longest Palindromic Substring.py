# _*_ coding : utf-8 _*_
# @Time : 2024/7/10 13:32
# @Author : Slave
# @File : Longest Palindromic Substring
# @Project : LeetCode

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 1:
            return s

        def checkPalind(left, right):
            """
            传入左右下标
            返回bool
            """
            if s[left] != s[right]:
                return False
            for i in range(1, (right - left + 1) // 2):
                # i代表要加和减的数
                if s[left + i] != s[right - i]:
                    return False
            return True

        for k in range(len(s), 1, -1):
            # k维护窗口大小
            for left in range(len(s)):
                # left维护左下标
                if left + k > len(s):
                    break
                if checkPalind(left, left + k - 1) is True:
                    return s[left:left + k]
        return s[0]


if __name__ == '__main__':
    s = "abcdbbfcba"
    print(Solution().longestPalindrome(s))
