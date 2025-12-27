class Solution:
    def romanToInt(self, s: str) -> int:
        dict_s={'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, "M":1000}

        s = s[::-1]
        # print(type(s))  -->     <class 'str'>     (<--maksudnya string?)

        total = 0
        prev_val = 0

        for char in s:
            current_value = dict_s[char]
            
            if current_value < prev_val:
                total -= current_value
            else:
                total += current_value
            
            prev_val = current_value
        return total

