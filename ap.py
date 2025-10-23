#articulation point
n = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))

graph = [[] for _ in range(n)]
print("Enter edges (0-based indices u v):")
for _ in range(e):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)  # undirected graph

dfn = [0] * n   # discovery time
L = [0] * n     # low value
num = 1
articulation_points = set()

def Art(u, v):
    global num
    global dfn, L, articulation_points
    dfn[u] = L[u] = num
    num += 1
    children = 0
    for w in graph[u]:
        if dfn[w] == 0:
            children += 1
            Art(w, u)  # DFS on unvisited child
            L[u] = min(L[u], L[w])
            if v != -1 and L[w] >= dfn[u]:
                articulation_points.add(u)
        elif w != v:
            L[u] = min(L[u], dfn[w])
    if v == -1 and children > 1:
        articulation_points.add(u)

Art(0,-1)

print("\nArticulation Points:")
for u in sorted(list(articulation_points)):
    print(u)
