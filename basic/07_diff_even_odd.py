a = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,33]
evensum = 0
oddsum = 0
for i in a:
  if(i%2 == 0):
    evensum = evensum + i
  else:
    oddsum = oddsum + i
print(evensum-oddsum)