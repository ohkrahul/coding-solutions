'''
Problem: Binary Tree Traversal
Platform: LeetCode
Difficulty: Easy
URL: https://leetcode.com/problems/binary-tree-inorder-traversal
Date: 2024-12-25
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from LeetCode - Easy
# Date: 2024-12-25

### Approach
We perform inorder traversal using stack data structure.

### Time Complexity
O(N), where N is the number of nodes.

### Space Complexity
O(N), for the stack.

```java
class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode() {}
    TreeNode(int val) { this.val = val; }
    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

class Solution {
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> inorder = new ArrayList<>();
        Stack<TreeNode> stack = new Stack<>();

        TreeNode curr = root;
        while (curr != null || !stack.isEmpty()) {
            while (curr != null) {
                stack.push(curr);
                curr = curr.left;
            }
            curr = stack.pop();
            inorder.add(curr.val);
            curr = curr.right;
        }
        return inorder;
    }
}
```

### Test Case:
Input: [1,null,2,3]
Output: [1,3,2]

### Alternative Approaches:
1. Recursive Inorder Traversal:
   - This approach is simpler in implementation but requires extra stack space for function calls.
2. Morris Inorder Traversal:
   - This approach uses no extra space, but it modifies the original tree.

# Connect with me: https://github.com/ohkrahul
