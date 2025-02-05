num=1
def function():
    global num
    num+=1
    return num

print("num is: ",function())
print("num is: ",function())
print("num is: ",function())


list=[1,2,3,4,5]

def inc(x):
    x+=1
    return x
x=map(inc,list)
print(inc(x))

