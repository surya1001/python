a = [10,20,30,40,50,60,70]
x = 40

def bserahc(a,x):
  low = 0
  high = len(a)-1
  while low <= high:
    mid = (low+high)//2
    if(a[mid] == x):
      return mid
    elif(a[mid] < x):
      low = mid + 1
    else:
      high = mid - 1
  return -1

print(bserahc(a,x))