import BangunDatar

print("MENGHITUNG LUAS PERSEGI")
s =  int(input("Masukkan sisi = "))

print("Luas Persegi = ", BangunDatar.luaspersegi(s))
print("--------------------------------------------")

print("MENGHITUNG LUAS PERSEGI PANJANG")
p =  int(input("Masukkan panjang = "))
l =  int(input("Masukkan lebar = "))

print("Luas Persegi Panjang = ", BangunDatar.luaspersegipanjang(p,l))
print("--------------------------------------------")

print("MENGHITUNG LUAS SEGI TIGA")
a =  int(input("Masukkan alas = "))
t =  int(input("Masukkan tinggi = "))

print("Luas Segitiga = ", BangunDatar.luassegitiga(a,t))
print("--------------------------------------------")

print("MENGHITUNG LUAS JAJARGENJANG")
a =  int(input("Masukkan alas = "))
t =  int(input("Masukkan tinggi = "))

print("Luas Jajargenjang = ", BangunDatar.luasjajargenjang(a,t))
print("--------------------------------------------")

print("MENGHITUNG LUAS LAYANG-LAYANG0")
d1 =  int(input("Masukkan diangonal1 = "))
d2 =  int(input("Masukkan diagonal2 = "))

print("Luas Layang-layang = ", BangunDatar.luaslayanglayang60
(d1, d2))