# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    # in order traversing BST gives ascending sorted array
    def inOrder(self, root, result):
        if not root:
            return
        self.inOrder(root.left, result)
        result.append(root.val)
        self.inOrder(root.right, result)

    
    def merge(self, list1, list2):
        # merge sorted array
        merged = []
        i = 0
        j = 0
        
        while i < len(list1) and j < len(list2):
            if list1[i] < list2[j]:
                merged.append(list1[i])
                i += 1
            else:
                merged.append(list2[j])
                j += 1
        
        # add any leftovers
        merged.extend(list1[i:])
        merged.extend(list2[j:])
        
        return merged

    def getAllElements(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> List[int]:
        result1, result2 = [], []
        self.inOrder(root1, result1)
        self.inOrder(root2, result2)
        return self.merge(result1, result2)

     # T O(n) S O(n)