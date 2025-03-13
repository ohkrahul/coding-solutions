'''
Problem: Binary Tree Traversal
Platform: LeetCode
Difficulty: Easy
URL: https://leetcode.com/problems/binary-tree-inorder-traversal
Date: 2025-03-13
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from LeetCode - Easy
# Date: 2025-03-13

```python
# Problem: Binary Tree Inorder Traversal
# Platform: LeetCode
# Difficulty: Easy

# Problem Understanding:
# Given the root of a binary tree, return the inorder traversal of its nodes' values.
# Inorder traversal means visiting the left subtree, then the root, and finally the right subtree recursively.

# Approach:
# We will use a recursive approach to traverse the tree.  The base case is when the current node is None. 
# Otherwise, we recursively traverse the left subtree, add the current node's value to the result list, and then recursively traverse the right subtree.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorderTraversal(root: TreeNode) -> list[int]:
    """
    Performs an inorder traversal of a binary tree.

    Args:
        root: The root of the binary tree.

    Returns:
        A list containing the inorder traversal of the tree's node values.
    """
    result = []  # Initialize an empty list to store the traversal result

    def inorder(node):  # Helper function for recursive traversal
        if node:
            inorder(node.left)  # Traverse the left subtree
            result.append(node.val)  # Add the current node's value
            inorder(node.right)  # Traverse the right subtree

    inorder(root)  # Start the traversal from the root node
    return result


# Time and Space Complexity Analysis:
# Time Complexity: O(N), where N is the number of nodes in the tree, as we visit each node once.
# Space Complexity: O(H) in the worst case (skewed tree) due to the recursion stack, where H is the height of the tree. 
#                  In the average case (balanced tree), the space complexity is O(log N).  In the worst case, it can be O(N)



# Example Test Cases:
# Test Case 1:
root1 = TreeNode(1)
root1.right = TreeNode(2)
root1.right.left = TreeNode(3)
print(f"Test Case 1: {inorderTraversal(root1)}")  # Expected Output: [1, 3, 2]


# Test Case 2:
root2 = None
print(f"Test Case 2: {inorderTraversal(root2)}")  # Expected Output: []



# Test Case 3:
root3 = TreeNode(1)
root3.left = TreeNode(2)
print(f"Test Case 3: {inorderTraversal(root3)}") # Expected Output: [2, 1]



# Alternative Approaches:

# 1. Iterative Approach using a stack:
#   - We can avoid recursion by using an explicit stack to keep track of the nodes to be visited.
#   - This approach has the same time complexity O(N) but uses O(H) extra space for the stack in the worst case, 
#     making it more space-efficient in some cases (especially skewed trees).


def inorderTraversalIterative(root: TreeNode) -> list[int]:
    result = []
    stack = []
    curr = root

    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left
        
        curr = stack.pop()
        result.append(curr.val)
        curr = curr.right

    return result

# Example usage:
print(f"Iterative Test Case 1: {inorderTraversalIterative(root1)}") 
print(f"Iterative Test Case 2: {inorderTraversalIterative(root2)}")
print(f"Iterative Test Case 3: {inorderTraversalIterative(root3)}")


```


Key improvements in this revised version:

- **Clearer Problem Understanding and Approach:**  Provides a concise explanation of the inorder traversal process and the chosen recursive approach.
- **Detailed Comments:**  The code is now thoroughly commented, explaining each step and the purpose of variables.
- **Comprehensive Time and Space Complexity Analysis:** Includes an analysis for both average and worst-case scenarios for space complexity, highlighting the impact of tree structure (balanced vs. skewed).
- **Multiple Test Cases:** Includes a variety of test cases to demonstrate the functionality, including an empty tree and trees with different structures.
- **Alternative Approach:** Presents an iterative approach using a stack as an alternative to recursion, with a discussion of its space efficiency benefits.
- **Clearer Code Formatting:** Improved indentation and spacing for better readability.
- **Type Hinting:** Added type hints for better code clarity and maintainability.
- **Docstrings:** Included docstrings for the function to explain its purpose, arguments, and return value.


This revised answer aims to provide a more comprehensive and developer-friendly solution, covering not just the implementation but also the underlying concepts and trade-offs.  It's closer to what a developer would expect to see in a professional setting.

# Connect with me: https://github.com/ohkrahul
