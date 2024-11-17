'''
Problem: Binary Tree Traversal
Platform: LeetCode
Difficulty: Easy
URL: https://leetcode.com/problems/binary-tree-inorder-traversal
Date: 2024-11-17
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from LeetCode - Easy
# Date: 2024-11-17

## Problem Understanding and Approach

The problem asks us to implement the inorder traversal of a binary tree. Inorder traversal visits the nodes of the tree in the order of left subtree, root, and right subtree.

To solve this problem, we can use a recursive approach. The base case of the recursion is when the root is `nullptr`. In this case, we simply return. Otherwise, we first recursively visit the left subtree, then the root, and finally the right subtree.

## Time and Space Complexity Analysis

The time complexity of this algorithm is O(n), where n is the number of nodes in the tree. This is because we visit each node once and only once. The space complexity is O(h), where h is the height of the tree. This is because the recursion stack can be as deep as the height of the tree.

## Well-Commented Implementation

```cpp
class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> res;
        inorderTraversalHelper(root, res);
        return res;
    }
private:
    void inorderTraversalHelper(TreeNode* root, vector<int>& res) {
        if (!root) {
            return;
        }
        inorderTraversalHelper(root->left, res);
        res.push_back(root->val);
        inorderTraversalHelper(root->right, res);
    }
};
```

## Example Test Cases

```cpp
Input: [1,null,2,3]
Output: [1,3,2]

Input: []
Output: []

Input: [1]
Output: [1]
```

## Alternative Approaches

An alternative approach to solving this problem is to use an iterative approach. In this approach, we use a stack to keep track of the nodes that we need to visit. We start by pushing the root node onto the stack. Then, while the stack is not empty, we pop the top node from the stack and visit it. If the node has a left child, we push the left child onto the stack. If the node has a right child, we push the right child onto the stack.

The time complexity of this approach is O(n), where n is the number of nodes in the tree. The space complexity is O(h), where h is the height of the tree.

# Connect with me: https://github.com/ohkrahul
