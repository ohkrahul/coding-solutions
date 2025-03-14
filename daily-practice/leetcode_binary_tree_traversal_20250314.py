'''
Problem: Binary Tree Traversal
Platform: LeetCode
Difficulty: Easy
URL: https://leetcode.com/problems/binary-tree-inorder-traversal
Date: 2025-03-14
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from LeetCode - Easy
# Date: 2025-03-14

## Binary Tree Inorder Traversal

**Problem:** Given the root of a binary tree, return the inorder traversal of its nodes' values.  (LeetCode #94)

**Platform:** LeetCode

**Difficulty:** Easy

**1. Problem Understanding and Approach:**

Inorder traversal follows the Left-Root-Right order.  We recursively visit the left subtree, then process the root node, and finally visit the right subtree.  This can be implemented iteratively using a stack as well.

We'll primarily focus on the recursive approach here due to its simplicity and clarity for this specific problem.


**2. Time and Space Complexity Analysis:**

* **Time Complexity:** O(N), where N is the number of nodes in the tree. We visit each node exactly once.
* **Space Complexity:** 
    * **Recursive:** O(H) in the worst case (skewed tree), where H is the height of the tree, due to the function call stack. In the best case (balanced tree), it's O(log N).
    * **Iterative:** O(H) as well, as the stack can store at most H nodes.  In the best case (balanced tree), it's O(log N).


**3. Well-commented Implementation (Recursive):**

```python
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorderTraversal(root: Optional[TreeNode]) -> List[int]:
    """
    Performs inorder traversal of a binary tree recursively.

    Args:
        root: The root of the binary tree.

    Returns:
        A list containing the inorder traversal of the tree's values.
    """
    result = []

    def inorder(node):
        if not node:
            return

        inorder(node.left)  # Traverse left subtree
        result.append(node.val)  # Visit root
        inorder(node.right)  # Traverse right subtree

    inorder(root)
    return result



```

**4. Example Test Cases:**

```python
# Test case 1: Single node
root1 = TreeNode(1)
print(inorderTraversal(root1))  # Output: [1]

# Test case 2: Balanced tree
root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(3)
print(inorderTraversal(root2))  # Output: [2, 1, 3]


# Test case 3: Skewed tree (left)
root3 = TreeNode(1)
root3.left = TreeNode(2)
root3.left.left = TreeNode(3)
print(inorderTraversal(root3))  # Output: [3, 2, 1]

# Test case 4: Empty tree
root4 = None
print(inorderTraversal(root4))  # Output: []

```


**5. Alternative Approaches (Iterative):**


```python
def inorderTraversalIterative(root: Optional[TreeNode]) -> List[int]:
    """
    Performs inorder traversal iteratively using a stack.
    """
    result = []
    stack = []
    curr = root

    while curr or stack:
        while curr:  # Go as left as possible
            stack.append(curr)
            curr = curr.left

        curr = stack.pop()  # Process the node
        result.append(curr.val)

        curr = curr.right  # Explore the right subtree

    return result
```

The iterative approach avoids the function call overhead and can be slightly more memory efficient for very deep, skewed trees, although the asymptotic complexity remains the same. It's also a good exercise in using stacks for tree traversals.

# Connect with me: https://github.com/ohkrahul
