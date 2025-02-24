from typing import Optional

"""
Given a binary tree root and an integer target, delete all the leaf nodes with value target.
Note that once you delete a leaf node with value target, if its parent node becomes a leaf node 
and has the value target, it should also be deleted (you need to continue doing that until you cannot).
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self._val = val
        self.left = left
        self.right = right

    @property
    def val(self):
        return self._val


class Solution:
    # Runtime 1 ms -> 54.51%
    # Memory 18.04 MB -> 99.52%
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        if not root:
            return None

        root.left = self.removeLeafNodes(root.left, target)
        root.right = self.removeLeafNodes(root.right, target)
        if not root.left and not root.right and root.val == target:
            return None
        return root


def result_print(root: TreeNode):
    q = [root]
    result = []

    while q:
        root = q.pop(0)
        result.append(root.val)
        if root.left:
            q.append(root.left)
        else:
            result.append('null')
        if root.right:
            q.append(root.right)
        else:
            result.append('null')

    print(result[:-2])


a = Solution()
result_print(a.removeLeafNodes(root=TreeNode(1, TreeNode(2, TreeNode(2, None, None), None), TreeNode(3, TreeNode(2, None, None), TreeNode(4, None, None))), target=2))  # [1,null,3,null,4]
# print(a.removeLeafNodes(root=[1, 2, 3, 2, None, 2, 4], target=2))  # [1,null,3,null,4]
# print(a.removeLeafNodes(root=[1, 3, 3, 3, 2], target=3))  # [1,3,null,null,2]
# print(a.removeLeafNodes(root=[1, 2, None, 2, None, 2], target=2))  # [1]
