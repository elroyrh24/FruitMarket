from tabulate import tabulate

def show(database, title='Daftar Buah Tersedia'):
    header = database[0]
    data = database[1:]
    print(tabulate(data, header, tablefmt="outline"))

def add(database):
    name = input("Input nama buah: ").capitalize()
    stock = int(input('Input stock buah: '))
    price = int(input('Ínput harga buah: '))
    index = len(database) - 1

    database = database.append([
        index, name, stock, price]
    )
    return database

def delete(database):
    index = int(input('Input indeks buah yang akan dihapus: '))
    for idx, val in enumerate(database[1:]):
        if index == val[0]:
            print(database[idx+1])
            del database[idx+1]
            break
        elif index > len(database) - 1:
            print('Buah yang dicari tidak ada')
            break
    return database

def buy(database):
    tabley = [['Index','Qty','Harga']]
    header = tabley[0]
    hargaTotal = 0
    while True:
        index = int(input("Masukkan indeks buah yang ingin dibeli: "))
        stock = int(input("Masukkan jumlah yang ingin dibeli: "))
        for idx, val in enumerate(database):
            if index == val[0]:
                if stock > val[2]:
                    print(f"Stock tidak cukup, stock {val[1]} tinggal {val[2]}")
                else:
                    tabley.append([val[0], val[2], val[3]])
                    print(tabley)
        restoftable = tabley[1:]
        print("Isi Cart:")
        print(tabulate(restoftable,header,tablefmt="outline"))
        check = input("Mau beli yang lain? (ya/tidak)").capitalize()
        if check == "Tidak":
            break
    tabley[0].append('Total Harga')
    for ind, value in enumerate(tabley[1:]):
        value.append(value[2]*value[1])
        hargaTotal += (value[2]*value[1])
    restoftable = tabley[1:]
    print("Daftar Belanja : ")
    print(tabulate(restoftable,header,tablefmt="outline"))
    print(f"Total Yang Harus Dibayar : {hargaTotal}")
    duitDikasih = int(input("Masukkan jumlah uang : "))
    while duitDikasih < hargaTotal:
        print(f"Uang anda kurang sebesar {hargaTotal-duitDikasih}")
        duitDikasih = int(input("Masukkan jumlah uang : "))
    print("Terima kasih")
    if duitDikasih > hargaTotal:
        print(f"\nUang kembali anda {duitDikasih - hargaTotal}")
