
# Travelling Salesman Problem using Dynamic Programming

def tsp(curr, visited, cost, dp):

    n = len(cost)

    # If all cities are visited, return to starting city
    if len(visited) == n:
        return cost[curr][0]

    # Create a key for memoization
    key = (curr, tuple(sorted(visited)))

    # Check whether the result is already calculated
    if key in dp:
        return dp[key]

    ans = float('inf')

    # Visit all unvisited cities
    for i in range(n):

        if i not in visited:

            visited.append(i)

            total = cost[curr][i] + tsp(i, visited, cost, dp)

            ans = min(ans, total)

            visited.pop()

    # Store the result in DP dictionary
    dp[key] = ans

    return ans


# Main function
def SolveTSP(cost):

    dp = {}

    return tsp(0, [0], cost, dp)


# User Interface
n = int(input("Enter number of cities: "))

cost = []

print("Enter the cost matrix:")

for i in range(n):

    row = list(map(int, input().split()))

    cost.append(row)


# Calculate minimum travelling cost
result = SolveTSP(cost)

print("\nMinimum Travelling Cost:", result)