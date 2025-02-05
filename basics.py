# getting user input and castin
'''
a=input("your name ")
b=int(input("your age "))
print("My name is ",a)
print("My age is ",str(b))

name=input("your name :")
score=int(input("enter your score for 100 :"))
department=input("your department :")
final_score=score/10
print("My name is ",name)
print("My score is ",final_score,"/10")
print("my department is ",department)
'''
#if else
'''
meghna=input("alive or dead :")
if (meghna=="dead"):
    print("surya meets priya")

else :
    print("surya weds meghna")
'''
'''
number=int(input("enter a number :"))
if(number%3==0 and number%5==0):
    print("yes,the number is divisible by both 3 and 5")
else:
    print("no,it is not divisible by both 3 and 5")
'''
'''
marks=int(input("enter your marks for 100 ;"))
if(marks<=35):
    print("poor performance")
elif(marks>35 and marks<=70):
    print("not a bad performance")
elif(marks>70 and marks<=100):
    print("very good performance")
else:
    print("invalid input")
'''
'''
a=int(input("enter a:"))
b=int(input("enter b:"))
operator=input("enter add or sub or mulor div :")
if(operator=="add"):
    print(a+b)
elif(operator=="sub"):
    print(a-b)
elif(operator=="mul"):
    print(a*b)
elif(operator=="div"):
    print(a/b)
else:
    print("invalid operator")
    salary=int(input("enter your salary:"))
age=int(input("enter age:"))
if(salary>=20000 or age<=25):
    loan=int(input("loan required:"))
    if(loan>50000):
        print("maximum loan is 50000")
    else:
        print("you are eligible for loan")
else:
    print("you are not eligible for loan")


year = int(input())
is_leap=False
if year%4==0:
    if year%100==0:
        if year%400==0:
            leap=True
    
elif year%4==0:
    leap=True
else:
    leap=False
    

print(leap)'''
