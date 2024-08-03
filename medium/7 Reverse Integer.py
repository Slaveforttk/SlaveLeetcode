# _*_ coding : utf-8 _*_
# @Time : 2024/7/16 10:46
# @Author : Slave
# @File : 7Reverse Integer
# @Project : LeetCode

# 07
# 给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。
# 如果反转后整数超过 32 位的有符号整数的范围 [−2^31,  2^31 − 1] ，就返回 0。
# 假设环境不允许存储 64 位整数（有符号或无符号）

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x > 0:
            s = '+' + str(x)
        else:
            s = str(x)
        list_x = list(s)
        for i in range(1, len(list_x) // 2 + 1):
            list_x[i], list_x[-i] = list_x[-i], list_x[i]
        s = ''.join(list_x)
        if -2 ** 31 <= int(s) <= 2 ** 31 - 1:
            return int(s)
        return 0


if __name__ == '__main__':
    x = -213
    s = Solution()
    print(s.reverse(x))
