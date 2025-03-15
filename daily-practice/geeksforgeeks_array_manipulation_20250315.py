'''
Problem: Array Manipulation
Platform: GeeksForGeeks
Difficulty: Medium
URL: https://practice.geeksforgeeks.org/problems/array-manipulation
Date: 2025-03-15
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from GeeksForGeeks - Medium
# Date: 2025-03-15

```cpp
#include <iostream>
#include <vector>
#include <numeric> // For accumulate

using namespace std;

/*
Problem: Array Manipulation (GeeksForGeeks - Medium)

Description:
You are given an array arr[] of size N. You need to perform two types of operations on the array:
1. "UPDATE i v": Update the value at index 'i' to 'v'.  (0 <= i < N)
2. "QUERY l r": Find the sum of elements from index 'l' to 'r' (inclusive). (0 <= l <= r < N)

Problem Understanding and Approach:

We can use a segment tree to efficiently solve this problem. A segment tree allows us to perform both update and query operations in O(log N) time, where N is the size of the array.  The basic idea is to store sums of ranges in the tree nodes.

Time and Space Complexity:

- Time Complexity:
    - Update: O(log N)
    - Query: O(log N)
- Space Complexity: O(N) (for the segment tree)


Alternative Approaches:

- Brute Force: Update is O(1), but Query is O(N).  Inefficient for frequent queries.
- Prefix Sum Array: Update is O(N), Query is O(1). Inefficient for frequent updates.


*/

class SegmentTree {
private:
    vector<int> tree;
    int n;

    void build(const vector<int>& arr, int node, int start, int end) {
        if (start == end) {
            tree[node] = arr[start];
        } else {
            int mid = (start + end) / 2;
            build(arr, 2 * node + 1, start, mid);
            build(arr, 2 * node + 2, mid + 1, end);
            tree[node] = tree[2 * node + 1] + tree[2 * node + 2];
        }
    }

    void updateValue(int node, int start, int end, int index, int val) {
        if (start == end) {
            tree[node] = val;
        } else {
            int mid = (start + end) / 2;
            if (index <= mid) {
                updateValue(2 * node + 1, start, mid, index, val);
            } else {
                updateValue(2 * node + 2, mid + 1, end, index, val);
            }
            tree[node] = tree[2 * node + 1] + tree[2 * node + 2];
        }
    }

    int querySum(int node, int start, int end, int l, int r) {
        if (r < start || end < l) {
            return 0; // No overlap
        }
        if (l <= start && end <= r) {
            return tree[node];  // Complete overlap
        }

        int mid = (start + end) / 2;
        int leftSum = querySum(2 * node + 1, start, mid, l, r);
        int rightSum = querySum(2 * node + 2, mid + 1, end, l, r);
        return leftSum + rightSum;
    }

public:
    SegmentTree(const vector<int>& arr) : n(arr.size()) {
        tree.resize(4 * n); // Allocate space for the segment tree
        build(arr, 0, 0, n - 1);
    }

    void update(int index, int val) {
        updateValue(0, 0, n - 1, index, val);
    }


    int query(int l, int r) {
        return querySum(0, 0, n - 1, l, r);
    }
};


int main() {
    // Example test cases:
    vector<int> arr = {1, 3, 5, 7, 9, 11};
    SegmentTree st(arr);


    cout << "Sum(0, 2): " << st.query(0, 2) << endl; // Expected: 9 (1 + 3 + 5)
    cout << "Sum(1, 3): " << st.query(1, 3) << endl; // Expected: 15 (3 + 5 + 7)


    st.update(1, 10);  // Update arr[1] to 10
    cout << "Sum(0, 2) after update: " << st.query(0, 2) << endl; // Expected: 16 (1 + 10 + 5)

     st.update(0, 20);
    cout << "Sum(0, 0): " << st.query(0, 0) << endl;



    return 0;
}
```

# Connect with me: https://github.com/ohkrahul
