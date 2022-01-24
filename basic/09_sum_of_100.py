sum = 0
# for num in range(0,100):
#   sum = sum + (num+1)
# print(sum)

#sum of even
# for num in range(0,101,2):
#   sum = sum + num
# print(sum)

for num in range(0,101):
  if(num % 2) == 0:
    sum += num
print(sum)