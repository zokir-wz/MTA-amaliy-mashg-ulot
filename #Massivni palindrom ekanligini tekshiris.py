#Massivni palindrom ekanligini tekshirish
def massivni_palindrom_tekshirish(massiv):
    n = len(massiv)
    for i in range(n // 2):
        if massiv[i] != massiv[n - i - 1]:
            return False   
    return True

A = [1, 2, 3, 2, 1]
elementsoni=int(input("Massiv elementlar sonini kiriting: "))
for i in range(elementsoni):
    A.append(int(input(f"{i+1}-elementni kiriting: ")))
print("Massiv:", A)
print("Palindrom:", massivni_palindrom_tekshirish(A))