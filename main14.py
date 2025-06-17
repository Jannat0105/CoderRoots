#question 1
str1="coder"
str2="roots"
str3="new"
str4="year"
print(str1[:2] + str2[-2:])
print(str3[:2] + str4[-2:])


#question 3
str1="abc"
str2="ing"
str3="ly"
a=len(str1)
if a>=3:
    if (str1.endswith("ing")):
            print(str1+str3)
    else:
         print(str1+str2)
else:
      print(str1)