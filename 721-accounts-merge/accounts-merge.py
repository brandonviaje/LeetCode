class DSU:
    def __init__(self, size):
        self.parent = [i for i in range(size)]  
        self.group_size = [1] * size         

    def find(self, node):
        # PATH COMPRESSION TO OPTIMIZE RUNTIME
        while node != self.parent[node]:
            self.parent[node] = self.parent[self.parent[node]]
            node = self.parent[node]
        return node

    def union(self, node1, node2):
        root1 = self.find(node1)
        root2 = self.find(node2)

        # its already in the same group 
        if root1 == root2:
            return False  

        # union smaller group to the bigger group
        if self.group_size[root1] > self.group_size[root2]:
            self.parent[root2] = root1
            self.group_size[root1] += self.group_size[root2]
        else:
            self.parent[root1] = root2
            self.group_size[root2] += self.group_size[root1]

        return True

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        """
        ["John","johnsmith@mail.com","john_newyork@mail.com"]
        ["John","johnsmith@mail.com","john00@mail.com"]
        ["Mary","mary@mail.com"]
        ["John","johnnybravo@mail.com"]

        ["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"]
        ["Mary","mary@mail.com"]
        ["John","johnnybravo@mail.com"]

        use a DSU to merge potential accounts together

        make the leading node the account index, since it would give us the same name but with a unique identifier
        iterate through the emails, if we find one already in our hashmap or set, then we unionize the current account index to the original 
        account index that we found earlier

        """

        # start as its own group
        dsu = DSU(len(accounts))
        emailToAcc = {}

        for i,account in enumerate(accounts):
            # account[i][0] is the name
            for email in account[1:]:
                # unionize these two together
                if email in emailToAcc:
                    dsu.union(i, emailToAcc[email]) 
                else:
                    emailToAcc[email] = i

        # take each index of account and map to its list of emails
        group = defaultdict(list) 
        for email, accountIndex in emailToAcc.items():
            owner = dsu.find(accountIndex)
            group[owner].append(email)

        result = []
        
        for i,emails in group.items():
            result.append([accounts[i][0]] + sorted(group[i]))

        return result