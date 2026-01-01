#version using: class and method

class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        map_num = {}

        '''Python dictionaries cannot have two identical or the same keys.'''

        for i , n in enumerate(nums):
            map_num[i]=n

        # k --> keys
        # v --> values

        dupli_num = {}
        for ke,va  in map_num.items():
            if va in dupli_num:
                dupli_num[va].append(ke)
            else:
                dupli_num[va] = [ke]  


        more_one = []
        for val in dupli_num.values():
            if len(val)>1:
                for i in range( len(val) - 1):
                    if val[i+1] - val[i] <=k:
                        return True
        return False

