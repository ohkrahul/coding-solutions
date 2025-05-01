'''
Problem: Binary Tree Traversal
Platform: LeetCode
Difficulty: Easy
URL: https://leetcode.com/problems/binary-tree-inorder-traversal
Date: 2025-05-01
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from LeetCode - Easy
# Date: 2025-05-01

## Binary Tree Inorder Traversal

**Platform:** LeetCode
**Difficulty:** Easy

**Problem Description:** Given the root of a binary tree, return *the inorder traversal* of its nodes' values.

**1. Problem Understanding and Approach**

Inorder traversal visits a binary tree in the order: **Left subtree -> Root -> Right subtree**.

We can implement this recursively:

1. Traverse the left subtree recursively.
2. Visit the root node (add its value to the result).
3. Traverse the right subtree recursively.

**2. Time and Space Complexity Analysis**

* **Time Complexity:** O(N), where N is the number of nodes in the tree. We visit each node exactly once.
* **Space Complexity:** O(H) in the worst case (skewed tree) due to the recursion stack, where H is the height of the tree. In the best case (balanced tree), it's O(log N).  Iterative solutions can achieve O(N) space in the worst case due to the size of the stack.

**3. Well-commented Implementation (Python)**

```python
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorderTraversal(root: Optional[TreeNode]) -> List[int]:
    """
    Performs an inorder traversal of a binary tree.

    Args:
        root: The root of the binary tree.

    Returns:
        A list containing the inorder traversal of the tree's node values.
    """
    result = []

    def inorder(node):  # Inner recursive function
        if node:
            inorder(node.left)  # Traverse left subtree
            result.append(node.val)  # Visit root
            inorder(node.right)  # Traverse right subtree

    inorder(root)  # Start traversal from the root
    return result

```

**4. Example Test Cases**

```python
# Test Case 1: Empty tree
root1 = None
print(inorderTraversal(root1))  # Output: []


# Test Case 2: Single node
root2 = TreeNode(1)
print(inorderTraversal(root2))  # Output: [1]


# Test Case 3: Balanced tree
root3 = TreeNode(1)
root3.left = TreeNode(2)
root3.right = TreeNode(3)
print(inorderTraversal(root3))  # Output: [2, 1, 3]


# Test Case 4: Skewed tree
root4 = TreeNode(1)
root4.right = TreeNode(2)
root4.right.right = TreeNode(3)
print(inorderTraversal(root4))  # Output: [1, 2, 3]
```

**5. Alternative Approaches**

**Iterative Approach using a Stack:**

```python
def inorderTraversalIterative(root: Optional[TreeNode]) -> List[int]:
    result = []
    stack = []
    curr = root

    while curr or stack:  # Continue while there are nodes to process
        while curr:  # Go left as far as possible
            stack.append(curr)
            curr = curr.left

        curr = stack.pop()  # Visit the node
        result.append(curr.val)

        curr = curr.right  # Go to the right subtree

    return result
```

The iterative approach avoids recursion, using a stack to keep track of the nodes to be visited.  This eliminates the risk of stack overflow for very deep trees and uses O(N) space in the worst-case scenario, matching the space needed to store the result. It has the same O(N) time complexity.



This comprehensive explanation covers the problem understanding, approach, time and space complexity, a well-commented implementation with type hints, example test cases, and an alternative iterative approach for the Binary Tree Inorder Traversal problem.  This style mirrors a real developer's approach to problem-solving.

# Connect with me: https://github.com/ohkrahul
