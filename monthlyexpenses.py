#for string concatenation use + for int concatenation use ,
things_input=input("Enter the things you spend money on seperated by a comma: ")
things_list=things_input.split(',')
balance=2941

for i in things_list:
    price=int(input("Enter the money you spent on "+i+" "))
    balance=balance-price

print("your remaining purse is ",balance)
