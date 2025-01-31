new_word=input("Enter the word: ")
def palindrome():
    rev_word=new_word[::-1]
    if new_word==rev_word:
        print("the word is palindrome")

    else:
        print("the given word is not palindrome")


palindrome()