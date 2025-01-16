'''
Problem: Binary Tree Traversal
Platform: LeetCode
Difficulty: Easy
URL: https://leetcode.com/problems/binary-tree-inorder-traversal
Date: 2025-01-16
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from LeetCode - Easy
# Date: 2025-01-16

### 1. Problem Understanding and Approach

Inorder traversal of a binary tree visits the nodes in the following order: left subtree, root, and right subtree.

We can use a recursive approach to implement inorder traversal. The base case is when the current node is None, in which case we return. Otherwise, we recursively call inorder traversal on the left subtree, print the current node's value, and then recursively call inorder traversal on the right subtree.

### 2. Time and Space Complexity Analysis

The time complexity of inorder traversal is O(n), where n is the number of nodes in the tree. This is because we visit each node once.

The space complexity of inorder traversal is O(n), as we need to store the recursion stack.

### 3. Well-commented implementation

```python
def inorder_traversal(root):
  """
  Performs an inorder traversal of a binary tree.

  Args:
    root: The root node of the tree.

  Returns:
    A list of the values of the nodes in the tree, in order.
  """

  # Base case: if the root is None, return an empty list.
  if root is None:
    return []

  # Recursively call inorder traversal on the left subtree.
  left_values = inorder_traversal(root.left)

  # Add the value of the current node to the list.
  left_values.append(root.val)

  # Recursively call inorder traversal on the right subtree.
  right_values = inorder_traversal(root.right)

  # Return the concatenation of the left, current, and right values.
  return left_values + right_values
```

### 4. Example test cases

```python
# Test case 1: an empty tree
root = None
assert inorder_traversal(root) == []

# Test case 2: a tree with a single node
root = TreeNode(1)
assert inorder_traversal(root) == [1]

# Test case 3: a tree with multiple nodes
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
assert inorder_traversal(root) == [2, 1, 3]
```

### 5. Alternative approaches

There are other ways to implement inorder traversal, such as using a stack or using the Morris traversal algorithm.

The stack-based approach uses a stack to keep track of the nodes that have been visited. The algorithm starts by pushing the root node onto the stack. Then, while the stack is not empty, the algorithm pops the top node from the stack and prints its value. If the popped node has a right child, the algorithm pushes the right child onto the stack. Then, the algorithm pushes the left child of the popped node onto the stack.

The Morris traversal algorithm does not use a stack. Instead, it uses a pointer to keep track of the current node. The algorithm starts by setting the pointer to the root node. Then, while the pointer is not None, the algorithm checks if the pointer has a left child. If it does, the algorithm finds the predecessor of the pointer's left child and sets the pointer's left child to the predecessor. Then, the algorithm sets the pointer to the pointer's left child. If the pointer does not have a left child, the algorithm prints the pointer's value and sets the pointer to the pointer's right child.

# Connect with me: https://github.com/ohkrahul
