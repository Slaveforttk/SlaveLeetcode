# _*_ coding : utf-8 _*_
# @Time : 2024/7/10 11:33
# @Author : Slave
# @File : Count the Number of Incremovable Subarrays I
# @Project : LeetCode


# 给你一个下标从0开始的正整数数组nums
# 如果 nums 的一个子数组满足：移除这个子数组后剩余元素 严格递增
# 那么我们称这个子数组为 移除递增 子数组。
# 比方说，[5, 3, 4, 6, 7] 中的 [3, 4] 是一个移除递增子数组，因为移除该子数组后，[5, 3, 4, 6, 7] 变为 [5, 6, 7] ，是严格递增的。
# 请你返回 nums 中 移除递增 子数组的总数目。
# 注意 ，剩余元素为空的数组也视为是递增的。
# 子数组 指的是一个数组中一段连续的元素序列
# II方法为优化的滑动窗口，普通方法为暴力滑动窗口

class Solution(object):
    def incremovableSubarrayCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def check(start, k):
            """
            :type start: int
            :type k: int
            :rtype: bool
            """
            if len(nums) - 1 <= k <= len(nums):
                # 特殊情况
                return True
            for i in range(len(nums) - 1):
                if start <= i < start + k:
                    continue
                if i == start - 1:
                    if start + k >= len(nums):
                        continue
                    if nums[i] >= nums[start + k]:
                        return False
                    else:
                        continue
                if nums[i] >= nums[i + 1]:
                    return False
            return True
        result = 0
        for i in range(len(nums)):
            # 尽可能删除从开头删除最多元素
            # 当任一尽可能多元素被删除后不递增即代表该起始元素已经遍历完
            for k in range(len(nums) - i, 0, -1):
                if check(i, k) is True:
                    result += 1
                else:
                    break
        return

    def incremovableSubarrayCountII(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 寻找前缀和后缀递增数组
        n = len(nums)
        left, right = 0, n - 1
        while left < n - 1 and nums[left] < nums[left + 1]: left += 1
        while right > left and nums[right] > nums[right - 1]: right -= 1
        # 特殊情况，整个数组递增，即删除任一子数组都递增
        if left == right:
            return n * (n + 1) // 2

        # 数组被分为三个部分：[0,left]递增，[right, n-1]递增，[left, right]非严格递增
        # 代表[left+1, right-1]必须删除
        # 枚举[0,left+1]，使用[i,j]代表删除元素的窗口
        # 特殊情况 -- 删除j前面所有元素即i < 0
        j = right
        # 此时删除子数组数量为右侧剩余元素个数即n - j + 1(+1为子数组不包含j)
        result = n - j + 1
        for i in range(left + 1):
            # 枚举左边界, 当左边界值大于等于右边界时，有边界必须删除即j+1
            while j < n and nums[i] >= nums[j]: j += 1
            result += n - j + 1  # 子数组为[j, n] // [i, j]中间的子数组

        return result


if __name__ == '__main__':
    nums = [6, 5, 7, 8]
    print(Solution().incremovableSubarrayCount(nums))
