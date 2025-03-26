'''
Problem: Binary Tree Traversal
Platform: LeetCode
Difficulty: Easy
URL: https://leetcode.com/problems/binary-tree-inorder-traversal
Date: 2025-03-26
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from LeetCode - Easy
# Date: 2025-03-26

```python
# Problem: Binary Tree Inorder Traversal
# Platform: LeetCode
# Difficulty: Easy

# Problem Understanding and Approach
# Inorder traversal of a binary tree visits nodes in the following order: left subtree, root, right subtree.
# Recursion is a natural fit for this problem, as the traversal pattern repeats itself for each subtree.
# We'll use a helper function to recursively traverse the left subtree, then process the current node, and finally traverse the right subtree.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        """
        Performs an inorder traversal of a binary tree.

        Args:
            root: The root of the binary tree.

        Returns:
            A list containing the inorder traversal of the tree.
        """

        result = []  # Initialize an empty list to store the traversal results

        def inorder(node):  # Helper function for recursive traversal
            if node:
                inorder(node.left)   # Traverse left subtree
                result.append(node.val)  # Visit the current node
                inorder(node.right)  # Traverse right subtree

        inorder(root)  # Initiate traversal from the root node
        return result


# Time and Space Complexity Analysis
# Time Complexity: O(N), where N is the number of nodes in the tree.  We visit each node once.
# Space Complexity: O(H) in the worst case (skewed tree) due to the recursion stack, where H is the height of the tree.
# In the average case (balanced tree), the space complexity is O(log N). In the best-case scenario, the tree has one element, and then the height would also be one, so it’s going to be O(1). The best-case input is a tree that only has one element, meaning only the root.

# Example Test Cases

# Test Case 1: Empty Tree
root1 = None
expected1 = []
actual1 = Solution().inorderTraversal(root1)
assert actual1 == expected1, f"Expected {expected1}, but got {actual1}"

# Test Case 2: Single Node Tree
root2 = TreeNode(1)
expected2 = [1]
actual2 = Solution().inorderTraversal(root2)
assert actual2 == expected2, f"Expected {expected2}, but got {actual2}"

# Test Case 3: Balanced Tree
root3 = TreeNode(1, TreeNode(2), TreeNode(3))
expected3 = [2, 1, 3]
actual3 = Solution().inorderTraversal(root3)
assert actual3 == expected3, f"Expected {expected3}, but got {actual3}"


# Test Case 4: Left Skewed Tree
root4 = TreeNode(1, TreeNode(2, TreeNode(3)))  #Nested left node
expected4 = [3, 2, 1]
actual4 = Solution().inorderTraversal(root4)
assert actual4 == expected4, f"Expected {expected4}, but got {actual4}"

# Alternative Approaches

# 1. Iterative Approach using Stack: An iterative approach using a stack can be implemented to avoid recursion and explicitly manage the traversal state.  This can be helpful in languages where recursion depth is limited.


# 2. Morris Traversal:  Morris traversal is a clever algorithm that performs inorder traversal without using recursion or a stack, thus achieving O(1) space complexity (excluding the output list). However, it modifies the tree structure temporarily. This is not very common during interviews, but it’s an interesting approach worth knowing.
```




# Connect with me: https://github.com/ohkrahul
