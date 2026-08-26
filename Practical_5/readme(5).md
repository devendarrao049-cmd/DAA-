| Case             | Time Complexity | Space Complexity |
| ---------------- | --------------- | ---------------- |
| **Best Case**    | O(n × W)        | O(n × W)         |
| **Average Case** | O(n × W)        | O(n × W)         |
| **Worst Case**   | O(n × W)        | O(n × W)         |
Where:

n = Number of items
W = Capacity of the knapsack
Explanation

This program uses Dynamic Programming to solve the 0/1 Knapsack Problem.

It creates a 2D DP table to store the maximum value for each item and capacity.
The outer loop runs for n items.
The inner loop runs for W capacity values.
Therefore, the total number of operations is n × W.
Time Complexity

O(n × W)

The same number of loops are executed regardless of the input values, so best, average, and worst cases are all O(n × W).

Space Complexity

O(n × W)

The program uses a 2D dp table of size (n+1) × (W+1) to store results.

Final Answer for Practical

Algorithm: 0/1 Knapsack using Dynamic Programming
Time Complexity: O(n × W)
Space Complexity: O(n × W)
Technique Used: Dynamic Programming