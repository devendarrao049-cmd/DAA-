v = 4

d = [
    [0, 5, float('inf'), 10],
    [float('inf'), 0, 3, float('inf')],
    [float('inf'), float('inf'), 0, 4],
    [float('inf'), float('inf'), float('inf'), 0]
]

for k in range(v):
    for i in range(v):
        for j in range(v):
            d[i][j] = min(d[i][j], d[i][k] + d[k][j])

print("Shortest distance matrix:")
for i in range(v):
    print(d[i])