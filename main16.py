# question 1
l1=[1,2,3,4,5,6,7,8,9,10]
print(l1)

#question 2
l1=[1,10,100,3,6,8]
l1.insert(2,59)
print(l1)
l1.append(5)
print(l1)
print(len(l1))

#question 3
list1= [1,4,2,42,4,6,2,56,4,56,2]
print(list1[0:len(list1):2])

#question 4
list1= ["Gaurav",12,23,33.33,"Sharma",True]
print(list1[::4])

#question 5
list1= ["Gaurav",12,23,33.33,"Sharma",True]
print(list1[::4])
u=(list1[1:4])
print(u)
for i in u:
    i+=i
    print(i)

#question 6
friends=["riya","kiran","surbhi","komal","jannat"]
userfriend=input("enter a friend's name: ")
friends.append(userfriend)
print(friends)
userfriend2=input("enter your most important friend name:")
u=int(input("enter the index value where you want to insert this name: "))
friends.insert(u, userfriend2)
print(friends)

