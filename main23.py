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
print("welcome to burger king!!!!")
item1="whopper burger"
item2="crispy veg"
item3="chicken wings"

print("the list of items is: ")
print("1.",item1)
print("2.",item2)
print("3.",item3)

item=(str(input("enter your item: ")))
code=input("enter if you have any coupon code available: ")
code.upper()

if item==item1:
    price=150
    print("the price for this itme is:",price)
elif item==item2:
    price=100
    print("the price for this item is: ",price)
elif item==item3:
    price=120
    print("the price for this item is: ",price)
print("coupon session: ")
if code=='KING50':
    
    code.upper()
    price=(price-(price*50/100))
    print("aftre discount you have: ",price)
elif code=='BK20':
    price=price-20
    print("after discount you have: ",price)
elif code=='NO DISCOUNT':
    print("no discount")
else:
    print("wrong input")



print("*******************")
print("your meal choice is: ", item)
print("your total price is:", price)
print("THANK YOU FOR THE MEAL")