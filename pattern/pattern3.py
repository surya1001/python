n = 5
# for i in range(1, n+1):
#     for j in range(i):
#         print(i-j, end="")
#     print("")

# for a in range(1, n + 1):
#     for b in range(1, a-1):
#       print(b, end="")
#     for b in range(a-1,0,-1):
#       print(b, end="")
#     print()

for i in range(1, n+1):
  for j in range(n,1,-1):
    print(n-j+1, end="")
  # for j in range(1,n+1):
  #   print(j, end="")
  print("")
