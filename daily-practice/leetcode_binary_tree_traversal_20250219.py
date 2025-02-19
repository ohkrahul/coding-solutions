'''
Problem: Binary Tree Traversal
Platform: LeetCode
Difficulty: Easy
URL: https://leetcode.com/problems/binary-tree-inorder-traversal
Date: 2025-02-19
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from LeetCode - Easy
# Date: 2025-02-19

### Problem Understanding

The inorder traversal of a binary tree visits the nodes in the following order: left subtree, root, right subtree.

### Approach

We can use a recursive algorithm to perform the inorder traversal. The algorithm will take a node as input and perform the following steps:

1. If the node is not null, then
2. Recursively call the algorithm on the left child of the node.
3. Visit the node.
4. Recursively call the algorithm on the right child of the node.

### Time and Space Complexity

The time complexity of the inorder traversal algorithm is O(n), where n is the number of nodes in the binary tree. This is because the algorithm visits each node in the tree once.

The space complexity of the inorder traversal algorithm is O(log(n)), where n is the number of nodes in the binary tree. This is because the algorithm uses a recursive call stack to traverse the tree.

### Well-Commented Implementation

```
public class InorderTraversal {
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> result = new ArrayList<>();
        inorderTraversalHelper(root, result);
        return result;
    }

    private void inorderTraversalHelper(TreeNode node, List<Integer> result) {
        if (node != null) {
            inorderTraversalHelper(node.left, result);
            result.add(node.val);
            inorderTraversalHelper(node.right, result);
        }
    }

    public static void main(String[] args) {
        TreeNode root = new TreeNode(1);
        root.left = new TreeNode(2);
        root.right = new TreeNode(3);
        root.left.left = new TreeNode(4);
        root.left.right = new TreeNode(5);

        InorderTraversal sol = new InorderTraversal();
        List<Integer> result = sol.inorderTraversal(root);
        System.out.println(result); // Output: [4, 2, 5, 1, 3]
    }
}
```

### Example Test Cases

* **Example 1:**

```
Input: [1, null, 2, 3]
Output: [1, 3, 2]
```

* **Example 2:**

```
Input: []
Output: []
```

* **Example 3:**

```
Input: [1]
Output: [1]
```

### Alternative Approaches

There are several alternative approaches to performing the inorder traversal of a binary tree. One approach is to use a stack. The algorithm would first push the root node onto the stack. Then, while the stack is not empty, the algorithm would pop the top node from the stack and visit it. If the popped node has a right child, then the algorithm would push the right child onto the stack. Finally, if the popped node has a left child, then the algorithm would push the left child onto the stack.

Another approach to performing the inorder traversal of a binary tree is to use Morris traversal. Morris traversal is a technique that uses threading to perform the inorder traversal without using a stack or recursion.

# Connect with me: https://github.com/ohkrahul
