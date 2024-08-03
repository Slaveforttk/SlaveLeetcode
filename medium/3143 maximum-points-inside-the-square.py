# _*_ coding : utf-8 _*_
# @Time : 2024/8/3 22:01
# @Author : Slave
# @File : 3143 maximum-points-inside-the-square
# @Project : LeetCode

# 3142 -- 哈希表的使用，记录次小和最小距离
# 给你一个二维数组 points 和一个字符串 s ，其中 points[i] 表示第 i 个点的坐标，s[i] 表示第 i 个点的 标签 。
#
# 如果一个正方形的中心在 (0, 0) ，所有边都平行于坐标轴，且正方形内 不 存在标签相同的两个点，那么我们称这个正方形是 合法 的。
#
# 请你返回 合法 正方形中可以包含的 最多 点数。
#
# 注意：
#
# 如果一个点位于正方形的边上或者在边以内，则认为该点位于正方形内。
# 正方形的边长可以为零

class Solution(object):
    def maxPointsInsideSquare(self, points, s):
        """
        :type points: List[List[int]]
        :type s: str
        :rtype: int
        """
        # 哈希表 -- 记录每个标号的最小
        max_edges = dict()
        # 此时边长次小为多少
        max_edge = float('inf')
        for i, point in enumerate(points):
            edge = max(abs(point[0]), abs(point[1]))
            if max_edges.get(s[i]) is None:
                max_edges[s[i]] = edge
            else:
                if edge >= max_edges.get(s[i]):
                    # 维护次小
                    max_edge = min(edge, max_edge)
                else:
                    # edge是最小的 -- 维护次小到max_edge
                    max_edge = min(max_edge, max_edges[s[i]])
                    # 存放最小的
                    max_edges[s[i]] = edge
        return sum(edge < max_edge for edge in max_edges.values())

