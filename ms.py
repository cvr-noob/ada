def mergesort(low,high):
  if low<high:
    mid=(low+high)//2
    mergesort(low,mid)
    mergesort(mid+1,high)
    merge(low,mid,high)
def merge(low,mid,high):
  h=low
  b=[]
  j=mid+1
  while (h<=mid and j<=high):
    if a[h]<=a[j]:
      b.append(a[h])
      h+=1
    else:
      b.append(a[j])
      j+=1
  if h<=mid:
    while h<=mid:
      b.append(a[h])
      h+=1
  else:
    while j<=high:
      b.append(a[j])
      j+=1
  for k in range(0,high-low+1):
    a[low+k]=b[k]
a=list(map(int,input().split()))
mergesort(0,len(a)-1)
print(a)
import matplotlib.pyplot as plt
from math import log
x=[2,4,8,16,32]
y=[i*log(i,2) for i in x]
plt.plot(x,y,marker='o')
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()
