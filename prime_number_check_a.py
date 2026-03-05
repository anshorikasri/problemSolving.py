class Solution:
    def is_prime(self, x):
        if x < 2:
            return False
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                return False
        return True



# instance
jwb=Solution()

# test -1
ans1 = jwb.is_prime(8)
print(ans1)

# test -2
ans2 = Solution().is_prime(5)
print(ans2)

# testing -1
print(int(3**0.5))
print(int(5**0.5))
print(int(7**0.5))
print('--')
# testing -2
print(int(4**0.5))
print(int(6**0.5))
print(int(8**0.5))
print('--')
# testing -3
print(int(9**0.5))
print('--')
print(int(10**0.5))
print(int(12**0.5))
print(int(14**0.5))
print(int(15**0.5))
print('--')
print(int(11**0.5))
print(int(13**0.5))
print('--')
# testing -2
print(int(16**0.5))