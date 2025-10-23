#prims
def prims(cost, n):
    INF = float('inf')
    t = [[-1, -1] for _ in range(n - 1)]
    near = [-1] * n
    mincost = 0
    min_val = INF
    u = v = -1
    for i in range(n):
        for j in range(n):
            if cost[i][j] < min_val:
                min_val = cost[i][j]
                u, v = i, j

    t[0][0] = u
    t[0][1] = v
    mincost += cost[u][v]

    for i in range(n):
        if cost[i][u] < cost[i][v]:
            near[i] = u
        else:
            near[i] = v
    near[u] = near[v] = -1
    for i in range(1, n - 1):
        min_val = INF
        k = -1
        for j in range(n):
            if near[j] != -1 and cost[j][near[j]] < min_val:
                min_val = cost[j][near[j]]
                k = j
        t[i][0] = k
        t[i][1] = near[k]
        mincost += cost[k][near[k]]
        near[k] = -1
        for j in range(n):
            if near[j] != -1 and cost[j][k] < cost[j][near[j]]:
                near[j] = k
    return t, mincost
INF = float('inf')
n = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))
cost = [[INF for _ in range(n)] for _ in range(n)]
print("Enter edges in format: u v c (0-based indices)")
for _ in range(e):
    u, v, c = map(int, input().split())
    u-=1
    v-=1#converting into #0-based index
    cost[u][v] = c
    cost[v][u] = c  # undirected graph
t, mincost = prims(cost, n)
print("\nEdges in the Minimum Spanning Tree:")
for edge in t:
    print(f"{edge[0]} - {edge[1]}")
print("\nMinimum Cost of Spanning Tree:", mincost)
