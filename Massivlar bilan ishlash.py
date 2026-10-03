# # arr=[10,20,30,40] 
# # x=arr[2]      # 0(1)
# # arr(2)=99      #0(1)
# #print(arr)
#  #skill ichida remove()-yashirin 0 (n^2)
# # for x in olib_tashlanadigan:
# #     arr.remove (x)

# #     #Tartib muhim bolmasa - 0(1)
# #     arr[i]=arr[-1]
# #     arr.pop()
# massiv=[3,17,2,8,12,9,1]
# olib_lashlanadigan=[2,8,9,]
# for x in olib_tashlanadigan:
#     massiv.remove (x)
# print(massiv)

# arr=[10,20,30,40,50]
# arr.append(60)    #O(1)
# print(arr)  
class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

head=Node (10)
head.next=Node (20)
print(head)