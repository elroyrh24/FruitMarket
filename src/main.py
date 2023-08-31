
# Stock
stockApel = 8
stockJeruk = 7
stockAnggur = 6

#  =Text jika lebih dari Stock yg beli
rejectionText = "Jumlah yang dimasukkan terlalu banyak "

# Tanya jumlah per buah
jumlahApel = int(input("Masukkan jumlah Apel : "))
while jumlahApel > stockApel:
    print(rejectionText)
    print(f"Stock Apel tinggal: {stockApel}")
    jumlahApel = int(input("Masukkan jumlah Apel : "))
jumlahJeruk = int(input("Masukkan jumlah Jeruk : "))
while jumlahJeruk > stockJeruk:
    print(rejectionText)
    print(f"Stock Jeruk tinggal: {stockJeruk}")
    jumlahJeruk = int(input("Masukkan jumlah Jeruk : "))
jumlahAnggur = int(input("Masukkan jumlah Anggur : "))
while jumlahAnggur > stockAnggur:
    print(rejectionText)
    print(f"Stock Anggur tinggal: {stockAnggur}")
    jumlahAnggur = int(input("Masukkan jumlah Anggur : "))

# Kurangi yg beli dari stock
stockApel -= jumlahApel
stockJeruk -= jumlahJeruk
stockAnggur -=jumlahAnggur

# Harga buah dikali dengan jumlahnya
totalHargaApel = jumlahApel * 10000
totalHargaJeruk = jumlahJeruk * 15000
totalHargaAnggur = jumlahAnggur * 20000

# Total harga semua buah dibeli tergabung
hargaTotal = totalHargaApel + totalHargaJeruk + totalHargaAnggur

# Printout / Receipt
print(
    f"""
Detail Belanja

Apel   : {jumlahApel} x 10000 = {totalHargaApel}
Jeruk  : {jumlahJeruk} x 15000 = {totalHargaJeruk}
Anggur : {jumlahAnggur} x 20000 = {totalHargaAnggur}

Total : {hargaTotal}
"""
)

# Minta duit
if hargaTotal > 0:
    uangDiberikan = int(input("Masukkan jumlah uang : "))
    while uangDiberikan < hargaTotal:
        print(f"Uang anda kurang sebesar {hargaTotal - uangDiberikan}")
        uangDiberikan = int(input("Masukkan jumlah uang : "))
    print("Terima kasih")
    if uangDiberikan > hargaTotal :
        print(f"Uang kembali anda {uangDiberikan - hargaTotal}")