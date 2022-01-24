num = 9876
sum = 0

# for i in range(0, len(str(num))+1):
#   sum = sum + num%10

def tot(n):
  if(n < 10): return n
  return tot(n//10) + n%10
print(tot(num))

print(198//10)