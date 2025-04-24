print("Welcome to the Tip Calculator!")

# Get user inputs
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people are splitting the bill? "))

# Calculate the tip and total bill per person
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people

# Format the final amount to 2 decimal places
final_amount = f"{bill_per_person:.2f}"

# Print the result
print(f"Each person should pay: ${final_amount}")
