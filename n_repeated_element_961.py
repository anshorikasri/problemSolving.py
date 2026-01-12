#start: 12.01.2026
# title: n-repeated element in size 2*n array

# link: https://leetcode.com/problems/n-repeated-element-in-size-2n-array/description/
# === === === ===


class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:

        dict_n = {}

        for n in nums:
            if n in dict_n:
                dict_n[n]=dict_n[n]+1
            else:
                dict_n[n]=1

        print(dict_n)

        for i in dict_n:
            if 2*dict_n[i] == len(nums):
                return i
