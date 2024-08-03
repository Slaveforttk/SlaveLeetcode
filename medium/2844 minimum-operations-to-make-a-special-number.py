# _*_ coding : utf-8 _*_
# @Time : 2024/7/25 14:28
# @Author : Slave
# @File : 2844 minimum-operations-to-make-a-special-number
# @Project : LeetCode

# 2844 字符串的使用 -- rfind函数
# 给你一个下标从 0 开始的字符串 num ，表示一个非负整数。
# 在一次操作中，您可以选择 num 的任意一位数字并将其删除。请注意，如果你删除 num 中的所有数字，则 num 变为 0。
# 返回最少需要多少次操作可以使 num 变成特殊数字。
# 如果整数 x 能被 25 整除，则该整数 x 被认为是特殊数字

# 方法1为多次遍历
# 方法2需要记录0和5再进行分析

class Solution(object):
    def minimumOperations1(self, num):
        """
        :type num: str
        :rtype: int
        """
        n = len(num)
        def find_str(s):
            # 从右往左寻找s里面的数字
            i = num.rfind(s[1])
            if i <= 0:
                # 第二个数字s[1]不能为0
                return n
            # 从i处开始往左寻找另一个组合数
            i = num.rfind(s[0], 0, i)
            # 此时i即为s[0]的数字，并且s[1]也存在于num中
            # 删除掉n - i + 2的数字即可
            return n if i < 0 else n - i - 2
        return min(n - 1 if '0' in num else n, find_str('00'), find_str('25'), find_str('50'), find_str('75'))

    def minimumOperations2(self, num):
        """
        :param num: str
        :return: int
        """
        n = len(num)
        found5 = found0 = False
        for i in range(n - 1, -1, -1):
            s = num[i]
            # 从右往左遍历
            if found0 and s in '05' or found5 and s in '72':
                return n - i - 2
            if s == '0':
                found0 = True
            elif s == '5':
                found5 = True
        return n - found0
