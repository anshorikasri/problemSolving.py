#start: 12.01.2026
# title: 66. plus one

# === === === ===

class Solution:
    def plusOne(self, digits: list[int]):
        balikArray= digits[::-1]

        # print(balikArray)
        banyakDigit = len(balikArray)
        # print(banyakDigit)
        
        total = 0
        for i,n in enumerate(balikArray):
            total+= n*(10**(i))
            # print(n)
            # print(i)
 
        # print(total)
        total+=1

        # ngetes aja
        # print(str(total)[1]+'b')

        #ini hasil output adalah object arr
        arr_object = (map(int , str(total))) 
        
        array = list(arr_object)
        # print(array)
        return array

# instance
jwb=Solution()

print(jwb.plusOne([1,2,3]))