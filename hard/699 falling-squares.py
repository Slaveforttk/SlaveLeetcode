# _*_ coding : utf-8 _*_
# @Time : 2024/7/28 22:24
# @Author : Slave
# @File : 699 falling-squares
# @Project : LeetCode

# 699 线段树 -- 待补充
# 方法1： 暴力求解
# 在二维平面上的 x 轴上，放置着一些方块。
# 给你一个二维整数数组 positions
# 其中 positions[i] = [lefti, sideLengthi] 表示：第 i 个方块边长为 sideLengthi ，其左侧边与 x 轴上坐标点 lefti 对齐。
# 每个方块都从一个比目前所有的落地方块更高的高度掉落而下。
# 方块沿 y 轴负方向下落，直到着陆到另一个正方形的顶边或者x轴上 。
# 一个方块仅仅是擦过另一个方块的左侧边或右侧边不算着陆。一旦着陆，它就会固定在原地，无法移动。
# 在每个方块掉落后，你必须记录目前所有已经落稳的 方块堆叠的最高高度 。
# 返回一个整数数组 ans ，其中 ans[i] 表示在第 i 块方块掉落后堆叠的最高高度

class Solution(object):
    def fallingSquares(self, positions):
        """
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        # 暴力求解
        n = len(positions)
        # 记录所有方块掉落的高度
        height = [0] * n
        for i, (left1, size) in enumerate(positions):
            # 必须落在方块上而不是擦边所以-1
            right1 = left1 + size - 1
            height[i] = size
            for j in range(i):
                # 枚举前面的所有方块，并更新高度
                left2, right2 = positions[j][0], positions[j][0] + positions[j][1] - 1
                if left1 <= right2 and left2 <= right1:
                    # 如果可以落下则更新高度
                    height[i] = max(height[i], height[j] + size)
        for i in range(1, n):
            # 从前往后更新结果
            height[i] = max(height[i], height[i - 1])
        return height


if __name__ == '__main__':
    positions = [[1, 2], [2, 3], [6, 1]]
    print(Solution().fallingSquares(positions))
