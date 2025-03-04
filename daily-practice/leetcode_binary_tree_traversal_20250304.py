'''
Problem: Binary Tree Traversal
Platform: LeetCode
Difficulty: Easy
URL: https://leetcode.com/problems/binary-tree-inorder-traversal
Date: 2025-03-04
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from LeetCode - Easy
# Date: 2025-03-04

```python
# Problem: Binary Tree Inorder Traversal (LeetCode)
# Difficulty: Easy

# 1. Problem Understanding and Approach

# The goal is to traverse a binary tree using the inorder method.  Inorder traversal visits nodes in the following order: left subtree, root, right subtree. 
# We'll use a recursive approach for its simplicity and clarity, although iterative solutions are also possible.

# 2. Time and Space Complexity Analysis

# Time Complexity: O(N), where N is the number of nodes in the tree. We visit each node exactly once.
# Space Complexity: O(H) in the worst case (skewed tree) due to recursion stack, where H is the height of the tree.  In the average case (balanced tree), the space complexity is O(log N).  In the best case (tree is a linked list), the height is N so space is O(N).


# 3. Implementation

class TreeNode:  # Definition for a binary tree node.
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorderTraversal(root: TreeNode):
    """
    Performs inorder traversal of a binary tree.

    Args:
        root: The root node of the binary tree.

    Returns:
        A list containing the values of the nodes visited in inorder.
    """

    result = []

    def inorder(node):
        if not node:
            return

        inorder(node.left) # Recursively traverse the left subtree
        result.append(node.val) # Visit the current node (add its value to the result)
        inorder(node.right) # Recursively traverse the right subtree

    inorder(root)  # Initiate the traversal from the root
    return result


# 4. Example Test Cases

# Test case 1:  Empty tree
root1 = None
print(f"Inorder traversal of root1: {inorderTraversal(root1)}") # Output: []

# Test case 2: Single node tree
root2 = TreeNode(1)
print(f"Inorder traversal of root2: {inorderTraversal(root2)}") # Output: [1]

# Test case 3:  A balanced tree
root3 = TreeNode(1)
root3.left = TreeNode(2)
root3.right = TreeNode(3)
print(f"Inorder traversal of root3: {inorderTraversal(root3)}") # Output: [2, 1, 3]

# Test case 4: A left-skewed tree (worst-case for space complexity)
root4 = TreeNode(1)
root4.left = TreeNode(2)
root4.left.left = TreeNode(3)
print(f"Inorder traversal of root4: {inorderTraversal(root4)}") # Output: [3, 2, 1]


# 5. Alternative Approaches

# Iterative Approach (using a stack):

def inorderTraversalIterative(root: TreeNode):
    result = []
    stack = []
    curr = root

    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left

        curr = stack.pop()
        result.append(curr.val)
        curr = curr.right

    return result


print(f"Iterative Inorder traversal of root3: {inorderTraversalIterative(root3)}") # Output: [2, 1, 3]


# Morris Traversal (O(1) space, but modifies the tree temporarily):
#  (Implementation omitted for brevity, but a worthwhile approach to research for its constant space complexity) 
```


Key improvements in this revised answer:

* **More detailed explanations:**  The problem understanding, approach, and complexity sections are explained more thoroughly.
* **Explicit TreeNode class:** Includes the `TreeNode` class definition for clarity and completeness.
* **Docstrings:** Added docstrings to the `inorderTraversal` function to enhance readability and explain parameters/return values.
* **More comprehensive test cases:**  Added test cases for an empty tree, single-node tree, balanced tree, and a skewed tree to illustrate the space complexity behavior.
* **Alternative approach with explanation:** Provided an iterative solution using a stack, and mentioned Morris Traversal as another space-efficient approach.
* **Clearer comments:**  Improved the comments within the code to explain the logic step-by-step.
* **Output included:** Added the expected outputs for the test cases, making it easier to understand the results.


This revised answer provides a more comprehensive and developer-friendly solution to the binary tree inorder traversal problem.

# Connect with me: https://github.com/ohkrahul
