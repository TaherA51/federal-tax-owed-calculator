# lab 2 program b
# fed tax owed calculator

income = float(input('Enter your total income this year: '))
tax_owed = 0.00
# Define the tax brackets based on income ranges and tax rates for each bracket
bracket1 = 11000 * 0.1  # 10% tax on income up to $11,000
bracket2 = (44725 - 11000) * 0.12  # 12% tax on income from $11,001 to $44,725
bracket3 = (95375 - 44725) * 0.22  # 22% tax on income from $44,726 to $95,375
bracket4 = (182100 - 95375) * 0.24  # 24% tax on income from $95,376 to $182,100
bracket5 = (231250 - 182100) * 0.32  # 32% tax on income from $182,101 to $231,250
bracket6 = (578125 - 231250) * 0.35  # 35% tax on income from $231,251 to $578,125

# Check which tax bracket the income falls into and calculate the tax owed
if 0 <= income <= 11000:
    # If income is less than or equal to $11,000, apply 10% tax rate
    tax_owed = income * 0.1
elif 11001 <= income <= 44725:
    # If income is between $11,001 and $44,725, apply 10% to first $11,000,
    # and 12% to the remaining amount
    tax_owed = bracket1 + (income - 11000) * 0.12
elif 44726 <= income <= 95375:
    # If income is between $44,726 and $95,375, apply 10% to first $11,000,
    # 12% to the next range, and 22% to the remaining amount
    tax_owed = bracket1 + bracket2 + ((income - 44725) * 0.22)
elif 95376 <= income <= 182100:
    # If income is between $95,376 and $182,100, apply 10%, 12%, 22%, and 24%
    tax_owed = bracket1 + bracket2 + bracket3 + ((income - 95375) * 0.24)
elif 182101 <= income <= 231250:
    # If income is between $182,101 and $231,250, apply 10%, 12%, 22%, 24%, and 32%
    tax_owed = bracket1 + bracket2 + bracket3 + bracket4 + ((income - 182100) * 0.32)
elif 231251 <= income <= 578125:
    # If income is between $231,251 and $578,125, apply 10%, 12%, 22%, 24%, 32%, and 35%
    tax_owed = bracket1 + bracket2 + bracket3 + bracket4 + bracket5 + ((income - 231250) * 0.35)
elif 578125 < income:
    # If income is greater than $578,125, apply 10%, 12%, 22%, 24%, 32%, 35%, and 37% to the rest
    tax_owed = bracket1 + bracket2 + bracket3 + bracket4 + bracket5 + bracket6 + ((income - 578125) * 0.37)

# Output the total tax owed, formatted to two decimal places
print(f'You owe ${tax_owed:.2f} this year.')


