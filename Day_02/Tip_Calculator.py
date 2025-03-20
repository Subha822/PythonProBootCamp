print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
tip = bill * (tip / 100) + bill
total_pay = tip / people
print(f'Each person should pay: ${total_pay:.2f}')


# Output:
# Welcome to the tip calculator!.
# What was the total bill? 
# $150
# How much tip would you like to give ? 10, 12, or 15? 
# 12
# How may people to split the bill? 
# 5
# Each person should pay: $33.60
