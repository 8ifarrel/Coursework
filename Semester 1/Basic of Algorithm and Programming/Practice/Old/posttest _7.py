# Import OS package
import os

# Import time
import time

# Install dan import Tabulate
os.system("pip install tabulate")
from tabulate import tabulate as tb

# Install dan import PWInput
os.system("pip install pwinput")
import pwinput

# Import Time
import time

# dictionary akun user
keys_ID_USER = 2
dict_akun_USER = {
    0: {"Username": "farrel","Password": "sirah123"},
    1: {"Username": "posttest7","Password": "12345678"}
    } 

# dictionary akun admin
dict_akun_ADMIN = {
    0: {"Username": "pengensekelompok","Password": "samasirkel"}
}

# dictionary smartphone
tb_headersSmartphone = ["Smartphone","Harga (Rp)"]

dict_smartphone = {
   0: {
    "Nama": "ASUS Zenfone 8",
    "Harga": 7999999
    },

   1: {
    "Nama": "ROG Phone 6",
    "Harga": 10999999
    },

   2: {
    "Nama": "iPhone 13",
    "Harga": 13999999
    },

   3: {
    "Nama": "iPhone 13 Pro",
    "Harga": 17999999
    }
}

# def clear screen
def def_clearScreen():
    os.system("cls" if os.name == "nt" else "clear")

# def header
def def_header():
    def_clearScreen()
    print("""\033[01m
     ___   _   _   ___  __   __   _       ___   _  _    ___    _  _   ___ 
    / __| | | | | | _ \ \ \ / /  /_\     | _ \ | || |  / _ \  | \| | | __|
    \__ \ | |_| | |   /  \ V /  / _ \    |  _/ | __ | | (_) | | .` | | _| 
    |___/  \___/  |_|_\   |_|  /_/ \_\   |_|   |_||_|  \___/  |_|\_| |___|
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━                                                                      
    \033[0m""")    

# def menu smarthone user
def def_menuSmartphone_USER():
    def_header()
    print(tb([["\033[1mSMARTPHONE\033[0;0m"]], tablefmt="rounded_grid")) 

    tb_menuSmartphone = [[*dict_smartphone.values()] for dict_smartphone, dict_smartphone in dict_smartphone.items()]
    print(tb(tb_menuSmartphone, headers=tb_headersSmartphone, tablefmt="grid", intfmt=","))

    input("Tekan ENTER untuk kembali")

# def konfirmasi log out
def def_konfirmasiLogout():
    global pilih_konfirmasiLogout
    while True:
        def_header()
        print(tb([["\033[1mLOG OUT\033[0;0m"]], tablefmt="rounded_grid"))

        pilih_konfirmasiLogout = input("Anda yakin ingin log out?\n[Y/N] ")

        # Ingin log out
        if pilih_konfirmasiLogout == "Y" or pilih_konfirmasiLogout == "y":
            break
        
        # Tidak ingin log out
        elif pilih_konfirmasiLogout == "N" or pilih_konfirmasiLogout == "n":
            break

        # Salah pilih
        else:
            print("\033[2;31mMasukkan pilihan dengan benar!\033[0;0m")
            input("Tekan ENTER untuk melanjutkan")

# def menu toko user
def def_menuToko_USER():
    while True:
        def_header()
        print(tb([["\033[1mMENU\033[0;0m\n1. Lihat smartphone\n2. Log out"]], tablefmt="rounded_grid"))

        pilih_menuAkun_tamu = input("Masukkan pilihan: ")

        # Lihat smartphone
        if pilih_menuAkun_tamu == "1":
            def_menuSmartphone_USER()

        
        # Log out
        elif pilih_menuAkun_tamu == "2":
            def_konfirmasiLogout()

            # Agar benar-benar ter-log out
            if pilih_konfirmasiLogout == "Y" or pilih_konfirmasiLogout == "y":
                break

        # Salah pilih        
        else:
            print("\033[2;31mMasukkan pilihan dengan benar!\033[0;0m")
            input("Tekan ENTER untuk melanjutkan")

# def register akun user
def def_registerAkun_USER():
    while True:
        def_header()
        print(tb([["\033[01mREGISTER AKUN USER\033[0m"]],tablefmt="rounded_grid"))
        print("\033[93mKosongkan isi lalu tekan ENTER untuk kembali\033[0m")
        
        input_usernameRegister_USER = input("Username: ")

        # Kembali
        if len(input_usernameRegister_USER) == 0:
            break

        # Menghindari penggunaan username yang sama
        for i in range(len(dict_akun_USER)):
            if input_usernameRegister_USER == dict_akun_USER[i]["Username"]:
                input("\033[2;31mUsername sudah digunakan\033[0;0m\nTekan ENTER untuk melanjutkan")
                break

        # Lanjut register
        else:
            while True:
                input_passwordRegister_USER = input("Passowrd: ")

                # Kembali
                if len(input_passwordRegister_USER) == 0:
                    break

                # Password tidak boleh kurang dari 8 karakter
                elif len(input_passwordRegister_USER) < 8:
                    input("\033[2;31mPassword tidak boleh kurang dari 8 karakter\033[0;0m\nTekan ENTER untuk melanjutkan")

                    def_header()
                    print(tb([["\033[01mREGISTER AKUN USER\033[0m"]],tablefmt="rounded_grid"))
                    print("\033[93mKosongkan isi lalu tekan ENTER untuk kembali\033[0m")
                    print(f"Username: {input_usernameRegister_USER}")

                # Register berhasil
                else:
                    keys_ID_USER = 2
                    dict_akun_USER[keys_ID_USER] = {"Username":input_usernameRegister_USER, "Password":input_passwordRegister_USER}
                    keys_ID_USER += 1

                    def_header()
                    print(tb([["\033[01mREGISTER AKUN USER\033[0m"]],tablefmt="rounded_grid"))
                    print("Tunggu sebentar...")
                    time.sleep(5) 

                    def_header()
                    print(tb([["\033[01mREGISTER AKUN USER\033[0m"]],tablefmt="rounded_grid"))
                    input("\033[32mAkun berhasil dibuat\033[0;0m\nTekan ENTER untuk melanjutkan")
                    break
   
# def login akun user
def def_loginAkun_USER():
    while True:
        def_header()
        print(tb([["\033[1mLOG IN AKUN USER\033[0;0m"]], tablefmt="rounded_outline"))
        print("\033[93mKosongkan isi lalu tekan ENTER untuk kembali\033[0m")
        
        input_usernameLogin_USER = input("Username: ")

        # Kembali
        if len(input_usernameLogin_USER) == 0:
            break

        # Lanjut login
        else:
            while True:
                input_passwordLogin_USER = input("Password: ")
                                
                # Kembali 
                if len(input_passwordLogin_USER) == 0:
                    break

                # Log in berhasil
                for i in range(len(dict_akun_USER)):
                    if input_usernameLogin_USER == dict_akun_USER[i]["Username"] and input_passwordLogin_USER == dict_akun_USER[i]["Password"]:
                        def_menuToko_USER()
                        break

                # Log in gagal
                else:
                    input("\033[2;31mLog in salah\033[0;0m\nTekan ENTER untuk melanjutkan")
                    break
            
                break

# def menu akun user
def def_menuAkun_USER():
    while True:
        def_header()
        print(tb([["\033[01mMENU AKUN USER\033[0m\n[1] Register\n[2] Log in\n[3] Kembali"]],tablefmt="rounded_grid"))

        input_menuAkun_USER = input("Masukkan pilihan: ")

        # Register akun user
        if input_menuAkun_USER == "1":
            def_registerAkun_USER()

        elif input_menuAkun_USER == "2":
            def_loginAkun_USER()

        # Kembali
        elif input_menuAkun_USER == "3":
            break 

        # Salah pilih
        else:
            input("\033[2;31mMasukkan pilihan dengan benar!\033[0;0m\nTekan ENTER untuk melanjutkan")


# def tambah smartphone admin
def def_tamnbahSmartphone_ADMIN():
    while True:
        try:
            def_header()
            print(tb([["\033[1mTAMBAH SMARTPHONE\033[0;0m"]], tablefmt="rounded_grid"))

            input_namaSmartphoneBaru_ADMIN = input("Masukkan nama: ")
            input_hargaSmartphoneBaru_ADMIN = int(input("Masukkan harga: "))

            keys_ID_smartphone = 4
            dict_smartphone[keys_ID_smartphone] = {"Nama": input_namaSmartphoneBaru_ADMIN, "Harga": input_hargaSmartphoneBaru_ADMIN}
            keys_ID_smartphone += 1

            def_header()
            print(tb([["\033[1mTAMBAH SMARTPHONE\033[0;0m"]],tablefmt="rounded_grid"))      
            print("Tunggu sebentar...")
            time.sleep(5)

            def_header()
            print(tb([["\033[1mTAMBAH SMARTPHONE\033[0;0m"]],tablefmt="rounded_grid"))
            input("Smartphone telah ditambah\nTekan ENTER untuk kembali")

            break

        except ValueError:
            input("\033[2;31mMasukkan harga dengan benar!\033[0;0m\nTekan ENTER untuk melanjutkan")   

# def hapus smartphone admin
def def_hapusSmartphone_ADMIN():
    def_header()
    print(tb([["\033[1mHAPUS SMARTPHONE\033[0;0m"]], tablefmt="rounded_grid"))

    tb_menuSmartphone2 = [[i, *dict_smartphone.values()] for i, dict_smartphone in dict_smartphone.items()]
    print(tb(tb_menuSmartphone2, headers=["ID","Smartphone","Harga (Rp)"], tablefmt="grid", intfmt=","))

    input_hapusSmartphone_ADMIN = int(input("Masukkan ID: "))

    del dict_smartphone[input_hapusSmartphone_ADMIN]

    def_header()
    print(tb([["\033[1mHAPUS SMARTPHONE\033[0;0m"]],tablefmt="rounded_grid"))      
    print("Tunggu sebentar...")
    time.sleep(5)

    def_header()
    print(tb([["\033[1mHAPUS SMARTPHONE\033[0;0m"]],tablefmt="rounded_grid"))
    input("Smartphone telah dihapus\nTekan ENTER untuk kembali")

# def kelola smartphone admin
def def_kelolaSmartphone_ADMIN():
    while True:
        try:
            def_header()
            tb_menuSmartphone = [[*dict_smartphone.values()] for dict_smartphone, dict_smartphone in dict_smartphone.items()]
            print(tb(tb_menuSmartphone, headers=tb_headersSmartphone, tablefmt="grid", intfmt=","))
            print(tb([["\033[1mKELOLA SMARTPHONE\033[0;0m\n1. Tambah smartphone\n2. hapus smartphone\n3. Kembali"]], tablefmt="rounded_grid"))

            input_kelolaSmartphone_ADMIN = input("Masukkann pilihan: ") 

            # Tambah smartphone
            if input_kelolaSmartphone_ADMIN == "1":
                def_tamnbahSmartphone_ADMIN()

            # Hapus smartphone
            elif input_kelolaSmartphone_ADMIN == "2":
                def_hapusSmartphone_ADMIN()

            # Kembali
            elif input_kelolaSmartphone_ADMIN == "3":
                break

            # Salah pilih
            else:
                input("\033[2;31mMasukkan pilihan dengan benar!\033[0;0m\nTekan ENTER untuk melanjutkan")

        except IndexError:
            input("\033[2;31mKode tidak ada\033[0;0m\nTekan ENTER untuk melanjutkan")   

def def_menuToko_ADMIN():
    while True:
        def_header()
        print(tb([["\033[1mMENU\033[0;0m\n1. Kelola smartphone\n2. Log out"]], tablefmt="rounded_grid"))
        
        pilih_menuToko_ADMIN = input("Masukkan pilihan: ")

        # Kelola smartphone
        if pilih_menuToko_ADMIN == "1":
            def_kelolaSmartphone_ADMIN()

        # Log out
        elif pilih_menuToko_ADMIN == "2":
            def_konfirmasiLogout()

            # Agar benar-benar ter-log out (ADMIN)
            if pilih_konfirmasiLogout == "Y" or pilih_konfirmasiLogout == "y":
                break

        # Salah pilih
        else:
            input("\033[2;31mMasukkan pilihan dengan benar!\033[0;0m\nTekan ENTER untuk melanjutkan")

def def_loginAkun_ADMIN():
    while True:
        def_header()
        print(tb([["\033[1mLOG IN AKUN ADMIN\033[0;0m"]], tablefmt="rounded_outline"))
        print("\033[93mKosongkan isi lalu tekan ENTER untuk kembali\033[0m")
        
        input_usernameLogin_ADMIN = input("Username: ")

        # Kembali
        if len(input_usernameLogin_ADMIN) == 0:
            break

        # Lanjut login
        else:
            while True:
                input_passwordLogin_ADMIN = input("Password: ")
                                
                # Kembali 
                if len(input_passwordLogin_ADMIN) == 0:
                    break

                # Log in berhasil

                if input_usernameLogin_ADMIN == dict_akun_ADMIN[0]["Username"] and input_passwordLogin_ADMIN == dict_akun_ADMIN[0]["Password"]:
                    def_menuToko_ADMIN()
                    break

                # Log in gagal
                else:
                    input("\033[2;31mLog in salah\033[0;0m\nTekan ENTER untuk melanjutkan")
                    break

# Menu utama
while True:
    def_header()
    print(tb([["\033[01mMENU UTAMA\033[0m\n[1] User\n[2] Admin\n[3] Keluar"]],tablefmt="rounded_grid"))

    input_menuUtama = input("Masukkan pilihan: ")

    # Menu akun user
    if input_menuUtama == "1":
        def_menuAkun_USER()

    elif input_menuUtama == "2":
        def_loginAkun_ADMIN()

    # Keluar dari program
    elif input_menuUtama == "3":
        def_clearScreen()
        exit("Selamat tinggal")

    else:
        input("\033[2;31mMasukkan pilihan dengan benar!\033[0;0m\nTekan ENTER untuk melanjutkan")