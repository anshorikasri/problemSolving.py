# 26.12.2025
class Solution:
    def romanToInt(self, s: str) -> int:
        dict_s={'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, "M":1000}
        
        arr_s=list(s)
        arr_balik=arr_s[::-1]
        # print(arr_balik)/// s='VIII' -> arr_balik=['I', 'I', 'I', 'V']
        print(list(reversed(s)))

        n=len(arr_balik)
        val= dict_s[arr_balik[0]]
        for i in range(n-1):
            if dict_s[arr_balik[i]] == dict_s[arr_balik[i+1]]:
                val = val + dict_s[arr_balik[i+1]]
                print(dict_s[arr_balik[i]])
                print(dict_s[arr_balik[i+1]])
            if dict_s[arr_balik[i]] < dict_s[arr_balik[i+1]]:
                val = val + dict_s[arr_balik[i+1]]
            if dict_s[arr_balik[i]] > dict_s[arr_balik[i+1]]:
                val = val - dict_s[arr_balik[i+1]]
        return val

        

        