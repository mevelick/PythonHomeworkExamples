# Asking user for the number of hours worked and assigning the variable
hours_worked = int(input("Enter the number of hours worked: "))

# Asking user for their pay rate and assigning the variable
hourly_pay_rate = float(input("Enter your hourly pay rate: "))

# Calculation for gross salary
gross_salary = hours_worked * hourly_pay_rate

# Outputting result to the console, rounded to 2 decimal places
print("Your gross salary is: ", round(gross_salary, 2))

