# _*_ coding : utf-8 _*_
# @Time : 2024/7/13 20:14
# @Author : Slave
# @File : Find if Array Can Be Sorted
# @Project : LeetCode

# 给你一个下标从0开始且全是正整数的数组 nums 。
# 一次操作中，如果两个相邻元素在二进制下数位为 1 的数目相同 ，那么你可以将这两个元素交换。你可以执行这个操作任意次（也可以 0 次）。
# 如果你可以使数组变有序，请你返回 true ，否则返回 false 。

class Solution(object):
    def canSortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # 分组循环
        # 尽可能将每个遍历到的相同二进制1数目数放在一组，当目前组最小的数大于上一组的时候就代表
        # 可以将数组排为有序的
        n = len(nums)
        i = now_ones = pre_max = now_max = 0
        while i < n:
            if bin(nums[i]).count('1') == now_ones:
                if nums[i] > pre_max:
                    now_max = max(now_max, nums[i])
                else:
                    # 当该组任一元素小于前一组时候则代表不可能切换为升序
                    return False
                i += 1
            else:
                # 不是上一组的元素，更新pre_max
                pre_max = now_max
                now_ones = bin(nums[i]).count('1')
        return True


if __name__ == '__main__':
    nums = [3, 16, 8, 4, 2]
    print(Solution().canSortArray(nums))
