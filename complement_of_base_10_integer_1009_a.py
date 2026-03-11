class Solution:
    def bitwiseComplement(self, n: int) -> int:
        
        # 09.07
        bin_n = ""
        if n>0:
            while n>=1:
                if n%2==1:
                    bin_n += '1'
                    
                else:
                    bin_n += '0'
                n = n//2
        elif n==0:
            bin_n += '0'
        
        # print(bin_n)

        res=""
        for c in bin_n:
            if c == '1':
                res += '0'
            else:
                res += "1"
        
        # print(res)

        val = 0
        for i in range(len(res)):
            val += int(res[i]) * (2**i)

        return val


# instance
jwb = Solution()
jwb1 = jwb.bitwiseComplement(5) # 5 is equal 0101
print(jwb1)
# 101 >< 010
# 010 is equal 2
# return -> 2

jwb2 = jwb.bitwiseComplement(10)
print(jwb2)

# 14 ->    1110 >< 0001    <- 1
# 10 ->    1010 >< 0101    <- 5
#  5 ->     101 ><  010    <- 2
jwb3 = jwb.bitwiseComplement(14)
print(jwb3)