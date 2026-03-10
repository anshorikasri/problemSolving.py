class Solution:
    def findDifferentBinaryString(self, nums: list[str]) -> str:

        res = ""

        for i in range(len(nums)):
            res += '1' if nums[i][i]=='0' else '0'
        
        
        return res


# instance
jwb = Solution()

jwb1 = jwb.findDifferentBinaryString(['1010' , '1001','0001' , '0011'])
print(jwb1)