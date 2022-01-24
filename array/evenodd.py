a = [12,13,14,16,17,18,19]
even = []
odd = []

for x in a:
  if(x%2 == 0):
    even.append(x)
  else:
    odd.append(x)

print(even, odd)