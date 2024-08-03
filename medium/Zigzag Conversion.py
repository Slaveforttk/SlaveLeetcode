# _*_ coding : utf-8 _*_
# @Time : 2024/7/14 15:27
# @Author : Slave
# @File : Zigzag Conversion
# @Project : LeetCode

# 06
# 将一个给定字符串 s 根据给定的行数 numRows ，以从上往下、从左到右进行 Z 字形排列。
# 比如输入字符串为 "PALATALISING" 行数为 3 时，排列如下：
# P   A   H   N
# A P L S I I G
# Y   I   R
# 之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："PAHNAPLSIIGYIR"。
# 二维数组暴力求解
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        n = len(s)
        if numRows == 1 or n <= numRows:
            return s
        result = []
        for i in range(numRows):
            # 初始化二维数组
            result.append([s[i]])
        i = numRows
        while i < len(s):
            # 从row - 2开始直到0(不包含0)
            for j in range(numRows - 2, 0, -1):
                result[j].append(s[i])
                i += 1
                if i >= n:
                    break;
            j = 0
            while j < numRows and i < n:
                # 顺着添加
                result[j].append(s[i])
                i += 1
                j += 1
        # 字符串转换
        x = ''
        for i in range(numRows):
            x = x + ''.join(result[i])
        return x
