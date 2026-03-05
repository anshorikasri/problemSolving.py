#start: 21.02.2026
# title: 762. Prime Number of Set Bits in Binary Representation

# === === === ===

class Solution:
    def is_prime(self , x):
        if x <= 1:
            return False
        for i in range(2,x):
            if x%i == 0:
                return False
        return True
        

    def countPrimeSetBits(self, left: int, right: int) -> int:
        list_bit =[]
        for n in range(left , right+1):
            list_n=[]

            while n >= 1:
                if n%2 == 1:
                    list_n.append(1) 
                else:
                    list_n.append(0)
                n=n//2

            list_n.reverse()

            value=0
            for i in range(len(list_n)):
                if list_n[i]==1:
                    value+=1
            # print(list_n)

            list_bit.append(value)
        # print('----')
        # print(list_bit)

        max_prime = 0
        for i in list_bit:
            if self.is_prime(i):
                max_prime+=1
            else:
                continue
        return max_prime
        


# implementasi
jwb = Solution()

jwb1=jwb.countPrimeSetBits(2,6)
print(jwb1) # --> 2
# 2 : 0 0 1 0
# 3 : 0 0 1 1
# 4 : 0 1 0 0
# 5 : 0 1 0 1
# 6 : 0 1 1 0