name=input("enter your name: ")
age=int(input("enter your age: "))
a=1500
b=1000
c=500
d=0


classs=input("enter your class from first , second, sleeper: ")
if age<5:
    price=1500
    print("your ticket price is: ", price)
elif classs=='first':
    print("the ticket price for this section is :", a)
    if age>5 and age<=60:
        print("your ticket price is: ",a)
    elif age>=60:
        print("you have a discount of 20 percent")
        price=a-(a*(20/100))
    print(price)
elif classs=='second':
    print("the ticket price for this section is :", b)
    if age>5 and age<=60:
        print("your ticket price is: ",b)
    elif age>=60:
        print("you have a discount of 20 percent")
        price=b-(b*(20/100))
    print(price)

else:
    price=c
    print("your ticket price is:", price)


meal=input("enter yes or no whether you want to add a meal or not: ")
meal=meal.lower()
if meal=='yes':
    price+=200
    print("your ticket price becomes: ", price)
else:
    price("your ticket price is: ", price)



print("passenger name: ", name)
print("age: ", age)
print("meal added: ",meal)
print("fina price", price)
print("enjoy yout journey!!")




# question 2
print("welcome to burger king!!")
print("here is the list of items: ")
cprice=0
a=int(input("enter your choice from 1,2,3: where 1 is whopper burger, 2 is crispy veg, 3 is chicken wings: "))
print(a)
if a==1:
    print("your choice is whopper burger")
    price=150
    print("your items holds price: ",price )
elif a==2:
    print("your choice is crispy veg")
    price=100
    print("your items holds price: ",price )
elif a==3:
    print("your choice is chicken wings")
    price=120
    print("your items holds price: ",price )
else:
    print("wrong choice...re-enter again from 1,2,3")

n=int(input("enter the quantity of your meal: "))
qprice=price*n
print(qprice)

print("coupon session: ")
coupon=input("do you have a coupon code? enter yes or no.")
coupon.lower()
if coupon=='yes':
    code=input("enter your coupon code: ")
    if code=="KING50":
        print("cupon applied")
        cprice=qprice-(qprice*50/100)
    print("your price is", cprice)
    if code=="BK20":
        print("coupon applied")
        cprice=qprice-20
    print("your price is", cprice)

    
else:
    print("no discount")

print("**********")
print("your total price", qprice )
print("price after applying coupon", cprice)
print("Thanks for ordering at burger king!!")