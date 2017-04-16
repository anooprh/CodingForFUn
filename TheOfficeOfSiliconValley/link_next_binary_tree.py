"""
A complete binary tree has an additional `next` field among its regular elements(`left` , `right`, `data`)

Given the root node, complete the tree such that it can be traversed in a level order with its `next` field
 
Follow up: can this solved with additional space ?

"""

from collections import deque

class TreeNode(object):
    def __init__(self, data, l=None, r=None, next=None):
      self.data = data
      self.left = l
      self.right = r
      self.next = next

# Time complexity O(n), space complexity O(n)
def completeTree(root):
    q = deque()
    q.append(root)
    while len(q) > 0:
        n = q.popleft()
        if n.left is not None: q.append(n.left)
        if n.right is not None: q.append(n.right)
        for item in q:
            n.next = item
            break

    return root

if __name__ == "__main__":
    two_node = TreeNode(2,TreeNode(4), TreeNode(5))
    three_node = TreeNode(3,TreeNode(6), TreeNode(7))
    tree = TreeNode(1, two_node, three_node)

    completeTree(tree)

    pass
