day = input ("Masukkan nama hari: ")

match day:
    case "Senin":
        print("Bekerja")
    case "Selasa":
        print("Turu")
    case "Rabu":
        print("Liburan")
    case _: #File Salah
        print("Inputan anda salah")