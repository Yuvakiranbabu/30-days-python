#manipulating lists
# getting list as input

number_input=input("Enter the numbers you want in the list seperated by a comma: ")
numbers_list=list(map(int, number_input.split(",")))
non_duplicate_list=[]

for i in numbers_list:
    if i not in non_duplicate_list:
        non_duplicate_list.append(i)

non_duplicate_list.sort()
print(non_duplicate_list)



