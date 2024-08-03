# _*_ coding : utf-8 _*_
# @Time : 2024/7/14 13:13
# @Author : Slave
# @File : Max Increase to Keep City Skyline
# @Project : LeetCode

# 807
# 给你一座由 n x n 个街区组成的城市，每个街区都包含一座立方体建筑。给你一个下标从 0 开始的 n x n 整数矩阵 grid ，其中 grid[r][c] 表示坐落于 r 行 c 列的建筑物的高度 。
# 城市的 天际线是从远处观察城市时，所有建筑物形成的外部轮廓。从东、南、西、北四个主要方向观测到的 天际线 可能不同。
# 我们被允许为任意数量的建筑物 的高度增加 任意增量（不同建筑物的增量可能不同）
# 高度为 0 的建筑物的高度也可以增加。然而，增加的建筑物高度不能影响从任何主要方向观察城市得到的天际线 。
# 在不改变从任何主要方向观测到的城市 天际线 的前提下，返回建筑物可以增加的 最大高度增量总和

class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # 获取每行每列的最大值
        rolMax = list(map(max, grid))
        colMax = list(map(max, zip(*grid)))
        result = sum(min(rolMax[i[0]], colMax[j]) - node_h
                     for i in enumerate(grid) for j, node_h in enumerate(grid[i[0]]))
        return result

