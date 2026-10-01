# Breadth First Search (BFS)

## Time Complexity of Breadth First Search Program

| **Case** | **Complexity** | **Description** |
|---|---|---|
| **Best Case** | **O(V + E)** | BFS visits the required vertices and checks their edges. |
| **Average Case** | **O(V + E)** | Each vertex is visited once and each edge is examined. |
| **Worst Case** | **O(V + E)** | BFS may visit all V vertices and examine all E edges. |

> **Where:**
>
> - `V` = Number of vertices
> - `E` = Number of edges

---

## Space Complexity

- **O(V)** → The `visited` set stores the vertices that have already been visited.
- **O(V)** → The `queue` can contain up to `V` vertices.
- **O(V + E)** → The `graph` dictionary stores all vertices and their adjacency lists.
- Therefore, the **overall space complexity is O(V + E)**.
- The **auxiliary space complexity is O(V)** for the `visited` set and queue.

---

## Conclusion

The **Breadth First Search (BFS)** algorithm is used to traverse a graph **level by level**.

In this program, the graph is represented using an **adjacency list**, and Python's `deque` is used as a **queue**.

The program starts from the given starting vertex, marks it as visited, and adds it to the queue. It then removes a vertex from the front of the queue and visits all its unvisited neighbouring vertices.

The **time complexity is O(V + E)** in the **best, average, and worst cases** because each vertex is visited once and each edge is examined during the traversal.

The **overall space complexity is O(V + E)** because the graph stores all vertices and edges. The **auxiliary space complexity is O(V)** for the `visited` set and queue.

BFS is commonly used for:

- Graph traversal
- Finding the shortest path in an unweighted graph
- Level-order traversal
- Checking graph connectivity