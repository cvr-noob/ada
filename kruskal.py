#kruskals
import heapq

def find(parent, u):
    if parent[u] != u:
        parent[u] = find(parent, parent[u])
    return parent[u]

def union(parent, u, v):
    ru = find(parent, u)
    rv = find(parent, v)
    if ru != rv:
        parent[ru] = rv
        return True
    return False

def kruskals(n, edges):
    heapq.heapify(edges)
    parent = [i for i in range(n)]
    mst = []
    mincost = 0.0
    e_count = 0

    while e_count < n - 1 and edges:
        cost, u, v = heapq.heappop(edges)
        if union(parent, u, v):
            mst.append((u, v, cost))
            mincost += cost
            e_count += 1

    if e_count != n - 1:
        print("No spanning tree")
        return None
    else:
        print("\nEdges in the Minimum Spanning Tree:")
        for u, v, cost in mst:
            print(f"{u} - {v} -> {cost}")
        return mincost

n = int(input("Enter number of vertices: "))
edges = int(input("Enter number of edges: "))
e = []
print("Enter edges in format: cost u v")
for _ in range(edges):
    cost, u, v = map(int, input().split())
    e.append((cost, u, v))

mincost = kruskals(n, e)
if mincost is not None:
    print("\nMinimum Cost of Spanning Tree:", mincost)

