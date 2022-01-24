n = 5

for i in range(1,n+1):
  for j in range(n-i+1):
    print(i, end="")
  print("")

for i in range(n):
  for j in range(n,i,-1):
    print(n-i, end="")
  print("")