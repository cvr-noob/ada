n = int(input("Enter no. of vertices: "))

cost = []

for _ in range(n):
    cost.append(
        list(map(lambda x: float("inf") if x == "inf" else float(x), input().split()))
    )


def dj(v, cost):
    n = len(cost)
    dist = [float("inf")] * n
    s = [False] * n

    for i in range(n):
        dist[i] = cost[v][i]
    dist[v] = 0
    s[v] = True

    for _ in range(n - 1):
        u = -1
        min_dist = float("inf")

        # Find u adjacent to v such that dist[u] is minimum
        for i in range(n):
            if not s[i] and dist[i] < min_dist:
                min_dist = dist[i]
                u = i

        # Early stop
        if u == -1:
            break

        s[u] = True
        # For all w adjacent to u
        for w in range(n):
            if not s[w] and dist[w] > dist[u] + cost[u][w]:
                dist[w] = dist[u] + cost[u][w]

    return dist


print(dj(0, cost))
