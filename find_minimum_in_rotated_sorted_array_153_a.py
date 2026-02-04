#start: 03.02.2026
# title: 153. Find minimum in rotated sorted array

# === === === ===

# here, previously I solved the problem by sorting. 
#  -->    sorted_arr = sorted(nums)

# but, it takes big of time complexity O(n * log n)
# if it was 1.000.000 elements, it need 20 million of operation

# but, if we use O(log n)
# it more safe the memory, without the need to consume additional memory of sorted

# == == ==
# here is my O(n * log n):

class Solution:
    def findMin(self, nums: list[int]) -> int:
        sorted_number = sorted(nums)
        return sorted_number[0]


jwb=Solution()

jwb1=jwb.findMin([4,5,6,7,0,1,2])
print(jwb1)


jwb2=jwb.findMin([4,5,6,7,8,9,1,2])
print(jwb2)