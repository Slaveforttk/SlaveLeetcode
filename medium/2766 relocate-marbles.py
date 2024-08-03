# _*_ coding : utf-8 _*_
# @Time : 2024/7/24 14:29
# @Author : Slave
# @File : 2766 relocate-marbles
# @Project : LeetCode

# 2766 哈希表的运用
# 给你一个下标从 0 开始的整数数组 nums ，表示一些石块的初始位置。再给你两个长度 相等 下标从 0 开始的整数数组 moveFrom 和 moveTo 。
# 在 moveFrom.length 次操作内，你可以改变石块的位置。在第 i 次操作中，你将位置在 moveFrom[i] 的所有石块移到位置 moveTo[i] 。
# 完成这些操作后，请你按升序返回所有有石块的位置。
# 注意：
# 如果一个位置至少有一个石块，我们称这个位置 有 石块。
# 一个位置可能会有多个石块
# 1为复杂写法 -- 多次集合dict转换
# 实际解法参考2 -- 哈希集合的使用

class Solution(object):
    def relocateMarbles1(self, nums, moveFrom, moveTo):
        """
        :type nums: List[int]
        :type moveFrom: List[int]
        :type moveTo: List[int]
        :rtype: List[int]
        """
        # 哈希字典存储各石头位置
        positions = dict()
        for i in range(len(nums)):
            if positions.get(nums[i]) is None:
                positions[nums[i]] = 1
            else:
                positions[nums[i]] += 1
        for i in range(len(moveFrom)):
            positions[moveTo[i]] = positions[moveFrom[i]]
            if moveTo[i] != moveFrom[i]:
                positions.pop(moveFrom[i])
        result = set()
        for position, value in positions.items():
            for _ in range(value):
                result.add(position)
        result = list(result)
        result.sort()
        return result

    def relocateMarbles2(self, nums, moveFrom, moveTo):
        """
        :type nums: List[int]
        :type moveFrom: List[int]
        :type moveTo: List[int]
        :rtype: List[int]
        """
        st = set(nums)
        for f, t in zip(moveFrom, moveTo):
            st.remove(f)
            st.add(t)
        return sorted(st)


if __name__ == '__main__':
    s = Solution()
    nums = [1, 6, 7, 8]
    moveFrom = [1, 7, 2]
    moveTo = [2, 9, 5]
    print(s.relocateMarbles1(nums, moveFrom, moveTo))
    print(s.relocateMarbles2(nums, moveFrom, moveTo))
