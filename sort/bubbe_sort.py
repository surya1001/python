#compare two elements
a = [2,10,8,7,27,12]

for i in range(len(a)-1):
  for j in range(len(a) - i -1):
    if(a[j] > a[j+1]):
      temp = a[j]
      a[j] = a[j+1]
      a[j+1] = temp

print(a)