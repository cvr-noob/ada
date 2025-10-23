#knapsack
n = int(input("Enter number of items: "))
profits = []
weights = []
for i in range(n):
    print(f"\nItem {i+1}:")
    p = float(input("Enter profit: "))
    w = float(input("Enter weight: "))
    profits.append(p)
    weights.append(w)
capacity = float(input("\nEnter knapsack capacity: "))
ratio = [profits[i] / weights[i] for i in range(n)]
items = list(zip(profits, weights, ratio))
items.sort(key=lambda x: x[2], reverse=True)
total_profit = 0
remaining = capacity

print("\nItems considered (profit, weight, ratio):")
for p, w, r in items:
    print(f"({p}, {w}, {r:.2f})")

print("\nItems selected:")
for p, w, r in items:
    if remaining == 0:
        break
    if w <= remaining:
        total_profit += p
        remaining -= w
        print(f"Full item taken -> profit = {p}, weight = {w}")
    else:
        fraction = remaining / w
        total_profit += p * fraction
        print(f"Fraction taken ({fraction*100:.2f}%) -> profit = {p * fraction:.2f}, weight = {remaining}")
        remaining = 0

print(f"\nMaximum profit: {total_profit:.2f}")

