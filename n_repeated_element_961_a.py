#start: 12.01.2026
# title: n-repeated element in size 2*n array

# link: https://leetcode.com/problems/n-repeated-element-in-size-2n-array/description/
# === === === ===


class Solution:
    def repeatedNTimes(self, nums: list[int]):

        dict_n = {}

        for n in nums:
            if n in dict_n:
                dict_n[n]=dict_n[n]+1
            else:
                dict_n[n]=1

        print('len(nums) =')
        print(len(nums))
        print('dict_n =')
        print(dict_n)

        for i in dict_n:
            if 2*dict_n[i] == len(nums):
                return i

# instance
jwb = Solution()

jwb1 = jwb.repeatedNTimes([1,7,3,7])
print(jwb1)