# _*_ coding : utf-8 _*_
# @Time : 2024/7/15 18:02
# @Author : Slave
# @File : Accounts Merge
# @Project : LeetCode

# 721
# 给定一个列表 accounts，每个元素 accounts[i] 是一个字符串列表，其中第一个元素 accounts[i][0] 是名称(name)，其余元素是 emails 表示该账户的邮箱地址。
# 现在，我们想合并这些账户。如果两个账户都有一些共同的邮箱地址，则两个账户必定属于同一个人。
# 请注意，即使两个账户具有相同的名称，它们也可能属于不同的人，因为人们可能具有相同的名称。一个人最初可以拥有任意数量的账户，但其所有账户都具有相同的名称。
# 合并账户后，按以下格式返回账户：每个账户的第一个元素是名称，其余元素是 按字符 ASCII 顺序排列 的邮箱地址。账户本身可以以 任意顺序返回

class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        # 构建哈希表，以邮箱地址为key值，用户下标为value
        hash_email = dict()
        for i, emails in enumerate(accounts):
            for email in emails[1:]:
                if hash_email.get(email):
                    hash_email[email].append(i)
                else:
                    hash_email[email] = [i]
        # 保存访问过的用户下标
        visited = [False] * len(accounts)

        def dfs(index):
            # 深度搜索字典中相同邮箱的用户所有邮箱集合
            visited[index] = True
            for email in accounts[index][1:]:
                if email in emails:
                    # 邮箱已经访问过，访问下一个邮箱
                    continue
                emails.add(email)
                # 访问这个邮箱下的所有用户邮箱
                for j in hash_email[email]:
                    if not visited[j]:
                        dfs(j)

        result = []
        for i, bol in enumerate(visited):
            if not visited[i]:
                # 保存访问的邮箱集合
                emails = set()
                dfs(i)
                result.append([accounts[i][0]] + sorted(emails))
        return result


if __name__ == '__main__':
    accounts = [["John", "johnsmith@mail.com", "john_newyork@mail.com"],
                ["John", "johnsmith@mail.com", "john00@mail.com"], ["Mary", "mary@mail.com"],
                ["John", "johnnybravo@mail.com"]]
    print(Solution().accountsMerge(accounts))
