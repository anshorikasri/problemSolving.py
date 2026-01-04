class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        last_seen={}


        for i,n in enumerate(nums):
            if n in last_seen and abs(i - last_seen[n]) <=k:
                return True
            last_seen[n]=i
        return False
        
solusi = Solution()
print(solusi.containsNearbyDuplicate([1,2,5,6,7,1,9] , 4))
print(solusi.containsNearbyDuplicate([1,2,5,6,7,1,9] , 6))