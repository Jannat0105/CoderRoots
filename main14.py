#question 1
str1="coder"
str2="roots"
str3="new"
str4="year"
print(str1[:2] + str2[-2:])
print(str3[:2] + str4[-2:])

# question 2 

st1="coder"
st2="roots"
st3=st1.replace("c","r")
st4=st2.replace("r","c")
print(st3 + " " + st4)



#question 3
str5="abc"
str6="ing"
str7="ly"
a=len(str1)
if a>=3:
    if (str5.endswith("ing")):
            print(str5+str7)
    else:
         print(str5+str6)
else:
      print(str5)

# question 4

s = "hello"
n = 2

if n < 0 or n >= len(s):
    print("Index out of range")
else:
    s = s[:n] + s[n+1:]
    print("Result:", s)

