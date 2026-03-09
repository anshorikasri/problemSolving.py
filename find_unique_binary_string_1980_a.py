#start: 08.03.2026
# title: 1980. Find unique binary string

# === === === ===

class Solution:
    def findDifferentBinaryString(self, nums: list[str]) -> str:
        dict_idx = {}

        for string in nums:
            for i,n in enumerate(string):
                if i not in dict_idx:
                    dict_idx[i]=0
                if n =='1':
                    dict_idx[i] +=1
        
        print(dict_idx)


        len_n = len(nums)
        res = ""
        for i in range(len_n):
            if dict_idx.get(i,0) > len_n//2:
                res += '0'
            else:
                res += '1'
        
        # print(res)


        if res in nums:
            # Gunakan slicing yang kita pelajari tadi
            last_char = '1' if res[-1] == '0' else '0'
            res = res[:-1] + last_char
            
        return res



#instance
jwb = Solution()

jwb1 = jwb.findDifferentBinaryString(['1110','1101','0101','1111'])
print(jwb1)