'''
Problem: Binary Tree Traversal
Platform: LeetCode
Difficulty: Easy
URL: https://leetcode.com/problems/binary-tree-inorder-traversal
Date: 2024-12-03
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from LeetCode - Easy
# Date: 2024-12-03

## Problem Understanding and Approach

Given a binary tree, the task is to perform an inorder traversal. Inorder traversal processes the nodes in the left subtree, then the root, and finally the right subtree.

Here's the general approach for inorder traversal:

1. If the current node is not null, traverse it recursively in the following order:
   - Left subtree
   - Root node
   - Right subtree

2. Once the current node is processed, add its value to the result array or perform the desired operation with it.

## Time and Space Complexity Analysis

**Time Complexity**: O(N), where N is the number of nodes in the binary tree. Since we traverse each node once, the overall time complexity is linear.

**Space Complexity**: O(N), where N is the number of nodes in the binary tree. In the worst case, the recursion stack can grow up to O(N) for an unbalanced tree.

## Well-Commented Implementation

```python
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []  # List to store the inorder traversal result

        # Recursively traverse the binary tree
        def inorder(curr_node):
            if not curr_node:  # Base case: Check if the current node is null
                return

            # Recursively traverse the left subtree
            inorder(curr_node.left)

            # Process the current node
            result.append(curr_node.val)

            # Recursively traverse the right subtree
            inorder(curr_node.right)

        inorder(root)
        return result
```

## Example Test Cases

**Test Case 1:**

```
Input: [1,null,2,3]
Output: [1,3,2]
```

**Test Case 2:**

```
Input: []
Output: []
```

## Alternative Approaches

**Iterative Approach:**

Instead of using recursion, we can use an iterative approach with a stack to perform inorder traversal. The idea is to push the left subtree nodes onto the stack until we reach the leftmost node. Then, pop the current node from the stack, visit it, and push the right subtree nodes onto the stack. Repeat this process until the stack is empty.

The iterative approach has the same time and space complexity as the recursive approach.

**Morris Traversal:**

Morris Traversal is a technique to perform inorder traversal without using recursion or a stack. The idea is to modify the tree structure temporarily to create a doubly linked list, perform the traversal, and then restore the original tree structure.

Morris Traversal has a time complexity of O(N) and a space complexity of O(1).

# Connect with me: https://github.com/ohkrahul
