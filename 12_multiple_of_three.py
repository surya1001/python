num = int(input("start range : "))
end = int(input("end range : "))

# for i in range(num, end+1, 1):
#   if i % 3 == 0:
#     print(i)

if num % 3 == 0:
  n = num
elif num % 3 == 1:
  n = num+2
elif num % 3 == 2:
  n = num+1

for i in range(n, end, 3):
  print(i)
