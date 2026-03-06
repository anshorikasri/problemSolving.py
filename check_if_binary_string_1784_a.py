#start: 06.03.2026
# title: 1784. check if binary string ...

# === === === ===

class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        value= True

        balik = s[::-1]
        prev=0

        for i in range(len(balik)):
            curr= int(balik[i])
            if curr >= prev:
                prev=curr
                continue
            else:
                value = False
                break
            

        return value

#instance
jwb=Solution()

print(jwb.checkOnesSegment('11110'))
print(jwb.checkOnesSegment('11101'))