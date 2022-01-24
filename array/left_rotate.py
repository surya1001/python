a = [1,2,3,4]
b = []
c = []
d = 2

# for i,ind in a:
#   b.append(a[i])

# b.append(a[0])
# print(b)

for i in range(d,len(a)):
  b.append(a[i])

for i in range(0,2):
  b.append(a[i])
  
print(b)