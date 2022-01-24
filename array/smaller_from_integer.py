a = [8,100,20,40,3,7]
x = 10
s = []
for i in a:
  if(i < x):
    s.append(i)

even = [x for x in range(11) if x % 2 == 0]
d1 = {x:x**3 for x in range(10)}
print(even, d1)

print(s)