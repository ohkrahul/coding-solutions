'''
Problem: Binary Tree Traversal
Platform: LeetCode
Difficulty: Easy
URL: https://leetcode.com/problems/binary-tree-inorder-traversal
Date: 2024-12-22
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from LeetCode - Easy
# Date: 2024-12-22

## Problem Understanding and Approach

The binary tree inorder traversal involves visiting the left subtree, the current node, and then the right subtree. This approach ensures that the elements are visited in ascending order based on their values.

To achieve this, we can use a recursive approach. The base case occurs when we reach a leaf node (i.e., a node with no children). In such cases, the inorder traversal is complete for that branch, and we return.

Otherwise, for a node with children, we first traverse the left subtree (which will recursively traverse all nodes in the left subtree). Then, we visit the current node, and finally, we traverse the right subtree. This recursive process continues until all nodes in the binary tree have been visited.

## Time and Space Complexity Analysis

* **Time Complexity**: The time complexity of the inorder traversal is O(N), where N is the number of nodes in the binary tree. This is because each node in the tree is visited exactly once during the traversal.
* **Space Complexity**: The space complexity is O(H), where H is the height of the binary tree. This is because the recursive calls can go as deep as the height of the tree.

## Well-Commented Implementation

```python
def inorder_traversal(root):
  """
  Performs inorder traversal of a binary tree.

  Parameters:
    root: The root node of the binary tree.

  Returns:
    A list of values in the binary tree visited in inorder.
  """
  if not root:
    # If the root is None, the traversal is complete
    return []

  return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right)
```

## Example Test Cases

```python
# Test case 1
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
print(inorder_traversal(root))  # Output: [2, 1, 3]

# Test case 2
root = None
print(inorder_traversal(root))  # Output: []
```

## Alternative Approaches

An alternative approach to inorder traversal is using a stack. We start by pushing the root node onto the stack. Then, we repeatedly pop the top element from the stack and visit it. If the popped node has a right child, we push the right child onto the stack. If the popped node has a left child, we push the left child onto the stack. This process continues until the stack is empty, and all nodes have been visited.

This alternative approach has the same time and space complexity as the recursive approach. However, some developers may find it easier to understand and implement.

# Connect with me: https://github.com/ohkrahul
