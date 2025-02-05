'''class Solution:
    def removeElement(nums, val):
        for x in nums:
            if x==val:
                nums.remove(x)
        return nums


solution1=Solution
print(solution1.removeElement([3,2,2,3],3))'''

class Solution:
        def index_finder(haystack,needle):
             if needle in haystack:
                index_of= int((haystack.index(needle)))
                print(index_of)
             else:
                print("-1")   

solu=Solution
solu.index_finder("sadbutsad","sad")