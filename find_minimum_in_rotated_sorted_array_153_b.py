#start: 03.02.2026
# title: 153. Find minimum in rotated sorted array

# === === === ===

# using O(log n)
# --- --- --- ---

# ilustration 1:
# 7,0,1, 2, 4,5,6
# 7,  0,  1,  2
# 7,  0
# 0

# ilustration 2:
# [4,5,6,  7  ,0,1,2]
# 0,   1,   2
# 0,   1
# 0 

# -- -- -- -- --
class Solution:
    def findMin(self, nums: list[int]) -> int:
        # sorted_number = sorted(nums)
        # return sorted_number[0]

        l,r = 0  , len(nums)-1

        while l <r:
            mid = (l+r)//2

            if nums[mid] < nums[r]:
                r=mid
            else:
                l=mid+1
        return nums[r]          #atau return nums[l]


jwb=Solution()

jwb1=jwb.findMin([7,0,1, 2, 4,5,6])
print(jwb1)

jwb2=jwb.findMin([4,5,6,  7  ,0,1,2])
print(jwb2)

