import random
name = input("Give me all the members name, with comma and space seprated\n")
names = name.split(", ")
print(len(names))


choice = random.randint(0,len(names)-1)
print(choice)

print(f"its time for {names[choice]} to pay the bill")