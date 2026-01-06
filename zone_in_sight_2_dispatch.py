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


# menggunakan dispatch (translate: 'tugas')
tugas = {
    "kali3" : kali3,
    "bagi2" : bagi2,
    "add5"  : add5,
    "sub4"  : subtract4
}

# =========
ans1 = tugas["kali3"](18)
ans2 = tugas["bagi2"](18)
ans3 = tugas["add5"](18)
ans4 = tugas["sub4"](18)


print(ans1)
print(ans2)
print(ans3)
print(ans4)