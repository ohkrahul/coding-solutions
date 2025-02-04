'''
Problem: Binary Tree Traversal
Platform: LeetCode
Difficulty: Easy
URL: https://leetcode.com/problems/binary-tree-inorder-traversal
Date: 2025-02-04
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from LeetCode - Easy
# Date: 2025-02-04

## Inorder Binary Tree Traversal

### Problem Understanding and Approach:

Inorder traversal, also known as left-root-right traversal, visits a node's left subtree, then the node itself, and lastly, the node's right subtree. We can use the recursive approach commonly known as the "divide and conquer" strategy to tackle this problem:

1. Base Case: If the tree is empty (i.e., the root node is null), there's nothing to traverse, so return immediately.
2. Recursive Case: For a non-empty tree, we follow the inorder traversal order:
   - Traverse the left subtree by recursively calling the traversal function on the left child node.
   - Visit the root node, i.e., print the value.
   - Traverse the right subtree by recursively calling the traversal function on the right child node.

### Time and Space Complexity Analysis:

- **Time Complexity:** O(N), where N is the number of nodes in the binary tree. This is because we visit each node precisely once during the traversal.
- **Space Complexity:** O(N) in the worst case, as the recursion stack can grow up to the height of the tree. However, in a balanced tree, the height is typically O(log N), resulting in a space complexity of O(log N).

### Well-commented Implementation:

```python
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        result = []  # Initialize an empty list to store the inorder traversal results.

        # Base case: If the tree is empty, return immediately.
        if not root:
            return result

        # Recursive case: Traverse the tree in inorder.
        result.extend(self.inorderTraversal(root.left))  # Traverse the left subtree.
        result.append(root.val)  # Visit the root node.
        result.extend(self.inorderTraversal(root.right))  # Traverse the right subtree.

        return result
```

### Example Test Cases:

1. Input: [1, null, 2, 3]
   Output: [1, 3, 2]

2. Input: []
   Output: []

3. Input: [1]
   Output: [1]

### Alternative Approaches:

- **Iterative Approach:** Using a stack to simulate the recursion, one can implement iterative inorder traversal. Start by pushing the root node into the stack. Then, while the stack is not empty, pop the top node from the stack, visit it, and push its right child (if any) into the stack. Repeat this process until the stack is empty.

- **Morris Traversal:** This is a space-optimized approach that uses thread pointers to eliminate the need for recursion or a stack. It involves creating a temporary link between a node and its predecessor and traversing the tree in a modified inorder fashion.

# Connect with me: https://github.com/ohkrahul
