
#Exercise2
#A certain cinema currently sells tickets for a full price of 6 pounds, but always sells tickets for half price
# to people who are less than 16 years old, and for a third of the price for people who are 60 years old or more.

Full_Price =6
Half_Price=6/2
Third_of_Price=6/3
Age=int(input("Enter the age: "))
if Age < 16:
    print("Your ticket costs £",Half_Price)
elif Age >= 60:
    print("Your ticket costs £",Third_of_Price)
else:
    print("Your ticket costs £",Full_Price)



#Exercise4
#Write a python program to recieve 3 numbers from the user and print the greatest among them

Num1 = float(input("Enter first Number:"))
Num2 = float(input("Enter second Number:"))
Num3 = float(input("Enter third Number:"))
if Num1 >= Num2 and Num1>= Num3:
    greatest=Num1
elif Num2 >= Num1 and Num2 >= Num3:
    greatest=Num2
else:
    greatest=Num3
print("The greatest number is",greatest)



# Exercise5
# Find the factorial of a given number using loops

Num=int(input("Enter a number:"))
factorial=1
for i in range(1,Num+1):
    factorial = factorial*i
print("Factorial of ",Num,"is ",factorial)



#Exercise6
#Reverse a number using while loop

Num=int(input("Enter a number: "))
Original_Number = Num
Reverse_Number = 0
while Num > 0:
    remainder = Num % 10
    Reverse_Number = Reverse_Number * 10 + remainder
    Num //= 10
print("Reversed Number:",Reverse_Number)


#Exercise7
#Finding the multiples of a number using loop

Num=int(input("Enter a number: "))
Limit=int(input("Enter the limit: "))
print("Multiples of",Num,"upto given limit")
for i in range(1,Limit+1):
    multiples = Num*i
    print(multiples)


#Exercise8
#Write a program to print the inputted value as it is and break the loop if the value is 'done'.

count = 0
while True:
    user_input =input("Enter a value:")
    print(user_input)
    count += 1
    if user_input == 'done':
        break



#Exercise9
# Write a program that prints the numbers from 1 to 10. But for multiples of three print "Fizz" instead of the number
# and for the multiple of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz"
for num in range(1, 11):
    if num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    elif num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    else:
        print(num)

#Exercise10
#Write a program to print the following pattern
#5 4 3 2 1
#4 3 2 1
#3 2 1
#2 1
#1

i=5
while i >0:
    for num in range(i,0,-1):
        print(num, end=' ')
    print()
    i -= 1

