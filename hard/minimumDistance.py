# _*_ coding : utf-8 _*_
# @Time : 2024/7/9 10:50
# @Author : Slave
# @File : minimumDistance
# @Project : LeetCode

# 给你一个下标从 0 开始的数组 points ，它表示二维平面上一些点的整数坐标，其中 points[i] = [xi, yi] 。
# 两点之间的距离定义为它们的曼哈顿距离，请你恰好移除一个点，返回移除后任意两点之间的最大距离可能的最小值
# 曼哈顿距离=|xi-xj|+|yi-yj|
# 最大值讨论=max(xi-xj,xj-xi)+max(yi-yj,yj-yi)
#         =max(xi-xj+yi-yj,xi-xj+yj-yi, xj-xi+yi-yj,xj-xi+yj-yi)
#         =max(|xi-yi-(xj-yj)|, |xi+yi-(xj+yj)|)
#         =max(max(xi-yi)-min(xj-yj), max(xi+yi)-min(xj+yj))

class Solution(object):
    def Distance(self, point1, point2):
        """
        :type point1: List[int]
        :type point2: List[int]
        :rtype: int
        """
        return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

    def _minimumDistance(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        result = float('inf')
        for i in range(len(points)):
            temp = -1
            for j in range(len(points)):
                # i点移除后的最大距离
                if j == i:
                    continue
                point = points[j]

                for z in range(len(points)):
                    if z == i or z == j:
                        continue
                    temp = max(temp, self.Distance(points[j], points[z]))
            # 该移除后更新最大距离最小情况
            result = min(temp, result)

        return result

    def minimumDistance(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        # max(max(xi-yi)-min(xj-yj), max(xi+yi)-min(xj+yj))
        point_info_add = []
        point_info_sub = []
        lenth = len(points)
        for i in range(lenth):
            # 记录每一个点的信息
            point_info_add.append((points[i][0] + points[i][1], i))
            point_info_sub.append((points[i][0] - points[i][1], i))
        point_info_sub.sort(key=lambda x: x[0])
        point_info_add.sort(key=lambda x: x[0])
        # 对于排序后最大曼哈顿距离为
        # max(point_info_sub[-1][0] - point_info_sub[0][0],
        #     point_info_add[-1][0] - point_info_add[0][0])
        # 考虑移除上述四点
        point_remove = [point_info_sub[-1][1], point_info_sub[0][1], point_info_add[-1][1], point_info_add[0][1]]
        # 记录移除后的最小最大距离
        result = float('inf')
        for i in point_remove:
            sub1 = point_info_sub[-1][0] if i != point_info_sub[-1][1] else point_info_sub[-2][0]

            sub2 = point_info_sub[0][0] if i != point_info_sub[0][1] else point_info_sub[1][0]

            add1 = point_info_add[-1][0] if i != point_info_add[-1][1] else point_info_add[-2][0]

            add2 = point_info_add[0][0] if i != point_info_add[0][1] else point_info_add[1][0]

            result = min(max(sub1 - sub2, add1 - add2), result)

        return result


if __name__ == '__main__':
    points = [[3, 10], [5, 15], [10, 2], [4, 4]]
    s = Solution()
    print(s.minimumDistance(points))
