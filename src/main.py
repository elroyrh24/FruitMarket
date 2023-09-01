#global vars
totalHargaApel = 0
totalHargaJeruk = 0
totalHargaAnggur = 0
hargaTotal = 0
jumlahApel = 0
jumlahJeruk = 0
jumlahAnggur = 0
hargaApel = 10000
hargaJeruk = 15000
hargaAnggur = 20000
# Stock
stockApel = 8
stockJeruk = 7
stockAnggur = 6

#  Text jika lebih dari Stock yg beli
rejectionText = "Jumlah yang dimasukkan terlalu banyak "

### F   U   N   C   T   I   O   N   S ###

# Tanya jumlah per buah
def input_fruit(name, stock, price):
    while True:
        n = int(input(f"Input jumlah {name.capitalize()}: "))
        if n <= stock:
            price = n * price
            break
        else:
            print(f"Jumlah terlalu banyak. {name.capitalize()} sisa {stock}")
    return price

# Harga buah dikali dengan jumlahnya + harga total semua

totalHargaApel = input_fruit('apel', stockApel, hargaApel)
totalHargaJeruk = input_fruit("jeruk", stockJeruk, hargaJeruk)
totalHargaAnggur = input_fruit("anggur", stockAnggur, hargaAnggur)

hargaTotal = totalHargaApel + totalHargaAnggur + totalHargaJeruk
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
duitDikasih = int(input("Masukkan jumlah uang : "))
while duitDikasih < hargaTotal:
    print(f"Uang anda kurang sebesar {hargaTotal-duitDikasih}")
    duitDikasih = int(input("Masukkan jumlah uang : "))
print("Terima kasih")
if duitDikasih > hargaTotal:
    print(f"Uang kembali anda {duitDikasih - hargaTotal}")

# Kurangi yg beli dari stock

stockApel -= jumlahApel
stockJeruk -= jumlahJeruk
stockAnggur -= jumlahAnggur
