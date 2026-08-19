# Searching Algorithms - Time and Space Complexity

| Algorithm | Best Case | Average Case | Worst Case | Space Complexity |
|-----------|-----------|--------------|------------|------------------|
| Linear Search | O(1) | O(n) | O(n) | O(1) |
| Binary Search | O(1) | O(log n) | O(log n) | O(1) |

## Linear Search

- **Best Case:** O(1) — when the target element is found at the first position.
- **Average Case:** O(n) — when the target is found somewhere in the middle.
- **Worst Case:** O(n) — when the target is at the last position or not present.
- **Space Complexity:** O(1)
- **Requirement:** The array does not need to be sorted.

## Binary Search

- **Best Case:** O(1) — when the target element is found at the middle position.
- **Average Case:** O(log n)
- **Worst Case:** O(log n) — when the search continues until the last possible division.
- **Space Complexity:** O(1) for the iterative method.
- **Requirement:** The array must be sorted.

## Conclusion

- **Linear Search:** Simple and works on both sorted and unsorted arrays, but it is slower for large datasets.
- **Binary Search:** Much faster for large sorted datasets because it repeatedly divides the search area into half.
- **Linear Search:** Suitable for small or unsorted data.
- **Binary Search:** Suitable for large and sorted data.

### Comparison

Binary Search is more efficient than Linear Search for large datasets, with a worst-case time complexity of **O(log n)** compared to **O(n)** for Linear Search.