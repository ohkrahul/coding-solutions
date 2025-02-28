'''
Problem: Binary Tree Traversal
Platform: LeetCode
Difficulty: Easy
URL: https://leetcode.com/problems/binary-tree-inorder-traversal
Date: 2025-02-28
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from LeetCode - Easy
# Date: 2025-02-28

```python
# Problem: Binary Tree Inorder Traversal (LeetCode)
# Difficulty: Easy

# 1. Problem Understanding and Approach

# The goal is to perform an inorder traversal of a given binary tree. Inorder traversal visits nodes in the following order: left subtree, root, right subtree.  We can achieve this recursively or iteratively using a stack.

# Approach: Recursive

# We'll use a recursive helper function. The base case is when the current node is None. Otherwise, we recursively traverse the left subtree, visit the root (add its value to the result list), and then recursively traverse the right subtree.


# 2. Time and Space Complexity Analysis

# Time Complexity: O(N), where N is the number of nodes in the tree. We visit each node exactly once.
# Space Complexity: O(H) in the worst case (skewed tree) due to recursion stack depth, where H is the height of the tree. In the average case (balanced tree), space complexity is O(log N).  In the iterative approach, space is also O(H).


# 3. Implementation

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorderTraversal(root: TreeNode):
    """
    Performs an inorder traversal of a binary tree.

    Args:
        root: The root of the binary tree.

    Returns:
        A list containing the values of the nodes visited in inorder.
    """

    result = []

    def inorder(node):
        if not node:  # Base case: empty node
            return

        inorder(node.left)  # Traverse left subtree
        result.append(node.val) # Visit root
        inorder(node.right)  # Traverse right subtree

    inorder(root)
    return result



# 4. Example Test Cases

# Test Case 1:  Single node tree
root1 = TreeNode(1)
print(inorderTraversal(root1))  # Output: [1]


# Test Case 2: Small balanced tree
root2 = TreeNode(1, TreeNode(2), TreeNode(3))
print(inorderTraversal(root2)) # Output: [2, 1, 3]

# Test Case 3: Skewed tree (left)
root3 = TreeNode(1, TreeNode(2, TreeNode(3)))
print(inorderTraversal(root3))  # Output: [3, 2, 1]


# Test Case 4: Empty tree
root4 = None
print(inorderTraversal(root4))  # Output: []


# 5. Alternative Approaches (Iterative)

def inorderTraversalIterative(root: TreeNode):
    """
    Performs an inorder traversal iteratively using a stack.
    """
    result = []
    stack = []
    curr = root

    while curr or stack:
        while curr:  # Go as left as possible
            stack.append(curr)
            curr = curr.left

        curr = stack.pop() # Process the node
        result.append(curr.val)

        curr = curr.right # Explore the right subtree

    return result

# Test Iterative
print("Iterative:")
print(inorderTraversalIterative(root1))  # Output: [1]
print(inorderTraversalIterative(root2)) # Output: [2, 1, 3]
print(inorderTraversalIterative(root3))  # Output: [3, 2, 1]
print(inorderTraversalIterative(root4))  # Output: []



```

# Connect with me: https://github.com/ohkrahul
