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

# ----------------------------------------------------------
# 30.01.2026

isReVersi = {5:True, 4:True, 3:False, 2:False, 1:False}

class Jawaban:
    def reVersi(self, n: int) -> int:
        
        left=1
        right=n

        while left<=right:
            mid = (left+right)//2
            res = isReVersi[mid]

            if res == False:
                left=mid+1
            elif res== True:
                right=mid-1
        return left

hasil=Jawaban()
hasil_1=hasil.reVersi(5)
print(hasil_1)

hasil=Jawaban()
hasil_2=hasil.reVersi(10)
print(hasil_2)