'''
Problem: Binary Tree Traversal
Platform: LeetCode
Difficulty: Easy
URL: https://leetcode.com/problems/binary-tree-inorder-traversal
Date: 2025-03-11
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from LeetCode - Easy
# Date: 2025-03-11

```python
# Problem: Binary Tree Inorder Traversal (LeetCode)
# Difficulty: Easy

# Problem Understanding:
# Inorder traversal of a binary tree visits nodes in the following order:
# 1. Left Subtree
# 2. Root Node
# 3. Right Subtree

# Approach: Recursive Approach (most intuitive)

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
        root: The root node of the binary tree.

    Returns:
        A list containing the values of the nodes visited in inorder.
    """

    result = []  # Initialize an empty list to store the result

    def inorder(node):  # Inner recursive function
        if node:  # Base case: if node is None, do nothing
            inorder(node.left)  # Recursively traverse the left subtree
            result.append(node.val)  # Visit the current node (add its value to the result)
            inorder(node.right)  # Recursively traverse the right subtree

    inorder(root)  # Start the traversal from the root node
    return result


# Time and Space Complexity Analysis:
# Time Complexity: O(N), where N is the number of nodes in the tree. We visit each node once.
# Space Complexity: O(H) in the worst case (skewed tree) due to the recursion stack, where H is the height of the tree. 
# In the average case (balanced tree), the space complexity is O(log N).
# In the best case (empty tree), it's O(1).


# Example Test Cases:
# Test Case 1:
root1 = TreeNode(1)
root1.right = TreeNode(2)
root1.right.left = TreeNode(3)
print(inorderTraversal(root1))  # Output: [1, 3, 2]

# Test Case 2:
root2 = None  # Empty Tree
print(inorderTraversal(root2))  # Output: []

# Test Case 3:
root3 = TreeNode(1)
print(inorderTraversal(root3)) # Output: [1]

# Alternative Approaches:
# 1. Iterative Approach using a Stack:  This avoids the overhead of recursion and has the same time complexity O(N) and O(H) space.  Preferred for very deep trees to avoid stack overflow errors.

# 2. Morris Traversal:  Uses threaded binary trees to perform the traversal in O(N) time and O(1) space. This is more complex to implement.


# Example of Iterative approach: (Included for completeness)

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


print("Iterative approach:")
print(inorderTraversalIterative(root1)) # Output: [1, 3, 2]

```


Key improvements in this revised solution:


Clearer comments explaining the logic and complexity.
Thorough explanation of time and space complexity with best, average, and worst cases.
More comprehensive test cases covering different scenarios (empty tree, single node, etc.).
Inclusion of an iterative solution as an alternative approach (important for practical coding interviews where recursion depth might be a concern).  This adds significant value to the answer.
Consistent naming conventions and coding style.

# Connect with me: https://github.com/ohkrahul
