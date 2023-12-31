import fruitmarket
import os

def clear_screen():
    """Fungsi membersihkan layar prompt
    """    
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')


# daftarBuah = [['Index','Nama','Stock','Harga'],
#               [0, 'Apel', 20, 10000],
#               [1, 'Jeruk', 15, 15000],
#               [2, 'Anggur', 25, 20000]
#               ]

daftarBuah = {'header':['Index','Nama','Stock','Harga'],
               'apel':[0,'Apel',20,10000],
               'jeruk':[1,'Jeruk',15,15000],
               'anggur':[2,'Anggur',25,20000]
               }

#  Text jika lebih dari Stock yg beli
rejectionText = "Jumlah yang dimasukkan terlalu banyak "

PROMPTMENU = '''
    Selamat Datang di Pasar Buah

    List Menu :
    1. Menampilkan Daftar Buah
    2. Menambah Buah
    3. Menghapus Buah
    4. Membeli Buah
    5. Exit Program
'''
def main():
    while True:
        print(PROMPTMENU)
        menu = int(input("Silahkan pilih menu : "))
        if menu == 1:
            fruitmarket.show(daftarBuah)
        elif menu == 2:
            fruitmarket.add(daftarBuah)
        elif menu == 3:
            fruitmarket.delete(daftarBuah)
        elif menu == 4:
            fruitmarket.buy(daftarBuah)
        elif menu == 5:
            break
        else:
            print("Menu tidak ada")

if __name__ == '__main__':
    main()

# #global vars
# totalHargaApel = 0
# totalHargaJeruk = 0
# totalHargaAnggur = 0
# hargaTotal = 0
# jumlahApel = 0
# jumlahJeruk = 0
# jumlahAnggur = 0
# hargaApel = 10000
# hargaJeruk = 15000
# hargaAnggur = 20000
# # Stock
# stockApel = 8
# stockJeruk = 7
# stockAnggur = 6

# #  Text jika lebih dari Stock yg beli
# rejectionText = "Jumlah yang dimasukkan terlalu banyak "

# ### F   U   N   C   T   I   O   N   S ###

# def input_fruit(name, stock, price):
#     while True:
#         n = int(input(f"Input jumlah {name.capitalize()}: "))
#         if n <= stock:
#             price = n * price
#             break
#         else:
#             print(f"Jumlah terlalu banyak. {name.capitalize()} sisa {stock}")
#     return price

#     """

#     Fungsi membeli buah

#     Args:
#         name(string): nama buah
#         stock(integer): stock buah terkini
#         price(integer): harga buah terkini
    
#     Returns:
#         n : jumlah buah
#         price : total harga buah
    
#     """

# # Harga buah dikali dengan jumlahnya + harga total semua

# totalHargaApel = input_fruit('apel', stockApel, hargaApel)
# totalHargaJeruk = input_fruit("jeruk", stockJeruk, hargaJeruk)
# totalHargaAnggur = input_fruit("anggur", stockAnggur, hargaAnggur)

# hargaTotal = totalHargaApel + totalHargaAnggur + totalHargaJeruk
# # Printout / Receipt
# print(
#     f"""
#     Detail Belanja

#     Apel   : {jumlahApel} x 10000 = {totalHargaApel}
#     Jeruk  : {jumlahJeruk} x 15000 = {totalHargaJeruk}
#     Anggur : {jumlahAnggur} x 20000 = {totalHargaAnggur}

#     Total : {hargaTotal}
#     """
# )



# # Minta duit
# duitDikasih = int(input("Masukkan jumlah uang : "))
# while duitDikasih < hargaTotal:
#     print(f"Uang anda kurang sebesar {hargaTotal-duitDikasih}")
#     duitDikasih = int(input("Masukkan jumlah uang : "))
# print("Terima kasih")
# if duitDikasih > hargaTotal:
#     print(f"Uang kembali anda {duitDikasih - hargaTotal}")
