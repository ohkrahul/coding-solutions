'''
Problem: Binary Tree Traversal
Platform: LeetCode
Difficulty: Easy
URL: https://leetcode.com/problems/binary-tree-inorder-traversal
Date: 2025-04-25
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from LeetCode - Easy
# Date: 2025-04-25

```python
# Problem: Binary Tree Inorder Traversal (LeetCode)
# Difficulty: Easy

# 1. Problem Understanding and Approach

# We are given a binary tree and need to implement an inorder traversal. Inorder traversal visits nodes in the following order: left subtree, root, right subtree.

# Approach: Recursive solution is the most intuitive and efficient for inorder traversal. We will define a helper function that performs the traversal recursively.

# 2. Time and Space Complexity Analysis

# Time Complexity: O(N), where N is the number of nodes in the tree. We visit each node exactly once.
# Space Complexity: O(H) in the worst case (skewed tree) due to recursion stack, where H is the height of the tree. In the average case, it's O(log N) for a balanced tree.  In the best case (a tree where every node has only a left child, for example), it is O(N), because there are N recursive calls on the stack.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorderTraversal(root: TreeNode):
    """
    Performs inorder traversal of a binary tree.

    Args:
        root: The root of the binary tree.

    Returns:
        A list containing the values of the nodes visited in inorder.
    """
    result = []  # Initialize an empty list to store the result

    def inorder(node):  # Helper function for recursive traversal
        if not node:  # Base case: If the node is null, return
            return

        inorder(node.left)   # Traverse the left subtree
        result.append(node.val)  # Visit the current node (add its value to the result)
        inorder(node.right)  # Traverse the right subtree
    
    inorder(root) # Start the traversal from the root node
    return result


# 4. Example Test Cases
# Test Case 1:  [1,null,2,3]
root1 = TreeNode(1, None, TreeNode(2, TreeNode(3)))
print(inorderTraversal(root1))  # Expected Output: [1, 3, 2]


# Test Case 2: []
root2 = None
print(inorderTraversal(root2))  # Expected Output: []


# Test Case 3: [1]
root3 = TreeNode(1)
print(inorderTraversal(root3))  # Expected Output: [1]

# Test Case 4: A more complex tree
root4 = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))
print(inorderTraversal(root4)) # Expected Output: [4, 2, 5, 1, 6, 3, 7]



# 5. Alternative Approaches

# Iterative Approach using a stack:

def inorderTraversalIterative(root: TreeNode):
    """
    Iterative inorder traversal using a stack.
    """
    result = []
    stack = []
    curr = root

    while curr or stack:  # Continue while current node exists or stack is not empty
        while curr:       # Go as far left as possible
            stack.append(curr)
            curr = curr.left

        curr = stack.pop() # Visit the node (add to result)
        result.append(curr.val)
        curr = curr.right # Go to the right subtree

    return result

# You can test the iterative approach with the same test cases as above.  It has the same time and space complexity as the recursive approach.

```

# Connect with me: https://github.com/ohkrahul
