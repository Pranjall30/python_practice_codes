#annual salary
annual_salary = float(input("Enter your annual salary: "))

#taxrate
tax_rate = float(input("Enter your tax rate (as a decimal): "))

#monthlysalary
monthly_salary = annual_salary / 12 * (1 - tax_rate)

print("Your monthly salary is: ", monthly_salary)