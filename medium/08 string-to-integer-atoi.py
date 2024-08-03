# _*_ coding : utf-8 _*_
# @Time : 2024/7/22 18:53
# @Author : Slave
# @File : 08 string-to-integer-atoi
# @Project : LeetCode

# 08 将字符串转化为32位整型输出
# 请你来实现一个 myAtoi(string s) 函数，使其能将字符串转换成一个 32 位有符号整数。
# 函数 myAtoi(string s) 的算法如下：
# 空格：读入字符串并丢弃无用的前导空格（" "） 符号：检查下一个字符（假设还未到字符末尾）为 '-' 还是 '+'。如果两者都不存在，则假定结果为正。
# 转换：通过跳过前置零来读取该整数，直到遇到非数字字符或到达字符串的结尾。如果没有读取数字，则结果为0。
# 截断到32位的数字

class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = []
        Flag = True
        for i in s:
            if not result and i == ' ':
                continue
            if i == '+' or i == '-':
                if Flag is True:
                    result.append(i)
                    Flag = False
                    continue
                else:
                    break
            if '0' <= i <= '9':
                result.append(i)
                Flag = False
                continue
            else:
                break
        if not result or result[-1] == '-' or result[-1] == '+':
            ans = 0
        else:
            ans = int(''.join(result))
        ans = -2 ** 31 if ans < -2 ** 31 else ans
        ans = 2 ** 31 - 1 if ans > 2 ** 31 - 1 else ans
        return ans
