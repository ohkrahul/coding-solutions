'''
Problem: Binary Tree Traversal
Platform: LeetCode
Difficulty: Easy
URL: https://leetcode.com/problems/binary-tree-inorder-traversal
Date: 2025-03-07
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from LeetCode - Easy
# Date: 2025-03-07

```python
# Problem: Binary Tree Inorder Traversal
# Platform: LeetCode
# Difficulty: Easy

# Problem Understanding and Approach:
# Inorder traversal visits a binary tree in the following order: Left subtree, root, right subtree. 
# We can achieve this recursively or iteratively. The recursive approach is easier to understand, 
# while the iterative approach avoids function call overhead for deep trees.

# Time Complexity: O(N), where N is the number of nodes in the tree. We visit each node once.
# Space Complexity: 
#   - Recursive: O(H) in the worst case (skewed tree) due to the recursion stack, where H is the height of the tree. 
#                 O(log N) on average for a balanced tree.
#   - Iterative: O(H) in the worst case (skewed tree) due to the stack used, where H is the height of the tree.
#                 O(log N) on average for a balanced tree.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal_recursive(self, root: TreeNode | None) -> list[int]:
        """
        Recursive inorder traversal.

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

    def inorderTraversal_iterative(self, root: TreeNode | None) -> list[int]:
        """
        Iterative inorder traversal using a stack.

        Args:
            root: The root of the binary tree.

        Returns:
             A list containing the inorder traversal of the tree.
        """
        result = []
        stack = []
        curr = root

        while curr or stack:
            while curr:  # Go left as far as possible
                stack.append(curr)
                curr = curr.left

            curr = stack.pop() # Visit the node
            result.append(curr.val)

            curr = curr.right # Explore the right subtree
        return result




# Example Test Cases:
root1 = TreeNode(1)
root1.right = TreeNode(2)
root1.right.left = TreeNode(3)

root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(3)


solution = Solution()

# Recursive approach
print(solution.inorderTraversal_recursive(root1))  # Output: [1, 3, 2]
print(solution.inorderTraversal_recursive(root2))  # Output: [2, 1, 3]
print(solution.inorderTraversal_recursive(None))  # Output: []


# Iterative approach
print(solution.inorderTraversal_iterative(root1))  # Output: [1, 3, 2]
print(solution.inorderTraversal_iterative(root2))  # Output: [2, 1, 3]
print(solution.inorderTraversal_iterative(None))  # Output: []




# Alternative Approaches (Morris Traversal):
# Morris Traversal performs inorder traversal without using recursion or a stack, thus achieving O(1) space complexity (excluding the output list). 
# It's more complex to implement but an interesting alternative for space-constrained scenarios.  It's not included here for brevity but can easily be added.
```

# Connect with me: https://github.com/ohkrahul
