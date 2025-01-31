word=input("enter the word:")
vowel_count=0
for i in word.lower():
    if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
        vowel_count=vowel_count+1

print("the number of vowels in ",word," is ",vowel_count)

def employee():
    print("i am deku")


employee()