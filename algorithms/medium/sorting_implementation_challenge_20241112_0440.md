# Sorting Implementation Challenge

## Category: algorithms
## Difficulty: medium

## Problem Description

Create an efficient solution for a algorithms problem focusing on sorting.

Requirements:
1. Implement the core functionality
2. Handle edge cases and errors
3. Optimize for performance
4. Add proper documentation
5. Include test cases

Focus on writing clean, maintainable code with proper error handling.
                    

## Solution
**Initial Approach and Thought Process:**

The best sorting algorithm to use depends on the specific requirements of the problem. For a medium-sized challenge, we can start with a simple and efficient algorithm like Merge Sort or Quick Sort. 

For Merge Sort, we recursively divide the array into smaller subarrays, sort them, and then merge them back together. This approach has a time complexity of O(n log n) and is relatively easy to implement.

**Complete Implementation with Comments:**

```
def merge_sort(arr):
    """Sort an array using Merge Sort algorithm.

    Parameters:
        arr (list): The array to be sorted.

    Returns:
        list: The sorted array.
    """

    # Base case: The array has only one element
    if len(arr) <= 1:
        return arr

    # Recursively sort the two halves of the array
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    # Merge the sorted halves
    merged_arr = []
    left_index = right_index = 0

    while left_index < len(left_half) and right_index < len(right_half):
        if left_half[left_index] <= right_half[right_index]:
            merged_arr.append(left_half[left_index])
            left_index += 1
        else:
            merged_arr.append(right_half[right_index])
            right_index += 1

    # Append the remaining elements
    merged_arr.extend(left_half[left_index:])
    merged_arr.extend(right_half[right_index:])

    return merged_arr
```

**Edge Cases and Error Handling:**

* If the input array is None or empty, return an empty list.
* If any elements in the input array are not comparable (e.g., mixed data types), raise a TypeError.

**Testing Strategy:**

* Test with various input arrays of different sizes and elements.
* Use edge cases: empty array, array with one element, array with duplicate elements.
* Compare the sorted array with the original array to ensure correctness.

**Performance Considerations:**

* Merge Sort has a worst-case time complexity of O(n log n) and a space complexity of O(n) since it uses additional memory to store the merged subarrays.
* For smaller arrays, faster sorting algorithms like Insertion Sort or Bubble Sort may be more efficient.

## Notes
- Added: 2024-11-12 04:40:40
- Author: [ohkrahul](https://github.com/ohkrahul)
- Category: algorithms
- Topics: arrays, strings, linked-lists, trees, graphs, dp, sorting
