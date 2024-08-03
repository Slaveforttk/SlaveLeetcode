# _*_ coding : utf-8 _*_
# @Time : 2024/7/8 12:17
# @Author : Slave
# @File : pivotIndex
# @Project : LeetCode

# 给你一个整数数组 nums ，请计算数组的 中心下标 。
# 数组 中心下标 是数组的一个下标，其左侧所有元素相加的和等于右侧所有元素相加的和。
# 如果中心下标位于数组最左端，那么左侧数之和视为 0 ，因为在下标的左侧不存在元素。这一点对于中心下标位于数组最右端同样适用。
# 如果数组有多个中心下标，应该返回 最靠近左边 的那一个。如果数组不存在中心下标，返回 -1

# 解法：设i处左侧之和为x，右侧之和为y，总数组和为total，即此处有y=total-x-nums[i]，y = x，即有2x=total-nums[i]

class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = sum(nums)
        pre = 0
        for i, num in enumerate(nums):
            if 2*pre + num == total:
                return i
            pre += num
        return -1


if __name__ == '__main__':
    nums = [-1, -1, 0, 1, 0, -1]
    print(Solution().pivotIndex(nums))
