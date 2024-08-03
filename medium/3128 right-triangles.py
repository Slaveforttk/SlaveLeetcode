# _*_ coding : utf-8 _*_
# @Time : 2024/8/2 13:11
# @Author : Slave
# @File : 3128 right-triangles
# @Project : LeetCode

# 3128 数学题目
# 给你一个二维 boolean 矩阵 grid 。
# 请你返回使用 grid 中的 3 个元素可以构建的 直角三角形 数目，且满足 3 个元素值 都 为 1 。
# 注意
# 如果 grid 中 3 个元素满足：
# 一个元素与另一个元素在 同一行，同时与第三个元素在 同一列 ，那么这 3 个元素称为一个 直角三角形 。这3个元素互相之间不需要相邻
# 思路：记录每一列的和 -- *grid和zip的使用
# 遍历每一行记录每一行的和，当某一行处元素为1，结果加上该行和该列的和相乘的结果(-1是排除该元素)

class Solution(object):
    def numberOfRightTriangles(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        col_sum = [sum(col) - 1 for col in zip(*grid)]
        result = 0
        for row in grid:
            row_sum = sum(row) - 1
            result += row_sum * sum(cs for x, cs in zip(row, col_sum) if x)
        return result

