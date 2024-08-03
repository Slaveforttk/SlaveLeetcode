# _*_ coding : utf-8 _*_
# @Time : 2024/7/16 11:07
# @Author : Slave
# @File : Find Common Elements Between Two Arrays
# @Project : LeetCode

# 2956
# 给你两个下标从 0 开始的整数数组 nums1 和 nums2 ，它们分别含有 n 和 m 个元素。
# 请你计算以下两个数值：
# 统计 0 <= i < n 中的下标 i ，满足 nums1[i] 在 nums2 中 至少 出现了一次。
# 统计 0 <= i < m 中的下标 i ，满足 nums2[i] 在 nums1 中 至少 出现了一次。
# 请你返回一个长度为 2 的整数数组 answer ，按顺序 分别为以上两个数值
# 1为复杂哈希写法
# 2为简洁哈希写法（使用集合）
# 运行时间基本一致

class Solution(object):
    def findIntersectionValues1(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result = [0, 0]
        nums1_dict = dict()
        nums2_dict = dict()
        for i in range(max(len(nums1), len(nums2))):
            if i < len(nums1):
                # 创建nums1的哈希表
                if nums1_dict.get(nums1[i]) is None:
                    # 遍历到首个未加入哈希表的数字
                    # 加入到哈希表并且将数量置为1
                    nums1_dict[nums1[i]] = 1
                else:
                    # 如果该数字已经存在于哈希表中则数量+1
                    nums1_dict[nums1[i]] += 1
            if i < len(nums2):
                if nums2_dict.get(nums2[i]) is None:
                    nums2_dict[nums2[i]] = 1
                else:
                    nums2_dict[nums2[i]] += 1
        for i in range(max(len(nums1), len(nums2))):
            # 对两个集合进行遍历(集合保证不遍历到重复元素)
            if i < len(nums1) and nums2_dict.get(nums1[i]):
                result[0] += 1
            if i < len(nums2) and nums1_dict.get(nums2[i]):
                result[1] += 1
        return result

    def findIntersectionValues(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        s1, s2 = set(nums1), set(nums2)
        return [sum(x in s2 for x in nums1), sum(x in s1 for x in nums2)]
