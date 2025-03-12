'''
Problem: Binary Tree Traversal
Platform: LeetCode
Difficulty: Easy
URL: https://leetcode.com/problems/binary-tree-inorder-traversal
Date: 2025-03-12
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from LeetCode - Easy
# Date: 2025-03-12

```python
# Problem: Binary Tree Inorder Traversal (LeetCode)
# Difficulty: Easy

# 1. Problem Understanding and Approach

# The inorder traversal of a binary tree follows the pattern: Left -> Root -> Right. 
# We recursively visit the left subtree, then process the root node, and finally visit the right subtree.  
# We'll use a recursive approach as it's natural for tree traversals.

# 2. Time and Space Complexity Analysis

# Time Complexity: O(N), where N is the number of nodes in the tree. We visit each node exactly once.
# Space Complexity: O(H) in the worst case (skewed tree) due to the recursion stack, where H is the height of the tree. 
# In the average case (balanced tree), the space complexity is O(log N).
# In the best case (tree with just one node or an empty tree), the space complexity is O(1).

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorderTraversal(root: TreeNode | None) -> list[int]:
    """
    Performs inorder traversal of a binary tree.

    Args:
        root: The root of the binary tree.

    Returns:
        A list containing the inorder traversal of the tree.
    """
    result = []

    def inorder(node):  # Inner recursive function
        if node:
            inorder(node.left)  # Traverse left subtree
            result.append(node.val)  # Process root node
            inorder(node.right)  # Traverse right subtree

    inorder(root)
    return result




# 4. Example Test Cases

# Test case 1:  [1,null,2,3]
root1 = TreeNode(1)
root1.right = TreeNode(2)
root1.right.left = TreeNode(3)
print(inorderTraversal(root1))  # Output: [1, 3, 2]

# Test case 2: [] 
root2 = None
print(inorderTraversal(root2))  # Output: []

# Test case 3: [1]
root3 = TreeNode(1)
print(inorderTraversal(root3)) # Output: [1]

# Test case 4: [1, 2, 3, 4, 5, 6, 7] (Balanced tree)
root4 = TreeNode(4)
root4.left = TreeNode(2)
root4.right = TreeNode(6)
root4.left.left = TreeNode(1)
root4.left.right = TreeNode(3)
root4.right.left = TreeNode(5)
root4.right.right = TreeNode(7)
print(inorderTraversal(root4))  # Output: [1, 2, 3, 4, 5, 6, 7]


# 5. Alternative Approaches

# Iterative approach using a stack:
def inorderTraversalIterative(root: TreeNode | None) -> list[int]:
    """
    Performs inorder traversal iteratively using a stack.
    """
    result = []
    stack = []
    node = root

    while node or stack:
        while node:  # Go left as far as possible
            stack.append(node)
            node = node.left
        
        node = stack.pop()  # Process the node
        result.append(node.val)
        node = node.right  # Move to the right subtree

    return result

print(inorderTraversalIterative(root1)) # Output: [1, 3, 2]

# Morris Traversal:  This approach achieves O(1) space complexity (excluding the output list)
# but modifies the tree structure temporarily.  It's more complex to implement.


```

# Connect with me: https://github.com/ohkrahul
