#Eng katta elementni topish 
def eng_katta_element(A):
    if not A:
        return None
    max_element = A[0]
    for element in A :
        if element > max_element:
         max_element : element
        return max_element 

    #Foydalanish
    massiv = [3,17,78,60,2,9,1]
    print(eng_katta_element(massiv))