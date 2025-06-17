#question 1
l1='hello this is the python code'
u=l1.split()
print(u)
v=[i for i in u if len(i)<4]
print(v)

# question 2
u='even'
v='odd'
y=[u if i%2==0 else v for i in range(20) ]
print(y)


#question 3
u=[i for i in range(1000) if i%7==0]
print(u)

# question 4
string2="hello this is the python code"
u=len([i for i in string2 if i==" "])
print(u)

# question 5
a=[1,2,3,4]
b=[2,3,4,5]
u=[i for i in a for j in b if i==j]
print(u)