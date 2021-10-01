# Programmer: Jonathan Ramos
# Course: CS151, Dr. Rajeev
# Date: September 29th, 2021
# Programming Assignment: 2
# Program Inputs: User inputs month represented by a number and also inputs the year
# Program Outputs: The program displays the number of days in that month and also identifies leap year

# User inputs
month = int(input("Enter Chosen Month (1-12) : "))
year = int(input("Enter Chosen Year (0000) : "))

# Check if input year is leap year
if year % 100 == 0:
    if year % 400 == 0:
        is_leap_year = True
    else:
        is_leap_year = False
elif year % 4 == 0:
    is_leap_year = True
else:
    is_leap_year = False

# Check for days if input month is February (Month 2) as it is affected by leap year
if is_leap_year == True and month == 2:
    is_month_valid = True
    days_of_month = "29"
elif is_leap_year == False and month == 2:
    is_month_valid = True
    days_of_month = "28"

# Check for days in months not affected by leap year
if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    is_month_valid = True
    days_of_month = "31"
elif month == 4 or month == 6 or month == 9 or month == 11:
    is_month_valid = True
    days_of_month = "30"
elif month < 1 or month > 12:
    is_month_valid = False

# Closing statements and validating month input
if is_leap_year == True and is_month_valid == True:
    print("\nYour chosen month has " + days_of_month + " days, and chosen year is a leap year!")
elif is_leap_year == False and is_month_valid == True:
    print("\nYour chosen month has " + days_of_month + " days, and chosen year is not a leap year!")
elif is_month_valid == False:
    print("\nMonth is not valid! Please enter months from 1-12 only.")
