'''
Problem: Binary Tree Traversal
Platform: LeetCode
Difficulty: Easy
URL: https://leetcode.com/problems/binary-tree-inorder-traversal
Date: 2025-02-10
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from LeetCode - Easy
# Date: 2025-02-10

## Problem Understanding and Approach

The inorder traversal of a binary tree visits the nodes in the following order: `left subtree`, `root`, `right subtree`. We can implement this traversal recursively by calling the function on the left subtree, then visiting the root, and finally calling the function on the right subtree.

## Time and Space Complexity Analysis

The time complexity of inorder traversal is O(n), where n is the number of nodes in the tree. This is because we visit each node exactly once. The space complexity is O(h), where h is the height of the tree. This is because the recursive calls can be stacked up to a depth of h.

## Well-Commented Implementation

```python
def inorder_traversal(root):
    """
    Performs inorder traversal of a binary tree.

    Args:
        root: The root node of the binary tree.

    Returns:
        A list of the values in the binary tree in inorder.
    """

    # If the root is None, return an empty list.
    if root is None:
        return []

    # Recursively call the function on the left subtree.
    left_subtree = inorder_traversal(root.left)

    # Add the root's value to the list.
    left_subtree.append(root.val)

    # Recursively call the function on the right subtree.
    right_subtree = inorder_traversal(root.right)

    # Return the list of values in inorder.
    return left_subtree + right_subtree
```

## Example Test Cases

The following test cases demonstrate the correctness of the inorder_traversal function:

```python
# Test case 1: Empty tree.
root = None
assert inorder_traversal(root) == []

# Test case 2: Tree with one node.
root = TreeNode(1)
assert inorder_traversal(root) == [1]

# Test case 3: Tree with multiple nodes.
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
assert inorder_traversal(root) == [2, 1, 3]
```

## Alternative Approaches

There are several alternative approaches to implementing inorder traversal of a binary tree:

* **Iterative approach:** The iterative approach uses a stack to keep track of the nodes that have been visited. The algorithm starts by pushing the root node onto the stack. Then, it repeatedly pops the top node from the stack and visits it. If the popped node has a right child, the right child is pushed onto the stack. If the popped node has a left child, the left child is pushed onto the stack. The algorithm terminates when the stack is empty.
* **Morris traversal:** Morris traversal is a space-efficient approach to inorder traversal. It uses a pointer to keep track of the current node. The algorithm starts by setting the pointer to the root node. Then, it repeatedly moves the pointer to the left child of the current node. If the left child is None, the algorithm visits the current node and moves the pointer to the right child of the current node. If the left child is not None, the algorithm finds the inorder predecessor of the current node and sets the right child of the inorder predecessor to the current node. The algorithm terminates when the pointer is None.

# Connect with me: https://github.com/ohkrahul
