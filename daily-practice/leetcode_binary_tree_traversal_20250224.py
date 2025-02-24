'''
Problem: Binary Tree Traversal
Platform: LeetCode
Difficulty: Easy
URL: https://leetcode.com/problems/binary-tree-inorder-traversal
Date: 2025-02-24
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from LeetCode - Easy
# Date: 2025-02-24

1. **Problem understanding and approach**:
Inorder traversal of a binary tree means visiting the left subtree, then the root, and finally the right subtree.
We can use a recursive approach to solve this problem. The base case is when the root is `null`, in which case we do nothing. Otherwise, we recursively traverse the left subtree, then visit the root, and finally recursively traverse the right subtree.

2. **Time and space complexity analysis**:
The time complexity of this algorithm is `O(n)`, where `n` is the number of nodes in the tree. This is because we visit each node once. The space complexity is `O(h)`, where `h` is the height of the tree. This is because the recursive calls can stack up to a maximum depth of `h`.

3. **Well-commented implementation**:
```python
def inorder_traversal(root):
  """
  Performs an inorder traversal of a binary tree.

  Parameters:
    root: The root node of the binary tree.

  Returns:
    A list of the values in the binary tree in inorder.
  """

  if not root:
    return []

  return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right)
```

4. **Example test cases**:
```python
# Example 1:
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
assert inorder_traversal(root) == [2, 1, 3]

# Example 2:
root = TreeNode(1)
root.right = TreeNode(2)
assert inorder_traversal(root) == [1, 2]

# Example 3:
root = None
assert inorder_traversal(root) == []
```

5. **Alternative approaches**:
We can also use an iterative approach to perform inorder traversal. The idea is to use a stack to store the nodes that we need to visit. We start by pushing the root node onto the stack. Then, while the stack is not empty, we pop the top node from the stack and visit it. If the popped node has a right child, we push the right child onto the stack. Then, we push the left child of the popped node onto the stack.

The time complexity of the iterative approach is also `O(n)`, and the space complexity is `O(h)`.

# Connect with me: https://github.com/ohkrahul
