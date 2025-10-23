arr = list(map(int, input('Enter array: ').split()))

def qs(arr, l, h):
  if l >= h:
    return
  
  pivot = partition(arr, l, h)
  qs(arr, l, pivot)
  qs(arr, pivot+1, h)

def partition(arr, l, h) -> int:
  i = l+1
  j = h
  pivot = arr[l]

  while i <= j:
    while i <= h and arr[i] < pivot:
      i += 1

    while j >= l and arr[j] > pivot:
      j -= 1

    if i < j:
      arr[i], arr[j] = arr[j], arr[i]

  arr[l], arr[j] = arr[j], arr[l]
  return j

qs(arr, 0, len(arr)-1)
print('Sorted:', arr)

import matplotlib.pyplot as plt
from math import log

n = [10, 20, 40, 80, 160, 320, 640, 1280]

best = [i * log(i, 2) for i in n]      # O(n log n)
average = [i * log(i, 2) for i in n]   # O(n log n)
worst = [i * i for i in n]             # O(n^2)

plt.plot(n, best, 'g-o')
plt.title("Quick Sort - Best Case Time Complexity")
plt.xlabel("Input Size (n)")
plt.ylabel("Operations (n log n)")
plt.show()

plt.plot(n, average, 'b-o')
plt.title("Quick Sort - Average Case Time Complexity")
plt.xlabel("Input Size (n)")
plt.ylabel("Operations (n log n)")
plt.show()

plt.plot(n, worst, 'r-o')
plt.title("Quick Sort - Worst Case Time Complexity")
plt.xlabel("Input Size (n)")
plt.ylabel("Operations (n²)")
plt.show()
