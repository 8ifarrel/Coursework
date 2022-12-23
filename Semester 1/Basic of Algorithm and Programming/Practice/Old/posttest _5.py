# Import OS module
import os

# Import math
import math
from math import sqrt

# Install dan import Tabulate   
os.system("pip install tabulate")
from tabulate import tabulate

# Install dan import module PWInput
os.system('pip install pwinput')
import pwinput

# def header
def header():
    os.system("cls")
    tabel_header = [["PostTest5App"]]
    print(tabulate(tabel_header, tablefmt = "heavy_outline"))

sisa_login = 0
# def salah log in
def salah_login(sisa_login):
    if sisa_login == 3:
       print(" Anda dikeluarkan dari program karena tiga kali salah log in")
    else: 
        input(" tekan ENTER untuk melanjutkan")

# def pembulatan untuk 0.5 atau di atasnya
def pembulatan_def(hasil):
    pembulatan = int(hasil) + 0.5
    if hasil >= pembulatan:
        hasilPembulatan = int(hasil) + 1
        print(" \u2022 Luas =", "{:.4}".format(hasil))
        print(" \u2022 Luas dibulatkan =", hasilPembulatan)
    else:
        print(" \u2022 Luas =", "{:.4}".format(hasil))
    input(" Tekan ENTER untuk kembali ke menu")
    os.system('cls')

# Halaman log in
while sisa_login < 3:
    header()
    username = input(" Username: ")
    password = pwinput.pwinput(prompt=" Password: ", mask="\u2022")

    # Log in benar
    if username == "bebek" and password == "ayam":

        # Program luas dan volume
                while True:
                    try:
                        header()
                        pt4 = [[" LUAS DAN VOLUME"], [" 1. Mencari luas"], [" 2. Mencari volume"], [" 3. Log out"]]
                        print(tabulate(pt4, tablefmt="rounded_outline"))
                        menu_pt4 = int(input(" Masukkkan pilihan: "))

                        # Luas
                        if menu_pt4 == 1:
                            while True:
                                try:
                                    header()
                                    menu_luas = [[" MENCARI LUAS"], [" 1. Persegi"], [" 2. Persegi panjang"], [" 3. Lingkaran"], [" 4. Segitiga"], [" 5. Trapesium"]]
                                    print(tabulate(menu_luas, tablefmt="rounded_outline"))
                                    menuLuas = int(input(" Masukkan pilihan: "))

                                    # Luas  Persegi
                                    if menuLuas == 1:
                                        while True:
                                            try:
                                                header()
                                                menu_persegi = [[" LUAS PERSEGI"], [" 1. Jika diketahui sisi"], [" 2. Jika diketahui diagonal"]]
                                                print(tabulate(menu_persegi, tablefmt="rounded_outline"))
                                                menuPersegi = int(input(" Masukkan pilihan: "))

                                                # Persegi jika diketahui sisi
                                                if menuPersegi == 1:
                                                    while True:
                                                        try:
                                                            header()
                                                            print(" LUAS PERSEGI JIKA DIKETAHUI SISI")
                                                            sisiPersegi = float(input(" \u2022 Sisi = "))
                                                            hasil = sisiPersegi ** 2
                                                            pembulatan_def(hasil)
                                                            break
                                                        except ValueError:
                                                            print("\033[2;31m Masukkan angka dengan benar!\033[0;0m")
                                                            input(" Tekan ENTER untuk melanjutkan")
                                                    break
                                                # PERSEGI JIKA DIKETAHUI DIAGONAL
                                                elif menuPersegi == 2:
                                                    while True:
                                                        try:
                                                            header()
                                                            print(" LUAS PERSEGI JIKA DIKETAHUI DIAGONAL")
                                                            diagonalPersegi = float(input(" \u2022 Diagonal = "))
                                                            hasil = (sqrt((diagonalPersegi ** 2) / 2)) ** 2
                                                            pembulatan_def(hasil)
                                                            break
                                                        except ValueError:
                                                            print("\033[2;31m Masukkan angka dengan benar!\033[0;0m")
                                                            input(" Tekan ENTER untuk melanjutkan")
                                                    break
                                                else:
                                                    print("\033[2;31m Masukkan pilihan dengan benar!\033[0;0m")
                                                    input(" Tekan ENTER untuk melanjutkan")       
                                            except ValueError:
                                                print("\033[2;31m Masukkan pilihan dengan benar!\033[0;0m")
                                                input(" Tekan ENTER untuk melanjutkan")
                                        break

                                    # Luas persegi panjang
                                    elif menuLuas == 2:
                                        while True:
                                            try:
                                                header()
                                                menu_persegipanjang = [[" LUAS PERSEGI PANJANG"], [" 1. Jika diketahui panjang dan lebar"], [" 2. Jika diketahui salah satu sisi dan diagonal"]]
                                                print(tabulate(menu_persegipanjang, tablefmt="rounded_outline"))
                                                menuPersegiPanjang = int(input(" Masukkan pilihan: "))

                                                # Persegi panjang jika diketahui panjang dan lebar
                                                if menuPersegiPanjang == 1:
                                                    while True:
                                                        try:
                                                            header()
                                                            print(" LUAS PERSEGI PANJANG JIKA DIKETAHUI PANJANG DAN LEBAR")
                                                            panjangPersegiPanjang = float(input(" \u2022 Panjang = "))
                                                            lebarPersegiPanjang = float(input(" \u2022 Lebar = "))
                                                            hasil = panjangPersegiPanjang * lebarPersegiPanjang
                                                            pembulatan_def(hasil)
                                                            break
                                                        except ValueError:
                                                            print("\033[2;31m Masukkan angka dengan benar!\033[0;0m")
                                                            input(" Tekan ENTER untuk melanjutkan")
                                                    break

                                                # Persegi panjang jika diketahui salah satu sisi dan diagonal
                                                elif menuPersegiPanjang == 2:
                                                    while True:
                                                        try:
                                                            while True:
                                                                header()
                                                                print(" LUAS PERSEGI PANJANG JIKA DIKETAHUI SALAH SATU SISI DAN DIAGONAL")
                                                                diagonalPersegiPanjang = float(input(" \u2022 Diagonal = "))
                                                                sisiPersegiPanjang = float(input(" \u2022 Sisi = "))
                                                                if diagonalPersegiPanjang <= sisiPersegiPanjang:
                                                                    print("\033[2;31m Diagonal tidak boleh lebih kecil atau sama dengan sisi\033[0;0m")
                                                                    input(" Tekan ENTER untuk melanjutkan")
                                                                else:
                                                                    hasil = sisiPersegiPanjang * sqrt((diagonalPersegiPanjang**2)-(sisiPersegiPanjang**2))
                                                                    pembulatan_def(hasil)
                                                                    break
                                                            break
                                                        except ValueError:
                                                            print("\033[2;31m Masukkan angka dengan benar!\033[0;0m")
                                                            input(" Tekan ENTER untuk melanjutkan")
                                                    break
                                                else:
                                                    print("\033[2;31m Masukkan pilihan dengan benar!\033[0;0m")
                                                    input(" Tekan ENTER untuk melanjutkan")
                                            except ValueError:
                                                print("\033[2;31m Masukkan pilihan dengan benar!\033[0;0m")
                                                input(" Tekan ENTER untuk melanjutkan")
                                        break

                                    # Luas lingkaran
                                    elif menuLuas == 3:
                                        while True:
                                            try:
                                                header()
                                                print(" LUAS LINGKARAN")
                                                jariJariLingkaran = float(input(" \u2022 Jari-jari = "))
                                                hasil = math.pi * jariJariLingkaran ** 2
                                                pembulatan_def(hasil)
                                                break
                                            except ValueError:
                                                print("\033[2;31m Masukkan angka dengan benar!\033[0;0m")
                                                input(" Tekan ENTER untuk melanjutkan")
                                        break    
            
                                    # Luas segitigaa
                                    elif menuLuas == 4:
                                        while True:
                                            try:
                                                header()
                                                menu_segitiga = [[" LUAS SEGITIGA"], [" 1. Jika diketahui alas dan tinggi"], [" 2. Jika diketahui ketiga sisi"]]
                                                print(tabulate(menu_segitiga, tablefmt="rounded_outline"))
                                                menuSegitiga = int(input(" Masukkan pilihan: "))

                                                # Segitiga jika diketahui alas dan tinggi
                                                if menuSegitiga == 1:
                                                    os.system('cls')
                                                    while True:
                                                        try:
                                                            header()
                                                            print(" LUAS SEGITIGA JIKA DIKETAHUI ALAS DAN TINGGI")
                                                            alasSegitiga = float(input(" \u2022 Alas = "))
                                                            tinggiSegitiga = float(input(" \u2022 Tinggi = "))
                                                            hasil = alasSegitiga * tinggiSegitiga / 2
                                                            pembulatan_def(hasil)
                                                            break
                                                        except ValueError:
                                                            print("\033[2;31m Masukkan angka dengan benar!\033[0;0m")
                                                            input(" Tekan ENTER untuk melanjutkan")
                                                    break

                                                # Segitiga jika diketahui ketiga sisi
                                                elif menuSegitiga == 2:
                                                    os.system('cls')
                                                    while True:
                                                        try:
                                                            while True:
                                                                header()
                                                                print(" LUAS SEGITIGA JIKA DIKETAHUI KETIGA SISI")
                                                                sisiSegitiga_a = float(input(" \u2022 Sisi a = "))
                                                                sisiSegitiga_b = float(input(" \u2022 Sisi b = "))
                                                                sisiSegitiga_c = float(input(" \u2022 Sisi c = "))
                                                                if sisiSegitiga_a + sisiSegitiga_b <= sisiSegitiga_c or sisiSegitiga_a + sisiSegitiga_c <= sisiSegitiga_b or sisiSegitiga_b + sisiSegitiga_c <= sisiSegitiga_a:
                                                                    print("\033[2;31m Sisi terpanjang tidak boleh lebih besar atau sama dengan jumlah dari dua sisi lainnya\033[0;0m")
                                                                    input(" Tekan ENTER untuk melanjutkan")
                                                                else:
                                                                    semiPerimeter = (sisiSegitiga_a + sisiSegitiga_b + sisiSegitiga_c) / 2
                                                                    hasil = sqrt(semiPerimeter * (semiPerimeter - sisiSegitiga_a) * (semiPerimeter - sisiSegitiga_b) * (semiPerimeter - sisiSegitiga_c))
                                                                    header()
                                                                    break
                                                            break
                                                        except ValueError:
                                                            print("\033[2;31m Masukkan angka dengan benar!\033[0;0m")
                                                            input(" Tekan ENTER untuk melanjutkan")
                                                    break        
                                                else:
                                                    print("\033[2;31m Masukkan pilihan dengan benar!\033[0;0m")
                                                    input(" Tekan ENTER untuk melanjutkan")  
                                            except ValueError:
                                                print("\033[2;31m Masukkan pilihan dengan benar!\033[0;0m")
                                                input(" Tekan ENTER untuk melanjutkan")
                                        break        

                                    # Luas trapesium
                                    elif menuLuas == 5:
                                        while True:
                                            try:
                                                os.system('cls')
                                                header()
                                                menu_trapesium = [[" LUAS TRAPESIUM"], [" 1. Jika diketahui sisi atas, sisi bawah, dan tinggi"], [" 2. Jika diketahui sisi atas, sisi bawah, dan sisi miring"]]
                                                print(tabulate(menu_trapesium, tablefmt="rounded_outline"))
                                                menuTrapesium = int(input(" Masukkan pilihan: "))

                                                # Trapesium jika diketahui sisi atas, sisi bawah, dan tinggi
                                                if menuTrapesium == 1:
                                                    os.system('cls')
                                                    while True:
                                                        try:
                                                            header()
                                                            print(" LUAS TRAPESIUM JIKA DIKETAHUI SISI ATAS< SISI BAWAH, DAN TINGGI")
                                                            sisiAtasTrapesium1 = float(input(" \u2022 Sisi atas = "))
                                                            sisiBawahTrapesium1 = float(input(" \u2022 Sisi bawah = "))
                                                            tinggiTrapesium1 = float(input(" \u2022 Tinggi = "))
                                                            hasil = (sisiAtasTrapesium1 + sisiBawahTrapesium1) * tinggiTrapesium1 / 2
                                                            pembulatan_def(hasil)
                                                            break
                                                        except ValueError:
                                                            print("\033[2;31m Masukkan angka dengan benar!\033[0;0m")
                                                            input(" Tekan ENTER untuk melanjutkan")
                                                    break

                                                # Trapesium jika diketahui sisi atas, sisi bawah, dan sisi miring
                                                elif menuTrapesium == 2:
                                                    while True:
                                                        try:
                                                            while True:
                                                                try:
                                                                    header()
                                                                    menu_trapesium2 = [[" LUAS TRAPESIUM JIKA DIKETAHUI SISI ATAS, SISI BAWAH, DAN SISI MIRING"], [" 1. Trapesium sama kaki"], [" 2. Trapesium siku-siku"]]
                                                                    print(tabulate(menu_trapesium2, tablefmt="rounded_outline"))
                                                                    subMenuTrapesium = int(input(" Masukkan pilihan: "))

                                                                    # Trapesium sama kaki
                                                                    while True:
                                                                        try:
                                                                            if subMenuTrapesium == 1:
                                                                                header()
                                                                                print(" LUAS TRAPESIUM SAMA KAKI JIKA DIKETAHUI SISI ATAS, SISI BAWAH, DAN SISI MIRING")
                                                                                sisiAtasTrapesium2_1 = float(input(" \u2022 Sisi atas = "))
                                                                                sisiBawahTrapesium2_1 = float(input(" \u2022 Sisi bawah = "))
                                                                                sisiMiringTrapesium2_1 = float(input(" \u2022 Sisi miring = "))
                                                                                hasil = sqrt(sisiMiringTrapesium2_1**2 - (abs(sisiAtasTrapesium2_1 - sisiBawahTrapesium2_1) / 2)**2)
                                                                                pembulatan_def(hasil)
                                                                            break
                                                                        except ValueError:
                                                                            print("\033[2;31m Masukkan angka dengan benar!\033[0;0m")
                                                                            input(" Tekan ENTER untuk melanjutkan")

                                                                    # Trapesium siku-siku
                                                                    while True:
                                                                        try:
                                                                            if subMenuTrapesium == 2:
                                                                                header()
                                                                                print(" LUAS TRAPESIUM SIKU-SIKU JIKA DIKETAHUI SISI ATAS, SISI BAWAH, DAN SISI MIRING")
                                                                                sisiAtasTrapesium2_2 = float(input(" \u2022 Sisi atas = "))
                                                                                sisiBawahTrapesium2_2 = float(input(" \u2022 Sisi bawah = "))
                                                                                sisiMiringTrapesium2_2 = float(input(" \u2022 Sisi miring = "))
                                                                                hasil = sqrt(sisiMiringTrapesium2_2**2 - (abs(sisiAtasTrapesium2_2 - sisiBawahTrapesium2_2))**2)
                                                                                pembulatan_def(hasil)
                                                                            break
                                                                        except ValueError:
                                                                            print("\033[2;31m Masukkan angka dengan benar!\033[0;0m")
                                                                            input(" Tekan ENTER untuk melanjutkan")
                                                                    break
                                                                except ValueError:
                                                                    print("\033[2;31m Masukkan pilihan dengan benar!\033[0;0m")
                                                                    input(" Tekan ENTER untuk melanjutkan")
                                                            break
                                                        except ValueError:
                                                            print("\033[2;31m Masukkan angka dengan benar!\033[0;0m")
                                                            input(" Tekan ENTER untuk melanjutkan")
                                                    break
                                                else:
                                                    print("\033[2;31m Masukkan pilihan dengan benar!\033[0;0m")
                                                    input(" Tekan ENTER untuk melanjutkan")
                                            except ValueError:
                                                print("\033[2;31m Masukkan pilihan dengan benar!\033[0;0m")
                                                input(" Tekan ENTER untuk melanjutkan")
                                        break            
                                    else:
                                        print("\033[2;31m Masukkan pilihan dengan benar!\033[0;0m")
                                        input(" Tekan ENTER untuk melanjutkan")
                                except ValueError:
                                    print("\033[2;31m Masukkan pilihan dengan benar!\033[0;0m")
                                    input(" Tekan ENTER untuk melanjutkan")

                        # Volume
                        elif menu_pt4 == 2:
                            while True:
                                try:
                                    header()
                                    menu_volume = [[" MENCARI VOLUME"], [" 1. Kubus"], [" 2. Balok"], [" 3. Bola"], [" 4. Kerucut"]]
                                    print(tabulate(menu_volume, tablefmt="rounded_outline"))
                                    menuVolume = int(input(" Masukkan pilihan: "))

                                    # Volume kubus
                                    if menuVolume == 1:
                                        while True:
                                            try:
                                                header()
                                                print(" VOLUME KUBUS")
                                                sisiKubus = float(input(" \u2022 Sisi = "))
                                                hasil = sisiKubus ** 3
                                                pembulatan_def(hasil)
                                                break
                                            except ValueError:
                                                print("\033[2;31m Masukkan angka dengan benar!\033[0;0m")
                                                input(" Tekan ENTER untuk melanjutkan")
                                        break

                                    # Volume balok
                                    elif menuVolume == 2:
                                        while True:
                                            try:
                                                header()
                                                print(" VOLUME BALOK")
                                                panjangBalok = float(input(" \u2022 Panjang = "))
                                                lebarBalok = float(input(" \u2022 Lebar = "))
                                                tinggiBalok = float(input(" \u2022 Tinggi = "))
                                                hasil = panjangBalok * lebarBalok * tinggiBalok
                                                pembulatan_def(hasil)
                                                break
                                            except ValueError:
                                                print("\033[2;31m Masukkan angka dengan benar!\033[0;0m")
                                                input(" Tekan ENTER untuk melanjutkan")
                                                os.system('cls')
                                        break

                                    # Volume bola
                                    elif menuVolume == 3:
                                        while True:
                                            try:
                                                header()
                                                print(" VOLUME BOLA")
                                                jariJariBola = float(input(" \u2022 Jari-jari = "))
                                                hasil = math.pi * jariJariBola ** 3 * 4 / 3
                                                pembulatan_def(hasil)
                                                break
                                            except ValueError:
                                                print("\033[2;31m Masukkan angka dengan benar!\033[0;0m")
                                                input(" Tekan ENTER untuk melanjutkan")
                                        break

                                    # Volume kerucut
                                    elif menuVolume == 4:
                                        while True:
                                            try:
                                                header()
                                                print(" VOLUME KERUCUT")
                                                jariJariKerucut = float(input(" \u2022 Jari-jari = "))
                                                tinggiKerucut = float(input(" \u2022 Tinggi = "))
                                                hasil = tinggiKerucut * math.pi * jariJariKerucut ** 2 / 3
                                                pembulatan_def(hasil)
                                                break
                                            except ValueError:
                                                print("\033[2;31m Masukkan angka dengan benar!\033[0;0m")
                                                input(" Tekan ENTER untuk melanjutkan")
                                        break
                                    else:
                                        print("\033[2;31m Masukkan pilihan dengan benar!\033[0;0m")
                                        input(" Tekan ENTER untuk melanjutkan")

                                except ValueError:
                                    print("\033[2;31m Masukkan pilihan dengan benar!\033[0;0m")
                                    input(" Tekan ENTER untuk melanjutkan")

                        # Log out
                        elif menu_pt4 == 3:
                            while True:
                                header()
                                print(" Anda yakin ingin log out?")
                                logout = input(" [Y/N] ")
                                if logout == "Y" or logout == "y":
                                    os.system('cls')
                                    break
                                elif logout == "N" or logout == "n":
                                    os.system('cls')
                                    break
                                else:
                                    print("\033[2;31m Masukkan pilihan dengan benar!\033[0;0m")
                                    input(" Tekan ENTER untuk melanjutkan")
                            if logout == "Y" or logout == "y":
                                break

                        # Salah pilih 
                        else:
                            print("\033[2;31m Masukkan pilihan dengan benar!\033[0;0m")
                            input(" Tekan ENTER untuk melanjutkan")    
          
                    except ValueError:
                        print("\033[2;31m Masukkan pilihan dengan benar!\033[0;0m")
                        input(" Tekan ENTER untuk melanjutkan")
        
    # Username salah
    elif username != "bebek" and password == "ayam":
        print("\033[2;31m Username Anda salah\033[0;0m")
        sisa_login += 1
        salah_login(sisa_login)

    # Password salah
    elif username == "bebek" and password != "ayam":
        print("\033[2;31m Password Anda salah\033[0;0m")
        sisa_login += 1
        salah_login(sisa_login)

    # Username dan password salah
    else:
        print("\033[2;31m Username dan password Anda salah\033[0;0m")
        sisa_login += 1
        salah_login(sisa_login)