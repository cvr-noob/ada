n = int(input("Enter the no. of vertices: "))
e = int(input("Enter the no. of edges: "))

graph = [[] for _ in range(n)]

print("Enter edges (0-based indexes u v):")
for _ in range(e):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

dfn = [0] * n
l = [0] * n
num = 1
aps = set()

def art(u, v):
    global num
    dfn[u] = l[u] = num
    num += 1
    children = 0
    
    for w in graph[u]:
        if not dfn[w]:  # W is an unvisited child of U
            children += 1
            art(w, u)
            l[u] = min(l[u], l[w])

            if v != -1 and l[w] >= dfn[u]:
                aps.add(u)
        elif w != v:  # (U, W) is a back edge
            l[u] = min(l[u], dfn[w])

    if v == -1 and children > 1:  # U is root node
        aps.add(u)

for v in range(n):
    if not dfn[v]:
        art(v, -1)

print(aps)
