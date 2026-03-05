class Solution:
    def is_prime(self, x):
        if x < 2:
            return False
        if x == 2:
            return True
        if x % 2 == 0:
            return False
        for i in range(3, int(x**0.5) + 1, 2):
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