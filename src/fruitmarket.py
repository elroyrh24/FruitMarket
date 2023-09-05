from tabulate import tabulate


def show(database, title='Daftar Buah Tersedia'):

    """
    fungsi menampilkan daftar buah
    
    Args:
        database (dict): database buah
        title (str, optional): judul tabel data buah. Default 'Daftar Buah Tersedia'
    """    
    # 
    header = database['header']
    data = list(database.values())[1:]

    # print tabel
    print(tabulate(data, header, tablefmt="outline"))

def add(database):

    """_summary_
    
    Args:
        database(dict) : database buah
    Returns:
        dict: database buah terbaru
    """   
    #input buah baru
    name = input("Input nama buah: ").capitalize()
    stock = int(input('Input stock buah: '))
    price = int(input('Ínput harga buah: '))
    index = len(database) - 1

    #update database 
    database.update({
        f'{name}': [index, name.capitalize(), stock, price]
    })
    return database

def delete(database):

    """
    Fungsi menghapus buah dari database

    Args:
        database(dict): database buah

    Returns:
        dict : database buah terbaru
    """    
    #show data before

    show(database,'Daftar Buah Tersedia')

    # input index
    index = int(input('Input indeks buah yang akan dihapus: '))

    # hapus buah berdasarkan index
    for key, val in database.items():
        if 'header' in val:
            continue
        elif index == val[0]:
            del database[key]
            break
        elif index > len(database) - 1:
            print('Buah yang dicari tidak ada')
            break

    # update indeks buah
    for i, val in enumerate(list(database.values())):
        if 'Index' in val:
            continue
        elif val[0] > i-1:
            val[0] -= 1
            database.update(
                {
                    val[1].lower(): val
                }
            )
            
    # show data after
    show(database,'Daftar Buah Tersedia')

    return database

def buy(database):
    """Fungsi membeli buah

    Args:
        database (List): Database buah

    Returns:
        List: Database terbaru
    """    
    chart = {
        'header': ['Nama', 'Qty', 'Harga'],
    }

    # show data
    show(database)

    # buying process
    rebuy = 'YES'
    while rebuy == 'YES':
        index = int(input('Input indeks buah: '))
        count = int(input('Input jumlah buah: '))

        for item in database.values():
            if index in item:
                id, name, stock, price = item
                if count <= stock:
                    chart.update(
                        {
                            f'{name.lower()}': [name, count, price]
                        }
                    )
                    database.update(
                        {
                            f'{name.lower()}' : [id, name, stock-count, price]
                        }
                    ) 
                else:
                    print(f'Stock {name} sisa {stock}')
                break
        
        show(chart)
        rebuy = input('Beli yang lain? (yes/no): ').upper()
    
    # calculate total price
    sumPrice = 0
    for item in chart.values():
        if 'nama' in item:
            item.append('total')
            chart.update(
                {
                    'header': item
                }
            )
        else:
            totalPrice = int(item[1])*int(item[2])
            item.append(totalPrice)
            chart.update(
                {
                    f'{item[0].lower()}': item
                }
            )
            sumPrice += totalPrice

    show(chart)
    print(f'Total belanja Anda: {sumPrice}')

    # payment process
    while True:
        pay = int(input('Masukkan jumlah uang: '))
        delta = pay - sumPrice
        if delta >= 0:
            print(f'Terima kasih. Uang kembalian {delta}')
            break
        else:
            print(f'Uang anda kurang sebesar {abs(delta)}')

    return database