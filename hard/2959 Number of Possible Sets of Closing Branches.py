# _*_ coding : utf-8 _*_
# @Time : 2024/7/17 10:59
# @Author : Slave
# @File : 2959 Number of Possible Sets of Closing Branches
# @Project : LeetCode

# 2959 未完成
# 二进制运算与集合与Floyed算法

class Solution(object):
    def numberOfSets(self, n, maxDistance, roads):
        """
        :type n: int
        :type maxDistance: int
        :type roads: List[List[int]]
        :rtype: int
        """
        # 构造距离矩阵
        matrix = [[float('inf')] * n for _ in range(n)]
        for i in range(len(roads)):
            if matrix[roads[i][0]][roads[i][1]] > roads[i][2]:
                matrix[roads[i][0]][roads[i][1]] = roads[i][2]
            if matrix[roads[i][1]][roads[i][0]] > roads[i][2]:
                matrix[roads[i][1]][roads[i][0]] = roads[i][2]
        # Floyed算法



if __name__ == '__main__':
    s = Solution()
    n = 3
    maxDistance = 5
    roads = [[0, 1, 2], [1, 2, 10], [0, 2, 10]]
    s.numberOfSets(n, maxDistance, roads)
