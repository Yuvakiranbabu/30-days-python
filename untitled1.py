'''
i=1
while i<2:
    car_state=input("> ")
    if car_state=="start":
        print("car started,ready to go!!!")

    elif car_state=="stop":
        print("car stopped")

    elif car_state=="quit":
        break

price=[10,20,30]
sum=0
for item in price:
    sum=sum+item

print(sum)'''

'''
nums=[2,7,11,15]
target=9
for x in nums:
    for y in nums:
        if x+y==9:
            var1=nums.index(x)
            var2=nums.index(y)

            print(var1,var2)
            break

    break
'''
'''
numbers=[5,15,4,4,30,26]
duplicate=0
for x in numbers:
    if x==duplicate:
        numbers.remove(x)
        print("the duplicate number is ",x)

    else:
        duplicate=x
        

print(numbers)
'''
'''
phone=input("enter your number: ")
words={
    "1":"one",
    "2":"two",
    "3":"three",
    "4":"four"
   
}
output=""
for x in phone:
    output=output+words.get(x)+" "
print(output)

def discount(price,discount_percentage):
    discount_amount=discount_percentage/100
    final_price=price-price*discount_amount
    return final_price 



print(discount(1000,20))


def string(sentence):
    x=0
    o=0
    for letter in sentence:
        if letter=="x":
            x=x+1
        elif letter=="o":
            o=o+1

    return x,o

print(string("xoxox"))
'''    
class Solution(object):
    def twoSum(self, nums, target):

            for x in nums:
                for y in nums:
                    if x+y==target:
                        xindex=nums.index(x)
                        yindex=nums.index(y)
                        final=[xindex,yindex]
                        print(final)
                break

Solution.twoSum(1,[2,11,7,15],9)
