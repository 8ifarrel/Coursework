# CATATAN format varibael
# xxx_yyy_zzz
#
# xxx = variblenya digunakan buat apa
#   def_yyy_zzz = def
#   input_yyy_zzz = input
#   tb_yyy_zzz = tabulate
#   dict_yyy_zzz = dictionary
#   key_yyy_zzz = key dalam dictionary
#   tuple_yyy_zzz = tuple
#
# yyy = nama variable
#   yyy_menuUtama_zzz
#   yyy_register_zzz
#   
# zzz = variable untuk siapa
#   xxx_yyy_USER = user
#   xxx_yyy_ADMIN = admin
#   xxx_yyy = semua

# Import OS
import os

# Import random
import random

# Install and import Tabulate
os.system("pip install tabulate")
from tabulate import tabulate as tb

# Install dan import PWInput
os.system('pip install pwinput')    
import pwinput

# Import sleep (from Time module)
from time import sleep

# Tuple akun admin
tuple_loginUsername_ADMIN = ("huda")
tuple_loginPassword_ADMIN = ("ganteng12")

# dictionary akun user
dict_akun_USER = {
    "35383": {
        "Username": "farrel",
        "Password": "sirah123"
    },
    "24372": {
        "Username": "bebek",
        "Password": "sapi1234"
        }
}

# list barang
list_barang = [
    ["Pensil",3000,16],
    ["Pulpen",3000,21],
    ["Penghapus",2500,13],
    ["Tip-x",4000,19],
    ["Penggaris",2500,10]
]

# list isi keranjang user
list_namaBarang_USER = [] # Nama
list_jumlahBarang_USER = [] # Jumlah
list_hargaBarang_USER = [] # Harga

# list berapa banyak barang yang sudah dibeli
list_namaPendataanBarang = [] # Nama
list_jumlahPendataanBarang = [] # Jumlah

# def clear screen
def def_clearScreen():
    os.system("cls" if os.name == "nt" else "clear")

# def header
def def_header():
    def_clearScreen()
    tb_header = [["\033[1m      TOKO ALAT TULIS KANTOR      \033[0;0m"]]
    print(tb(tb_header, tablefmt="double_outline"))
    print()

# def register (USER)
def def_registerAkun_USER():
    def_header()
    tb_register_USER = [["\033[1mREGISTER AKUN USER\033[0;0m"]]
    print(tb(tb_register_USER, tablefmt="rounded_outline"))
    print("\033[93mKosongkan isi lalu tekan ENTER untuk kembali\033[0m")    

    input_registerUsername_USER = input("Username: ")

    # Kembali
    if len(input_registerUsername_USER) == 0:
        def_menuAkun_USER()

    # Menghindari penggunaan username yang sama
    for i, j in dict_akun_USER.items():
        if input_registerUsername_USER == dict_akun_USER[i]["Username"]:
            input("\033[2;31mUsername sudah digunakan\033[0;0m\nTekan ENTER untuk melanjutkan")
            def_registerAkun_USER()

    # Lanjut register
    else:
        while True:
            input_registerPassword_USER = pwinput.pwinput(prompt="Password: ", mask="\u2022")

            # Kembali
            if len(input_registerPassword_USER) == 0:
                def_registerAkun_USER()

            # Password tidak boleh kurang dari 8 karakter
            elif len(input_registerPassword_USER) < 8:
                input("\033[2;31mPassword tidak boleh kurang dari 8 karakter\033[0;0m\nTekan ENTER untuk melanjutkan")

                def_header()
                print(tb(tb_register_USER, tablefmt="rounded_outline"))
                print("\033[93mKosongkan isi lalu tekan ENTER untuk kembali\033[0m")   
                print(f"Username: {input_registerUsername_USER}")
                
            # Konfirmasi password
            else:
                input_registerPasswordKonfirmasi_USER = pwinput.pwinput(prompt="Konfirmasi password: ", mask="\u2022")

                # Password tidak sesuai
                if input_registerPassword_USER != input_registerPasswordKonfirmasi_USER:
                    input("\033[2;31mPassword tidak sesuai\033[0;0m\nTekan ENTER untuk melanjutkan")
                    
                    def_header()
                    print(tb(tb_register_USER, tablefmt="rounded_outline"))
                    print("\033[93mKosongkan isi lalu tekan ENTER untuk kembali\033[0m")   
                    print(f"Username: {input_registerUsername_USER}")

                # Register berhasil
                else:    
                    keys_ID_USER = str(random.randint(0, 99999))
                    dict_akun_USER[keys_ID_USER] = {"Username":input_registerUsername_USER, "Password":input_registerPassword_USER}

                    def_header()
                    print(tb(tb_register_USER, tablefmt="rounded_outline"))
                    print("Tunggu sebentar...")
                    sleep(3) 

                    def_header()
                    print(tb(tb_register_USER, tablefmt="rounded_outline")) 
                    input("\033[32mAkun berhasil dibuat\033[0;0m\nTekan ENTER untuk melanjutkan")
                    def_menuAkun_USER()

# def lihat barang (USER)
def def_lihatBarang_USER():
    def_header()
    tb_lihatBarang = [["\033[1mBARANG\033[0;0m"]]
    print(tb(tb_lihatBarang, tablefmt="rounded_outline"))

    header_barang = ["Barang","Harga (Rp)","Stok"]
    print(tb(list_barang, intfmt=",", headers=header_barang, tablefmt="grid"))

    input("Tekan ENTER untuk kembali")     
    def_menuToko_USER()     

# def pesan barang (USER)
def def_pesanBarang_USER():
    global input_idBarang_USER
    global input_jumlahBarang_USER

    try:
        def_header()
        tb_pesanBarang_USER = [["\033[1mPESAN BARANG\033[0;0m"]]
        print(tb(tb_pesanBarang_USER, tablefmt="rounded_outline"))  
        print("\033[93mKetik 12345 untuk kembali\033[0m")    

        header_pesanBarang_USER = ["ID", "Barang","Harga (Rp)","Stok"]
        print(tb(list_barang, intfmt=",", headers=header_pesanBarang_USER, tablefmt="grid", showindex=True))
        
        # Input ID barang
        input_idBarang_USER = int(input("Masukkan ID: "))

        # Kembali
        if input_idBarang_USER == 12345:
            def_beliBarang_USER()
        
        # Input jumlah barang
        else:
            input_jumlahBarang_USER = int(input("Masukkan jumlah: "))

            # Kembali
            if input_jumlahBarang_USER == 12345:
                def_pesanBarang_USER()
            
            # Jumlah barang tidak boleh kurang dari atau sama dengan 0
            elif input_jumlahBarang_USER <= 0:
                input("\033[2;31mMasukkan angka dengan benar!\033[0;0m\ntekan ENTER untuk melanjutkan") 
                def_pesanBarang_USER()

            # Jumlah barang tidak boleh lebih dari stok yang ada
            if input_jumlahBarang_USER > list_barang[input_idBarang_USER][2]:
                input("\033[2;31mStok tidak cukup\033[0;0m\ntekan ENTER untuk melanjutkan")
                def_pesanBarang_USER()

            # Berhasil pesan barang
            else:
                a = list_barang[input_idBarang_USER][0] # Nama
                b = input_jumlahBarang_USER # Jumlah
                c = list_barang[input_idBarang_USER][1] * input_jumlahBarang_USER # Harga

                # Jika barang tersebut pertama kali dimasukkan
                if a not in list_namaBarang_USER:
                    list_namaBarang_USER.append(a)
                    list_jumlahBarang_USER.append(b)        
                    list_hargaBarang_USER.append(c)

                # Jika barang tersebut sudah pernah dimasukkan
                else:
                    list_jumlahBarang_USER[list_namaBarang_USER.index(a)] += b
                    list_hargaBarang_USER[list_namaBarang_USER.index(a)] += c

                # Pengurangan stok
                list_barang[input_idBarang_USER][2] -= b
                def_beliBarang_USER()

    except ValueError:
        input("\033[2;31mMasukkan angka dengan benar!\033[0;0m\ntekan ENTER untuk melanjutkan")
        def_pesanBarang_USER()            

    except IndexError:
        input("\033[2;31mMasukkan angka dengan benar!\033[0;0m\ntekan ENTER untuk melanjutkan") 
        def_pesanBarang_USER() 

# def lihat keranjang (USER)
def def_lihatKeranjang_USER():
    def_header()
    tb_lihatIsiKeranjang_USER = [["\033[1mISI KERANJANG\033[0;0m"]]
    print(tb(tb_lihatIsiKeranjang_USER, tablefmt="rounded_outline"))

    # Keranjang ada isinya
    if len(list_namaBarang_USER) > 0:
        print("==================================")
        for i in range(len(list_namaBarang_USER)):
            print(f"Nama barang\t: {list_namaBarang_USER[i]}")
            print(f"Jumlah barang\t: {list_jumlahBarang_USER[i]}")
            print("==================================")

    # Keranjang masih kosong
    else:
        print("Keranjang masih kosong")
    
    input("tekan ENTER untuk kembali")
    def_beliBarang_USER()

# def Kurangi isi keranjang (USER)
def def_kurangiIsiKeranjang_USER():
    try:
        # Keranjang ada isinya
        if len(list_namaBarang_USER) > 0:
            def_header()
            print(tb([["\033[1mKURANGI ISI KERANJANG\033[0;0m"]], tablefmt="rounded_outline"))
            print("\033[93mKetik 12345 untuk kembali\033[0m")  

            print("==================================")
            for i in range(len(list_namaBarang_USER)):
                print(f"ID\t\t: {i}")
                print(f"Nama barang\t: {list_namaBarang_USER[i]}")
                print(f"Jumlah barang\t: {list_jumlahBarang_USER[i]}")
                print("==================================")

            input_kurangiIsiKeranjang = int(input("Masukkan ID: "))

            # Kembali
            if input_kurangiIsiKeranjang == 12345:
                def_beliBarang_USER()
            
            # Berhasil kurangi isi keranjang
            else:
                for j in range(len(list_barang)):
                    try:
                        list_barang[j].index(list_namaBarang_USER[input_kurangiIsiKeranjang])
                        break
                    except ValueError:
                        None
                list_barang[j][2] += list_jumlahBarang_USER[input_kurangiIsiKeranjang]
                
                del list_namaBarang_USER[input_kurangiIsiKeranjang]
                del list_jumlahBarang_USER[input_kurangiIsiKeranjang]
                del list_hargaBarang_USER[input_kurangiIsiKeranjang]
                def_beliBarang_USER()

        # Keranjang masih kosong
        else:
            def_header()
            print(tb([["\033[1mKURANGI ISI KERANJANG\033[0;0m"]], tablefmt="rounded_outline"))
            input("Keranjang masih kosong\nTekan ENTER untuk kembali")
            def_beliBarang_USER()

    except ValueError:
        input("\033[2;31mMasukkan angka dengan benar!\033[0;0m\ntekan ENTER untuk melanjutkan")     
        def_kurangiIsiKeranjang_USER()

    except IndexError:
        input("\033[2;31mMasukkan angka dengan benar!\033[0;0m\ntekan ENTER untuk melanjutkan")     
        def_kurangiIsiKeranjang_USER()

# def belanja lagi (USER)
def def_belanjaLagi_USER():
    def_header()
    tb_terimaKasih_USER = [["\033[1mBAYAR\033[0;0m"]]   
    print(tb(tb_terimaKasih_USER, tablefmt="rounded_outline"))      

    input_belanjaLagi_USER = input("Ingin belanja lagi?\n[Y/N] ")

    if input_belanjaLagi_USER == "Y" or input_belanjaLagi_USER == "y":
        def_menuToko_USER()

    elif input_belanjaLagi_USER == "N" or input_belanjaLagi_USER == "n":
        def_header()
        print("Terima kasih telah berbelanja")
        sleep(3)
        def_menuUtama()

    else:
        input("\033[2;31mMasukkan pilihan dengan benar!\033[0;0m\nTekan ENTER untuk melanjutkan")
        def_belanjaLagi_USER() 

# def pendataan berapa banyak barang sudah dibeli
def def_pendataanBarang():
    for i in range(len(list_namaBarang_USER)):
        a = list_namaBarang_USER[i]
        b = list_jumlahBarang_USER[i]
    
        if a not in list_namaPendataanBarang:
            list_namaPendataanBarang.append(a)
            list_jumlahPendataanBarang.append(b)

        else:
            list_jumlahPendataanBarang[list_namaPendataanBarang.index(a)] += b
        
# def bayar (USER)
def def_bayar_USER():
    def_header()
    tb_setruk_USER = [["\033[1mSETRUK BELANJA\033[0;0m"]]
    print(tb(tb_setruk_USER, tablefmt="rounded_outline"))
    
    print("==================================")
    for i in range(len(list_namaBarang_USER)):
        print(f"Nama barang\t: {list_namaBarang_USER[i]}")
        print(f"Jumlah barang\t: {list_jumlahBarang_USER[i]}")
        print(f"Harga\t\t: {list_hargaBarang_USER[i]}")
        print("==================================")
    print(f"Metode bayar\t: {metodePembayaran_USER}")
    print(f"Jumlah harga\t: {round(jumlahHarga_USER)}")
    print("==================================")
    input("Tekan ENTER untuk melanjutkan")

    def_pendataanBarang()
    list_namaBarang_USER.clear()
    list_jumlahBarang_USER.clear()
    list_hargaBarang_USER.clear()
    def_belanjaLagi_USER()

# def metode pembayaran
def def_metodePembayar_USER():
    global metodePembayaran_USER
    global jumlahHarga_USER
    jumlahHarga_USER = sum(list_hargaBarang_USER)

    def_header()
    tb_bayar_USER = [["\033[1mBAYAR\033[0;0m"]]
    print(tb(tb_bayar_USER, tablefmt="rounded_outline"))

    tb_metodePembayaran_USER = [
    ["\033[1mMETODE PEMBAYARAN\033[0;0m"],
    ["[1] Tunai"],
    ["[2] Debit"],
    ["[3] Kembali"],
    ["\033[32mDapatkan potongan 5% jika menggunakan debit\033[0;0m"]
    ]
    print(tb(tb_metodePembayaran_USER, tablefmt="rounded_outline"))

    input_metodePembayaran_USER = input("Masukkan metode pembayaran: ")

    # Tunai
    if input_metodePembayaran_USER == "1":
        metodePembayaran_USER = "Tunai"
        def_bayar_USER()

    # Debit
    elif input_metodePembayaran_USER == "2":
        metodePembayaran_USER = "Debit"
        jumlahHarga_USER -= jumlahHarga_USER * 0.05
        def_bayar_USER()

    # Kembali
    elif input_metodePembayaran_USER == "3":
        def_konfirmasiBayar_USER()

    # Salah pilih
    else:
        def_metodePembayar_USER()

# def konfirmasi bayar (USER)
def def_konfirmasiBayar_USER():
    def_header()
    tb_bayar_USER = [["\033[1mBAYAR\033[0;0m"]]
    print(tb(tb_bayar_USER, tablefmt="rounded_outline"))

    # Keranjang ada isinya
    if len(list_namaBarang_USER) > 0:
        print("==================================")
        for i in range(len(list_namaBarang_USER)):
            print(f"Nama barang\t: {list_namaBarang_USER[i]}")
            print(f"Jumlah barang\t: {list_jumlahBarang_USER[i]}")
            print(f"Harga\t\t: {list_hargaBarang_USER[i]}")
            print("==================================")
        print(f"Jumlah harga\t: {sum(list_hargaBarang_USER)}")
        print("==================================")

        pilih_bayar_USER = input("Anda ingin bayar?\n[Y/N] ")

        # Bayar
        if pilih_bayar_USER == "Y" or pilih_bayar_USER == "y":
            def_metodePembayar_USER()

        # Kembali
        elif pilih_bayar_USER == "N" or pilih_bayar_USER == "n":
            def_beliBarang_USER()

        # Salah pilih
        else:
            input("\033[2;31mMasukkan pilihan dengan benar!\033[0;0m\nTekan ENTER untuk melanjutkan")
            def_konfirmasiBayar_USER()

    # Keranjang masih kosong
    else:
        def_header()
        print(tb(tb_bayar_USER, tablefmt="rounded_outline"))
        input("Keranjang masih kosong\nTekan ENTER untuk kembali")
        def_beliBarang_USER()


# def beli barang (USER)
def def_beliBarang_USER():
    def_header() 
    tb_beliBarang_USER = [
    ["\033[1mBeli Barang\033[0;0m"],
    ["[1] Pesan barang"],
    ["[2] Lihat keranjang"],
    ["[3] Kurangi isi keranjang"],
    ["[4] Bayar"],
    ["[5] Kembali"]
    ]
    print(tb(tb_beliBarang_USER, tablefmt="rounded_outline"))

    input_beliBarang_USER = input("Masukkan pilihan: ")

    # Pesan barang
    if input_beliBarang_USER == "1":
        def_pesanBarang_USER()

    # Lihat keranjang
    elif input_beliBarang_USER == "2":
        def_lihatKeranjang_USER()

    # Kurangi isi keranjang
    elif input_beliBarang_USER == "3":
        def_kurangiIsiKeranjang_USER()

    # Bayar
    elif input_beliBarang_USER == "4":
        def_konfirmasiBayar_USER()

    # Kembali
    elif input_beliBarang_USER == "5":
        def_menuToko_USER()

    # Salah pilih
    else:
        input("\033[2;31mMasukkan pilihan dengan benar\033[0;0m\ntekan ENTER untuk melanjutkan")
        def_beliBarang_USER()

# def menu toko (USER)
def def_menuToko_USER():
    while True:
        def_header() 
        tb_menuToko_USER = [
        ["\033[1mMENU\033[0;0m"],
        ["[1] Lihat barang"],
        ["[2] Beli barang"],
        ["[3] Log out"]
        ]
        print(tb(tb_menuToko_USER, tablefmt="rounded_outline"))

        input_menuToko_USER = input("Masukkan pilihan: ")

        # Lihat barang
        if input_menuToko_USER == "1":
            def_lihatBarang_USER()

        # Beli barang
        elif input_menuToko_USER == "2":
            def_beliBarang_USER()

        # Log out
        elif input_menuToko_USER == "3":
            def_konfirmasiLogout()

        # Salah pilih 
        else:
            input("\033[2;31mMasukkan pilihan dengan benar\033[0;0m\ntekan ENTER untuk melanjutkan")
            def_menuToko_USER()

# def login (USER)
def def_loginAkun_USER():
    def_header()
    tb_login_USER = [["\033[1mLOG IN AKUN USER\033[0;0m"]]
    print(tb(tb_login_USER, tablefmt="rounded_outline"))
    print("\033[93mKosongkan isi lalu tekan ENTER untuk kembali\033[0m")    

    input_loginUsername_USER = input("Username: ")

    # Kembali
    if len(input_loginUsername_USER) == 0:
        def_menuAkun_USER()

    # Lanjut login
    else:
        input_loginPassword_USER = pwinput.pwinput(prompt="Password: ", mask="\u2022")

        # Kembali
        if len(input_loginPassword_USER) == 0:
            def_loginAkun_USER()

        # Log in berhasil
        for i, j in dict_akun_USER.items():
            if input_loginUsername_USER == dict_akun_USER[i]["Username"] and input_loginPassword_USER == dict_akun_USER[i]["Password"]:
                def_menuToko_USER()

        # Log in salah
        else:
            input("\033[2;31mLog in salah\033[0;0m\nTekan ENTER untuk melanjutkan")
            def_loginAkun_USER()              
 
# def menu akun (USER)
def def_menuAkun_USER():
    def_header()
    tb_menuAkun_USER = [
    ["\033[1mAKUN USER\033[0;0m"],
    ["1. Register"],
    ["2. Log in"],
    ["3. Kembali"]
    ]
    print(tb(tb_menuAkun_USER, tablefmt="rounded_outline"))

    input_menuAkun_USER = input("Masukkan pilihan: ")

    # Register user
    if input_menuAkun_USER == "1":
        def_registerAkun_USER()

    # Log in user
    elif input_menuAkun_USER == "2":
        def_loginAkun_USER()

    # Kembali
    elif input_menuAkun_USER == "3":
        def_menuUtama()

    # Salah pilih
    else:
        input("\033[2;31mMasukkkan pilihan dengan benar\033[0;0m\nTekan ENTER untuk melanjutkan") 
        def_menuAkun_USER()          

# def tambah barang (ADMIN)
def def_tambahBarang_ADMIN():
    try:
        def_header()
        tb_tambahBarang_ADMIN = [["\033[1mTAMBAH BARANG\033[0;0m"]]
        print(tb(tb_tambahBarang_ADMIN, tablefmt="rounded_outline"))

        header_barang = ["ID","Barang","Harga (Rp)","Stok"]
        print(tb(list_barang, intfmt=",", headers=header_barang, tablefmt="grid",showindex=True))
        print("\033[93mKetik 12345 untuk kembali\033[0m")

        # Isi nama
        input_tambahNama_ADMIN = input("Masukkan nama: ").capitalize()

        # Kembali
        if input_tambahNama_ADMIN == "12345":
            def_kelolaBarang_ADMIN()

        # Tidak boleh menambahkan barang yang sama
        elif any(input_tambahNama_ADMIN in i for i in list_barang) == True:
            input("\033[2;31mBarang sudah ada\033[0;0m\ntekan ENTER untuk melanjutkan") 
            def_tambahBarang_ADMIN()

        # Isi harga
        else:
            input_tambahHarga_ADMIN = int(input("Masukkan harga: "))

            # Kembali
            if input_tambahHarga_ADMIN == 12345:
                def_kelolaBarang_ADMIN()

            # Tidak boleh kurang dari atau sama dengan 0
            elif input_tambahHarga_ADMIN <= 0:
                input("\033[2;31mMasukkan angka dengan benar!\033[0;0m\ntekan ENTER untuk melanjutkan") 
                def_tambahBarang_ADMIN()

            # Isi stok
            else:
                input_tambahStok_ADMIN = int(input("Masukkan stok: ")) 

                # Kembali
                if input_tambahStok_ADMIN == 12345:
                    def_kelolaBarang_ADMIN()

                # Tidak boleh kurang dari atau sama dengan 0
                elif input_tambahStok_ADMIN <= 0:
                    input("\033[2;31mMasukkan angka dengan benar!\033[0;0m\ntekan ENTER untuk melanjutkan") 
                    def_tambahBarang_ADMIN()

                # Tambah barang berhasil
                else:
                    list_barang.append([input_tambahNama_ADMIN,input_tambahHarga_ADMIN,input_tambahStok_ADMIN])

                    def_header()
                    print(tb(tb_tambahBarang_ADMIN, tablefmt="rounded_outline"))
                    print("Tunggu sebentar...")
                    sleep(3) 

                    def_header()
                    print(tb(tb_tambahBarang_ADMIN, tablefmt="rounded_outline"))
                    input("\033[32mBarang berhasil ditambahkan\033[0;0m\nTekan ENTER untuk melanjutkan")
                    def_kelolaBarang_ADMIN()

    except ValueError:
        input("\033[2;31mMasukkan angka dengan benar!\033[0;0m\ntekan ENTER untuk melanjutkan") 
        def_tambahBarang_ADMIN()            

# def ubah harga (ADMIN)
def def_ubahHarga_ADMIN():
    try:
        def_header()
        tb_ubahHarga_ADMIN = [["\033[1mUBAH HARGA\033[0;0m"]]
        print(tb(tb_ubahHarga_ADMIN, tablefmt="rounded_outline")) 

        header_barang2 = ["ID","Barang","Harga (Rp)","Stok"]
        print(tb(list_barang, intfmt=",", headers=header_barang2, tablefmt="grid", showindex=True))
        print("\033[93mKetik 12345 untuk kembali\033[0m")

        input_idBarang_ADMIN = int(input("Masukkan ID: "))               
        input_hargaBaru_ADMIN = int(input("Masukkan Harga baru: "))

        # Kembali
        if input_idBarang_ADMIN == 12345 or input_hargaBaru_ADMIN == 12345:
            def_kelolaBarang_ADMIN()

        # Harga tidak boleh kurang dari atau sama dengan 0
        elif input_hargaBaru_ADMIN <= 0:
            input("\033[2;31mMasukkan angka dengan benar!\033[0;0m\ntekan ENTER untuk melanjutkan")  
            def_ubahHarga_ADMIN()

        # Berhasil ubah harga
        else:
            list_barang[input_idBarang_ADMIN][1] = input_hargaBaru_ADMIN

            def_header()
            print(tb(tb_ubahHarga_ADMIN, tablefmt="rounded_outline"))
            print("Tunggu sebentar...")
            sleep(3) 

            def_header()
            print(tb(tb_ubahHarga_ADMIN, tablefmt="rounded_outline"))
            input("\033[32mHarga telah diubah\033[0;0m\nTekan ENTER untuk melanjutkan")
            def_kelolaBarang_ADMIN()

    except ValueError:
        input("\033[2;31mMasukkan angka dengan benar!\033[0;0m\ntekan ENTER untuk melanjutkan")    
        def_ubahHarga_ADMIN()               

    except IndexError:
        input("\033[2;31mMasukkan angka dengan benar!\033[0;0m\ntekan ENTER untuk melanjutkan")     
        def_ubahHarga_ADMIN()              

# def hapus barang (ADMIN)
def def_hapusBarang_ADMIN():
    try:
        def_header()
        tb_hapusBarang_ADMIN = [["\033[1mHAPUS BARANG\033[0;0m"]]
        print(tb(tb_hapusBarang_ADMIN, tablefmt="rounded_outline")) 

        header_barang2 = ["ID","Barang","Harga (Rp)","Stok"]
        print(tb(list_barang, intfmt=",", headers=header_barang2, tablefmt="grid", showindex=True))
        print("\033[93mKetik 12345 untuk kembali\033[0m")

        input_idBarang_ADMIN = int(input("Masukkan ID: "))               

        # Kembali
        if input_idBarang_ADMIN == 12345:
            def_kelolaBarang_ADMIN()

        # Berhasil hapus barang
        else:
            del list_barang[input_idBarang_ADMIN]

            def_header()
            print(tb(tb_hapusBarang_ADMIN, tablefmt="rounded_outline"))
            print("Tunggu sebentar...")
            sleep(3) 

            def_header()
            print(tb(tb_hapusBarang_ADMIN, tablefmt="rounded_outline"))
            input("\033[32mBarang berhasil dihapus\033[0;0m\nTekan ENTER untuk melanjutkan")
            def_kelolaBarang_ADMIN()

    except ValueError:
        input("\033[2;31mMasukkan angka dengan benar!\033[0;0m\ntekan ENTER untuk melanjutkan") 
        def_hapusBarang_ADMIN()                  

    except IndexError:
        input("\033[2;31mMasukkan angka dengan benar!\033[0;0m\ntekan ENTER untuk melanjutkan")  
        def_hapusBarang_ADMIN()                 

# def lihat barang (ADMIN)
def def_lihatBarang_ADMIN():
    def_header()
    tb_lihatBarang_ADMIN = [["\033[1mBARANG\033[0;0m"]]
    print(tb(tb_lihatBarang_ADMIN, tablefmt="rounded_outline"))

    header_barang_ADMIN = ["ID","Barang","Harga (Rp)","Stok"]
    print(tb(list_barang, intfmt=",", headers=header_barang_ADMIN, tablefmt="grid", showindex=True))

    input("Tekan ENTER untuk kembali")     
    def_kelolaBarang_ADMIN()

# def tambah stok (ADMIN)
def def_tambahStok_ADMIN():
    try:
        def_header()
        tb_tambahStok_ADMIN = [["\033[1mTAMBAH STOK\033[0;0m"]]
        print(tb(tb_tambahStok_ADMIN, tablefmt="rounded_outline")) 

        header_barang_ADMIN = ["ID","Barang","Harga (Rp)","Stok"]
        print(tb(list_barang, intfmt=",", headers=header_barang_ADMIN, tablefmt="grid", showindex=True))
        print("\033[93mKetik 12345 untuk kembali\033[0m")

        # Input ID baranng
        input_idBarang_ADMIN = int(input("Masukkan ID: "))

        # Kembali
        if input_idBarang_ADMIN == 12345:
            def_kelolaBarang_ADMIN()

        # Input stok tambahan
        else:
            input_tambahStok_ADMIN =  int(input("Masukkan stok tambahan: "))

            # Kembali
            if input_tambahStok_ADMIN == 12345:
                def_tambahStok_ADMIN()

            # Berhasil tambah stok
            elif input_tambahStok_ADMIN > 0:
                list_barang[input_idBarang_ADMIN][2] += input_tambahStok_ADMIN 

                def_header()
                print(tb(tb_tambahStok_ADMIN, tablefmt="rounded_outline"))
                print("Tunggu sebentar...")
                sleep(3) 

                def_header()
                print(tb(tb_tambahStok_ADMIN, tablefmt="rounded_outline"))
                input("\033[32mStok berhasil ditambah\033[0;0m\nTekan ENTER untuk melanjutkan")
                def_kelolaBarang_ADMIN()

            # Tidak boleh kurang dari atau sama dengan 0
            else:
                input("\033[2;31mMasukkan angka dengan benar!\033[0;0m\nTekan ENTER untuk melanjutkan")
                def_tambahStok_ADMIN()

    except IndexError:
        input("\033[2;31mID tidak ada\033[0;0m\nTekan ENTER untuk melanjutkan")       
        def_tambahStok_ADMIN()

    except ValueError:
        input("\033[2;31mMasukkan angka dengan benar!\033[0;0m\nTekan ENTER untuk melanjutkan")
        def_tambahStok_ADMIN()

# def lihat riwayat penjualan (ADMIN)
def def_lihatRiwayatPenjualan_ADMIN():
    def_header()
    tb_lihatRiwayatPenjualan_ADMIN = [["\033[1mRIWAYAT PENJUALAN\033[0;0m"]]
    print(tb(tb_lihatRiwayatPenjualan_ADMIN, tablefmt="rounded_outline"))

    if len(list_namaPendataanBarang) > 0:
        print("==================================")
        for i in range(len(list_namaPendataanBarang)):
            print(f"Nama barang\t: {list_namaPendataanBarang[i]}")
            print(f"Barang terjual\t: {list_jumlahPendataanBarang[i]}")
            print("==================================")
        print(f"Jumlah\t\t: {sum(list_jumlahPendataanBarang)}")
        print("==================================")

    # Keranjang kosong
    else:
        print("Riwayat penjualan masih kosong")
    
    input("tekan ENTER untuk kembali")
    def_kelolaBarang_ADMIN()

# def kelola barang (ADMIN)
def def_kelolaBarang_ADMIN():
    def_header() 
    tb_kelolaBarang_ADMIN = [
    ["\033[1mMENU\033[0;0m"],
    ["[1] Lihat barang"],
    ["[2] Tambah barang"],
    ["[3] Ubah Harga"],
    ["[4] Hapus barang"],
    ["[5] Tambah stok"],
    ["[6] Lihat riwayat penjualan"],
    ["[7] Kembali"]
    ]
    print(tb(tb_kelolaBarang_ADMIN, tablefmt="rounded_outline"))

    input_kelolaBarang_ADMIN = input("Masukkan menu: ")

    # Lihat barang
    if input_kelolaBarang_ADMIN == "1":
        def_lihatBarang_ADMIN()

    # Tambah barang  
    elif input_kelolaBarang_ADMIN == "2":
        def_tambahBarang_ADMIN()

    # Ubah harga
    elif input_kelolaBarang_ADMIN == "3":
        def_ubahHarga_ADMIN()

    # Ubah harga
    elif input_kelolaBarang_ADMIN == "4":
        def_hapusBarang_ADMIN()

    # Tambah stok
    elif input_kelolaBarang_ADMIN == "5":
        def_tambahStok_ADMIN()

    # Lihat riwayat penjualan
    elif input_kelolaBarang_ADMIN == "6":
        def_lihatRiwayatPenjualan_ADMIN()

    # Kembali
    elif input_kelolaBarang_ADMIN == "7":
        def_menuToko_ADMIN()

    # Salah pilih
    else:
        input("\033[2;31mMasukkan pilihan dengan benar\033[0;0m\ntekan ENTER untuk melanjutkan")  
        def_kelolaBarang_ADMIN()           

# def lihat akun user (ADMIN)
def def_lihatAkunUser_ADMIN():
    def_header()
    tb_lihatAkunUser_ADMIN = [[i, *dict_akun_USER.values()] for i, dict_akun_USER in dict_akun_USER.items()]
    header_lihatAkunUser_ADMIN = ["ID","Username","Password"]
    print(tb(tb_lihatAkunUser_ADMIN, headers=header_lihatAkunUser_ADMIN, tablefmt="grid"))

    input("Tekan ENTER untuk kembali")
    def_kelolaAkunUser_ADMIN()

# def ubah username user (ADMIN)
def def_ubahUsernameUser_ADMIN():
    try:
        def_header()
        tb_ubahUsernameUser_ADMIN = [["\033[1mUBAH USERNAME AKUN USER\033[0;0m"]]
        print(tb(tb_ubahUsernameUser_ADMIN, tablefmt="rounded_outline"))
        print("\033[93mKosongkan isi lalu tekan ENTER untuk kembali\033[0m")

        tb_lihatAkunUser_ADMIN = [[i, *dict_akun_USER.values()] for i, dict_akun_USER in dict_akun_USER.items()]
        header_lihatAkunUser_ADMIN = ["ID","Username","Password"]
        print(tb(tb_lihatAkunUser_ADMIN, headers=header_lihatAkunUser_ADMIN, tablefmt="grid"))

        # Input ID 
        input_idUser_ADMIN = input("Masukkan ID: ")

        # Kembali
        if len(input_idUser_ADMIN) == 0:
            def_kelolaAkunUser_ADMIN()

        # Input username baru
        else:
            input_usernameBaruUser_ADMIN = input("Masukkan username baru: ")

            # Kembali
            if len(input_usernameBaruUser_ADMIN) == 0:
                def_ubahUsernameUser_ADMIN()

            # Menghindari penggunaan username yang sama
            for i, j in dict_akun_USER.items():
                if input_usernameBaruUser_ADMIN == dict_akun_USER[i]["Username"]:
                    input("\033[2;31mUsername sudah digunakan\033[0;0m\nTekan ENTER untuk melanjutkan")
                    def_ubahUsernameUser_ADMIN()

            # Ganti username berhail
            else:
                dict_akun_USER[input_idUser_ADMIN]["Username"] = input_usernameBaruUser_ADMIN

                def_header()
                print(tb(tb_ubahUsernameUser_ADMIN, tablefmt="rounded_outline"))
                print("Tunggu sebentar...")
                sleep(3) 

                def_header()
                print(tb(tb_ubahUsernameUser_ADMIN, tablefmt="rounded_outline"))
                input("\033[32mUsername berhasil diubah\033[0;0m\nTekan ENTER untuk melanjutkan")
                def_kelolaAkunUser_ADMIN()

    except KeyError:
        input("\033[2;31mID tidak ada\033[0;0m\nTekan ENTER untuk melanjutkan")       
        def_ubahUsernameUser_ADMIN()

# def ubah password user (ADMIN)
def def_ubahPasswordUser_ADMIN():
    try:
        def_header()
        tb_ubahPasswordUser_ADMIN = [["\033[1mUBAH PASSWORD AKUN USER\033[0;0m"]]
        print(tb(tb_ubahPasswordUser_ADMIN, tablefmt="rounded_outline"))
        print("\033[93mKosongkan isi lalu tekan ENTER untuk kembali\033[0m")

        tb_lihatAkunUser_ADMIN = [[i, *dict_akun_USER.values()] for i, dict_akun_USER in dict_akun_USER.items()]
        header_lihatAkunUser_ADMIN = ["ID","Username","Password"]
        print(tb(tb_lihatAkunUser_ADMIN, headers=header_lihatAkunUser_ADMIN, tablefmt="grid"))

        # Input ID 
        input_idUser_ADMIN = input("Masukkan ID: ")

        # Kembali
        if len(input_idUser_ADMIN) == 0:
            def_kelolaAkunUser_ADMIN()

        # Input password baru
        else:
            input_passwordBaruUser_ADMIN = input("Masukkan password baru: ")

            # Kembali
            if len(input_passwordBaruUser_ADMIN) == 0:
                def_ubahPasswordUser_ADMIN()

            # Password tidak boleh kurang dari 8 karakter
            elif len(input_passwordBaruUser_ADMIN) < 8:
                input("\033[2;31mPassword tidak boleh kurang dari 8 karakter\033[0;0m\nTekan ENTER untuk melanjutkan")
                def_ubahPasswordUser_ADMIN()

            # Register berhasil
            else:
                dict_akun_USER[input_idUser_ADMIN]["Password"] = input_passwordBaruUser_ADMIN

                def_header()
                print(tb(tb_ubahPasswordUser_ADMIN, tablefmt="rounded_outline"))
                print("Tunggu sebentar...")
                sleep(3) 

                def_header()
                print(tb(tb_ubahPasswordUser_ADMIN, tablefmt="rounded_outline"))
                input("\033[32mPassword berhasil diubah\033[0;0m\nTekan ENTER untuk melanjutkan")
                def_kelolaAkunUser_ADMIN()

    except KeyError:
        input("\033[2;31mID tidak ada\033[0;0m\nTekan ENTER untuk melanjutkan")       
        def_ubahPasswordUser_ADMIN()

# def hapus akun user (ADMIN)
def def_hapusAkunUser_ADMIN():
    try:
        def_header()
        tb_hapusAkunUser_ADMIN = [["\033[1mHAPUS AKUN USER USER\033[0;0m"]]
        print(tb(tb_hapusAkunUser_ADMIN, tablefmt="rounded_outline"))
        print("\033[93mKosongkan isi lalu tekan ENTER untuk kembali\033[0m")

        tb_lihatAkunUser_ADMIN = [[i, *dict_akun_USER.values()] for i, dict_akun_USER in dict_akun_USER.items()]
        header_lihatAkunUser_ADMIN = ["ID","Username","Password"]
        print(tb(tb_lihatAkunUser_ADMIN, headers=header_lihatAkunUser_ADMIN, tablefmt="grid"))

        # Input ID 
        input_idUser_ADMIN = input("Masukkan ID: ")

        # Kembali
        if len(input_idUser_ADMIN) == 0:
            def_kelolaAkunUser_ADMIN()

        # Berhasil hapus akun
        else:
            del dict_akun_USER[input_idUser_ADMIN]

            def_header()
            print(tb(tb_hapusAkunUser_ADMIN, tablefmt="rounded_outline"))
            print("Tunggu sebentar...")
            sleep(3) 

            def_header()
            print(tb(tb_hapusAkunUser_ADMIN, tablefmt="rounded_outline"))
            input("\033[32mAkun telah dihapus\033[0;0m\nTekan ENTER untuk melanjutkan")
            def_kelolaAkunUser_ADMIN()

    except KeyError:
        input("\033[2;31mID tidak ada\033[0;0m\nTekan ENTER untuk melanjutkan")       
        def_hapusAkunUser_ADMIN()

# def kelola akun user (ADMIN)
def def_kelolaAkunUser_ADMIN():
    def_header() 
    tb_kelolaAkunUser_ADMIN = [
    ["\033[1mKELOLA AKUN USER\033[0;0m"],
    ["[1] Lihat akun user"],
    ["[2] Ubah username"],
    ["[3] Ubah password"],
    ["[4] Hapus akun"],
    ["[5] Kembalii"]
    ]
    print(tb(tb_kelolaAkunUser_ADMIN, tablefmt="rounded_outline"))    

    input_kelolaAkunUser_ADMIN = input("Masukkan pilihan: ")

    # Lihat akun user
    if input_kelolaAkunUser_ADMIN == "1":
        def_lihatAkunUser_ADMIN()

    # Ubah username
    elif input_kelolaAkunUser_ADMIN == "2":
        def_ubahUsernameUser_ADMIN()

    # Ubah password
    elif input_kelolaAkunUser_ADMIN == "3":
        def_ubahPasswordUser_ADMIN()

    elif input_kelolaAkunUser_ADMIN == "4":
        def_hapusAkunUser_ADMIN()

    # Kembali
    elif input_kelolaAkunUser_ADMIN == "5":
        def_menuToko_ADMIN()
    
    # Salah pilih
    else:
        input("\033[2;31mMasukkan pilihan dengan benar\033[0;0m\ntekan ENTER untuk melanjutkan")
        def_kelolaAkunUser_ADMIN()

# def menu toko (ADMIN)
def def_menuToko_ADMIN():
    while True:
        def_header() 
        tb_menuToko_ADMIN = [
        ["\033[1mMENU\033[0;0m"],
        ["[1] Kelola barang"],
        ["[2] Kelola akun user"],
        ["[3] Log out"]
        ]
        print(tb(tb_menuToko_ADMIN, tablefmt="rounded_outline"))

        input_menuToko_ADMIN = input("Masukkan pilihan: ")

        # Kelola barang
        if input_menuToko_ADMIN == "1":
            def_kelolaBarang_ADMIN()

        # Kelola akun user
        elif input_menuToko_ADMIN == "2":
            def_kelolaAkunUser_ADMIN()

        # Log out
        elif input_menuToko_ADMIN == "3":
            def_konfirmasiLogout()

        # Salah pilih
        else:
            input("\033[2;31mMasukkan pilihan dengan benar\033[0;0m\ntekan ENTER untuk melanjutkan")
            def_menuToko_ADMIN()           

# def login akun (ADMIN)
def def_loginAkun_ADMIN():
    def_header()
    tb_login_ADMIN = [["\033[1mLOG IN AKUN ADMIN\033[0;0m"]]
    print(tb(tb_login_ADMIN, tablefmt="rounded_outline"))
    print("\033[93mKosongkan isi lalu tekan ENTER untuk kembali\033[0m")    

    input_loginUsername_ADMIN = input("Username: ")

    if len(input_loginUsername_ADMIN) == 0:
        def_menuUtama()
    
    else:
        input_loginPassword_ADMIN = pwinput.pwinput(prompt="Password: ", mask="\u2022")

        if len(input_loginPassword_ADMIN) == 0:
            def_loginAkun_ADMIN()

        elif input_loginUsername_ADMIN == tuple_loginUsername_ADMIN and input_loginPassword_ADMIN == tuple_loginPassword_ADMIN:
            def_menuToko_ADMIN()

        else:
            input("\033[2;31mLog in salah\033[0;0m\nTekan ENTER untuk melanjutkan")
            def_loginAkun_ADMIN()

# def konfirmasi exit
def def_konfirmasiExit():
    def_header()
    print(tb([["\033[1mEXIT\033[0;0m"]], tablefmt="rounded_grid"))

    pilih_konfirmasiExit = input("Anda yakin ingin keluar dari program?\n[Y/N] ")

    # Ingin log out
    if pilih_konfirmasiExit == "Y" or pilih_konfirmasiExit == "y":  
        def_clearScreen()
        exit("Selamat tinggal")
    
    # Tidak ingin log out
    elif pilih_konfirmasiExit == "N" or pilih_konfirmasiExit == "n":
        def_menuUtama()

    # Salah pilih
    else:
        input("\033[2;31mMasukkan pilihan dengan benar!\033[0;0m\nTekan ENTER untuk melanjutkan")
        def_konfirmasiExit()

# def menu utama
def def_menuUtama():
    def_header()
    tb_menuUtama = [
    ["\033[1mMENU UTAMA\033[0;0m"],
    ["[1] User"],
    ["[2] Admin"],
    ["[3] Exit"]
    ]
    print(tb(tb_menuUtama, tablefmt="rounded_outline"))

    input_menutUtama = input("Masukkan pilihan: ")

    # Menu user
    if input_menutUtama == "1":
        def_menuAkun_USER()
    
    # Menu admin
    elif input_menutUtama == "2":
        def_loginAkun_ADMIN()

    # Exit
    elif input_menutUtama == "3":
        def_konfirmasiExit()

    # Salah pilih
    else:
        input("\033[2;31mMasukkan pilihan dengan benar\033[0;0m\ntekan ENTER untuk melanjutkan")
        def_menuUtama()

# def mengembalikan stok setelah log out
def def_stokLogout():
    for j in list_barang:
        for k in list_namaBarang_USER:
            if k in j:
                list_barang[list_barang.index(j)][2] += list_jumlahBarang_USER[list_namaBarang_USER.index(k)]

    list_namaBarang_USER.clear()
    list_jumlahBarang_USER.clear()
    list_hargaBarang_USER.clear()

# def konfirmasi log out
def def_konfirmasiLogout():
    while True:
        def_header()
        print(tb([["\033[1mLOG OUT\033[0;0m"]], tablefmt="rounded_grid"))

        pilih_konfirmasiLogout = input("Anda yakin ingin log out?\n[Y/N] ")

        # Ingin log out
        if pilih_konfirmasiLogout == "Y" or pilih_konfirmasiLogout == "y":  
            def_stokLogout()
            def_menuUtama()
        
        # Tidak ingin log out
        elif pilih_konfirmasiLogout == "N" or pilih_konfirmasiLogout == "n":
            break

        # Salah pilih
        else:
            input("\033[2;31mMasukkan pilihan dengan benar!\033[0;0m\nTekan ENTER untuk melanjutkan")

def_menuUtama()