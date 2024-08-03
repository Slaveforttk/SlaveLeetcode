# _*_ coding : utf-8 _*_
# @Time : 2024/7/7 14:07
# @Author : Slave
# @File : checkColor
# @Project : LeetCode

# 枚举法暴力求解--遍历8个方向
class Solution(object):
    def leftMove(self, board, rMove, cMove, color):
        # 进行左边线段检查,使用i记录线段是否合法
        i = 0
        c = cMove - 1
        anotherColor = 'W' if color == 'B' else 'B'
        while c >= 0:
            if board[rMove][c] == anotherColor:
                i += 1
            elif board[rMove][c] == color:
                if i > 0:
                    return True
                else:
                    return False
            if board[rMove][c] == '.':
                return False
            c -= 1
        return False

    def rightMove(self, board, rMove, cMove, color):
        # 进行右边线段检查,使用i记录线段是否合法
        i = 0
        c = cMove + 1
        anotherColor = 'W' if color == 'B' else 'B'
        while c < 8:
            if board[rMove][c] == anotherColor:
                i += 1
            elif board[rMove][c] == color:
                if i > 0:
                    return True
                else:
                    return False
            if board[rMove][c] == '.':
                return False
            c += 1
        return False

    def upMove(self, board, rMove, cMove, color):
        # 进行上边线段检查,使用i记录线段是否合法
        i = 0
        r = rMove - 1
        anotherColor = 'W' if color == 'B' else 'B'
        while r >= 0:
            if board[r][cMove] == anotherColor:
                i += 1
            elif board[r][cMove] == color:
                if i > 0:
                    return True
                else:
                    return False
            if board[r][cMove] == '.':
                return False
            r -= 1
        return False

    def downMove(self, board, rMove, cMove, color):
        # 进行下边线段检查,使用i记录线段是否合法
        i = 0
        r = rMove + 1
        anotherColor = 'W' if color == 'B' else 'B'
        while r < 8:
            if board[r][cMove] == anotherColor:
                i += 1
            elif board[r][cMove] == color:
                if i > 0:
                    return True
                else:
                    return False
            if board[r][cMove] == '.':
                return False
            r += 1
        return False

    def leftDigmove(self, board, rMove, cMove, color):
        # 进行左主对角线段检查,使用i记录线段是否合法
        i = 0
        c = cMove - 1
        r = rMove - 1
        anotherColor = 'W' if color == 'B' else 'B'
        while c >= 0 and r >= 0:
            if board[r][c] == anotherColor:
                i += 1
            elif board[r][c] == color:
                if i > 0:
                    return True
                else:
                    return False
            if board[r][c] == '.':
                return False
            r -= 1
            c -= 1
        return False

    def rightDigmove(self, board, rMove, cMove, color):
        # 进行右主对角线段检查,使用i记录线段是否合法
        i = 0
        c = cMove + 1
        r = rMove + 1
        anotherColor = 'W' if color == 'B' else 'B'
        while c < 8 and r < 8:
            if board[r][c] == anotherColor:
                i += 1
            elif board[r][c] == color:
                if i > 0:
                    return True
                else:
                    return False
            if board[r][c] == '.':
                return False
            r += 1
            c += 1
        return False

    def leftDeputydigMove(self, board, rMove, cMove, color):
        # 进行左副对角线段检查,使用i记录线段是否合法
        i = 0
        c = cMove - 1
        r = rMove + 1
        anotherColor = 'W' if color == 'B' else 'B'
        while c >= 0 and r < 8:
            if board[r][c] == anotherColor:
                i += 1
            elif board[r][c] == color:
                if i > 0:
                    return True
                else:
                    return False
            if board[r][c] == '.':
                return False
            r += 1
            c -= 1
        return False

    def rightDeputydigMove(self, board, rMove, cMove, color):
        # 进行右副对角线段检查,使用i记录线段是否合法
        i = 0
        c = cMove + 1
        r = rMove - 1
        anotherColor = 'W' if color == 'B' else 'B'
        while c < 8 and r >= 0:
            if board[r][c] == anotherColor:
                i += 1
            elif board[r][c] == color:
                if i > 0:
                    return True
                else:
                    return False
            if board[r][c] == '.':
                return False
            r -= 1
            c += 1
        return False

    def checkMove(self, board, rMove, cMove, color):
        """
        :type board: List[List[str]]
        :type rMove: int
        :type cMove: int
        :type color: str
        :rtype: bool
        """
        if (self.leftMove(board, rMove, cMove, color)
                or self.rightMove(board, rMove, cMove, color)
                or self.upMove(board, rMove, cMove, color)
                or self.downMove(board, rMove, cMove, color)
                or self.leftDigmove(board, rMove, cMove, color)
                or self.rightDigmove(board, rMove, cMove, color)
                or self.leftDeputydigMove(board, rMove, cMove, color)
                or self.rightDeputydigMove(board, rMove, cMove, color)):
            return True
        else:
            return False


if __name__ == '__main__':
    board = [["B", "B", ".", ".", "B", "W", "W", "."], [".", "W", "W", ".", "B", "W", "B", "B"],
             [".", "W", "B", "B", "W", ".", "W", "."], ["B", ".", ".", "B", "W", "W", "W", "."],
             ["W", "W", "W", "B", "W", ".", "B", "W"], [".", ".", ".", "W", ".", "W", ".", "B"],
             ["B", "B", "W", "B", "B", "W", "W", "B"], ["W", ".", "W", "W", ".", "B", ".", "W"]]
    rMove = 2
    cMove = 5
    color = 'W'
    solution = Solution()
    print(solution.leftMove(board, rMove, cMove, color))
    print(solution.rightMove(board, rMove, cMove, color))
    print(solution.upMove(board, rMove, cMove, color))
    print(solution.downMove(board, rMove, cMove, color))
    print(solution.checkMove(board, rMove, cMove, color))
