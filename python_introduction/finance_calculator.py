# Prompt user for monthly income
income = float(input("Enter your monthly income: "))

# Prompt user for monthly expenses
expenses = float(input("Enter your total monthly expenses: "))

# Calculate monthly savings
monthly_savings = income - expenses

# Calculate projected savings after one year with 5% interest
annual_savings = monthly_savings * 12
projected_savings = annual_savings + (annual_savings * 0.05)

# Display results
print(f"Your monthly savings are ${monthly_savings}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings}.")

# Output:
# Enter your monthly income: 5000
# Enter your total monthly expenses: 4000
#Your monthly savings are $1000.0.
#Projected savings after one year, with interest, is: $12600.0.