'''
Problem: Binary Tree Traversal
Platform: LeetCode
Difficulty: Easy
URL: https://leetcode.com/problems/binary-tree-inorder-traversal
Date: 2024-12-16
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from LeetCode - Easy
# Date: 2024-12-16

### 1. Problem Understanding and Approach
In a binary tree, inorder traversal visits the left node, then the root, and finally, the right node.

### 2. Time and Space Complexity Analysis
**Time Complexity:** O(N) where N is the number of nodes in the tree.
**Space Complexity:** O(H) where H is the height of the tree.

### 3. Well-Commented Implementation
```python
def inorder_traversal(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    if not root:
        return []
    
    stack = []
    result = []
    
    while root or stack:
        # Keep going left until we reach the left-most node
        while root:
            stack.append(root)
            root = root.left
            
        # We have reached the left-most node, now pop it and add its value to the result
        root = stack.pop()
        result.append(root.val)
        
        # Now move to its right subtree
        root = root.right
    
    return result
```

### 4. Example Test Cases
```python
# Test case 1
root = [1, None, 2, 3]
inorder_traversal(root)  # [1, 3, 2]

# Test case 2
root = []
inorder_traversal(root)  # []

# Test case 3
root = [1]
inorder_traversal(root)  # [1]

# Test case 4
root = [1, 2, 3, 4, 5, 6, 7]
inorder_traversal(root)  # [4, 2, 5, 1, 6, 3, 7]
```

### 5. Alternative Approaches
**Recursive Approach:**
```python
def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.val)
        inorder_traversal(root.right)
```

# Connect with me: https://github.com/ohkrahul
