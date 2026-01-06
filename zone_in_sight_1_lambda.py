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

coba1 = Variatif()

coba1.addFive(2)
coba1.addSix(2)


