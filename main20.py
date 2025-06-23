# question 1
for i in range(51):
    
    if i%3==0 and i%5==0:
        print("fizzbuzz")
    elif i%3==0:
        print("fizz")
    elif i%5==0:
        print("buzz")
    else:
        print(i)


# question 2
def primes():
    for num in range(1,101):
  
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                print(num)

primes()


# question 3

grade=int(input("enter the grade scored: "))

if grade<=100 and grade>=90:
    print("A")
elif grade<=90 and grade>=89:
    print("B")
elif grade<=89 and grade>=79:
    print("C")
elif grade<=79 and grade>=60:
    print("D")
else: 
    print("fail")


# question 4
a=int(input("enter a number: "))
for i in range(11):
    print(a,"*",i, "=", a*i )


# question 5
c=[]
for i in range(21):
    if i%2==0:
        c.append(i*i)
print(c)


# question 6 
b=int(input("enter a year: "))
if b%4==0 or b%400==0:
    print("leap year")
else:
    print("not a leap")

# question 7 
a=int(input("enter the first side of a triangle: "))
b=int(input("enter the second side of a triangle: "))
c=int(input("enter the third side of a triangle: "))

if a==b and b==c and c==a:
    print("the triangle is equilateral")
if a==b or b==c or c==a:
    print("the triangle is isosceles")
else:
    print("the triangle is scalene")

# question 8
c=int(input("enter a number: "))

if c<0:
    print(" a negative number")
elif c>0:
    print("a positive number")
elif c==0:
    print("the number is a zero")
else:
    print("invalid choice")



# question 9
import string 
pwd=input("enter your password: ")
a=False
b=False
c=False

if len(pwd)<=8:
    print("password length is correct")
else:
    print("password needs to be written with at least 8 characters")

for i in pwd:
    if i.isupper():
        a=True 
    if i.islower():
        b=True
    if i in string.punctuation:
        c=True
if (a and b):
    print("password contains both upper as well as lower characters")
else:
    print("password must contain at least one upper and lower character")

if i.isdigit():
    print("password contains a digit")
else:
    print("there is no digit....contain at least one")

if c:
    print("contains special character and your password is ready to go")
else:
    print("contain a special character to complete the process")


# question 10
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in cm: "))

bmi = weight / ((height / 100) ** 2)  
print("Your BMI is:", round(bmi, 2))

if bmi<18.5:
    print("underweight")
elif 18.5 <= bmi < 24.9:
    print("normal weight")
elif 25 <= bmi < 29.9:
    print("overweight")
elif bmi >= 30:
    print("obesity")
else:
    print("invalid choice")


# question 11
a= int(input("enter your number from 1 to 7: "))
if a==1:
    print("monday")
elif a==2:
    print("tuesday")
elif a==3:
    print("wednesday")
elif a==4:
    print("thursday")
elif a==5:
    print("friday")
elif a==6:
    print("saturday")
elif a==7:
    print("sunday")

else:
    print("invalid input")


# question 12

price = float(input("Enter the price of the product: "))

if price > 1000:
    discount = price * 0.10
elif price >= 500 and price<=1000:
    discount = price * 0.05
else:
    discount = 0

print("Discount:", discount)
print("Final price:", price - discount)



# question 13
n=int(input("enter the range of numbers"))
sum=0
for i in range (n+1):
    sum+=i
print(sum)


# qurstion 14

employee_details={1:{"name":"harry", "department":"engineer", "salary":10000},
                  2:{"name":"sharry", "department":"receptionist", "salary":6000},
                  3:{"name":"iriee", "department":"maths", "salary": 60000},
                  4:{"name":"john", "department":"physics", "salary":70000}}

high_salary=[]

for emp in employee_details.values():
    if emp['salary']> 50000:
        high_salary.append(emp['name'])

print(high_salary)




# question 15 
str1=input("enter the string ")
str1=str1.lower()
count=0

for i in str1:
    if i=='a' or i=='e' or i=='i' or i=='o' or  i=='u':
        count+=1

if count==0:
    print("no vowels found")
else:
    print("the number of vowels are :", count)

# question 16
num=input("enter the number: ")
sum=0
for i in num:
    sum=sum + int(i)
print(sum)


# question 17 
for i in range(6):
    for j in range(1,i+1):
        print("*", end="")
    print()


# question 18
import random

number = random.randint(1, 100)

while True:
    guess = int(input("Guess a number between 1 and 100: "))
    
    if guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed it right.")
        break


# question 19
num = int(input("Enter a number: "))

for i in range(1, num + 1):
    if i % 2 == 0:
        print(i)


# question 20
numbers = [10, 25, 33, 25, 50, 42, 25, 60, 71, 80]

if 25 in numbers:
    print("25 exists in the list")
else:
    print("25 does not exist in the list")

print("Length of list:", len(numbers))
print("Total occurrence of 25:", numbers.count(25))

print("Traversing each element:")
for num in numbers:
    print(num)

print("Even numbers in the list:")
for num in numbers:
    if num % 2 == 0:
        print(num)


# question 21
text = input("Enter a string with 10 to 19 words: ")
words = text.split()

if len(words) < 10 or len(words) > 19:
    print("Invalid input. Please enter between 10 and 19 words.")
else:
    print("Full string:", text)
    print("Length of string:", len(text))

    if text == text[::-1]:
        print("The string is a palindrome")
    else:
        print("The string is not a palindrome")

    middle_index = len(words) // 2
    print("Middle word:", words[middle_index])
    print("Second last word:", words[-2])




# question 22

print("Welcome to Calci:")
print("1. Power")
print("2. Sum")
print("3. Sub")
print("4. Multiple")

choice = int(input("Enter your choice. --> "))
if choice == 1:
    x = float(input("Enter 1st Number for Power: "))
    y = float(input("Enter 2nd Number for Power: "))
    print("Result is", x ** y)
elif choice == 2:
    x = float(input("Enter 1st Number for Sum: "))
    y = float(input("Enter 2nd Number for Sum: "))
    print("Sum is", x + y)

elif choice == 3:
    x = float(input("Enter 1st Number for Sub: "))
    y = float(input("Enter 2nd Number for Sub: "))
    print("Subtraction is", x - y)
elif choice == 4:
    x = float(input("Enter 1st Number for Multiple: "))
    y = float(input("Enter 2nd Number for Multiple: "))
    print("Multiplication is", x * y)
else:
    print("Invalid choice")


# question 23

X = ['abc', 'xyz', 'aba', '1221']
count = 0

for word in X:
    if len(word) >= 2 and word[0] == word[-1]:
        count += 1

print("Output:")
print(count)
