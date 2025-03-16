'''
Problem: Binary Tree Traversal
Platform: LeetCode
Difficulty: Easy
URL: https://leetcode.com/problems/binary-tree-inorder-traversal
Date: 2025-03-16
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from LeetCode - Easy
# Date: 2025-03-16

```python
# Problem: Binary Tree Inorder Traversal (LeetCode)
# Difficulty: Easy

# 1. Problem Understanding and Approach:

# The goal is to perform an inorder traversal of a binary tree.  Inorder traversal visits nodes in the order: Left subtree -> Root -> Right subtree.  
# We can achieve this recursively or iteratively using a stack.  The recursive approach is simpler to understand, while the iterative approach is sometimes preferred for avoiding potential stack overflow issues with very deep trees.

# 2. Time and Space Complexity Analysis:

# * Time Complexity: O(N), where N is the number of nodes in the tree.  We visit each node once.
# * Space Complexity:
#     - Recursive: O(H) in the worst case (skewed tree) due to the recursion stack, where H is the height of the tree. O(log N) in the average case for a balanced tree.
#     - Iterative: O(H) in the worst case (skewed tree) due to the stack used, where H is the height of the tree. O(log N) in the average case for a balanced tree.

# 3. Well-commented Implementation (Recursive):

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

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
            inorder(node.left)   # Traverse left subtree
            result.append(node.val) # Visit root
            inorder(node.right)  # Traverse right subtree

    inorder(root)
    return result


# 3. Well-commented Implementation (Iterative):

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

    while curr or stack:
        while curr: # Go left as far as possible
            stack.append(curr)
            curr = curr.left
        
        curr = stack.pop()   # Process the node
        result.append(curr.val)
        curr = curr.right   # Explore right subtree

    return result


# 4. Example Test Cases:

# Test Case 1:
root1 = TreeNode(1)
root1.right = TreeNode(2)
root1.right.left = TreeNode(3)
print(f"Recursive: {inorderTraversal_recursive(root1)}")  # Output: [1, 3, 2]
print(f"Iterative: {inorderTraversal_iterative(root1)}")  # Output: [1, 3, 2]



# Test Case 2:
root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(3)
print(f"Recursive: {inorderTraversal_recursive(root2)}")  # Output: [2, 1, 3]
print(f"Iterative: {inorderTraversal_iterative(root2)}")  # Output: [2, 1, 3]

# Test Case 3: Empty Tree
root3 = None
print(f"Recursive: {inorderTraversal_recursive(root3)}")  # Output: []
print(f"Iterative: {inorderTraversal_iterative(root3)}")  # Output: []



# 5. Alternative Approaches:

#  Morris Traversal: This is an advanced approach that achieves inorder traversal in O(N) time and O(1) space (excluding the output list). It manipulates the tree structure temporarily by using threaded binary trees.  However, it's generally more complex to implement and understand.


```

# Connect with me: https://github.com/ohkrahul
