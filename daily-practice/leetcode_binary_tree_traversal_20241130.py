'''
Problem: Binary Tree Traversal
Platform: LeetCode
Difficulty: Easy
URL: https://leetcode.com/problems/binary-tree-inorder-traversal
Date: 2024-11-30
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from LeetCode - Easy
# Date: 2024-11-30

## Problem Understanding and Approach
### Problem Understanding
The problem asks us to implement the inorder traversal of a binary tree. Inorder traversal visits the left subtree, the root node, and then the right subtree. This is a recursive approach that can be easily implemented using a divide-and-conquer strategy.
### Approach
We will use a recursive approach to traverse the binary tree. The recursive function will take the root node as the input and perform the following steps:

1. Recursively traverse the left subtree by calling the function with the left child as the input.
2. Visit the root node by printing its data.
3. Recursively traverse the right subtree by calling the function with the right child as the input.

## Time and Space Complexity Analysis
### Time Complexity
The time complexity of the inorder traversal algorithm is O(n), where n is the number of nodes in the binary tree. This is because the algorithm visits each node in the tree exactly once.
### Space Complexity
The space complexity of the inorder traversal algorithm is O(h), where h is the height of the binary tree. This is because the algorithm uses a stack to store the nodes that are waiting to be visited. In the worst case, the height of the tree is n, so the space complexity is O(n).

## Well-Commented Implementation
```python
def inorder_traversal(root):
    """
    Performs an inorder traversal of a binary tree.

    Parameters:
    root: The root node of the binary tree.

    Returns:
    A list of the data in the binary tree in inorder.
    """
    if not root:
        return []

    return inorder_traversal(root.left) + [root.data] + inorder_traversal(root.right)


# Example binary tree
tree = BinaryTree(1)
tree.left = BinaryTree(2)
tree.right = BinaryTree(3)
tree.left.left = BinaryTree(4)
tree.left.right = BinaryTree(5)

# Print the inorder traversal of the binary tree
print(inorder_traversal(tree))  # Output: [4, 2, 5, 1, 3]
```

## Example Test Cases
### Test Case 1
```python
tree = BinaryTree(1)
tree.left = BinaryTree(2)
tree.right = BinaryTree(3)
tree.left.left = BinaryTree(4)
tree.left.right = BinaryTree(5)

inorder_traversal(tree) == [4, 2, 5, 1, 3]
```
### Test Case 2
```python
tree = BinaryTree(1)
tree.right = BinaryTree(2)

inorder_traversal(tree) == [1, 2]
```
### Test Case 3
```python
tree = None

inorder_traversal(tree) == []
```

## Alternative Approaches
### Using a Stack
Instead of using recursion, we can also use a stack to implement the inorder traversal of a binary tree. The algorithm is as follows:

1. Push the root node onto the stack.
2. While the stack is not empty, do the following:
    - Pop the top node from the stack.
    - Print the data of the popped node.
    - Push the right child of the popped node onto the stack.
    - Push the left child of the popped node onto the stack.

### Using Morris Traversal
Morris traversal is a technique that allows us to perform inorder traversal of a binary tree without using a stack or recursion. The algorithm is as follows:

1. Start from the root node.
2. If the left child of the current node is null, then print the data of the current node and move to the right child of the current node.
3. Otherwise, find the inorder predecessor of the current node.
4. If the right child of the inorder predecessor is null, then make the right child of the inorder predecessor point to the current node and move to the left child of the current node.
5. Otherwise, make the right child of the inorder predecessor point to null and print the data of the current node.
6. Move to the right child of the current node.

# Connect with me: https://github.com/ohkrahul
