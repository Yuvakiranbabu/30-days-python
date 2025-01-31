'''numbers=[1,2,3,4,26,6,7,8,9]
greatest=numbers[0]
for i in numbers:
    if greatest>=i:
        greatest=greatest
    elif greatest<i:
        greatest=i
print(greatest)
'''
#dictionaries

student_grades={
    "MOHITH":"O",
    "DHARUN":"O",
    "ANDREW GARFIELD":"F"
}

student_list=["mohith","dharun","ANDREW GARFIELD"]
print(student_list)
name=input("Enter the name of the student from the above list:")
print("His grade is ",student_grades[name.upper()])