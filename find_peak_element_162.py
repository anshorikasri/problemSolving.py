#start: 03.02.2026
# title: 162. Find Peak Element

# === === === ===

class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        l=0
        r=len(nums)-1

# [1,2,1, 3 ,7,6,4]
# low=1   m=6    right=4

# [ 7    ,6      ,4]
# low=7   m=6    right=4

# [7 ,           6]
# low=7   m=7    right=6

# [7]
# low=7   m=7    right=7

        while l < r:
            mid = (l+r)//2

            if nums[mid] < nums[mid+1]:
                l=mid+1
            else:
                r=mid
        return l

jwb=Solution()

jwb1=jwb.findPeakElement([1,9,1, 3 ,7,6,4])
print(jwb1)
