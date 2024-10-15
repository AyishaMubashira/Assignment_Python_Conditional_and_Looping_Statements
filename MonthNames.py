
# Exercise1
# Name your file: MonthNames.py
# Write a program that reads an integer value between 1 and 12 from the user and
# prints output the corresponding month of the year.

Month_names = {1: "January",2: "February",3: "March",4: "April",5: "May",6: "June",7: "July",
               8: "August",9: "September",10: "October",11: "November",12: "December"}
Month_number = int(input("Enter the Month: "))
if 1<= Month_number <= 12:
    print(f"Month {Month_number} is {Month_names.get(Month_number)}")
else:
    print("Invalid_month")




































