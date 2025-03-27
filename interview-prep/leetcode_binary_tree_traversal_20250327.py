'''
Problem: Binary Tree Traversal
Platform: LeetCode
Difficulty: Easy
URL: https://leetcode.com/problems/binary-tree-inorder-traversal
Date: 2025-03-27
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from LeetCode - Easy
# Date: 2025-03-27

```python
# Problem: Binary Tree Inorder Traversal (LeetCode)
# Difficulty: Easy

# 1. Problem Understanding and Approach

# The inorder traversal of a binary tree is a depth-first search algorithm that visits nodes in the following order:
# 1. Left subtree
# 2. Root node
# 3. Right subtree

# We can implement this recursively or iteratively.  The recursive approach is often easier to understand, while the iterative approach avoids the overhead of function calls and potential stack overflow for very deep trees.  We'll implement both below.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 2. Time and Space Complexity Analysis

# Recursive Approach:
# - Time Complexity: O(N), where N is the number of nodes in the tree.  We visit each node once.
# - Space Complexity: O(H) in the worst case (skewed tree) due to recursion stack, where H is the height of the tree.  O(log N) on average for balanced trees.

# Iterative Approach:
# - Time Complexity: O(N), where N is the number of nodes.
# - Space Complexity: O(H) in the worst case (skewed tree) due to the stack, where H is the height of the tree. O(log N) on average for balanced trees.

# 3. Implementation

# Recursive Approach:
def inorderTraversal_recursive(root):
    """
    Performs inorder traversal of a binary tree recursively.

    Args:
        root: The root of the binary tree.

    Returns:
        A list containing the inorder traversal of the tree.
    """
    result = []

    def inorder(node):
        if node:
            inorder(node.left)
            result.append(node.val)
            inorder(node.right)

    inorder(root)
    return result



# Iterative Approach:
def inorderTraversal_iterative(root):
    """
    Performs inorder traversal of a binary tree iteratively.

    Args:
        root: The root of the binary tree.

    Returns:
        A list containing the inorder traversal of the tree.
    """

    result = []
    stack = []
    curr = root

    while curr or stack:  # Continue while there's a node to process or the stack isn't empty
        while curr:  # Go as far left as possible
            stack.append(curr)
            curr = curr.left

        curr = stack.pop()  # Process the leftmost node
        result.append(curr.val)
        curr = curr.right  # Move to the right subtree

    return result



# 4. Example Test Cases

# Test Case 1:
root1 = TreeNode(1, right=TreeNode(2, left=TreeNode(3)))
print(f"Recursive: {inorderTraversal_recursive(root1)}")  # Output: [1, 3, 2]
print(f"Iterative: {inorderTraversal_iterative(root1)}")  # Output: [1, 3, 2]

# Test Case 2:
root2 = None
print(f"Recursive: {inorderTraversal_recursive(root2)}")  # Output: []
print(f"Iterative: {inorderTraversal_iterative(root2)}")  # Output: []


# Test Case 3:
root3 = TreeNode(1)
print(f"Recursive: {inorderTraversal_recursive(root3)}")  # Output: [1]
print(f"Iterative: {inorderTraversal_iterative(root3)}")  # Output: [1]



# 5. Alternative Approaches (Morris Traversal)


# Morris Traversal is an alternative iterative approach that achieves O(1) space complexity by temporarily modifying the tree structure (threading). It's more complex to implement but offers improved space efficiency. We won't implement it here for the sake of simplicity, as the iterative approach using a stack is more common and easier to understand for an "Easy" level problem.

```

# Connect with me: https://github.com/ohkrahul
