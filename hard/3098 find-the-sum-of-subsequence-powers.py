# _*_ coding : utf-8 _*_
# @Time : 2024/7/23 21:51
# @Author : Slave
# @File : find-the-sum-of-subsequence-powers
# @Project : LeetCode
from functools import cache
from typing import List


# 3098 动态记忆搜索 dfs深度搜索
class Solution:
    def sumOfPowers(self, nums: List[int], k: int) -> int:
        # dfs深度优先搜索
        # 动态记忆
        n = len(nums)
        mod = 10 ** 9 + 7
        # 预排序 -- 元素位置更换子序列依旧不变
        nums.sort()

        # 有序之后更容易计算最小差值
        # 构造dfs函数
        # dfs(i, j, k, mindiff) -- 此时遍历到i元素，上一个遍历的为j元素，还差k个构成子序列
        # 对任一元素nums[i]都有两种选择
        # 1. 该元素不加入子序列
        # 递推式 -- dfs(i+1, j, k, mindiff)
        # 2. 该元素加入子序列
        # 1) j == n 约定为子序列没有元素
        # 此时dfs(i+1, i, k-1, mindiff)
        # 2) j < n即在完善子序列的途中
        # 选择子序列中已经存在的最小差值
        # (此处为上次遍历的减去本次遍历 -- 上上次遍历减本次一定大于上次减本次 -- 预排序)
        # 此时dfs(i+1, i, k-1, min(mindiff, nums[i] - nums[j]))
        @cache
        # python cache 容器 -- 记录递归的值从而减少时间消耗
        def dfs(i, j, k, mindiff):
            # 边界条件
            if i >= n:
                # k = 0即完成子序列构成
                return mindiff if k == 0 else 0
            if n - i < k:
                # 剩余元素不足以构成k个元素的子序列
                return 0
            # 情况1：不包含i处元素的子序列
            ans = dfs(i + 1, j, k, mindiff)
            # 情况2：包含i处的子序列
            # 1) 子序列中没有元素(不存在实际mindiff)
            if j == n:
                ans += dfs(i + 1, i, k - 1, mindiff)
            # 2) 子序列已经存在一个实际mindiff即至少两个元素
            else:
                # i一定小于j(上次遍历为i+1)
                ans += dfs(i + 1, i, k - 1, min(mindiff, nums[i] - nums[j]))
            ans %= mod
            return ans

        return dfs(0, n, k, float('inf'))