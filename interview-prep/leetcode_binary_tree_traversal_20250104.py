'''
Problem: Binary Tree Traversal
Platform: LeetCode
Difficulty: Easy
URL: https://leetcode.com/problems/binary-tree-inorder-traversal
Date: 2025-01-04
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from LeetCode - Easy
# Date: 2025-01-04

**Problem Understanding and Approach:**

The inorder traversal of a binary tree visits the nodes in the following order: left subtree, root, and right subtree. We can implement this recursively by first traversing the left subtree, then visiting the root, and finally traversing the right subtree.

**Time and Space Complexity Analysis:**

Time Complexity: O(n), where n is the number of nodes in the tree. We visit each node once.
Space Complexity: O(h), where h is the height of the tree. The recursive calls create a stack of at most h frames.

**Well-commented Implementation:**

```python
def inorderTraversal(root):
    """
    Inorder traversal of a binary tree.

    Parameters:
        root (TreeNode): The root node of the tree.

    Returns:
        list: A list of the values of the nodes in inorder.
    """

    if root is None:
        return []

    return inorderTraversal(root.left) + [root.val] + inorderTraversal(root.right)
```

**Example Test Cases:**

```python
# Example 1:
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
expected = [2, 1, 3]
assert inorderTraversal(root) == expected

# Example 2:
root = None
expected = []
assert inorderTraversal(root) == expected
```

**Alternative Approaches:**

An alternative approach to inorder traversal is to use a stack. We start by pushing the root node onto the stack. While the stack is not empty, we pop the top node, visit it, and push its right child onto the stack. If the left child of the visited node is not None, we push it onto the stack. This process continues until the stack is empty.

# Connect with me: https://github.com/ohkrahul
