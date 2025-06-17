name=input("enter your name: ")
sclass=input("enter your class: ")
section = input("enter your section: ")

a=int(input("enter first subject marks: "))
b=int(input("enter second subject marks: "))
c=int(input("enter third subject marks: "))
d=int(input("enter fourth subject marks: " ))
e=int(input("enter fifth subject marks: "))
result=(a+b+c+d+e)/5

print("name: ", name)
print("class: ", sclass)
print("section: ", section)
print("your total percentage is ", result )

# sum of numbers 
h=int(input("enter the first number: "))
s=int(input("enter the second number: "))
j=int(input("enter the third number: "))
sum = (a+b+c)
print("the sum of numbers is: ", sum)
#square of a number
print(h*h)

#temperature
celsius=str(input("enter the temperature: "))
conv=float(celsius)
fahr=((conv*9/5)+32)
print("the result in celsius is : ", celsius)
print("the result in fahrenheit is: ", fahr)

#quotient and reamainder

num1=int(input("enter the first number: "))
num2=int(input("enter the second number: "))
print(num1//num2)
print(num1%num2)