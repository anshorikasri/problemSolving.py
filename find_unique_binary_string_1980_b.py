class Solution:
    def findDifferentBinaryString(self, nums: list[str]) -> str:

        res = ""

        for i in range(len(nums[0])):
            if i < len(nums):
                res += '1' if nums[i][i]=='0' else '0'
            else:
                res += '0'  #or you can also res+='1'
        
        return res


# instance
jwb = Solution()

jwb1 = jwb.findDifferentBinaryString(['1010' , '1101','0001'])
print(jwb1)