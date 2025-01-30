'''
Problem: Binary Tree Traversal
Platform: LeetCode
Difficulty: Easy
URL: https://leetcode.com/problems/binary-tree-inorder-traversal
Date: 2025-01-30
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from LeetCode - Easy
# Date: 2025-01-30

## Problem Understanding and Approach

**Problem:** Implement inorder traversal of a binary tree. Inorder traversal visits nodes in the following order: left subtree, root, right subtree.

**Approach:**

1. Use a recursive function to traverse the binary tree.
2. In the function, first traverse the left subtree.
3. Then, visit the root node.
4. Finally, traverse the right subtree.

## Time and Space Complexity Analysis

* **Time complexity:** O(n), where n is the number of nodes in the binary tree. The function visits each node in the tree once.
* **Space complexity:** O(h), where h is the height of the binary tree. The function uses a stack to store the nodes that have been visited but not yet processed. The maximum depth of the stack is the height of the tree.

## Well-commented Implementation

```python
def inorder_traversal(root):
    """
    Perform inorder traversal of a binary tree.

    Args:
        root: The root node of the binary tree.

    Returns:
        A list of the nodes in the binary tree in inorder.
    """

    # If the root node is None, return an empty list.
    if root is None:
        return []

    # Create a list to store the nodes in inorder.
    nodes = []

    # Recursively traverse the left subtree.
    nodes.extend(inorder_traversal(root.left))

    # Visit the root node.
    nodes.append(root.val)

    # Recursively traverse the right subtree.
    nodes.extend(inorder_traversal(root.right))

    # Return the list of nodes in inorder.
    return nodes
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

There are other ways to implement inorder traversal of a binary tree. One alternative approach is to use a stack. The following Python code shows how to implement inorder traversal using a stack:

```python
def inorder_traversal_stack(root):
    """
    Perform inorder traversal of a binary tree using a stack.

    Args:
        root: The root node of the binary tree.

    Returns:
        A list of the nodes in the binary tree in inorder.
    """

    # Create a stack to store the nodes that have been visited but not yet processed.
    stack = []

    # Initialize the current node to the root node.
    current = root

    # While the current node is not None or the stack is not empty, continue the traversal.
    while current is not None or stack:
        # If the current node is not None, push it onto the stack and move to its left child.
        if current is not None:
            stack.append(current)
            current = current.left

        # Otherwise, pop the top node from the stack and visit it.
        else:
            current = stack.pop()
            yield current.val
            current = current.right

    # Return the list of nodes in inorder.
    return list(inorder_traversal_stack(root))
```

# Connect with me: https://github.com/ohkrahul
