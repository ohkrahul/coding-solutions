'''
Problem: Binary Tree Traversal
Platform: LeetCode
Difficulty: Easy
URL: https://leetcode.com/problems/binary-tree-inorder-traversal
Date: 2025-04-30
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from LeetCode - Easy
# Date: 2025-04-30

## Binary Tree Inorder Traversal

**Platform:** LeetCode
**Difficulty:** Easy

**1. Problem Understanding and Approach**

The problem requires us to implement an inorder traversal of a binary tree. Inorder traversal visits nodes in the order: left subtree, root, right subtree.  We can accomplish this recursively or iteratively.  We'll primarily use a recursive approach due to its simplicity and clarity for this "Easy" level problem.


**2. Time and Space Complexity Analysis**

* **Time Complexity:** O(N), where N is the number of nodes in the tree.  We visit each node exactly once.
* **Space Complexity:**
    * Recursive: O(H) in the worst case and O(log N) in the average case, where H is the height of the tree. This is due to the function call stack used in recursion. In a skewed tree (worst case), H can be equal to N. In a balanced tree (average case), H is proportional to log N.
    * Iterative: O(H) in the worst case and O(log N) in the average case. The space complexity is determined by the size of the stack we use for iteration.


**3. Well-commented Implementation (Python)**

```python
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorderTraversal(root: TreeNode) -> list[int]:
    """
    Performs an inorder traversal of a binary tree.

    Args:
        root: The root of the binary tree.

    Returns:
        A list of node values in inorder traversal order.
    """
    result = []

    def inorder(node):
        if node:
            inorder(node.left)  # Traverse left subtree
            result.append(node.val) # Visit the root
            inorder(node.right) # Traverse right subtree

    inorder(root)
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

# Test Case 3: Small balanced tree
root3 = TreeNode(1, TreeNode(2), TreeNode(3))
print(inorderTraversal(root3))  # Output: [2, 1, 3]

# Test Case 4: Left-skewed tree
root4 = TreeNode(1, TreeNode(2, TreeNode(3)))
print(inorderTraversal(root4))  # Output: [3, 2, 1]
```



**5. Alternative Approaches (Iterative)**

```python
def inorderTraversalIterative(root: TreeNode) -> list[int]:
    """
    Performs an inorder traversal iteratively.

    Args:
        root: The root of the binary tree.

    Returns:
        A list of node values in inorder traversal order.
    """

    result = []
    stack = []
    current = root

    while current or stack:
        while current: # Go all the way left
            stack.append(current)
            current = current.left

        current = stack.pop() # Process the node
        result.append(current.val)

        current = current.right # Explore the right subtree
    
    return result
```


The iterative approach uses a stack to simulate the recursive calls, offering the same time complexity but can be slightly more memory-efficient in some languages due to stack frame overhead associated with recursion. However, for Python, the recursive solution often remains more concise and readable for this specific problem.  The iterative solution is more complex but eliminates recursion, which can be important if the tree is extremely deep and you want to avoid stack overflow errors.

# Connect with me: https://github.com/ohkrahul
