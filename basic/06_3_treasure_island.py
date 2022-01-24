print("Welcome to treasure island. Find the hidden tressure")

input("left or right")
if("right"):
  print("Game over")
elif("left"):
  input("swim or wait")
  if("swim"):
    print("Game over")
  else:
    input("which door! Red Blue or yellow")
    if("yellow"):
      print("You win")
    else:
      print("Game over")
