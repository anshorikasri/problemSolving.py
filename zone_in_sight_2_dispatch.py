#lesson:control flow\dispatch
#start: 06.01.2026
# =========

# ide: menjalankan dalam 1 kali mencari sehingga O(1)
# untuk saat ini, yang kupahami:
# kita tetap perlu menyediakan bermacam fungsi,
# untuk diletak pada dictionary (sebut saja dispatch/tugas)

# Libataku: kaLi, Bagi, Tambah, Kurang
class Libataku:
    def kali3(self,k):
        return k*3
    
    bagi2 = lambda self, b: b/2

    add5 = lambda self, a: a+5

    subtract4 = lambda self, s: s-4

# =========


jawab= Libataku()

jwb1 = jawab.kali3(12)
jwb2 = jawab.bagi2(12)
jwb3 = jawab.add5(12)
jwb4 = jawab.subtract4(12)

print(jwb1)
print(jwb2)
print(jwb3)
print(jwb4)

# =========


