'''
    * If
    * If <kondisi>: dimana kondisi adalah sebuah ekspresi boolean yang menghasilkan nilai True atau False
    * Jika kondisi bernilai True, maka blok kode di dalam if akan dijalankan
    * Jika kondisi bernilai False, maka blok kode di dalam if tidak akan dijalankan
'''
nama = input ("Masukkan nama anda : ")
umur= int(input("Masukkan umur anda : ")) # Passing dari String ke Int

if umur > 20: # Benar 
    print("Boleh Masuk Bioskop")
else:
    print ("Tidak Boleh Masuk Bioskop")