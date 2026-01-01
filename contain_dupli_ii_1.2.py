#leetcode:219 (COntains Duplicate II)
#status: unfinished to solve
#start: 01.01.2026

# previous version, code's run time is 265 ms
# becaause:
# looping through the data three separate times 
# and creating multiple extra objects in memory.

# we can use: One-Pass Hash Map

class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:

        last_seen = {}

        for i,n in enumerate(nums):
            if n in last_seen and (i - last_seen[n] <= k):
                return True
            last_seen[n] = i
        return False 

