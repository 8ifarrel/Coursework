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

# # # # # # # # # #
#                 #
#     L I S T     #
#                 #
# # # # # # # # # # ###############################################################################

# list akun tamu (nested list)
list_akunTamu = [["farrel77", "1sampai9"],["dipa69", "123456789"]]

# List akun admin (nested list)
list_akunAdmin = [["admin1805", "hujanduid"],["dapingaje","ahmadapin456"],["c","c"]]

# list barang (nested list)
tb_headerSmartphone_tamu = ["Smartphone","Harga (Rp)"]
tb_headerSmartphone_admin = ["kode","Smartphone","Harga (Rp)"]
list_smartphone_ASUS = [["ROG Phone 6",10999999],["ROG Phone 6 Pro",18999999],["ASUS Zenfone 8",7999999]]
list_smartphone_HUAWEI = [["HUAWEI nova 9",7599999],["HUAWEI P50 Pro",14999999],["HUAWEI Mate Xs",38999999]] 
list_smartphone_iPhone = [["iPhone 13",13999999],["iPhone 13 Pro",17999999],["iPhone 13 Pro Max",19499999]]
list_smartphone_OPPO = [["OPPO Find X5 Pro 5G",14999999],["OPPO Reno8 Pro 5G",9999999],["OPPO Reno8 5G",7999999]]
list_smartphone_realme = [["realme GT NEO 3",10999999],["realme narzo 50i Prime",1399999],["realme GT 2 Pro",9999999]]
list_smartphone_Samsung = [["Samsung Galaxy S22",12999999],["Samsung Galaxy S22+",15999999],["Samsung Galaxy S22 Ultra",20999999]]
list_smartphone_vivo = [["vivo X80",11999999],["vivo X80 Pro",15999999]]
list_smartphone_Xiaomi = [["Xiaomi 11T",4999999],["Xiaomi 11T Pro",6499999],["Redmi Note 10 Pro",3199999]]

# # # # # # # #
#             #
#     DEF     #
#             #
# # # # # # # # #################################################################################

# def header
def def_header():
    os.system("cls")
    print(tb([["\033[1mSURYA PHONE\033[0;0m"]], tablefmt="heavy_outline"))

# def konfirmasi log out
def def_konfirmasiLogout():
    global pilih_konfirmasiLogout
    while True:
        def_header()
        print(tb([["\033[1mLOG OUT\033[0;0m"]], tablefmt="grid"))

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

# # # # # # # # #
#               #
#   DEF  USER   #
#               #
# # # # # # # # # ###############################################################################

# def registrasi akun (TAMU)
def def_registerAkunTamu():
    while True:
        def_header()
        print(tb([["\033[1mREGISTER AKUN TAMU\033[0;0m"]], tablefmt="grid"))

        # input registrasi akun tamu
        registerAkunTamu_username = input("Username: ")

        # Menghindari pemilihan username yang sama
        for i in range(len(list_akunTamu)):
            if registerAkunTamu_username == (list_akunTamu[i][0]):
                input("\033[2;31mUsername sudah digunakan\033[0;0m\nTekan ENTER untuk melanjutkan")
                break

        # Lanjut input registrasi akun tamu
        else:
            registerAkunTamu_password = input("Password: ")
            list_akunTamu.append([registerAkunTamu_username,registerAkunTamu_password])

            def_header()
            print(tb([["\033[1mREGISTER AKUN TAMU\033[0;0m"]], tablefmt="grid"))
            print("Tunggu sebentar...")
            time.sleep(5)

            def_header()
            print(tb([["\033[1mREGISTER AKUN TAMU\033[0;0m"]], tablefmt="grid"))
            input("Selamat, akun Anda berhasil dibuat\nTekan ENTER untuk kembali")
            break

# def log in akun (TAMU)
def def_loginAkunTamu_tamu():
    def_header()
    print(tb([["\033[1mLOG IN AKUN TAMU\033[0;0m"]], tablefmt="grid"))

    # Input log in akun tamu
    loginAkunTamu_username = input("Username: ")
    loginAkunTamu_password = pwinput.pwinput(prompt="Password: ", mask="\u2022")

    # Log in akun tamu berhasil
    if [loginAkunTamu_username,loginAkunTamu_password] in list_akunTamu:
        def_menuUtama_tamu()

    # Log in akun tamu salah
    else:
        input("\033[2;31mLog in salah\nPastikan akun telah diregistrasi\033[0;0m\nTekan ENTER untuk melanjutkan")

# def menu smartphone (TAMU)
def def_menuSmartphone_tamu():
    while True:
        def_header()
        print(tb([['''\033[1mSMARTPHONE\033[0;0m\n1. ASUS\n2. HUAWEI\n3. iPhone\n4. OPPO\n5. realme\n6. Samsung\n7. vivo\n8. Xiaomi\n9. Kembali''']], tablefmt="grid"))
        pilih_menuSmartphone_tamu = input("Masukkan pilihan: ")
        
        def_header()

        # ASUS
        if pilih_menuSmartphone_tamu == "1":
            print(tb(list_smartphone_ASUS, intfmt=",", headers=tb_headerSmartphone_tamu, tablefmt="grid"))
            input("Tekan ENTER untuk kembali")

        # HUAWEI
        elif pilih_menuSmartphone_tamu == "2":
            print(tb(list_smartphone_HUAWEI, intfmt=",", headers=tb_headerSmartphone_tamu, tablefmt="grid"))
            input("Tekan ENTER untuk kembali")

        # iPhone
        elif pilih_menuSmartphone_tamu == "3":
            print(tb(list_smartphone_iPhone, intfmt=",", headers=tb_headerSmartphone_tamu, tablefmt="grid"))
            input("Tekan ENTER untuk kembali")

        # OPPO
        elif pilih_menuSmartphone_tamu == "4":
            print(tb(list_smartphone_OPPO, intfmt=",", headers=tb_headerSmartphone_tamu, tablefmt="grid"))
            input("Tekan ENTER untuk kembali")

        # realme
        elif pilih_menuSmartphone_tamu == "5":
            print(tb(list_smartphone_realme, intfmt=",", headers=tb_headerSmartphone_tamu, tablefmt="grid"))

        # Samsung
        elif pilih_menuSmartphone_tamu == "6":
            print(tb(list_smartphone_Samsung, intfmt=",", headers=tb_headerSmartphone_tamu, tablefmt="grid"))
            input("Tekan ENTER untuk kembali")

        # vivo
        elif pilih_menuSmartphone_tamu == "7":
            print(tb(list_smartphone_vivo, intfmt=",", headers=tb_headerSmartphone_tamu, tablefmt="grid"))
            input("Tekan ENTER untuk kembali")

        # Xiaomi
        elif pilih_menuSmartphone_tamu == "8":
            print(tb(list_smartphone_Xiaomi, intfmt=",", headers=tb_headerSmartphone_tamu, tablefmt="grid"))
            input("Tekan ENTER untuk kembali")

        # Kembali ke menu
        elif pilih_menuSmartphone_tamu == "9":
            break

        # Salah pilih
        else:
            def_header()
            print(tb([["\033[1mSMARTPHONE\033[0;0m\n1. ASUS\n2. HUAWEI\n3. iPhone\n4. OPPO\n5. realme\n6. Samsung\n7. vivo\n8. Xiaomi\n9. Kembali"]], tablefmt="grid"))
            print(f"Masukkan pilihan: {pilih_menuSmartphone_tamu}")
            print("\033[2;31mMasukkan pilihan dengan benar!\033[0;0m")
            input("Tekan ENTER untuk melanjutkan")

# def menu utama (TAMU)
def def_menuUtama_tamu():
    while True:
        def_header()
        print(tb([["\033[1mMENU\033[0;0m\n1. Lihat smartphone\n2. Log out"]], tablefmt="grid"))

        pilih_menuAkun_tamu = input("Masukkan pilihan: ")

        # Lihat smartphone
        if pilih_menuAkun_tamu == "1":
            def_menuSmartphone_tamu()
        
        # Log out
        elif pilih_menuAkun_tamu == "2":
            def_konfirmasiLogout()

            # Agar benar-benar ter-log out (1/2) (TAMU)
            if pilih_konfirmasiLogout == "Y" or pilih_konfirmasiLogout == "y":
                break

        # Salah pilih        
        else:
            print("\033[2;31mMasukkan pilihan dengan benar!\033[0;0m")
            input("Tekan ENTER untuk melanjutkan")

# # # # # # # # #
#               #
#   DEF ADMIN   #
#               #
# # # # # # # # # ###############################################################################

# def log in akun (ADMIN) 
def def_loginAkun_admin():
    global pilih_konfirmasiLogout
    def_header()
    print(tb([["\033[1mLOG IN AKUN ADMIN\033[0;0m"]], tablefmt="grid"))

    # Input log in akun tamu
    loginAkunAdmin_username = input("Username: ")
    loginAkunAdmin_password = pwinput.pwinput(prompt="Password: ", mask="\u2022")

    # Log in akun tamu berhasil
    if [loginAkunAdmin_username,loginAkunAdmin_password] in list_akunAdmin:
        def_menuUtama_admin()

    # Log in akun tamu salah
    else:
        input("\033[2;31mLog in salah\033[0;0m\nTekan ENTER untuk melanjutkan")

# def menu utama (ADMIN)
def def_menuUtama_admin():
    while True:
        def_header()
        print(tb([["\033[1mMENU\033[0;0m\n1. Kelola smartphone\n2. Kelola akun\n3. Log out"]], tablefmt="grid"))
        
        pilih_menuAkun_admin = input("Masukkan pilihan: ")

        # Kelola smartphone
        if pilih_menuAkun_admin == "1":
            def_menuSmartphone_admin()

        # Kelola akun
        elif pilih_menuAkun_admin == "2":
            def_menuKelolaAkun_admin()

        # Log out
        elif pilih_menuAkun_admin == "3":
            def_konfirmasiLogout()

            # Agar benar-benar ter-log out (1/1) (ADMIN)
            if pilih_konfirmasiLogout == "Y" or pilih_konfirmasiLogout == "y":
                break

        # Salah pilih
        else:
            input("\033[2;31mMasukkan pilihan dengan benar!\033[0;0m\nTekan ENTER untuk melanjutkan")

# def menu kelola smartphone (ADMIN)
def def_kelolaSmartphone_admin():
    global pilih_kelolaSmartphone_admin
    print(tb([["\033[1mKELOLA SMARTPHONE\033[0;0m\n1. Tambah smartphone\n2. Ubah harga\n3. hapus smartphone\n4. Kembali"]], tablefmt="grid"))
    print("\033[93mINGAT KODE PRODUK YANG INGIN DIKELOLA SEBELUM MASUK KE MENU\033[0;0m")

    pilih_kelolaSmartphone_admin = input("Masukkann pilihan: ")

# def input smartphone baru (ADMIN)
def def_tambahSmartphone_input_admin():
    global tambahSmartphone_harga_admin
    global tambahSmartphone_nama_admin

    while True:
        try:
            def_header()
            print(tb([["\033[1mTAMBAH SMARTPHONE\033[0;0m"]],tablefmt="grid"))        

            tambahSmartphone_nama_admin = input("Masukkan nama: ")
            tambahSmartphone_harga_admin = int(input("Masukkan harga: "))
            break
        
        except ValueError:
            input("\033[2;31mMasukkan angka dengan benar!\033[0;0m\nTekan ENTER untuk melanjutkan")

# def notifikasi bahwa smartphone telah ditambah (ADMIN)
def def_tambahSmartphone_notifikasi_admin():
    def_header()
    print(tb([["\033[1mTAMBAH SMARTPHONE\033[0;0m"]],tablefmt="grid"))      
    print("Tunggu sebentar...")
    time.sleep(5)

    def_header()
    print(tb([["\033[1mTAMBAH SMARTPHONE\033[0;0m"]],tablefmt="grid"))
    input("Smartphone telah ditambah\nTekan ENTER untuk kembali")

# def ubah harga (ADMIN)
def def_ubahHarga_input_admin():
    global ubahHarga_kode_admin
    global ubahHarga_harga_admin

    while True:
        try:
            def_header()
            print(tb([["\033[1mUBAH HARGA\033[0;0m"]],tablefmt="grid"))     

            ubahHarga_kode_admin = int(input("Masukkan kode: "))
            ubahHarga_harga_admin = int(input("Masukkan harga: "))
            break

        except ValueError:
            input("\033[2;31mMasukkan angka dengan benar!\033[0;0m\nTekan ENTER untuk melanjutkan")     

# def notifikasi bahwa harga telah diganti (ADMIN)
def def_ubahHarga_notifikasi_admin():
    def_header()
    print(tb([["\033[1mUBAH HARGA\033[0;0m"]],tablefmt="grid"))      
    print("Tunggu sebentar...")
    time.sleep(5)

    def_header()
    print(tb([["\033[1mUBAH HAGRA\033[0;0m"]],tablefmt="grid"))
    input("Harga telah diubah\nTekan ENTER untuk kembali")

# def hapus smartphone (ADMIN)
def def_hapusSmartphone_input_admin():
    global hapusSmartphone_kode_admin

    while True:
        try:
            def_header()
            print(tb([["\033[1mHAPUS SMARTPHONE\033[0;0m"]],tablefmt="grid"))      

            hapusSmartphone_kode_admin = int(input("Masukkan kode: "))  
            break
        
        except ValueError:
            input("\033[2;31mMasukkan angka dengan benar!\033[0;0m\nTekan ENTER untuk melanjutkan")

# def notifikasi bahwa smartphone telah dihapus (ADMIN)
def def_hapusSmartphone_notifikasi_admin():
    def_header()
    print(tb([["\033[1mHAPUS SMARTPHONE\033[0;0m"]],tablefmt="grid"))      
    print("Tunggu sebentar...")
    time.sleep(5)

    def_header()
    print(tb([["\033[1mHAPUS SMARTPHONE\033[0;0m"]],tablefmt="grid"))
    input("SMartphone telah dihapus\nTekan ENTER untuk kembali")

# def kelola ASUS (ADMIN)
def def_ASUS_admin():
    while True:
        try:
            def_header()
            print(tb(list_smartphone_ASUS, intfmt=",", headers=tb_headerSmartphone_admin, tablefmt="grid",showindex=True))
            def_kelolaSmartphone_admin()

            # Tambah smartphone
            if pilih_kelolaSmartphone_admin == "1":
                def_tambahSmartphone_input_admin()
                list_smartphone_ASUS.append([tambahSmartphone_nama_admin,tambahSmartphone_harga_admin])
                def_tambahSmartphone_notifikasi_admin()

            # Ubah harga
            elif pilih_kelolaSmartphone_admin == "2":
                def_ubahHarga_input_admin()
                list_smartphone_ASUS[ubahHarga_kode_admin][1] = ubahHarga_harga_admin
                def_ubahHarga_notifikasi_admin()

            # Hapus smartphone
            elif pilih_kelolaSmartphone_admin == "3":
                def_hapusSmartphone_input_admin()
                del list_smartphone_ASUS[hapusSmartphone_kode_admin]
                def_hapusSmartphone_notifikasi_admin()

            # Kembali
            elif pilih_kelolaSmartphone_admin == "4":
                break

            # Salah pilih
            else:
                input("\033[2;31mMasukkan pilihan dengan benar!\033[0;0m\nTekan ENTER untuk melanjutkan")

        except IndexError:
            input("\033[2;31mKode tidak ada\033[0;0m\nTekan ENTER untuk melanjutkan")     

# def kelola HUAWEI (ADMIN)
def def_HUAWEI_admin():
    print(tb(list_smartphone_HUAWEI, intfmt=",", headers=tb_headerSmartphone_admin, tablefmt="grid",showindex=True))
    while True:
        try:
            def_header()
            print(tb(list_smartphone_HUAWEI, intfmt=",", headers=tb_headerSmartphone_admin, tablefmt="grid",showindex=True))
            def_kelolaSmartphone_admin()

            # Tambah smartphone
            if pilih_kelolaSmartphone_admin == "1":
                def_tambahSmartphone_input_admin()
                list_smartphone_HUAWEI.append([tambahSmartphone_nama_admin,tambahSmartphone_harga_admin])
                def_tambahSmartphone_notifikasi_admin()

            # Ubah harga
            elif pilih_kelolaSmartphone_admin == "2":
                def_ubahHarga_input_admin()
                list_smartphone_HUAWEI[ubahHarga_kode_admin][1] = ubahHarga_harga_admin
                def_ubahHarga_notifikasi_admin()

            # Hapus smartphone
            elif pilih_kelolaSmartphone_admin == "3":
                def_hapusSmartphone_input_admin()
                del list_smartphone_HUAWEI[hapusSmartphone_kode_admin]
                def_hapusSmartphone_notifikasi_admin()

            # Kembali
            elif pilih_kelolaSmartphone_admin == "4":
                break

            # Salah pilih
            else:
                input("\033[2;31mMasukkan pilihan dengan benar!\033[0;0m\nTekan ENTER untuk melanjutkan")

        except IndexError:
            input("\033[2;31mKode tidak ada\033[0;0m\nTekan ENTER untuk melanjutkan")        

# def kelola iPhone (ADMIN)
def def_iPhone_admin():
    print(tb(list_smartphone_iPhone, intfmt=",", headers=tb_headerSmartphone_admin, tablefmt="grid",showindex=True))
    while True:
        try:
            def_header()
            print(tb(list_smartphone_iPhone, intfmt=",", headers=tb_headerSmartphone_admin, tablefmt="grid",showindex=True))
            def_kelolaSmartphone_admin()


            # Tambah smartphone
            if pilih_kelolaSmartphone_admin == "1":
                def_tambahSmartphone_input_admin()
                list_smartphone_iPhone.append([tambahSmartphone_nama_admin,tambahSmartphone_harga_admin])
                def_tambahSmartphone_notifikasi_admin()

            # Ubah harga
            elif pilih_kelolaSmartphone_admin == "2":
                def_ubahHarga_input_admin()
                list_smartphone_iPhone[ubahHarga_kode_admin][1] = ubahHarga_harga_admin
                def_ubahHarga_notifikasi_admin()

            # Hapus smartphone
            elif pilih_kelolaSmartphone_admin == "3":
                def_hapusSmartphone_input_admin()
                del list_smartphone_iPhone[hapusSmartphone_kode_admin]
                def_hapusSmartphone_notifikasi_admin()

            # Kembali
            elif pilih_kelolaSmartphone_admin == "4":
                break

            # Salah pilih
            else:
                input("\033[2;31mMasukkan pilihan dengan benar!\033[0;0m\nTekan ENTER untuk melanjutkan")

        except IndexError:
            input("\033[2;31mKode tidak ada\033[0;0m\nTekan ENTER untuk melanjutkan")        

# def kelola OPPO (ADMIN)
def def_OPPO_admin():
    print(tb(list_smartphone_OPPO, intfmt=",", headers=tb_headerSmartphone_admin, tablefmt="grid",showindex=True))
    while True:
        try:
            def_header()
            print(tb(list_smartphone_OPPO, intfmt=",", headers=tb_headerSmartphone_admin, tablefmt="grid",showindex=True))
            def_kelolaSmartphone_admin()

            # Tambah smartphone
            if pilih_kelolaSmartphone_admin == "1":
                def_tambahSmartphone_input_admin()
                list_smartphone_OPPO.append([tambahSmartphone_nama_admin,tambahSmartphone_harga_admin])
                def_tambahSmartphone_notifikasi_admin()

            # Ubah harga
            elif pilih_kelolaSmartphone_admin == "2":
                def_ubahHarga_input_admin()
                list_smartphone_OPPO[ubahHarga_kode_admin][1] = ubahHarga_harga_admin
                def_ubahHarga_notifikasi_admin()

            # Hapus smartphone
            elif pilih_kelolaSmartphone_admin == "3":
                def_hapusSmartphone_input_admin()
                del list_smartphone_OPPO[hapusSmartphone_kode_admin]
                def_hapusSmartphone_notifikasi_admin()

            # Kembali
            elif pilih_kelolaSmartphone_admin == "4":
                break

            # Salah pilih
            else:
                input("\033[2;31mMasukkan pilihan dengan benar!\033[0;0m\nTekan ENTER untuk melanjutkan")

        except IndexError:
            input("\033[2;31mKode tidak ada\033[0;0m\nTekan ENTER untuk melanjutkan")        

# def kelola realme (ADMIN)
def def_realme_admin():
    print(tb(list_smartphone_realme, intfmt=",", headers=tb_headerSmartphone_admin, tablefmt="grid",showindex=True))
    while True:
        try:
            def_header()
            print(tb(list_smartphone_realme, intfmt=",", headers=tb_headerSmartphone_admin, tablefmt="grid",showindex=True))
            def_kelolaSmartphone_admin()

            # Tambah smartphone
            if pilih_kelolaSmartphone_admin == "1":
                def_tambahSmartphone_input_admin()
                list_smartphone_realme.append([tambahSmartphone_nama_admin,tambahSmartphone_harga_admin])
                def_tambahSmartphone_notifikasi_admin()

            # Ubah harga
            elif pilih_kelolaSmartphone_admin == "2":
                def_ubahHarga_input_admin()
                list_smartphone_realme[ubahHarga_kode_admin][1] = ubahHarga_harga_admin
                def_ubahHarga_notifikasi_admin()

            # Hapus smartphone
            elif pilih_kelolaSmartphone_admin == "3":
                def_hapusSmartphone_input_admin()
                del list_smartphone_realme[hapusSmartphone_kode_admin]
                def_hapusSmartphone_notifikasi_admin()

            # Kembali
            elif pilih_kelolaSmartphone_admin == "4":
                break

            # Salah pilih
            else:
                input("\033[2;31mMasukkan pilihan dengan benar!\033[0;0m\nTekan ENTER untuk melanjutkan")

        except IndexError:
            input("\033[2;31mKode tidak ada\033[0;0m\nTekan ENTER untuk melanjutkan")        

# def kelola Samsung (ADMIN)
def def_Samsung_admin():
    print(tb(list_smartphone_Samsung, intfmt=",", headers=tb_headerSmartphone_admin, tablefmt="grid",showindex=True))
    while True:
        try:
            def_header()
            print(tb(list_smartphone_Samsung, intfmt=",", headers=tb_headerSmartphone_admin, tablefmt="grid",showindex=True))
            def_kelolaSmartphone_admin()

            # Tambah smartphone
            if pilih_kelolaSmartphone_admin == "1":
                def_tambahSmartphone_input_admin()
                list_smartphone_Samsung.append([tambahSmartphone_nama_admin,tambahSmartphone_harga_admin])
                def_tambahSmartphone_notifikasi_admin()

            # Ubah harga
            elif pilih_kelolaSmartphone_admin == "2":
                def_ubahHarga_input_admin()
                list_smartphone_Samsung[ubahHarga_kode_admin][1] = ubahHarga_harga_admin
                def_ubahHarga_notifikasi_admin()

            # Hapus smartphone
            elif pilih_kelolaSmartphone_admin == "3":
                def_hapusSmartphone_input_admin()
                del list_smartphone_Samsung[hapusSmartphone_kode_admin]
                def_hapusSmartphone_notifikasi_admin()

            # Kembali
            elif pilih_kelolaSmartphone_admin == "4":
                break

            # Salah pilih
            else:
                input("\033[2;31mMasukkan pilihan dengan benar!\033[0;0m\nTekan ENTER untuk melanjutkan")

        except IndexError:
            input("\033[2;31mKode tidak ada\033[0;0m\nTekan ENTER untuk melanjutkan")        

# def kelola vivo (ADMIN)
def def_vivo_admin():
    print(tb(list_smartphone_vivo, intfmt=",", headers=tb_headerSmartphone_admin, tablefmt="grid",showindex=True))
    while True:
        try:
            def_header()
            print(tb(list_smartphone_vivo, intfmt=",", headers=tb_headerSmartphone_admin, tablefmt="grid",showindex=True))
            def_kelolaSmartphone_admin()

            # Tambah smartphone
            if pilih_kelolaSmartphone_admin == "1":
                def_tambahSmartphone_input_admin()
                list_smartphone_vivo.append([tambahSmartphone_nama_admin,tambahSmartphone_harga_admin])
                def_tambahSmartphone_notifikasi_admin()

            # Ubah harga
            elif pilih_kelolaSmartphone_admin == "2":
                def_ubahHarga_input_admin()
                list_smartphone_vivo[ubahHarga_kode_admin][1] = ubahHarga_harga_admin
                def_ubahHarga_notifikasi_admin()

            # Hapus smartphone
            elif pilih_kelolaSmartphone_admin == "3":
                def_hapusSmartphone_input_admin()
                del list_smartphone_vivo[hapusSmartphone_kode_admin]
                def_hapusSmartphone_notifikasi_admin()

            # Kembali
            elif pilih_kelolaSmartphone_admin == "4":
                break

            # Salah pilih
            else:
                input("\033[2;31mMasukkan pilihan dengan benar!\033[0;0m\nTekan ENTER untuk melanjutkan")

        except IndexError:
            input("\033[2;31mKode tidak ada\033[0;0m\nTekan ENTER untuk melanjutkan")        

# def kelola Xiaomi (ADMIN)
def def_Xiaomi_admin():
    print(tb(list_smartphone_Xiaomi, intfmt=",", headers=tb_headerSmartphone_admin, tablefmt="grid",showindex=True))
    while True:
        try:    
            def_header()
            print(tb(list_smartphone_Xiaomi, intfmt=",", headers=tb_headerSmartphone_admin, tablefmt="grid",showindex=True))
            def_kelolaSmartphone_admin()

            # Tambah smartphone
            if pilih_kelolaSmartphone_admin == "1":
                def_tambahSmartphone_input_admin()
                list_smartphone_Xiaomi.append([tambahSmartphone_nama_admin,tambahSmartphone_harga_admin])
                def_tambahSmartphone_notifikasi_admin()

            # Ubah harga
            elif pilih_kelolaSmartphone_admin == "2":
                def_ubahHarga_input_admin()
                list_smartphone_Xiaomi[ubahHarga_kode_admin][1] = ubahHarga_harga_admin
                def_ubahHarga_notifikasi_admin()

            # Hapus smartphone
            elif pilih_kelolaSmartphone_admin == "3":
                def_hapusSmartphone_input_admin()
                del list_smartphone_Xiaomi[hapusSmartphone_kode_admin]
                def_hapusSmartphone_notifikasi_admin()

            # Kembali
            elif pilih_kelolaSmartphone_admin == "4":
                break

            # Salah pilih
            else:
                input("\033[2;31mMasukkan pilihan dengan benar!\033[0;0m\nTekan ENTER untuk melanjutkan")

        except IndexError:
            input("\033[2;31mKode tidak ada\033[0;0m\nTekan ENTER untuk melanjutkan")        

# def menu smartphone (ADMIN)
def def_menuSmartphone_admin():
    while True:
        def_header()
        print(tb([['''\033[1mSMARTPHONE\033[0;0m\n1. ASUS\n2. HUAWEI\n3. iPhone\n4. OPPO\n5. realme\n6. Samsung\n7. vivo\n8. Xiaomi\n9. Kembali''']], tablefmt="grid"))

        pilih_menuSmartphone_admin = input("Masukkan pilihan: ")
        
        # ASUS
        if pilih_menuSmartphone_admin == "1":
            def_ASUS_admin()
            
        # HUAWEI
        elif pilih_menuSmartphone_admin == "2":
            def_HUAWEI_admin()

        # iPhone
        elif pilih_menuSmartphone_admin == "3":
            def_iPhone_admin()

        # OPPO
        elif pilih_menuSmartphone_admin == "4":
            def_OPPO_admin()

        # realme
        elif pilih_menuSmartphone_admin == "5":
            def_realme_admin()

        # Samsung
        elif pilih_menuSmartphone_admin == "6":
            def_Samsung_admin()

        # vivo
        elif pilih_menuSmartphone_admin == "7":
            def_vivo_admin()

        # Xiaomi
        elif pilih_menuSmartphone_admin == "8":
            def_Xiaomi_admin()

        # Kembali ke menu
        elif pilih_menuSmartphone_admin == "9":
            break

        # Salah pilih
        else:
            def_header()
            print(tb([['''\033[1mSMARTPHONE\033[0;0m\n1. ASUS\n2. HUAWEI\n3. iPhone\n4. OPPO\n5. realme\n6. Samsung\n7. vivo\n8. Xiaomi\n9. Kembali''']], tablefmt="grid"))
            print(f"Masukkan pilihan: {pilih_menuSmartphone_admin}")
            input("\033[2;31mMasukkan pilihan dengan benar!\033[0;0m\nTekan ENTER untuk melanjutkan")

# def edit username tamu (ADMIN)
def def_editUsernameTamu_admin():
    while True:
        try: 
            def_header()
            print(tb(list_akunTamu, headers=["Kode", "Username", "Password"], showindex=True, tablefmt="grid"))
            print(tb([["\033[1mGANTI USERNAME\033[0;0m"]], tablefmt="grid"))

            editUsernameTamu_kode_admin = int(input("Masukkan kode: "))
            editUsernameTamu_username_admin = input("Masukkan username baru: ")

            list_akunTamu[editUsernameTamu_kode_admin][0] = editUsernameTamu_username_admin

            def_header()
            print(tb([["\033[1mGANTI USERNAME\033[0;0m"]], tablefmt="grid"))
            print("Tunggu sebentar...")
            time.sleep(5)
            
            def_header()
            print(tb([["\033[1mGANTI USERNAME\033[0;0m"]],tablefmt="grid"))
            input("Username telah diganti\nTekan ENTER untuk kembal")

            break

        except ValueError:
            input("\033[2;31mMasukkan angka dengan benar!\033[0;0m\nTekan ENTER untuk melanjutkan")

        except IndexError:
            input("\033[2;31mMasukkan angka dengan benar!\033[0;0m\nTekan ENTER untuk melanjutkan")     

#def edit password tamu (ADMIN)
def def_editPasswordTamu_admin():
    while True:
        try: 
            def_header()
            print(tb(list_akunTamu, headers=["Kode", "Username", "Password"], showindex=True, tablefmt="grid"))
            print(tb([["\033[1mGANTI PASSWORD\033[0;0m"]], tablefmt="grid"))

            editPasswordTamu_kode_admin = int(input("Masukkan kode: "))
            editPasswordTamu_password_admin = input("Masukkan password baru: ")

            list_akunTamu[editPasswordTamu_kode_admin][0] = editPasswordTamu_password_admin
            
            def_header()
            print(tb([["\033[1mGANTI PASSWORD\033[0;0m"]], tablefmt="grid"))
            print("Tunggu sebentar...")
            time.sleep(5)
            
            def_header()
            print(tb([["\033[1mGANTI PASSWORD\033[0;0m"]],tablefmt="grid"))
            input("Password telah diganti\nTekan ENTER untuk kembali")

            break

        except ValueError:
            input("\033[2;31mMasukkan angka dengan benar!\033[0;0m\nTekan ENTER untuk melanjutkan")     

        except IndexError:
            input("\033[2;31mMasukkan angka dengan benar!\033[0;0m\nTekan ENTER untuk melanjutkan")    

# def edit akun tamu (ADMIN)
def def_editAkunTamu_admin():
    while True:
        def_header()
        print(tb(list_akunTamu, headers=["Kode", "Username", "Password"], showindex=True, tablefmt="grid"))
        print(tb([["\033[1mEDIT AKUN\033[0;0m\n1. Username\n2. Password\n3. Kembali"]], tablefmt="grid"))

        pilih_editAkunTamu_admin = input("Masukkan pilihan: ")

        # Ganti username
        if pilih_editAkunTamu_admin == "1":
            def_editUsernameTamu_admin()
        
        # Ganti password
        elif pilih_editAkunTamu_admin == "2":
            def_editPasswordTamu_admin()
            
        elif pilih_editAkunTamu_admin == "3":
            break

        else:
            input("\033[2;31mMasukkan angka dengan benar!\033[0;0m\nTekan ENTER untuk melanjutkan")   

# def hapus akun tamu (ADMIN)
def def_hapusAkunTamu_admin():
    while True:
        try:
            def_header()
            print(tb(list_akunTamu, headers=["Kode", "Username", "Password"], showindex=True, tablefmt="grid"))
            print(tb([["\033[1mHAPUS AKUN\033[0;0m"]], tablefmt="grid"))

            hapusAkunTamu_kode_admin = int(input("Masukkan kode: "))

            del list_akunTamu[hapusAkunTamu_kode_admin]

            def_header()
            print(tb([["\033[1mHAPUS AKUN\033[0;0m"]], tablefmt="grid"))
            print("Tunggu sebentar...")
            time.sleep(5)
            
            def_header()
            print(tb([["\033[1mHAPUS AKUN\033[0;0m"]],tablefmt="grid"))
            input("Akun telah dihapus\nTekan ENTER untuk kembali")

            break

        except ValueError: 
            input("\033[2;31mMasukkan angka dengan benar!\033[0;0m\nTekan ENTER untuk melanjutkan")   

        except IndexError:
            input("\033[2;31mKode tidak ada\033[0;0m\nTekan ENTER untuk melanjutkan")  

# def kelola akun tamu (ADMIN)
def def_kelolaAkunTamu_admin():
    while True:
        def_header()
        print(tb([["\033[1mKELOLA AKUN TAMU\033[0;0m\n1. Lihat daftar akun\n2. Registrasi\n3. Edit akun\n4. Hapus akun\n5. Kembali"]], tablefmt="grid"))

        pilih_kelolaAkunTamu_admin = input("Masukkan pilihan: ")

        # Lihat daftar akun
        if pilih_kelolaAkunTamu_admin == "1":
            def_header()
            print(tb(list_akunTamu, headers=["Username", "Password"], tablefmt="grid"))
            input("Tekan ENTER untuk kembali")

        # Registrasi
        elif pilih_kelolaAkunTamu_admin == "2":
            def_registerAkunTamu()

        # Edit akun
        elif pilih_kelolaAkunTamu_admin == "3":
            def_editAkunTamu_admin()

        # Hapus akun
        elif pilih_kelolaAkunTamu_admin == "4":
            def_hapusAkunTamu_admin()

        # Kembali
        elif pilih_kelolaAkunTamu_admin == "5":
            break

        # Salah pilih
        else:
            input("\033[2;31mMasukkan pilihan dengan benar!\033[0;0m\nTekan ENTER untuk melanjutkan")  

# def edit username admin (ADMIN)
def def_editUsernameAdmin_admin():
    while True:
        try: 
            def_header()
            print(tb(list_akunAdmin, headers=["Kode", "Username", "Password"], showindex=True, tablefmt="grid"))
            print(tb([["\033[1mGANTI USERNAME\033[0;0m"]], tablefmt="grid"))

            editUsernameAdmin_kode_admin = int(input("Masukkan kode: "))
            editUsernameAdmin_username_admin = input("Masukkan username baru: ")

            list_akunAdmin[editUsernameAdmin_kode_admin][0] = editUsernameAdmin_username_admin

            def_header()
            print(tb([["\033[1mGANTI USERNAME\033[0;0m"]], tablefmt="grid"))
            print("Tunggu sebentar...")
            time.sleep(5)
            
            def_header()
            print(tb([["\033[1mGANTI USERNAME\033[0;0m"]],tablefmt="grid"))
            input("Username telah diganti\nTekan ENTER untuk kembal")

            break

        except ValueError:
            input("\033[2;31mMasukkan angka dengan benar!\033[0;0m\nTekan ENTER untuk melanjutkan")

        except IndexError:
            input("\033[2;31mMasukkan angka dengan benar!\033[0;0m\nTekan ENTER untuk melanjutkan")     

#def edit password admin (ADMIN)
def def_editPasswordAdmin_admin():
    while True:
        try: 
            def_header()
            print(tb(list_akunAdmin, headers=["Kode", "Username", "Password"], showindex=True, tablefmt="grid"))
            print(tb([["\033[1mGANTI PASSWORD\033[0;0m"]], tablefmt="grid"))

            editPasswordAdmin_kode_admin = int(input("Masukkan kode: "))
            editPasswordAdmin_password_admin = input("Masukkan password baru: ")

            list_akunTamu[editPasswordAdmin_kode_admin][0] = editPasswordAdmin_password_admin
            
            def_header()
            print(tb([["\033[1mGANTI PASSWORD\033[0;0m"]], tablefmt="grid"))
            print("Tunggu sebentar...")
            time.sleep(5)
            
            def_header()
            print(tb([["\033[1mGANTI PASSWORD\033[0;0m"]],tablefmt="grid"))
            input("Password telah diganti\nTekan ENTER untuk kembali")

            break

        except ValueError:
            input("\033[2;31mMasukkan angka dengan benar!\033[0;0m\nTekan ENTER untuk melanjutkan")     

        except IndexError:
            input("\033[2;31mMasukkan angka dengan benar!\033[0;0m\nTekan ENTER untuk melanjutkan")    

# def edit akun admin (ADMIN)
def def_editAkunAdmin_admin():
    while True:
        def_header()
        print(tb(list_akunAdmin, headers=["Kode", "Username", "Password"], showindex=True, tablefmt="grid"))
        print(tb([["\033[1mEDIT AKUN\033[0;0m\n1. Username\n2. Password\n3. Kembali"]], tablefmt="grid"))

        pilih_editAkunAdmin_admin = input("Masukkan pilihan: ")

        # Ganti username
        if pilih_editAkunAdmin_admin == "1":
            def_editUsernameAdmin_admin()
        
        # Ganti password
        elif pilih_editAkunAdmin_admin == "2":
            def_editPasswordAdmin_admin()
            
        elif pilih_editAkunAdmin_admin == "3":
            break

# def hapus akun tamu (ADMIN)
def def_hapusAkunAdmin_admin():
    while True:
        try:
            def_header()
            print(tb(list_akunAdmin, headers=["Kode", "Username", "Password"], showindex=True, tablefmt="grid"))
            print(tb([["\033[1mHAPUS AKUN\033[0;0m"]], tablefmt="grid"))

            hapusAkunAdmin_kode_admin = int(input("Masukkan kode: "))

            del list_akunAdmin[hapusAkunAdmin_kode_admin]

            def_header()
            print(tb([["\033[1mHAPUS AKUN\033[0;0m"]], tablefmt="grid"))
            print("Tunggu sebentar...")
            time.sleep(5)
            
            def_header()
            print(tb([["\033[1mHAPUS AKUN\033[0;0m"]],tablefmt="grid"))
            input("Akun telah dihapus\nTekan ENTER untuk kembali")

            break

        except ValueError: 
            input("\033[2;31mMasukkan angka dengan benar!\033[0;0m\nTekan ENTER untuk melanjutkan")   

        except IndexError:
            input("\033[2;31mKode tidak ada\033[0;0m\nTekan ENTER untuk melanjutkan")  

# def registrasi akun admin (ADMIN)
def def_registerAkunAdmin_admin():
   while True:
        def_header()
        print(tb([["\033[1mREGISTER AKUN ADMIN\033[0;0m"]], tablefmt="grid"))

        # input registrasi akun admin
        registerAkunAdmin_username = input("Username: ")

        # Menghindari pemilihan username yang sama
        for i in range(len(list_akunAdmin)):
            if registerAkunAdmin_username == (list_akunAdmin[i][0]):
                input("\033[2;31mUsername sudah digunakan\033[0;0m\nTekan ENTER untuk melanjutkan")
                break

        # Lanjut input registrasi akun tamu
        else:
            registerAkunAdmin_password = input("Password: ")
            list_akunAdmin.append([registerAkunAdmin_username,registerAkunAdmin_password])

            def_header()
            print(tb([["\033[1mREGISTER AKUN ADMIN\033[0;0m"]], tablefmt="grid"))
            print("Tunggu sebentar...")
            time.sleep(5)

            def_header()
            print(tb([["\033[1mREGISTER AKUN ADMIN\033[0;0m"]], tablefmt="grid"))
            input("Selamat, akun Anda berhasil dibuat\nTekan ENTER untuk kembali")
            break

# def kelola akun admin (ADMIN)
def def_kelolaAkunAdmin_admin():
    while True:
        def_header()
        print(tb([["\033[1mKELOLA AKUN ADMIN\033[0;0m\n1. Lihat daftar akun\n2. Registrasi\n3. Edit akun\n4. Hapus akun\n5. Kembali"]], tablefmt="grid"))

        pilih_kelolaAkunAdmin_admin = input("Masukkan pilihan: ")

        # Lihat daftar akun
        if pilih_kelolaAkunAdmin_admin == "1":
            def_header()
            print(tb(list_akunAdmin, headers=["Username", "Password"], tablefmt="grid"))
            input("Tekan ENTER untuk kembali")

        # Registrasi
        elif pilih_kelolaAkunAdmin_admin == "2":
            def_registerAkunAdmin_admin()

        # Edit akun
        elif pilih_kelolaAkunAdmin_admin == "3":
            def_editAkunAdmin_admin()

        # Hapus akun
        elif pilih_kelolaAkunAdmin_admin == "4":
            def_hapusAkunAdmin_admin()

        # Kembali
        elif pilih_kelolaAkunAdmin_admin == "5":
            break

        # Salah pilih
        else:
            input("\033[2;31mMasukkan pilihan dengan benar!\033[0;0m\nTekan ENTER untuk melanjutkan")  

# def menu akun (ADMIN)
def def_menuKelolaAkun_admin():
    while True:
        def_header()
        print(tb([["\033[1mKELOLA AKUN\033[0;0m\n1. Akun user\n2. Akun admin\n3. Kembali"]], tablefmt="grid"))

        pilih_menuKelolaAkun = input("Masukkan pilihan: ")

        # Kelola akun tamu
        if pilih_menuKelolaAkun == "1":
            def_kelolaAkunTamu_admin()

        #kelola akun admin
        elif pilih_menuKelolaAkun == "2":
            def_kelolaAkunAdmin_admin()

        # Kembali ke menu
        elif pilih_menuKelolaAkun == "3":
            break

        # Salah pilih
        else:
            input("\033[2;31mMasukkan pilihan dengan benar!\033[0;0m\nTekan ENTER untuk melanjutkan")   

# # # # # # # # #
#               #
#  SURYA PHONE  # 
#               #
# # # # # # # # # ###############################################################################

# SURYA PHONE
while True:

    # Pemilihan akun
    def_header()
    print(tb([["\033[1mAKUN\033[0;0m\n1. Tamu\n2. Admin"]], tablefmt="grid"))
    pilih_jenisAkun = input("Masukkan pilihan: ")

    # Akun tamu
    if pilih_jenisAkun ==  "1":

        while True:

            def_header()
            print(tb([["\033[1mAKUN TAMU\033[0;0m\n1. Register\n2. Log in\n3. Kembali"]], tablefmt="grid"))
            
            pilih_akunTamu = input("Masukkan pilihan: ")

            # Registrasi akun tamu
            if pilih_akunTamu == "1":
                def_registerAkunTamu()

            # Log in akun tamu
            elif pilih_akunTamu == "2":
                def_loginAkunTamu_tamu()

                # Agar benar-benar ter-log out (2/2) (TAMU)
                try:
                    if pilih_konfirmasiLogout == "Y" or pilih_konfirmasiLogout == "y":
                        break
                except NameError:
                    continue

            # Kembali ke menu pemillihan akun
            elif pilih_akunTamu == "3":
                break

            # Salah pilih
            else:
                input("\033[2;31mMasukkan pilihan dengan benar!\033[0;0m\nTekan ENTER untuk melanjutkan")

    # Akun admin
    elif pilih_jenisAkun == "2":
        def_loginAkun_admin()

    # Salah pilih
    else:
        input("\033[2;31mMasukkan pilihan dengan benar!\033[0;0m\nTekan ENTER untuk melanjutkan")   