

#question 1 print the names of months as per user input
a= int(input("enter your number from 1 to 12: "))
if a==1:
    print("january")
elif a==2:
    print("february")
elif a==3:
    print("march")
elif a==4:
    print("april")
elif a==5:
    print("may")
elif a==6:
    print("june")
elif a==7:
    print("july")
elif a==8:
    print("august")
elif a==9:
    print("september")
elif a==10:
    print("october")
elif a==11:
    print("november")
elif a==12:
    print("december")

else:
    print("invalid input")

# question 2 apply conditions on numbbers



a=int(input("enter your first number: "))
b=int(input("enter your second number: "))
c=input("enter your first name")
d=input("enter your last name")

if a==b:
    print("both the numbers are equal")


elif a>b:
    print("a is greater")
    for i in range(5):
        print(c)

elif a<b:
    print("b is greater")
    for i in range(3):
        print(d)
else:
    print("invalid conditions")

if a<=b:
    print("a is less than or equal to b")
else:
    print("a is not less than or equal to b")

#question 3
a=input("enter the first string")
b=input("enter the second string")

if a==b:
    print(" both are equal using ==")
else:
    print("invalid")

print(" equality using is: ", (a is b))

# question 4
n=str(input("enter the first string"))
g=str(input("enter the second string"))
a=int(n)
b=int(g)

print(a is b)


#question 5
m=int(input("enter a number"))
result=0
for i in range(0,m+1):
    result+=i
print(result)


#question 6
s=int(input("enter the number"))

for i in range (0,s):
    if i%2==0:
       print(i)

#question 7
n=int(input("enter a number"))
for i in range(0,n,1):
    print(i)


for j in range(n, 0,-1):
    print(j)


#question 8
i=int(input("enter the number"))
for j in range(10):
    print(i, "*", j ,"=", i*j )

#question 9
for i in range(5):
    for j in range(1, i+1):
        print(j, end="")
    print()


#question 10
for i in range(10):
    print(i**2, end="")
    print()



