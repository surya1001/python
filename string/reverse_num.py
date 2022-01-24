n = 10

# for i in range(n, 0, -1):
#   print(i)

# def printno(n):
#   if n == 0: return
#   print(n)
#   printno(n-1)

# printno(5)

def printnos(x):
  if(x > n): return
  print(x)
  printnos(x+1)

printnos(1)