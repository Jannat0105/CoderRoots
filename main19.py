# question 1
dict={}
u=int(input("enter the number of times you want to enter the data items: "))
dict={input("enter the keys: ") : input("enter the values: ") for i in range(u)}
print(dict)

# question 2
employee_details={1:{"name":"harry", "department":"engineer", "salary":10000},
                  2:{"name":"sharry", "department":"receptionist", "salary":6000},
                  3:{"name":"iriee", "department":"maths", "salary": 60000},
                  4:{"name":"john", "department":"physics", "salary":70000}}

high_salary=[]

for emp in employee_details.values():
    if emp['salary']> 50000:
        high_salary.append(emp['name'])

print(high_salary)

# question 3
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


# question 4

price = float(input("Enter the price of the product: "))

if price > 1000:
    discount = price * 0.10
elif price >= 500 and price<=1000:
    discount = price * 0.05
else:
    discount = 0

print("Discount:", discount)
print("Final price:", price - discount)

    # question 5
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


# question 6
li=[20,30,40,[57,66,30,[70,80],"Hello"],50,True]
li[3][3].insert(1,76)
print(li)
li[3].insert(1,88)
print(li)
print(li[3][5][0])



print("Welcome to Trip Planner")
budget = int(input("Enter your budget (5000-10000, 10000-20000, 20000-30000, 30000-40000): "))

destinations = {
    "India": "Taj Mahal",
    "Australia": "Sydney Opera House",
    "USA": "Grand Canyon",
    "France": "Eiffel Tower",
    "Japan": "Mount Fuji"
}

if 5000 <= budget <= 10000:
    options = ["India"]
elif 10000 < budget <= 20000:
    options = ["India", "Australia"]
elif 20000 < budget <= 30000:
    options = ["India", "Australia", "USA"]
elif 30000 < budget <= 40000:
    options = ["India", "Australia", "USA", "France", "Japan"]
else:
    options = []
    print("Sorry, we have no suggestions for this budget.")

if options:
    print("Countries available under", budget, "are:")
    for country in options:
        print("-", country)
    
    choice = input("Select your choice: ")
    choice = choice.title()
    
    if choice in destinations and choice in options:
        print("The place to visit in", choice, "is the", destinations[choice])
    else:
        print("Invalid selection.")
