#leetcode:219 (COntains Duplicate II)
#status: unfinished to solve
#start: 01.01.2026

# Given an integer array nums and an integer k, 
# return true if there are two distinct indices i and j in the array 
# such that:
# nums[i] == nums[j] and abs(i - j) <= k

def containsNearbyDuplicate(nums, k) -> bool:
        map_num = {}

        '''Python dictionaries cannot have two identical or the same keys.'''

        for i , n in enumerate(nums):
            map_num[i]=n
            # if n in map_num.values():
            #     return abs()
        print('map_num = ')
        print(map_num)


        # k --> keys
        # v --> values

        dupli_num = {}
        for ke,va  in map_num.items():
            if va in dupli_num:
                dupli_num[va].append(ke)
            else:
                dupli_num[va] = [ke]  
                #kalu nilai yang ditambah dgn menggunakan kurung, nanti jadi list
        print('dupli_num =')
        print(dupli_num)


        more_one = []
        for val in dupli_num.values():
            for i in range( len(val) - 1):
                if val[i+1] - val[i] <= k:
        #             return True
        # return False
                    return print('True')
        return print('False')





containsNearbyDuplicate([9,7,1,9,8,2], 3)
containsNearbyDuplicate([9,7,1,9,8,2], 1)
