def kruskal(vertices, edges):
    edges.sort(key=lambda edge: edge[2])

    groups = [[v] for v in vertices]
    mst = []
    cost = 0

    for i, j, weight in edges:
        grp_i = None
        grp_j = None

        for group in groups:
            if i in group:
                grp_i = group

            if j in group:
                grp_j = group

        if grp_i != grp_j:
            mst.append((i, j, weight))
            cost += weight

            grp_i.extend(grp_j)
            groups.remove(grp_j)

    return mst, cost


# Input
vertices = ['A', 'B', 'C', 'D', 'E']

edges = [
    ('A', 'B', 2),
    ('A', 'C', 3),
    ('B', 'C', 1),
    ('B', 'D', 4),
    ('C', 'D', 5),
    ('C', 'E', 6),
    ('D', 'E', 7)
]

mst, cost = kruskal(vertices, edges)

print("Minimum Spanning Tree:", mst)
print("Total Cost:", cost)
