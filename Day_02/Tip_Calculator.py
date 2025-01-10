print("Welcome to the tip calculator!.")
total_bill=float(input("What was the total bill? \n$"))
tip = int(input("How much tip would you like to give ? 10, 12, or 15? \n"))
people_split=int(input("How may people to split the bill? \n"))
output=(total_bill)/people_split*(1+(tip/100))
print(f"Each person should pay: ${output:.2f}")


# Output:
# Welcome to the tip calculator!.
# What was the total bill? 
# $150
# How much tip would you like to give ? 10, 12, or 15? 
# 12
# How may people to split the bill? 
# 5
# Each person should pay: $33.60
