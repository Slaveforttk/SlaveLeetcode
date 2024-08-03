# _*_ coding : utf-8 _*_
# @Time : 2024/7/8 13:20
# @Author : Slave
# @File : lengthOfLongestSubstring
# @Project : LeetCode

# 给定一个字符串 s ，请你找出其中不含有重复字符的最长 子串的长度。
# 滑动窗口--维护窗口

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = ans = 0
        window = set()
        for right, char in enumerate(s):
            while char in window:
                # 窗口右移直到重复元素后
                window.remove(s[left])
                left += 1
            window.add(char)
            # 更新最大值
            ans = max(ans, (right - left + 1))
        return ans

