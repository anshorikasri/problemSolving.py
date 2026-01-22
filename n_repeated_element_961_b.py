#start: 22.01.2026
# title: n-repeated element in size 2*n array

# link: https://leetcode.com/problems/n-repeated-element-in-size-2n-array/description/
# === === === ===

class Solution:
    def repeatedNTimes(self, nums: list[int]):
        seen = set()
        for n in nums:
            if n in seen:
                return n
            seen.add(n)


#instance
jwb = Solution()
print(jwb.repeatedNTimes([2,1,3,3]))
print(jwb.repeatedNTimes([2,1,3,1,3,1]))