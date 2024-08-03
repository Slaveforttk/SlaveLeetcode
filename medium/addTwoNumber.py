# _*_ coding : utf-8 _*_
# @Time : 2024/7/7 11:50
# @Author : Slave
# @File : addTwoNumber
# @Project : Leetcode

class Nodelist(object):
    def __init__(self, val=0, next=None):
        self.val = int(val)
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :param l1: 链表1
        :param l2: 链表2
        :return: Nodelist逆序链表相加结果
        """
        if l1.val == 0:
            return l2
        elif l2.val == 0:
            return l1
        l3 = Nodelist(val=0)
        head = l3
        val1, val2 = l1.val, l2.val
        while l1 is not None or l2 is not None:
            temp = val1 + val2 + l3.val
            l3.val = temp % 10
            l3.next = Nodelist(val=(temp / 10))
            l3 = l3.next
            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None
            val1 = l1.val if l1 is not None else 0
            val2 = l2.val if l2 is not None else 0
        return head


if __name__ == '__main__':
    l1 = Nodelist(9, Nodelist(9, Nodelist(9, Nodelist(9))))
    l2 = Nodelist(9,
                  Nodelist(9, Nodelist(9, Nodelist(9, Nodelist(9, Nodelist(9, Nodelist(9)))))))
    head = Solution().addTwoNumbers(l1, l2)
    while head is not None:
        print(head.val)
        head = head.next
