# _*_ coding : utf-8 _*_
# @Time : 2024/7/22 18:52
# @Author : Slave
# @File : 2101 detonate-the-maximum-bombs
# @Project : LeetCode

# 2101 引爆最多炸弹
# 深度优先查找 -- dfs复习
# 给你一个炸弹列表。一个炸弹的 爆炸范围 定义为以炸弹为圆心的一个圆。
# 炸弹用一个下标从 0 开始的二维整数数组 bombs 表示，其中 bombs[i] = [xi, yi, ri] 。
# xi 和 yi 表示第 i 个炸弹的 X 和 Y 坐标，ri 表示爆炸范围的 半径 。
# 你需要选择引爆 一个 炸弹。当这个炸弹被引爆时，所有 在它爆炸范围内的炸弹都会被引爆，这些炸弹会进一步将它们爆炸范围内的其他炸弹引爆。
# 给你数组 bombs ，请你返回在引爆 一个 炸弹的前提下，最多 能引爆的炸弹数目

class Solution(object):
    def maximumDetonation(self, bombs):
        """
        :type bombs: List[List[int]]
        :rtype: int
        """
        # dfs 深度优先搜索
        # 遍历坐标，构建引爆列表
        g = [[] for _ in range(len(bombs))]
        for i, [x0, y0, r0] in enumerate(bombs):
            for j, [x, y, r] in enumerate(bombs):
                if i == j:
                    continue
                dx = x0 - x
                dy = y0 - y
                # 两圆心距离小于等于圆0的半径
                if dx * dx + dy * dy <= r0 * r0:
                    # 可以连带引爆
                    g[i].append(j)
        # 引爆列表完成，dfs深度查找连续引爆实现：
        def dfs(i):
            visited[i] = True
            max_bombs = 1
            for j in g[i]:
                if visited[j] is False:
                    max_bombs += dfs(j)
            return max_bombs
        # 循环查找最大引爆数量
        result = 0
        for i in range(len(bombs)):
            visited = [False for _ in range(len(bombs))]
            result = max(result, dfs(i))
        return result
