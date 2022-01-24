a = [10,20, 10, 40]

def checkSorted(a):
  for i, ind in enumerate(a):
    if(i > i+1):
      print("no")

print(checkSorted(a))