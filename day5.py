numbers=[1,2,3,4,5,6,7,8,9,10]
num_sq=[]
for x in numbers:
    square_numbers=x**2
    num_sq.append(square_numbers)
    

is_even=[]
is_odd=[]
is_factor3=[]
for i in num_sq:
    if i%3==0:
        is_factor3.append(i)
        
    if i%2==0:
        is_even.append(i)
    else:
        is_odd.append(i)
    
    

print(num_sq)
print(is_factor3,is_even,is_odd)


