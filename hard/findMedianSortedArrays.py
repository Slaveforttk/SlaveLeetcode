# _*_ coding : utf-8 _*_
# @Time : 2024/7/9 14:37
# @Author : Slave
# @File : findMedianSortedArrays
# @Project : LeetCode


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(nums1)
        n = len(nums2)

        # 比较两数组k/2-1处大小排除k-2个元素
        def findKmin(k):
            # 两个数组左下标
            L1, L2 = 0, 0
            while True:
                if L1 == m:
                    # 一数组元素全部排除
                    return nums2[L2 + k - 1]
                if L2 == n:
                    return nums1[L1 + k - 1]
                if k == 1:
                    return min(nums1[L1], nums2[L2])
                index1 = min(L1 + k // 2 - 1, m - 1)
                index2 = min(L2 + k // 2 - 1, n - 1)
                if nums1[index1] >= nums2[index2]:
                    # 排除二数组前k/2-1的元素即该元素之前都不可能为中值（最小只有k-2个元素小于）
                    k = k - (index2 - L2 + 1)
                    L2 = index2 + 1
                else:
                    # 排除一数组的前元素
                    k = k - (index1 - L1 + 1)
                    L1 = index1 + 1

        lenth = m + n
        if lenth % 2 == 1:
            # 奇数的情况下
            return findKmin((lenth + 1) // 2)
        else:
            return (findKmin((lenth) // 2) + findKmin((lenth) // 2 + 1)) / 2


if __name__ == '__main__':
    nums1 = [1, 2]
    nums2 = [3, 4]
    print(Solution().findMedianSortedArrays(nums1=nums1, nums2=nums2))
