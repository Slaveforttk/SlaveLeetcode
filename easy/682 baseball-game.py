# _*_ coding : utf-8 _*_
# @Time : 2024/7/29 16:37
# @Author : Slave
# @File : 682 baseball-game
# @Project : LeetCode

class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        result = []
        for i in range(len(operations)):
            if operations[i] == "C":
                result.remove(result[-1])
            elif operations[i] == "+":
                result.append(result[-1] + result[-2])
            elif operations[i] == "D":
                result.append(result[-1] * 2)
            else:
                result.append(int(operations[i]))
        return result


if __name__ == "__main__":
    ops = ["5", "2", "C", "D", "+"]
    print(Solution().calPoints(ops))
