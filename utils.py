def maxi(numbers):
    max=numbers[0]
    for x in numbers:
        if x>max:
            max=x
        
    return max


numbers=[5,4,5,7,6]
print(maxi(numbers))
