# _*_ coding : utf-8 _*_
# @Time : 2024/8/1 22:47
# @Author : Slave
# @File : LCP 40 心算挑战
# @Project : LeetCode


# LCP 40 LeetCode周赛
# 不是简单题目：需要考虑奇数时移除最小偶数还是移除最小奇数
# 贪心

class Solution(object):
    def maxmiumScore(self, cards, cnt):
        """
        :type cards: List[int]
        :type cnt: int
        :rtype: int
        """
        result = 0
        temp = 0
        # 记录结果的最小奇偶数
        even = odd = -1
        cards.sort(reverse=True)
        # 贪心将数组前cnt进行相加
        for i in range(cnt):
            temp += cards[i]
            if cards[i] % 2 == 1:
                odd = cards[i]
            else:
                even = cards[i]
        # 如果为偶数直接返回
        if temp % 2 == 0:
            return temp
        # 如果结果为奇数，有两种选择
        for i in range(cnt, len(cards)):
            if cards[i] % 2 == 1:
                # 替换数组中最小的偶数
                if even != -1:
                    result = max(result, temp - even + cards[i])
            else:
                if odd != -1:
                    result = max(result, temp - odd + cards[i])
        return result
