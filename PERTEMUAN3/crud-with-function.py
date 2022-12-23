'''
    * CRUD 
        - Create : Buat entri / nilai baru 
        - Read   : Membaca entri / nilai  
        - Update : Memperbaharui entri / nilai  
        - Delete : Menghapus entri / nilai  
'''

# Variabel fruits / buah - buahan
fruits = ["Mangga", "Apel"]


'''
    * CREATE
'''

def store(fruitName):
    fruits.append(fruitName)




'''
    * UPDATE
'''

def update (position, fruitName):
    fruits[position] = fruitName

fruits[0] = "Pisang"


'''
    * DELETE
'''
def destory (position):
    del fruits[1]
    # fruits.remove(position)


'''
    * READ
'''
def index():
    for fruit in fruits:
        print (fruit)

# menampilkan semua data
print("Menampilkan Semua Data dalam Variabel List Furits")
index()

# Menampilkan data baru
print("Menambahkan data baru")
store("Anggur")
index()

# Challange

# Pangil fungsi update, delete
print("Data Update")
update(1, "Melon")
index()
print()

#Delete
print("Delete Data")
destory (0)
index()
print()


