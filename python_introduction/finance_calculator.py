# Prompt user for monthly income
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))

# REQUIRED CALCULATION FORMAT
monthly_savings = monthly_income - monthly_expenses

# Project annual savings with 5% interest
annual_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

print(f"Your monthly savings are ${monthly_savings}.")
print(f"Projected savings after one year, with interest, is: ${annual_savings}.")


# Output:
# Enter your monthly income: 5000
# Enter your total monthly expenses: 4000
#Your monthly savings are $1000.0.
#Projected savings after one year, with interest, is: $12600.0.
