#Tanya jumlah

jumlahApel = int(input("Masukkan jumlah Apel : "))
jumlahJeruk = int(input("Masukkan jumlah Jeruk : "))
jumlahAnggur = int(input("Masukkan jumlah Anggur : "))

#Harga buah dengan jumlahnya

totalHargaApel = jumlahApel * 10000
totalHargaJeruk = jumlahJeruk * 15000
totalHargaAnggur = jumlahAnggur * 20000

#Total harga semua buah

hargaTotal = totalHargaApel + totalHargaJeruk + totalHargaAnggur

#Printout

print(
    f"""
Detail Belanja

Apel   : {jumlahApel} x 10000 = {totalHargaApel}
Jeruk  : {jumlahJeruk} x 15000 = {totalHargaJeruk}
Anggur : {jumlahAnggur} x 20000 = {totalHargaAnggur}

Total : {hargaTotal}
      
"""
)