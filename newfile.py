print ("POGRAM MENGHITUNG BERAT BADAN IDEAL")

#input
berat_badan = int (input ("Masukkan berat badan anda (kg) = "))
tinggi_badan = int (input ("Masukkan tinggi badan anda (cm) = "))

#konversi tinggi badan ke meter
tinggi_badan = tinggi_badan/100

#rumus
nilai_berat_ideal = berat_badan / (tinggi_badan**2)

#output
print ("Nilai Berat Badan Ideal anda adalah : " , nilai_berat_ideal)

# Sistem logika dengan if else
if nilai_berat_ideal < 18.5:
	print("Berat badan anda kurang")
elif nilai_berat_ideal > 18.5 and nilai_bmi < 24.9:
	print("Berat badan anda normal")
elif nilai_berat_ideal > 25 and nilai_bmi < 29.9:
	print("Anda kelebihan berat badan")
elif nilai_berat_ideal > 30:
	print("Anda obesitas")
