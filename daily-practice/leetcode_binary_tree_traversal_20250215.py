'''
Problem: Binary Tree Traversal
Platform: LeetCode
Difficulty: Easy
URL: https://leetcode.com/problems/binary-tree-inorder-traversal
Date: 2025-02-15
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from LeetCode - Easy
# Date: 2025-02-15

## 1. Problem Understanding and Approach

The problem requires us to implement the inorder traversal of a binary tree. Inorder traversal involves visiting the nodes of the tree in the following order: left subtree, current node, right subtree.

To solve this problem, we can use a recursive approach. We can define a function `inorderTraversal` that takes the root of the binary tree as its input. The function will then perform the following steps:

1. If the left subtree is not empty, call `inorderTraversal` recursively on the left subtree.
2. Visit the current node.
3. If the right subtree is not empty, call `inorderTraversal` recursively on the right subtree.

By following these steps, we can visit all the nodes of the binary tree in inorder.

## 2. Time and Space Complexity Analysis

The time complexity of the inorder traversal is O(n), where n is the number of nodes in the binary tree. This is because we visit each node of the tree once.

The space complexity of the inorder traversal is O(n), since we need to store the nodes of the tree in a stack.

## 3. Well-commented implementation

```python
def inorderTraversal(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    # If the root is empty, return an empty list
    if not root:
        return []

    # Create a stack to store the nodes of the tree
    stack = []

    # Push the root node onto the stack
    stack.append(root)

    # Create a list to store the inorder traversal
    inorder = []

    # While the stack is not empty
    while stack:
        # Pop the top node from the stack
        node = stack.pop()

        # Visit the node
        inorder.append(node.val)

        # If the node has a right child, push the right child onto the stack
        if node.right:
            stack.append(node.right)

        # If the node has a left child, push the left child onto the stack
        if node.left:
            stack.append(node.left)

    # Return the inorder traversal
    return inorder
```

## 4. Example test cases

```python
# Test case 1
root = [1, None, 2, 3]
expected = [1, 3, 2]
output = inorderTraversal(root)
assert output == expected

# Test case 2
root = []
expected = []
output = inorderTraversal(root)
assert output == expected

# Test case 3
root = [1]
expected = [1]
output = inorderTraversal(root)
assert output == expected
```

## 5. Alternative approaches

An alternative approach to implementing inorder traversal is to use an iterative approach. The iterative approach involves using a stack to store the nodes of the tree. We start by pushing the root node onto the stack. Then, while the stack is not empty, we pop the top node from the stack and visit it. If the node has a right child, we push the right child onto the stack. If the node has a left child, we push the left child onto the stack. We continue this process until the stack is empty.

The iterative approach has the same time and space complexity as the recursive approach. However, the iterative approach is often preferred because it is easier to implement and it does not require the use of recursion.

# Connect with me: https://github.com/ohkrahul
