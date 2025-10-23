# OBST: Optimal Binary Search Tree using Dynamic Programming
def obst(p, q, n):
    w = [[0]*(n+1) for _ in range(n+1)]
    c = [[0]*(n+1) for _ in range(n+1)]
    r = [[0]*(n+1) for _ in range(n+1)]

    for i in range(n+1):
        w[i][i] = q[i]
        c[i][i] = 0
        r[i][i] = 0
        if i < n:
            w[i][i+1] = q[i] + q[i+1] + p[i+1]
            c[i][i+1] = w[i][i+1]
            r[i][i+1] = i+1

    for m in range(2, n+1):
        for i in range(n - m + 1):
            j = i + m
            w[i][j] = w[i][j-1] + p[j] + q[j]
            min_cost = float('inf')
            l = 0
            start = r[i][j-1] if r[i][j-1] != 0 else i+1
            end = r[i+1][j] if r[i+1][j] != 0 else j
            for k in range(start, end+1):
                cost = c[i][k-1] + c[k][j]
                if cost < min_cost:
                    min_cost = cost
                    l = k
            c[i][j] = w[i][j] + min_cost
            r[i][j] = l
    return c, w, r

n = int(input("Enter number of keys: "))
p = [0]*(n+1)
q = [0]*(n+1)

print("Enter probabilities for keys p[1..n]:")
for i in range(1, n+1):
    p[i] = float(input(f"p[{i}]: "))

print("Enter probabilities for dummy keys q[0..n]:")
for i in range(n+1):
    q[i] = float(input(f"q[{i}]: "))

c, w, r = obst(p, q, n)

print(f"\nMinimum cost of OBST: {c[0][n]:.2f}")

