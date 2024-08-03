# _*_ coding : utf-8 _*_
# @Time : 2024/7/30 15:04
# @Author : Slave
# @File : 2961 double-modular-exponentiation
# @Project : LeetCode

# 2961 快速幂运算的应用(快速幂运算递归模块)
# 给你一个下标从 0 开始的二维数组 variables ，其中 variables[i] = [ai, bi, ci, mi]，以及一个整数 target 。
# 如果满足以下公式，则下标 i 是 好下标：
# 0 <= i < variables.length
# ((ai^bi % 10)^ci) % mi == target
# 返回一个由 好下标 组成的数组，顺序不限


# 50 快速幂运算
# 实现 pow(x, n) ，即计算 x 的整数 n 次幂函数（即，xn ）。

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        # 50
        def quickMul(n):
            if n == 0:
                return 1.0
            num = quickMul(n // 2)
            return num * num if n % 2 == 0 else num * num * x

        return quickMul(n) if n >= 0 else 1.0 / quickMul(-n)

    def getGoodIndices(self, variables, target):
        """
        :type variables: List[List[int]]
        :type target: int
        :rtype: List[int]
        """
        # 2961
        result = []
        for i, nums in enumerate(variables):
            if pow(pow(nums[0], nums[1], 10), nums[2], nums[3]) == target:
                result.append(i)
        return result
