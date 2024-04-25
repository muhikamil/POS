from barang import Barang
from prettytable import PrettyTable as pt

#Data barang menggunakan list
list=[["Pocari",5000,23],["cheetos",3000,37],["pocky",7000,53],["catburry",21000,43],["mizone",4000,69]]
insert={}

#instansiasi data Barang
for data in range(len(list)):
    insert[data]=Barang(list[data][0],list[data][1],list[data][2])

#fungsi untuk menampilkan seluruh data
def tampilData():
    dt=pt()
    dt.field_names=["No","Nama Barang","Harga Barang","Stock Barang"]
    nomor=1
    for data in range(len(list)):
        dt.add_row([nomor, insert[data].tampil[0], insert[data].tampil[1], insert[data].tampil[2]])
        nomor+=1
    print(dt)

#Fungsi untuk memilih data
def pilihData():
    global i
    dt=pt()
    dt.field_names=["No","Nama Barang","Harga Barang","Stock Barang"]
    nomor=1
    for data in range(len(list)):
        dt.add_row([nomor, insert[data].tampil[0], insert[data].tampil[1], insert[data].tampil[2]])
        nomor+=1
    print(dt)

    i=int(input("Pilih Data Nomor: "))
    if i >5:
        print('Data Tidak ada')
        i = None
    else:
        print(f'Nomor Data yang dipilih {i}')
        i -=1

#Fungsi untuk menampilkan data terpilih
def dataTerpilih():
    print(f'Nama Barang : {insert[i].tampil[0]}')
    print(f'Harga Barang : {insert[i].tampil[1]}')
    print(f'Stock Barang : {insert[i].tampil[2]}')

#Fungsi Untuk Mengubah Nama Barang
def ubahnBarang():
    ver= input('Ubah Nama [Y/N]? ').upper()
    if ver == 'Y': 

        print(f'Nama data barang yang mau diubah : {list[i][0]} ')
        uNama = input("Nama Barang baru: ")
        print('')
        insert[i].tampil=[uNama,insert[i].tampil[1],insert[i].tampil[2]]
        print(f'Nama Barang : {insert[i].tampil[0]}')
        print(f'Harga Barang : {insert[i].tampil[1]}')
        print(f'Stock Barang : {insert[i].tampil[2]}')
    else:
        print(f'Nama Barang : {list[i][0]}')
        print(f'Harga Barang : {list[i][1]}')
        print(f'Stock Barang : {list[i][2]}')

#Fungsi untuk mengubah Harga Barang
def ubahHBarang():
    ver= input('Ubah Harga [Y/N]? ').upper()
    if ver == 'Y': 

        print(f'Nama barang : {insert[i].tampil[0]}')
        print(f'Harga barang yang mau diubah : {list[i][1]}')
        uHarga = input("Harga baru: ")
        print('')
        insert[i].tampil=[insert[i].tampil[0],uHarga,insert[i].tampil[2]]
        print(f'Nama Barang : {insert[i].tampil[0]}')
        print(f'Harga Barang : {insert[i].tampil[1]}')
        print(f'Stock Barang : {insert[i].tampil[2]}')
    else:
        print(f'Nama Barang : {list[i][0]}')
        print(f'Harga Barang : {list[i][1]}')
        print(f'Stock Barang : {list[i][2]}')

#Fungsi untuk merubah stock barang
def ubahsBarang():
    ver= input('Ubah Jumlah Stock [Y/N]? ').upper()
    if ver == 'Y': 

        print(f'Nama barang : {insert[i].tampil[0]}')
        print(f'Jumlah Stock barang : {list[i][2]}')
        uStock = input("Update Stock Barang: ")
        print('')
        insert[i].tampil=[insert[i].tampil[0],insert[i].tampil[1],uStock]
        print(f'Nama Barang : {insert[i].tampil[0]}')
        print(f'Harga Barang : {insert[i].tampil[1]}')
        print(f'Stock Barang : {insert[i].tampil[2]}')
    else:
        print(f'Nama Barang : {list[i][0]}')
        print(f'Harga Barang : {list[i][1]}')
        print(f'Stock Barang : {list[i][2]}')

#Fungsi untuk menampilkan menu yang tersedia didalam program
def menu():
    while True:
        print('''
========================
        MENU
1. Tampil Semua Data
2. Pilih Data
3. Tampil Data Dipilih
4. Ubah Nama Barang
5. Ubah Harga Barang
6. Ubah Stock Barang
7. Keluar Program
========================
''')
        m = int(input("Pilih Menu: "))
        if m == 1:
            tampilData()
        elif m == 2:
            pilihData()
        elif m == 3:
            dataTerpilih()
        elif m == 4:
            if i == None:
                print('Tidak ada Data Terpilih')
                continue
            else:
                ubahnBarang()
        elif m == 5:
            if i == None:
                print('Tidak ada Data Terpilih')
                continue
            else:
                ubahHBarang()
        elif m == 6:
            if i == None:
                print('Tidak ada Data Terpilih')
                continue
            else:
                ubahsBarang()
        elif m == 7:
            exit()
        else:
            break

menu()