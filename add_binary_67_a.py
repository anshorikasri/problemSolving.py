class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        list_a = list(map(int,a))
        list_a.reverse()
        # print(list_a)

        list_b = list(map(int,b))
        list_b.reverse()
        # print(list_b)

        total = 0
        for i,n in enumerate(list_a):
            total += n*(2**i)

        for i,n in enumerate(list_b):
            total += n*(2**i)      

        # print(total)

        res=[]

        if total ==0:
            res.append(0)

        else:
            while total>=1:
                if total%2==1:
                    res.append(1)
                    total= total//2
                else:
                    res.append(0)
                    total=total//2
        
        res.reverse()
        # print(res)

        result = map(str,res)
        sep=""
        hasil=  sep.join(result)
        return hasil


# instance
jwb =  Solution()
print(jwb.addBinary('110' , '1'))

print(jwb.addBinary('1001' , '11')) # 9 + 3 = 12    <==>  '1100'