age = int(input("what is you current age : "))

years_left = 90 - age
days = years_left * 365
months = years_left * 12
week = years_left * 52

print(f"You have {days} days {months} months, {week} weeks left")