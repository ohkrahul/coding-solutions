'''
Problem: Binary Tree Traversal
Platform: LeetCode
Difficulty: Easy
URL: https://leetcode.com/problems/binary-tree-inorder-traversal
Date: 2025-02-22
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from LeetCode - Easy
# Date: 2025-02-22

## Problem Understanding and Approach

Inorder traversal of a binary tree is a recursive algorithm that visits the nodes of the tree in the following order:

1. Traverse the left subtree
2. Visit the current node
3. Traverse the right subtree

We can implement this algorithm using a recursive function. The base case of the function is when the current node is `null`, in which case we do nothing. Otherwise, we recursively call the function on the left subtree, then visit the current node, and finally recursively call the function on the right subtree.

## Time and Space Complexity Analysis

The time complexity of the inorder traversal algorithm is O(n), where n is the number of nodes in the tree. This is because the algorithm visits each node in the tree exactly once.

The space complexity of the algorithm is O(h), where h is the height of the tree. This is because the algorithm uses a recursive call stack, and the depth of the call stack is equal to the height of the tree.

## Well-Commented Implementation

```
public class Solution {
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> result = new ArrayList<>();
        inorderTraversalHelper(root, result);
        return result;
    }

    private void inorderTraversalHelper(TreeNode node, List<Integer> result) {
        if (node == null) {
            return;
        }

        inorderTraversalHelper(node.left, result);
        result.add(node.val);
        inorderTraversalHelper(node.right, result);
    }
}
```

## Example Test Cases

The following are some example test cases for the inorder traversal algorithm:

```
Input: root = [1,null,2,3]
Output: [1,3,2]

Input: root = []
Output: []

Input: root = [1]
Output: [1]
```

## Alternative Approaches

There are a few alternative approaches to inorder traversal of a binary tree. One approach is to use a stack. In this approach, we push the current node onto the stack, then recursively call the inorder traversal algorithm on the left subtree. When we reach a leaf node, we pop the current node from the stack and visit it. Then, we recursively call the inorder traversal algorithm on the right subtree.

Another approach is to use a Morris traversal. In this approach, we use a pointer to traverse the tree. If the pointer is currently pointing to a node with a null left child, we visit the node and move the pointer to the right child. Otherwise, we find the predecessor of the current node and make the current node the right child of its predecessor. We then move the pointer to the left child of the current node.

The Morris traversal algorithm is more efficient than the recursive algorithm in both time and space complexity. However, it is more difficult to implement.

# Connect with me: https://github.com/ohkrahul
