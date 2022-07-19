from abc import ABC
import sys
"""
#print("Hello World")
#print(sys.version)

#learning to comment
#print("{} is my country. All Indians are my brothers and sisters".format('India'))
#print("India is my country. All Indians are my brothers and sisters".count('India'))
#mystring="Superman"
#print(mystring.endswith('man'))
#print(mystring.endswith('man',3))
#print(mystring.endswith(('man','ma'),2,6))

mystring2="Good morning"
print(mystring2.find('Go'))
#test check 1,2,3

#tuples in python
months=("Jan","Feb","Mar")
print(months[0])
print(months[-1])
print(len(months))
print("Jan" in months)
#del(months)
print(months)#NameError: name 'months' is not defined
print(months+months)
print("ORA "*10)

#dictionary 
#method 1
students={"ABC":12,"DEF":14,"JKL":13}
#method 2
students=dict(ABC=12,DEF=14,JKL=13)
#method 3
students=dict({"ABC":12,"DEF":14,"JKL":13})

print(students)

#dict func
print(students.get("JKL"))#returns correspoing value
print(students.items())#returns dict items as array of tuples
print(students.keys())#returns key of dict
print(students.values())#return values of dict
print("DEF" in students)#check if key is present
print(14 in students.values())#check if value is present
print(len(students))

students2={"GHI":15,"XYZ":16}
students.update(students2)#adds the new val to old dict
print(students)

students.clear() #clears items
print(students)
del students #del dict
print(students)

#set
months={"Jan","Feb","Mar"}
print(months)
print(type(months))

for i in months:
    print(i)

#declare an empty set
days=set()
#add values to set
days.add("Mon")
days.add("Tue")
days.add("Wed")
days.update(["Thu","Fri"])
#if [] not present in update() o/p will come as ind letters

days.discard("Thu")#remove items but doesnt show error if not present
#days.remove("Thu")#remove items but shows error if not present
for day in days:
    print(day)
#clear elt in set
days.clear()

#set operations
months={"Jan","Feb","Mar"}
months2={"Apr","May","Mar"}
months4={"Mar","Apr","Jun","Jul"}

#union operation
months3=months|months2
print(months3)
for month in months:
    print(month)

#intersection
months3=months&months2
print(months3)

#intersect update
#months.intersection_update(months2,months4)
#print(months)

#diff
months3=months-months2
print(months3)

#symmetric diff-all elt except common ones
months3=months^months2
print(months3)

#set comparison
months={"Jan","Feb","Mar","Apr","May","Jun"}
months2={"Apr","May","Mar"}
months3={"Mar","Apr","Jun","Jul"}

#check if months is superset of months2
print(months>months2)
#equal(no of elt and elts shld be same)
print(months3==months2)
#equal and month is superset of month2
print(months>=months2)

#frozen set
frozenmonth=frozenset(["Nov","Dec"])#immutable set
print(type(frozenmonth))
print(frozenmonth)
frozenmonth.add("Oct")


#i/p and o/p func
studentname=input("Enter your name: ")
studentage=input("Enter your age: ")
print(studentname)
print(type(studentname))
print(studentage)
print(type(studentage))

#diff print stmt
print("The name is",studentname,"and the age is",studentage)
print("The name is %s and the age is %s"%(studentname,studentage))
print("The name is {} and the age is {}".format(studentname,studentage))

#print in multiple lines
print('''Hello World
How are you?''')

#print a new line
print("Hello\nhow are you?")
print("I'm 5\'3\"")


#conditional stmt
#if
num=input("Enter 1 or 2:")
if num=='1' :
    print("Num entered is 1")
elif num=='2':
    print("Num entered is 2")
else:
    print("Invalid no")

#inline if stmt
b=12
a=12 if b==10 else 13
print(a)

print("b is ten" if b==10 else "b is not 10")


#switch or match case stmt
#func def
def http_status(status):
    match(status):
        case 400:
            return "Bad request"
        case 404:
            return "pg not found"
        case _: 
            return "unknown error"

#calling func inside print stmt
print(http_status(404))
"""


