# _*_ coding : utf-8 _*_
# @Time : 2024/7/7 14:51
# @Author : Slave
# @File : checkColor_way
# @Project : LeetCode

# 给你一个下标从 0 开始的 8 x 8 网格 board ，其中 board[r][c] 表示游戏棋盘上的格子 (r, c) 。棋盘上空格用 '.' 表示，白色格子用 'W' 表示，黑色格子用 'B' 表示。
# 游戏中每次操作步骤为：选择一个空格子，将它变成你正在执行的颜色（要么白色，要么黑色）。但是，合法 操作必须满足：涂色后这个格子是 好线段的一个端点 （好线段可以是水平的，竖直的或者是对角线）。
# 好线段 指的是一个包含 三个或者更多格子（包含端点格子）的线段，线段两个端点格子为 同一种颜色 ，且中间剩余格子的颜色都为 另一种颜色 （线段上不能有任何空格子）
# 简洁写法，利用向量组()()()()()进行8个方向循环
# 在可能为好线段的时候进行判定（方向相邻一个元素一定为不同元素）-- 以color结尾并且没有空

class Solution(object):
    def checkMove(self, board, rMove, cMove, color):
        """
        :type board: List[List[str]]
        :type rMove: int
        :type cMove: int
        :type color: str
        :rtype: bool
        """
        # 记录行列数
        m, n = len(board), len(board[0])
        for dx, dy in (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1):
            x, y = rMove + dx, cMove + dy
            if x < 0 or x >= m or y < 0 or y >= n or board[x][y] == '.' or board[x][y] == color:
                # 下一个方向遍历，即当前方向不可能存在好线段
                continue
            # 当该方向相邻一个为不同颜色的时候则进入判断好线段循环
            while True:
                x += dx
                y += dy
                if x < 0 or x >= m or y < 0 or y >= n or board[x][y] == '.':
                    break
                if board[x][y] == color:
                    return True
        return False

