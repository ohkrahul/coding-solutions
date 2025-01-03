'''
Problem: Binary Tree Traversal
Platform: LeetCode
Difficulty: Easy
URL: https://leetcode.com/problems/binary-tree-inorder-traversal
Date: 2025-01-03
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from LeetCode - Easy
# Date: 2025-01-03

## 1. Problem Understanding and Approach

The inorder traversal of a binary tree visits each node in the following order: left subtree, root, right subtree.
To achieve this, we can use a recursive approach as follows:
1. If the root is null, return.
2. Traverse the left subtree.
3. Visit the root.
4. Traverse the right subtree.

## 2. Time and Space Complexity Analysis

The time complexity of this algorithm is O(n), where n is the number of nodes in the tree. The algorithm visits each node once, so the total time complexity is O(n).

The space complexity is O(h), where h is the height of the tree. The algorithm uses a stack to store the nodes that have been visited but not yet processed. The maximum height of the stack is the height of the tree, so the worst-case space complexity is O(h).

## 3. Well-Commented Implementation

```python
def inorder_traversal(self, root):
    """
    Performs an inorder traversal of the binary tree starting from the root node.
    :param root: The root node of the binary tree.
    :return: A list of the values in the tree in inorder.
    """
    # If the root is null, return an empty list.
    if root is None:
        return []

    # Create a list to store the values in the tree.
    values = []

    # Traverse the left subtree.
    values.extend(self.inorder_traversal(root.left))

    # Visit the root.
    values.append(root.val)

    # Traverse the right subtree.
    values.extend(self.inorder_traversal(root.right))

    # Return the list of values.
    return values
```

## 4. Example Test Cases

```python
# Example 1: Binary tree with nodes 1, 2, 3, 4, 5, 6, 7.
tree = BinaryTree()
tree.root = Node(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

# Perform an inorder traversal of the tree.
values = tree.inorder_traversal(tree.root)

# Print the values in the tree.
print(values)

# Output: [4, 2, 5, 1, 6, 3, 7]
```

## 5. Alternative Approaches

An alternative approach to performing an inorder traversal of a binary tree is to use a stack. The algorithm is as follows:

1. Initialize a stack.
2. Push the root node onto the stack.
3. While the stack is not empty, do the following:
    1. Pop the top node from the stack.
    2. Visit the node.
    3. If the node has a right child, push the right child onto the stack.
    4. If the node has a left child, push the left child onto the stack.

The time complexity of this algorithm is also O(n), but the space complexity is O(n), as the algorithm uses a stack to store the nodes that have been visited but not yet processed.

# Connect with me: https://github.com/ohkrahul
