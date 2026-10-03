# Tartiblanmagan ro'yxatni saralash uchun Pufakchali Saralash algoritmi
def pufakchali_saralash(royxat):
    n = len(royxat)
    for i in range(n):
        for j in range(0, n-i-1):
            if royxat[j] > royxat[j+1]:
                royxat[j], royxat[j+1] = royxat[j+1], royxat[j]
    return royxat
royxat = []
elementlar_soni = int(input("Ro'yxatdagi elementlar sonini kiriting: "))
for i in range(elementlar_soni):
    element = int(input(f"Element {i+1}: "))
    royxat.append(element)
print("Tartiblanmagan ro'yxat:", royxat)
print("Tartiblangan ro'yxat:", pufakchali_saralash(royxat))
