'''
Problem: Binary Tree Traversal
Platform: LeetCode
Difficulty: Easy
URL: https://leetcode.com/problems/binary-tree-inorder-traversal
Date: 2025-03-10
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from LeetCode - Easy
# Date: 2025-03-10

```python
# Problem: Binary Tree Inorder Traversal (LeetCode)
# Difficulty: Easy

# Problem Understanding:
# Given the root of a binary tree, return the inorder traversal of its nodes' values.
# Inorder traversal follows the Left-Root-Right pattern.


# Approach: Recursive
# We will use a recursive function to traverse the tree. The base case is when the node is null.
# Otherwise, we recursively traverse the left subtree, then visit the root node, and finally traverse the right subtree.


# Time Complexity: O(N), where N is the number of nodes in the tree. We visit each node once.
# Space Complexity: O(H) in the worst case (skewed tree) due to the recursive call stack, where H is the height of the tree. 
#                  O(log N) in the average case for a balanced tree.  In the best case (already sorted, thus linear), space is O(1).


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorderTraversal(root):
    """
    Performs inorder traversal of a binary tree recursively.

    Args:
        root: The root node of the binary tree.

    Returns:
        A list containing the inorder traversal of the tree's values.
    """

    result = []

    def inorder(node):
        if not node:  # Base case: empty node
            return

        inorder(node.left)    # Traverse left subtree
        result.append(node.val)  # Visit root
        inorder(node.right)   # Traverse right subtree

    inorder(root)
    return result




# Example Test Cases:

# Test Case 1:  Simple tree
root1 = TreeNode(1)
root1.right = TreeNode(2)
root1.right.left = TreeNode(3)
print(inorderTraversal(root1))  # Output: [1, 3, 2]

# Test Case 2: Empty tree
root2 = None
print(inorderTraversal(root2))  # Output: []


# Test Case 3: Larger tree
root3 = TreeNode(4)
root3.left = TreeNode(2)
root3.right = TreeNode(6)
root3.left.left= TreeNode(1)
root3.left.right = TreeNode(3)
root3.right.left= TreeNode(5)
root3.right.right = TreeNode(7)

print(inorderTraversal(root3)) # Output: [1, 2, 3, 4, 5, 6, 7]





# Alternative Approach: Iterative using a stack
# We can also perform inorder traversal iteratively using a stack to simulate the recursion.

def inorderTraversalIterative(root):
    """
    Performs inorder traversal of a binary tree iteratively using a stack.

    Args:
        root: The root node of the binary tree.

    Returns:
        A list containing the inorder traversal of the tree's values.
    """

    result = []
    stack = []
    curr = root

    while curr or stack:
        while curr:  # Go left as far as possible
            stack.append(curr)
            curr = curr.left

        curr = stack.pop() # Process the node
        result.append(curr.val)

        curr = curr.right   # Traverse right subtree

    return result

#Testing Iterative version:
print(inorderTraversalIterative(root1)) # Output: [1, 3, 2]
print(inorderTraversalIterative(root2)) # Output: []
print(inorderTraversalIterative(root3)) # Output: [1, 2, 3, 4, 5, 6, 7]


```

# Connect with me: https://github.com/ohkrahul
