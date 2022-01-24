s = int(input("Enter the start number: "))
e = int(input("Enter the end number: "))

#for checking whether number is prime or not
# flag = False

# for d in range(2, e-1):
#   if e % d == 0:
#     flag = True

# if flag:
#   print("not prime")
# else:
#   print("prime") 

# for prime numbers between range
# for d in range(s, e-1):
#   print(d % e)

for i in range(s, e-1):
  if(i % e == 0):
    print("not prime", i)