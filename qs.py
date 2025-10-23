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
