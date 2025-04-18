'''
Problem: Binary Tree Traversal
Platform: LeetCode
Difficulty: Easy
URL: https://leetcode.com/problems/binary-tree-inorder-traversal
Date: 2025-04-18
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from LeetCode - Easy
# Date: 2025-04-18

```python
# Problem: Binary Tree Inorder Traversal (LeetCode)
# Difficulty: Easy

# Problem Understanding:
# Given the root of a binary tree, return the inorder traversal of its nodes' values.
# Inorder traversal follows the pattern: Left -> Root -> Right.

# Approach:
# We will use a recursive approach to traverse the tree. The recursive function will 
# first traverse the left subtree, then add the root's value to the result, and finally
# traverse the right subtree.


# Time Complexity: O(N), where N is the number of nodes in the tree. We visit each node once.
# Space Complexity: O(H) in the worst case and O(log N) in the average case, where H is the height of the tree. 
#                  This is due to the recursive call stack. In the worst case (a skewed tree), H can be N.
#                  In a balanced tree, the height is logarithmic to the number of nodes.

from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorderTraversal(root: Optional[TreeNode]) -> List[int]:
    """
    Performs inorder traversal of a binary tree.

    Args:
      root: The root node of the binary tree.

    Returns:
      A list containing the inorder traversal of the tree's node values.
    """

    result = []

    def inorder(node):
        if not node:  # Base case: empty node
            return

        inorder(node.left)   # Traverse left subtree
        result.append(node.val)  # Visit root
        inorder(node.right)  # Traverse right subtree
    
    inorder(root)
    return result



# Example Test Cases:
# Test Case 1: Single node
root1 = TreeNode(1)
print(inorderTraversal(root1))  # Output: [1]


# Test Case 2: Small tree
root2 = TreeNode(1, None, TreeNode(2, TreeNode(3)))
print(inorderTraversal(root2))  # Output: [1, 3, 2]



# Test Case 3: Balanced tree
root3 = TreeNode(1, TreeNode(2), TreeNode(3))
print(inorderTraversal(root3))  # Output: [2, 1, 3]

# Test Case 4: Empty tree
root4 = None
print(inorderTraversal(root4)) # Output: []


# Alternative Approaches:

# 1. Iterative Approach using a stack:
#    We can perform inorder traversal iteratively using a stack. This approach avoids recursion and hence has a 
#    space complexity of O(H) in the worst case and O(logN) in the average case.
# 2. Morris Traversal:
#    Morris traversal achieves inorder traversal in O(N) time and O(1) space complexity by temporarily modifying
#    the tree structure (using threaded binary trees). It is less intuitive but very space efficient.
#   (Implementation not included here for brevity, but it can be found online).


```




# Connect with me: https://github.com/ohkrahul
