print("Welcome to the tip calculator.")

bill = float(input("What was the total bill? $"))
tip = int(input("What percentage of the tip would youlike to give? 10, 12, or 15 ?"))
people = int(input("How many people would split the bill ?"))


new_bill = (bill * (tip / 100) + bill)
final_bill = bill / people
rounded_bill = round(final_bill, 2)

print(f"Each person should pay: ${rounded_bill}")