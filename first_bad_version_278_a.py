#start: 27.01.2026
# title: 278. First Bad Version

# === === === ===

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:



# ini pakai O(n)--> memakan waktu saat n sangat besar
# Memory Limit Exceeded



# karena kita tidak punya ada API -- isBadVersion() --  yang siap pakai,
# kita buat aja permisalan nilai
isBadVersion = {5:True, 4:True, 3:False, 2:False, 1:False}


class Solution:
    def firstBadVersion(self, n: int) -> int:
        list_n=[]
        for i in range(n,0,-1):
            list_n.append(i)
        # print(list_n)

        first=0
        for i in list_n:
            if isBadVersion[i] == True:
                first = i
        # print(first)
        return first


# kalau n bernilai kecil, karena O(n) maka masih ringan.
jwb=Solution()
jwb1=jwb.firstBadVersion(5)
print(jwb1)

jwb=Solution()
jwb2=jwb.firstBadVersion(4)
print(jwb2)

            