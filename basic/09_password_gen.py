import random
# char = int(input("Enter number of letter in password"))
# sym = int(input("Enter number of symbols in password"))
# no = int(input("Enter number of numbers in password"))

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','#','$','%','&','(',')','*','+','=','-','_','{','}','[',']','<','>','?']

sp = []
#simple pass
for i in range(0, 10):
  rd = random.randint(0, len(letters)-1)
  sp = sp.append(letters[rd])

for i in range(0, 5):
  rd = random.randint(0, len(numbers)-1)
  sp = sp.append(numbers[rd])

for i in range(0, 5):
  rd = random.randint(0, len(symbols)-1)
  sp = sp.append(symbols[rd])
  
print(sp)