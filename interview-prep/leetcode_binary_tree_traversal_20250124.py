'''
Problem: Binary Tree Traversal
Platform: LeetCode
Difficulty: Easy
URL: https://leetcode.com/problems/binary-tree-inorder-traversal
Date: 2025-01-24
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from LeetCode - Easy
# Date: 2025-01-24

## 1. Problem Understanding and Approach

The inorder traversal of a binary tree is a traversal that visits the left subtree, then the root, and finally the right subtree. This can be implemented using recursion or a stack.

### Recursive Approach

The recursive approach is to call the inorder traversal function on the left subtree, then visit the root, and finally call the inorder traversal function on the right subtree. The following is the recursive algorithm:

1. If the tree is empty, return.
2. Call the inorder traversal function on the left subtree.
3. Visit the root.
4. Call the inorder traversal function on the right subtree.

### Iterative Approach

The iterative approach is to use a stack to keep track of the nodes that have not been visited yet. The following is the iterative algorithm:

1. Push the root node onto the stack.
2. While the stack is not empty, pop the top node from the stack and visit it.
3. Push the left child of the node that was just visited onto the stack.
4. Repeat steps 2 and 3 until the stack is empty.

## 2. Time and Space Complexity Analysis

### Recursive Approach

The time complexity of the recursive approach is O(n), where n is the number of nodes in the tree. The space complexity is also O(n), since the recursion stack can be as deep as the height of the tree.

### Iterative Approach

The time complexity of the iterative approach is also O(n), since it visits each node in the tree once. The space complexity is O(h), where h is the height of the tree, since the stack can be as deep as the height of the tree.

## 3. Well-Commented Implementation

### Recursive Approach

```python
def inorder_traversal_recursive(root):
    """
    Perform inorder traversal of a binary tree recursively.

    Args:
        root: The root node of the binary tree.

    Returns:
        A list of the nodes in the tree in inorder.
    """

    if not root:
        return []

    return inorder_traversal_recursive(root.left) + [root.val] + inorder_traversal_recursive(root.right)
```

### Iterative Approach

```python
def inorder_traversal_iterative(root):
    """
    Perform inorder traversal of a binary tree iteratively.

    Args:
        root: The root node of the binary tree.

    Returns:
        A list of the nodes in the tree in inorder.
    """

    stack = []
    result = []

    while root or stack:
        if root:
            stack.append(root)
            root = root.left
        else:
            root = stack.pop()
            result.append(root.val)
            root = root.right

    return result
```

## 4. Example Test Cases

### Test Case 1

```
      1
     / \
    2   3
   / \
  4   5
```

**Output:**

```
[4, 2, 5, 1, 3]
```

### Test Case 2

```
     1
    /
   2
  / \
 3   4
```

**Output:**

```
[3, 2, 4, 1]
```

### Test Case 3

```
Empty tree
```

**Output:**

```
[]
```

## 5. Alternative Approaches

There are other ways to perform inorder traversal of a binary tree, such as using Morris traversal or threaded binary trees. However, the recursive and iterative approaches are the most common and straightforward.

# Connect with me: https://github.com/ohkrahul
