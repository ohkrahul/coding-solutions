'''
Problem: Binary Tree Traversal
Platform: LeetCode
Difficulty: Easy
URL: https://leetcode.com/problems/binary-tree-inorder-traversal
Date: 2025-03-06
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from LeetCode - Easy
# Date: 2025-03-06

```python
# Problem: Binary Tree Inorder Traversal (LeetCode)
# Difficulty: Easy

# 1. Problem Understanding and Approach

# The goal is to perform an inorder traversal of a binary tree.  Inorder traversal visits nodes in the following order:
# Left Subtree -> Root -> Right Subtree

# We can achieve this recursively or iteratively.  The recursive approach is simpler to understand, while the iterative approach 
# avoids potential stack overflow issues for very deep trees.


# 2. Time and Space Complexity Analysis

# Recursive Approach:
# Time Complexity: O(N), where N is the number of nodes in the tree. We visit each node exactly once.
# Space Complexity: O(H) in the worst case (skewed tree) due to the recursion stack, where H is the height of the tree. 
#                  In the average case (balanced tree), the space complexity is O(log N).


# Iterative Approach:
# Time Complexity: O(N)
# Space Complexity: O(H) in the worst case (skewed tree), where H is the height of the tree. This is due to the space used by the stack.
#                  In the average case (balanced tree), the space complexity is O(log N).


# 3. Well-commented Implementation (Recursive)

class TreeNode:  # Definition for a binary tree node (LeetCode standard)
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorderTraversalRecursive(root: TreeNode):
    """
    Performs inorder traversal recursively.
    """
    result = []

    def inorder(node):
        if node:
            inorder(node.left)  # Traverse left subtree
            result.append(node.val) # Visit root
            inorder(node.right) # Traverse right subtree

    inorder(root)
    return result


# 3. Well-commented Implementation (Iterative)
def inorderTraversalIterative(root: TreeNode):
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

        curr = stack.pop()  # Visit the node
        result.append(curr.val)

        curr = curr.right  # Explore the right subtree

    return result

# 4. Example Test Cases


# Test case 1:  [1,null,2,3]
root1 = TreeNode(1)
root1.right = TreeNode(2)
root1.right.left = TreeNode(3)
print(inorderTraversalRecursive(root1))  # Output: [1, 3, 2]
print(inorderTraversalIterative(root1))  # Output: [1, 3, 2]


# Test case 2: []  (Empty tree)
root2 = None
print(inorderTraversalRecursive(root2))  # Output: []
print(inorderTraversalIterative(root2))  # Output: []


# Test case 3: [1] (Single node)
root3 = TreeNode(1)
print(inorderTraversalRecursive(root3))  # Output: [1]
print(inorderTraversalIterative(root3))  # Output: [1]


# 5. Alternative Approaches (Morris Traversal -  O(1) space, modifies the tree temporarily)

# Morris traversal is an advanced technique that performs inorder traversal without recursion or a stack, using O(1) extra space.
# It's a more complex approach involving manipulating tree pointers.  It's not as commonly used as the recursive or iterative methods using a stack.

# (Implementation of Morris Traversal can be added if specifically requested.)
```




# Connect with me: https://github.com/ohkrahul
