#dijkstra
import math
n = int(input("Enter number of vertices: "))
print("Enter the adjacency matrix :")
cost = []
for i in range(n):
    row = list(map(float, input().split()))
    row=[float(x) if x!="inf" else float('inf') for x in row]
    cost.append(row)

source = int(input("Enter source vertex (0-based index): "))

dist = [math.inf] * n       # shortest distance from source
S = [False] * n             # visited vertices
dist[source] = 0

for i in range(n):
    for j in range(n):
        if cost[i][j] == 0 and i != j:
            cost[i][j] = math.inf

for _ in range(n):
    # Pick vertex u not in S with minimum dist[u]
    min_dist = math.inf
    u = -1
    for i in range(n):
        if not S[i] and dist[i] < min_dist:
            min_dist = dist[i]
            u = i

    if u == -1:  # All reachable vertices visited
        break

    S[u] = True

    for v in range(n):
        if not S[v] and dist[v] > dist[u] + cost[u][v]:
            dist[v] = dist[u] + cost[u][v]

print("\nShortest distances from vertex", source)
for i in range(n):
    print(f"Vertex {i}: {dist[i]}")

