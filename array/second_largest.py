a = [10,5,8,89,20, 78]
max = 0
max2 = 0
for i in a:
  if(max < i):
    max = i

for x in a:
  if x != max:
    if max2 == 0:
      max2 = x
    else:
      max2 = x

print(max)
print(max2)