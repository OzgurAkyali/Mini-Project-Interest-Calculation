principal = float(input("Enter your principal amount: "))
interest_rate = float(input("Enter your interest rate: "))
days = float(input("Enter the number of days: "))
tax_rate = float(input("Enter the tax rate on interest (as a percentage): "))

daily_interest_rate = principal / 100
annual_rate_adjusted = interest_rate / 365
interest_earned = daily_interest_rate * annual_rate_adjusted * days

print("--------------------------------")

print("Interest Earned:", float(interest_earned))

tax_amount = float(interest_earned * (tax_rate / 100))
print(f"Tax on the interest ({tax_rate}%):", tax_amount)

amount_after_tax = float(interest_earned - tax_amount)
print("Amount after tax deduction:", amount_after_tax)

print("Total amount after interest:", amount_after_tax + principal)
