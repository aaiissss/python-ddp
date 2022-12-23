'''
   *list
   *index / Urutannya dimulai dari 0
   *nilai di pisah pakai tanda
'''

manchesterUnited = ["Ronaldo" , "Rooney" , "Rafael" , "Nani" , "Anderson"]

#Menampilkan semua data
print (manchesterUnited)
print (manchesterUnited[0:3])

# Aray / List Slicing
# print (manchesterUnited[0:2:3])

for i in range (1, 101):
   if i == 13:
      continue
   else:
      print(i)

newList = []
for i in range (1, 101):
   newList.append(i)

for j in newList:
   print(j)

i = 0
for index in range (1, 101):
   print(f"{i} : Ngoding yukkkk")
   i+=1 