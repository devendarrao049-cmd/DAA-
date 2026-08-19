# Factorial - Time and Space Complexity

| Method | Best Case | Average Case | Worst Case | Space Complexity |
|--------|-----------|--------------|------------|------------------|
| Iterative Factorial | O(n) | O(n) | O(n) | O(1) |
| Recursive Factorial | O(n) | O(n) | O(n) | O(n) |

## Iterative Factorial

- **Best Case:** O(n)
- **Average Case:** O(n)
- **Worst Case:** O(n)
- **Space Complexity:** O(1)
- Uses a loop to calculate the factorial.
- Does not use recursive function calls.

## Recursive Factorial

- **Best Case:** O(n)
- **Average Case:** O(n)
- **Worst Case:** O(n)
- **Space Complexity:** O(n)
- Uses recursive function calls.
- Each recursive call uses space in the call stack.

## Conclusion

- **Iterative Factorial** is more memory-efficient because it uses **O(1)** space.
- **Recursive Factorial** uses **O(n)** space because of the recursion call stack.
- Both methods have **O(n)** time complexity.
- For better memory usage, the **iterative method is preferred**.
- The recursive method is useful for understanding **recursion and recursive problem solving**.

### Comparison

| Feature | Iterative | Recursive |
|---------|-----------|-----------|
| Technique | Loop | Recursion |
| Time Complexity | O(n) | O(n) |
| Space Complexity | O(1) | O(n) |
| Memory Usage | Low | Higher |
| Easy to Implement | Yes | Yes |