# Fungsi2

def pilihan(i):
    switcher = {
        1:'Cuaca Hujan',
        2:'Cuaca Adem'
    }
    return switcher.get(i, "Masukan Pilihan Yang Benar")

print("1. Hujan")
print("2. Adem")
nomor = int(input("Masukan Pilihan: "))
cuaca = pilihan(nomor)
print(cuaca)

if nomor==1:
    print("Karena Cuaca Hujan maka, kuliah naik gocar")
if nomor==2:
    print("Karena Cuaca Adem maka, kuliah naik motor")