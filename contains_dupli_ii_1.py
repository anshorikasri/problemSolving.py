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
        for k,v  in map_num.items():
            if v in dupli_num:
                dupli_num[v].append(k)
            else:
                dupli_num[v] = [k]  
                #kalu nilai yang ditambah dgn menggunakan kurung, nanti jadi list
        print('dupli_num =')
        print(dupli_num)


        more_one = []
        for val in dupli_num.values():
            if len(val)>1:
                print('val =')
                print(val)




ans = containsNearbyDuplicate([9,7,1,9,8,8], 3)
