# Sorting Algorithms - Time and Space Complexity

| Algorithm | Best Case | Average Case | Worst Case | Space Complexity |
|-----------|-----------|--------------|------------|------------------|
| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) |
| Selection Sort | O(n²) | O(n²) | O(n²) | O(1) |
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) |
| Quick Sort | O(n log n) | O(n log n) | O(n²) | O(log n)* |

## Conclusion

- **Bubble Sort:** Simple to understand, but inefficient for large datasets.
- **Selection Sort:** Simple and uses less memory, but always takes O(n²) time.
- **Insertion Sort:** Best for small or nearly sorted datasets.
- **Merge Sort:** Provides consistent O(n log n) performance but requires O(n) extra space.
- **Quick Sort:** Very fast on average with O(n log n) time, but its worst case is O(n²).

### Note

Quick Sort has O(log n) average/best-case auxiliary space and can require O(n) space in the worst case because of recursion.