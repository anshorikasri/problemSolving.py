#lesson:lambda
#start: 06.01.2026
# =========

# IT CAN WORK, BECAUSE WITH 'self'

class Variatif:
    # traditional
    def addFive(self,n):
        return n+5

    #lambda
    addSix= lambda self,x: x+6

# instance
coba1 = Variatif()

ans5 = coba1.addFive(2)
ans6 = coba1.addSix(2)

print(ans5)
print(ans6)

