# _*_ coding : utf-8 _*_
# @Time : 2024/7/31 22:16
# @Author : Slave
# @File : 3111 minimum-rectangles-to-cover-points
# @Project : LeetCode


# 3111 贪心算法
# 简单思想（简单题）
class Solution(object):
    def minRectanglesToCoverPoints(self, points, w):
        """
        :type points: List[List[int]]
        :type w: int
        :rtype: int
        """
        # 根据x坐标进行预排序
        points.sort(key=lambda x: x[0])
        result = 0
        n = len(points)
        # dx记录某个矩形的开端
        dx = points[0][0]
        for i in range(n):
            if i == n - 1:
                # 最后一个点不论自构成矩形或者参与构成都只需要+1
                result += 1
            if points[i][0] - dx <= w:
                continue
            else:
                # 上一个矩形构成完毕
                result += 1
                # 该点作为下个矩形的开端
                dx = points[i][0]
        return result
