#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

total_cost = float(input("Welcome to the tip calculator!\nWht was the total bill? "))
tip = float(input("How much tip would you like to give? "))
split_num = float(input("How many people to split the bill? "))

tip_fact = 1.00 + tip / 100.00

final_cost = (total_cost / split_num) * tip_fact

PerPerson = "{:.2f}".format(final_cost)
print(f"Each person should pay {PerPerson}")
