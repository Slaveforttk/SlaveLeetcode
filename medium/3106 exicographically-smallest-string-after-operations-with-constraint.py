# _*_ coding : utf-8 _*_
# @Time : 2024/7/27 22:19
# @Author : Slave
# @File : 3106 exicographically-smallest-string-after-operations-with-constraint
# @Project : LeetCode

# 3106 贪婪策略的使用(更像简单题) -- 字典序的理解(翻字典的顺序即ba > ac > ab > aa)
# 给你一个字符串 s 和一个整数 k 。
# 定义函数 distance(s1, s2) ，用于衡量两个长度为 n 的字符串 s1 和 s2 之间的距离，即：
# 字符 'a' 到 'z' 按 循环 顺序排列，对于区间 [0, n - 1] 中的 i ，计算所有「 s1[i] 和 s2[i] 之间 最小距离」的 和 。
# 例如，distance("ab", "cd") == 4 ，且 distance("a", "z") == 1 。
# 你可以对字符串 s 执行 任意次 操作。在每次操作中，可以将 s 中的一个字母 改变 为 任意 其他小写英文字母。
# 返回一个字符串，表示在执行一些操作后你可以得到的 字典序最小 的字符串 t ，且满足 distance(s, t) <= k 。

class Solution(object):
    def getSmallestString(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        # 贪婪策略 -- 优先将字符变为a，如果剩余步骤次数大于等于变为a的距离
        # 如果小于则用完所有次数尽可能小(从左进行减小 -- 并非逼近a)
        result = list(s)
        for i, element in enumerate(s):
            # 往该元素前后进行对比。寻找最小变为a的距离
            distance = min(ord(s[i]) - ord('a'), ord('z') - ord(s[i]) + 1)
            if distance <= k:
                result[i] = 'a'
                k -= distance
            else:
                result[i] = chr(ord(s[i]) - k)
                break
        return "".join(result)
