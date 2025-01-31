#getting string list as input

fruits_input=input("Enter the list of fruits seperated by space: ")
fruits_list=fruits_input.split()
print(fruits_list)

#getting int list as input
numbers_input=input("Enter the numbers seperated by space: ")
numbers_list=list(map(int, numbers_input.split()))
print(numbers_list)
if 5 in numbers_list:
    print("Your fav number is there")
else:
    print("your fav number is not there")
