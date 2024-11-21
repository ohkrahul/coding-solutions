'''
Problem: Binary Tree Traversal
Platform: LeetCode
Difficulty: Easy
URL: https://leetcode.com/problems/binary-tree-inorder-traversal
Date: 2024-11-21
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from LeetCode - Easy
# Date: 2024-11-21

## Problem Understanding and Approach

Inorder traversal of a binary tree involves visiting the nodes in the following order: left subtree, root, and right subtree. We can use a recursive approach to solve this problem. The base case of the recursion is when the root is `None`, in which case we simply return. Otherwise, we recursively traverse the left subtree, visit the root, and then recursively traverse the right subtree.

## Time and Space Complexity Analysis

The time complexity of the algorithm is O(n), where n is the number of nodes in the binary tree. The algorithm visits each node exactly once, so the total time complexity is O(n). The space complexity of the algorithm is O(h), where h is the height of the binary tree. The algorithm uses a stack to store the nodes that have been visited but not yet processed. The maximum number of nodes that can be stored in the stack is h, which is the height of the binary tree.

## Well-Commented Implementation

```python
def inorderTraversal(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    result = []

    def helper(node):
        if not node:
            return

        helper(node.left)
        result.append(node.val)
        helper(node.right)

    helper(root)
    return result
```

## Example Test Cases

* Input: `[1, null, 2, 3]`
* Output: `[1, 3, 2]`

* Input: `[]`
* Output: `[]`

* Input: `[1]`
* Output: `[1]`

## Alternative Approaches

* **Iterative approach:** We can also use an iterative approach to perform inorder traversal. The idea is to use a stack to store the nodes that have been visited but not yet processed. We start by pushing the root node onto the stack. Then, while the stack is not empty, we pop the top node from the stack and visit it. If the node has a left child, we push the left child onto the stack. If the node has a right child, we push the right child onto the stack.
* **Morris traversal:** Morris traversal is a technique that allows us to perform inorder traversal without using a stack. The idea is to use a pointer to keep track of the current node. We start by setting the pointer to the root node. Then, we repeatedly move the pointer to the left until we reach a node that has no left child. At this point, we visit the node and then move the pointer to the right. We continue this process until we reach the end of the tree.

# Connect with me: https://github.com/ohkrahul
