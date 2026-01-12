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
