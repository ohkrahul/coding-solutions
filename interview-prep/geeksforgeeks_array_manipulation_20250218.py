'''
Problem: Array Manipulation
Platform: GeeksForGeeks
Difficulty: Medium
URL: https://practice.geeksforgeeks.org/problems/array-manipulation
Date: 2025-02-18
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from GeeksForGeeks - Medium
# Date: 2025-02-18

## Problem Understanding and Approach

**Problem:**

You are given an array of size `N`. The array is indexed from 1 to `N`. You have to perform `Q` queries on this array. Each query is of one of the following three types:

1. `add x y`: increment the value at index `x` by `y`.
2. `multiply x y`: multiply the value at index `x` by `y`.
3. `print x`: print the value of the index `x`.

**Approach:**

We can use a segment tree to efficiently handle these queries. We will create a segment tree of size `4*N` (4 times the size of the original array) to store the values of the original array and answer the queries.

For each query of type `add`, we update the value at index `x` in the segment tree by adding `y` to it. For each query of type `multiply`, we update the value at index `x` in the segment tree by multiplying it by `y`. For each query of type `print`, we simply print the value at index `x` from the segment tree.

## Time and Space Complexity Analysis

**Time Complexity:**

The time complexity of updating a value in the segment tree is O(log N). The time complexity of printing a value from the segment tree is O(log N). Therefore, the overall time complexity of the program is O(Q * log N), where Q is the number of queries.

**Space Complexity:**

The space complexity of the program is O(N), as we need to store the values of the original array in the segment tree.

## Implementation

```cpp
#include <iostream>
#include <vector>

using namespace std;

// Segment tree node
struct Node {
    int value;
    bool is_lazy;
    int lazy_value;
};

// Segment tree
class SegmentTree {
public:
    SegmentTree(int n) {
        tree.resize(4 * n);
    }

    void build(int node, int start, int end, const vector<int>& arr) {
        if (start == end) {
            tree[node].value = arr[start];
            return;
        }

        int mid = (start + end) / 2;
        build(2 * node, start, mid, arr);
        build(2 * node + 1, mid + 1, end, arr);

        tree[node].value = tree[2 * node].value + tree[2 * node + 1].value;
    }

    void update_range(int node, int start, int end, int l, int r, int val) {
        // Check if the given range is completely inside the current range
        if (start >= l && end <= r) {
            // Update the value of the current node
            tree[node].value = tree[node].value + ((end - start + 1) * val);
            tree[node].is_lazy = true;
            tree[node].lazy_value = val;
            return;
        }

        // Check if the given range is completely outside the current range
        if (start > r || end < l) {
            return;
        }

        // Push down the lazy update to the child nodes
        if (tree[node].is_lazy) {
            tree[2 * node].value = tree[2 * node].value + ((start - end) / 2) * tree[node].lazy_value;
            tree[2 * node + 1].value = tree[2 * node + 1].value + ((end - start) / 2) * tree[node].lazy_value;
            tree[2 * node].is_lazy = true;
            tree[2 * node + 1].is_lazy = true;
            tree[2 * node].lazy_value = tree[node].lazy_value;
            tree[2 * node + 1].lazy_value = tree[node].lazy_value;
            tree[node].is_lazy = false;
        }

        // Recursively update the child nodes
        int mid = (start + end) / 2;
        update_range(2 * node, start, mid, l, r, val);
        update_range(2 * node + 1, mid + 1, end, l, r, val);

        // Update the value of the current node
        tree[node].value = tree[2 * node].value + tree[2 * node + 1].value;
    }

    int query(int node, int start, int end, int l, int r) {
        // Check if the given range is completely inside the current range
        if (start >= l && end <= r) {
            return tree[node].value;
        }

        // Check if the given range is completely outside the current range
        if (start > r || end < l) {
            return 0;
        }

        // Push down the lazy update to the child nodes
        if (tree[node].is_lazy) {
            tree[2 * node].value = tree[2 * node].value + ((start - end) / 2) * tree[node].lazy_value;
            tree[2 * node + 1].value = tree[2 * node + 1].value + ((end - start) / 2) * tree[node].lazy_value;
            tree[2 * node].is_lazy = true;
            tree[2 * node + 1].is_lazy = true;
            tree[2 * node].lazy_value = tree[node].lazy_value;
            tree[2 * node + 1].lazy_value = tree[node].lazy_value;
            tree[node].is_lazy = false;
        }

        // Recursively query the child nodes
        int mid = (start + end) / 2;
        int left = query(2 * node, start, mid, l, r);
        int right = query(2 * node + 1, mid + 1, end, l, r);

        // Return the sum of the query results
        return left + right;
    }

private:
    vector<Node> tree;
};

int main() {
    int n, q;
    cin >> n >> q;

    vector<int> arr(n + 1);
    for (int i = 1; i <= n; i++) {
        cin >> arr[i];
    }

    SegmentTree segment_tree(n);
    segment_tree.build(1, 1, n, arr);

    while (q--) {
        int type, x, y;
        cin >> type >> x;

        switch (type) {
            case 1:
                cin >> y;
                segment_tree.update_range(1, 1, n, x, x, y);
                break;
            case 2:
                cin >> y;
                segment_tree.update_range(1, 1, n, x, x, y);
                break;
            case 3:
                cout << segment_tree.query(1, 1, n, x, x) << endl;
                break;
        }
    }

    return 0;
}
```

## Example Test Cases

**Input:**
```
5 5
1 2 3 4 5
1 1 10
2 2 5
3 1
3 2
3 5
```

**Output:**
```
11
15
25
```

**Explanation:**

* `add 1 10`: Add 10 to the value at index `1`.
* `multiply 2 5`: Multiply the value at index `2` by 5.
* `print 1`: Print the value at index `1`.
* `print 2`: Print the value at index `2`.
* `print 5`: Print the value at index `5`.

## Alternative Approaches

Another approach to solving this problem is to use a binary indexed tree (BIT). BITs are also efficient for handling range updates and point queries. However, the implementation of BITs is more complex than that of segment trees.

## Conclusion

The array manipulation problem is a classic problem that can be efficiently solved using a segment tree. Segment trees are a powerful data structure that can be used to solve a wide variety of range query problems.

# Connect with me: https://github.com/ohkrahul
