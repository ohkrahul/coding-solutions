'''
Problem: Binary Tree Traversal
Platform: LeetCode
Difficulty: Easy
URL: https://leetcode.com/problems/binary-tree-inorder-traversal
Date: 2025-04-22
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from LeetCode - Easy
# Date: 2025-04-22

```python
# Problem: Binary Tree Inorder Traversal
# Platform: LeetCode
# Difficulty: Easy

# Problem Understanding:
# Given the root of a binary tree, return the inorder traversal of its nodes' values.
# Inorder traversal follows the Left-Root-Right order.

# Approach:
# We'll use a recursive approach to traverse the tree.  The base case is when we reach a null node.
# Otherwise, we recursively traverse the left subtree, then process the current node (add its value to the result), and finally recursively traverse the right subtree.

# Time and Space Complexity Analysis:
# Time Complexity: O(N), where N is the number of nodes in the tree. We visit each node exactly once.
# Space Complexity: O(H) in the worst case (skewed tree) due to the recursion stack, where H is the height of the tree.  In the best case (balanced tree), it's O(log N). Average case is also O(log N).


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorderTraversal(root):
    """
    Performs inorder traversal of a binary tree.

    Args:
        root: The root of the binary tree.

    Returns:
        A list containing the inorder traversal of the tree's node values.
    """

    result = []

    def inorder(node):
        # Base Case: Empty subtree
        if not node:
            return

        # Recursive call on the left subtree
        inorder(node.left)

        # Process the current node (add value to result)
        result.append(node.val)

        # Recursive call on the right subtree
        inorder(node.right)


    inorder(root)
    return result


# Example Test Cases
# Test Case 1: Single node
root1 = TreeNode(1)
print(f"Inorder Traversal of [1]: {inorderTraversal(root1)}")  # Expected: [1]

# Test Case 2: Small tree
root2 = TreeNode(1, right=TreeNode(2, left=TreeNode(3)))
print(f"Inorder Traversal of [1,null,2,3]: {inorderTraversal(root2)}") # Expected: [1, 3, 2]


# Test Case 3:  Larger balanced tree
root3 = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6),TreeNode(9)))
print(f"Inorder Traversal of larger tree: {inorderTraversal(root3)}") # Expected [1, 2, 3, 4, 6, 7, 9]

# Alternative Approaches:
# 1. Iterative approach using a stack: This approach avoids recursion and thus has O(H) space complexity in the worst-case due to the stack, and O(log N) space on average (and best case for balanced tree). The iterative approach can be slightly more complex to implement but avoids potential stack overflow issues for very deep trees.


# Iterative Inorder Traversal (using a stack)
def inorderTraversalIterative(root):
    result = []
    stack = []
    curr = root

    while curr or stack:  # Continue while we have nodes to process
        while curr:   # Go as far left as possible
            stack.append(curr)
            curr = curr.left

        curr = stack.pop() # Process the leftmost node (or the one popped from the stack)
        result.append(curr.val)

        curr = curr.right  # Move to the right subtree
    
    return result


print(f"Iterative Inorder Traversal of larger tree: {inorderTraversalIterative(root3)}") # Expected [1, 2, 3, 4, 6, 7, 9]

#  Morris Traversal: This is a less common but clever approach that achieves inorder traversal with O(1) space complexity (in-place).  It's more complex to implement but offers optimal space efficiency. This could be a good follow up question in an interview context.



```

# Connect with me: https://github.com/ohkrahul
