'''
Problem: Binary Tree Traversal
Platform: LeetCode
Difficulty: Easy
URL: https://leetcode.com/problems/binary-tree-inorder-traversal
Date: 2025-04-24
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from LeetCode - Easy
# Date: 2025-04-24

```python
# Problem: Binary Tree Inorder Traversal (LeetCode)
# Difficulty: Easy

# Problem Understanding:
# Inorder traversal visits a binary tree in the order: Left subtree, Root, Right subtree.  
# The goal is to return a list of the node values in this order.

# Approach:
# We'll use recursion to traverse the tree. The base case is when the current node is null (None).
# Otherwise, we recursively traverse the left subtree, then append the current node's value,
# and finally recursively traverse the right subtree.

# Time Complexity: O(N) where N is the number of nodes in the tree. We visit each node once.
# Space Complexity: O(H) in the worst case due to the recursion stack, where H is the height of the tree. 
#                   In the best case (balanced tree), H = logN, and in the worst case (skewed tree), H = N.
#                   Iterative approach using a stack would have O(H) space complexity as well.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorderTraversal(root):
    """
    Performs inorder traversal of a binary tree.

    Args:
        root: The root of the binary tree.

    Returns:
        A list of node values in inorder traversal order.
    """

    result = []

    def inorder(node):
        if not node:  # Base case: Empty subtree
            return

        inorder(node.left)  # Traverse left subtree
        result.append(node.val)  # Visit root (append value)
        inorder(node.right)  # Traverse right subtree

    inorder(root)
    return result


# Example Test Cases:
# Test Case 1: Empty tree
root1 = None
print(inorderTraversal(root1))  # Output: []

# Test Case 2: Single node tree
root2 = TreeNode(1)
print(inorderTraversal(root2))  # Output: [1]

# Test Case 3: Balanced tree
root3 = TreeNode(1)
root3.left = TreeNode(2)
root3.right = TreeNode(3)
print(inorderTraversal(root3))  # Output: [2, 1, 3]



# Test Case 4: Skewed tree (left)
root4 = TreeNode(1)
root4.left = TreeNode(2)
root4.left.left = TreeNode(3)

print(inorderTraversal(root4))  # Output: [3, 2, 1]


# Alternative Approaches:

# Iterative Approach (using a stack):
def inorderTraversalIterative(root):
    result = []
    stack = []
    curr = root

    while curr or stack:
        while curr:  # Go as left as possible
            stack.append(curr)
            curr = curr.left

        curr = stack.pop() # Backtrack from the stack
        result.append(curr.val)  # Visit node
        curr = curr.right # Explore right subtree

    return result

# Example using iterative approach:
print(inorderTraversalIterative(root3)) # Output: [2, 1, 3]


```


Key improvements in this refined solution:

- **Clearer Problem Understanding:** The explanation of inorder traversal and the purpose is more concise.
- **Improved Comments:** The code is more thoroughly commented, explaining the purpose of each section and key steps.
- **Explicit Base Case:** The base case for the recursion is clearly stated and handled.
- **More Test Cases:**  Added more test cases covering different tree structures (empty, single node, balanced, skewed).
- **Alternative Approach:**  Included an iterative solution using a stack as an alternative, demonstrating a different way to solve the problem. 
- **Class Definition:** Included the `TreeNode` class definition for completeness and clarity.
- **Function Docstrings:** Docstrings are added to the function for better documentation.

# Connect with me: https://github.com/ohkrahul
