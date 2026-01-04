#start: 01.01.2026
# title: control flow

# we can use: various way for using if-else
# === === === ===

# 1. if-else
ifels_n = [2, 3, 5, 7, 8]
ans=[]

for n in ifels_n:
    if n%2==0:
        ans.append('even')
    else:
        ans.append('odd')

print(ans)
# === === === ===


# 2. ternary
ternary_n = [2, 3, 5, 7, 8]
ans_t = []

for n in ternary_n:
    ans_t.append('even') if n%2 == 0 else ans_t.append('odd')

print(ans_t)
# === === === ===


# 3. 