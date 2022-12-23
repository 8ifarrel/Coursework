# # CATATAN
# # LOGIN: 1. Username: farrel_praktikan
# #        2. Password: pengenSekelompokSamaSirkel
# # MENU: 1. Luas
# #           a. Persegi
# #              1. Jika diketahui sisi
# #              2. Jika diketahui diagonal
# #           b. Persegi panjang
# #              1. Jika diketahui panjang dan lebar
# #              2. Jika diketahui salah satu sisi dan diagonal
# #           c. lingkaran  
# #           d. Segitiga
# #              1. Jika diketahui alas dan tinggi
# #              2. Jika  diketahui ketiga sisi
# #           e. Trapesium
# #              1. Jika diketahui sisi atas, sisi bawah, dan tinggi
# #              2. Jika diketahui sisi atas, sisi bawah, dan sisi miring
# #                 a. Trapesium sama kaki
# #                 b. Trapesium siku-siku
# #        2. Volume
# #           a. Kubus
# #           b. Balok
# #           c. Bola
# #        3. Log out

import os
import math
from math import sqrt

# Install module pwinput biar bisa sensor password
os.system('pip install pwinput')
import pwinput

# LOG IN
while True:
    os.system('cls')
    print("╔══════════════╗")
    print("║ PostTest4App ║")
    print("╚══════════════╝")
    username = input(" Username: ")
    password = pwinput.pwinput(prompt=" Password: ", mask="\u2022")
    # LOGIN USERNAME DAN PASSWORD BENAR
    if username == "farrel_praktikan" and password == "pengenSekelompokSamaSirkel":
        os.system('cls')     
        # MENU UTAMA
        while True:
            try:
                print("╔══════════════╗")
                print("║ PostTest4App ║")
                print("╚══════════════╝")
                print(" MENU")
                print(" 1. Mencari luas")
                print(" 2. Mencari volume")
                print(" 3. Log out")
                menuUtama = int(input(" Masukkkan pilihan: "))
                # MENU LUAS
                if menuUtama == 1:
                    while True:
                        try:
                            os.system('cls')
                            print("╔══════════════╗")
                            print("║ PostTest4App ║")
                            print("╚══════════════╝")
                            print(" MENCARI LUAS")
                            print(" 1. Persegi")
                            print(" 2. Persegi panjang") 
                            print(" 3. Lingkaran")
                            print(" 4. Segitiga")
                            print(" 5. Trapesium")
                            menuLuas = int(input(" Masukkan pilihan: "))
                            # LUAS PERSEGI
                            if menuLuas == 1:
                                while True:
                                    try:
                                        os.system('cls')
                                        print("╔══════════════╗")
                                        print("║ PostTest4App ║")
                                        print("╚══════════════╝")
                                        print(" LUAS PERSEGI")
                                        print(" 1. Jika diketahui sisi")
                                        print(" 2. Jika diketahui diagonal")
                                        menuPersegi = int(input(" Masukkan pilihan: "))
                                        # PERSEGI JIKA DIKETAHUI SISI
                                        if menuPersegi == 1:
                                            os.system('cls')
                                            while True:
                                                try:
                                                    print("╔══════════════╗")
                                                    print("║ PostTest4App ║")
                                                    print("╚══════════════╝")
                                                    print(" LUAS PERSEGI JIKA DIKETAHUI SISI")
                                                    sisiPersegi = float(input(" \u2022 Sisi = "))
                                                    luasPersegi1 = sisiPersegi ** 2
                                                    pembulatan = int(luasPersegi1) + 0.5
                                                    if luasPersegi1 >= pembulatan:
                                                        hasilPembulatan = int(luasPersegi1) + 1
                                                        print(" \u2022 Luas =", "{:.4}".format(luasPersegi1))
                                                        print(" \u2022 Luas dibulatkan =", hasilPembulatan)
                                                    else:
                                                        print(" \u2022 Luas =", "{:.4}".format(luasPersegi1))
                                                    input(" Tekan ENTER untuk kembali ke menu")
                                                    os.system('cls')
                                                    break
                                                except ValueError:
                                                    print("\033[2;31m Masukkan angka dengan benar!\033[0;0m")
                                                    input(" Tekan ENTER untuk melanjutkan")
                                                    os.system('cls')
                                            break
                                        # PERSEGI JIKA DIKETAHUI DIAGONAL
                                        elif menuPersegi == 2:
                                            os.system('cls')
                                            while True:
                                                try:
                                                    print("╔══════════════╗")
                                                    print("║ PostTest4App ║")
                                                    print("╚══════════════╝")
                                                    print(" LUAS PERSEGI JIKA DIKETAHUI DIAGONAL")
                                                    diagonalPersegi = float(input(" \u2022 Diagonal = "))
                                                    luasPersegi2 = (sqrt((diagonalPersegi ** 2) / 2)) ** 2
                                                    pembulatan = int(luasPersegi2) + 0.5
                                                    if luasPersegi2 >= pembulatan:
                                                        hasilPembulatan = int(luasPersegi2) + 1
                                                        print(" \u2022 Luas =", "{:.4}".format(luasPersegi2))
                                                        print(" \u2022 Luas dibulatkan =", hasilPembulatan)
                                                    else:
                                                        print(" \u2022 Luas =", "{:.4}".format(luasPersegi2))
                                                    input(" Tekan ENTER untuk kembali ke menu")
                                                    os.system('cls')
                                                    break
                                                except ValueError:
                                                    print("\033[2;31m Masukkan angka dengan benar!\033[0;0m")
                                                    input(" Tekan ENTER untuk melanjutkan")
                                                    os.system('cls')
                                            break
                                        else:
                                            print("\033[2;31m Masukkan pilihan dengan benar!\033[0;0m")
                                            input(" Tekan ENTER untuk melanjutkan")
                                            os.system('cls')        
                                    except ValueError:
                                        print("\033[2;31m Masukkan pilihan dengan benar!\033[0;0m")
                                        input(" Tekan ENTER untuk melanjutkan")
                                        os.system('cls')
                                break
                            # LUAS PERSEGI PANJANG
                            elif menuLuas == 2:
                                while True:
                                    try:
                                        os.system('cls')
                                        print("╔══════════════╗")
                                        print("║ PostTest4App ║")
                                        print("╚══════════════╝")
                                        print(" LUAS PERSEGI PANJANG")
                                        print(" 1. Jika diketahui panjang dan lebar")
                                        print(" 2. Jika diketahui salah satu sisi dan diagonal")
                                        menuPersegiPanjang = int(input(" Masukkan pilihan: "))
                                        # PERSEGI PANJANG JIKA DIKETAHUI PANJANG DAN LEBAR
                                        if menuPersegiPanjang == 1:
                                            os.system('cls')
                                            while True:
                                                try:
                                                    print("╔══════════════╗")
                                                    print("║ PostTest4App ║")
                                                    print("╚══════════════╝")
                                                    print(" LUAS PERSEGI PANJANG JIKA DIKETAHUI PANJANG DAN LEBAR")
                                                    panjangPersegiPanjang = float(input(" \u2022 Panjang = "))
                                                    lebarPersegiPanjang = float(input(" \u2022 Lebar = "))
                                                    luasPersegiPanjang1 = panjangPersegiPanjang * lebarPersegiPanjang
                                                    pembulatan = int(luasPersegiPanjang1) + 0.5
                                                    if luasPersegiPanjang1 >= pembulatan:
                                                        hasilPembulatan = int(luasPersegiPanjang1) + 1
                                                        print(" \u2022 Luas =", "{:.4}".format(luasPersegiPanjang1))
                                                        print(" \u2022 Luas dibulatkan =", hasilPembulatan)
                                                    else:
                                                        print(" \u2022 Luas =", "{:.4}".format(luasPersegiPanjang1))
                                                    input(" Tekan ENTER untuk kembali ke menu")
                                                    os.system('cls')
                                                    break
                                                except ValueError:
                                                    print("\033[2;31m Masukkan angka dengan benar!\033[0;0m")
                                                    input(" Tekan ENTER untuk melanjutkan")
                                                    os.system('cls')
                                            break
                                        # PERSEGI PANJANG JIKA DIKETAHUI SALAH SATU SISI DAN DIAGONAL
                                        elif menuPersegiPanjang == 2:
                                            os.system('cls')
                                            while True:
                                                try:
                                                    while True:
                                                        os.system('cls')
                                                        print("╔══════════════╗")
                                                        print("║ PostTest4App ║")
                                                        print("╚══════════════╝")
                                                        print(" LUAS PERSEGI PANJANG JIKA DIKETAHUI SALAH SATU SISI DAN DIAGONAL")
                                                        diagonalPersegiPanjang = float(input(" \u2022 Diagonal = "))
                                                        sisiPersegiPanjang = float(input(" \u2022 Sisi = "))
                                                        if diagonalPersegiPanjang <= sisiPersegiPanjang:
                                                            print("\033[2;31m Diagonal tidak boleh lebih kecil atau sama dengan sisi\033[0;0m")
                                                            input(" Tekan ENTER untuk melanjutkan")
                                                        else:
                                                            luasPersegiPanjang2 = sisiPersegiPanjang * sqrt((diagonalPersegiPanjang**2)-(sisiPersegiPanjang**2))
                                                            pembulatan = int(luasPersegiPanjang2) + 0.5
                                                            if luasPersegiPanjang2 >= pembulatan:
                                                                hasilPembulatan = int(luasPersegiPanjang2) + 1
                                                                print(" \u2022 Luas =", "{:.4}".format(luasPersegiPanjang2))
                                                                print(" \u2022 Luas dibulatkan =", hasilPembulatan)
                                                            else:
                                                                print(" \u2022 Luas =", "{:.4}".format(luasPersegiPanjang2))
                                                            input(" Tekan ENTER untuk kembali ke menu")
                                                            os.system('cls')
                                                            break
                                                    break
                                                except ValueError:
                                                    print("\033[2;31m Masukkan angka dengan benar!\033[0;0m")
                                                    input(" Tekan ENTER untuk melanjutkan")
                                                    os.system('cls')
                                            break
                                        else:
                                            print("\033[2;31m Masukkan pilihan dengan benar!\033[0;0m")
                                            input(" Tekan ENTER untuk melanjutkan")
                                            os.system('cls')  
                                    except ValueError:
                                        print("\033[2;31m Masukkan pilihan dengan benar!\033[0;0m")
                                        input(" Tekan ENTER untuk melanjutkan")
                                        os.system('cls')
                                break
                            # LUAS LINGKARAN
                            elif menuLuas == 3:
                                while True:
                                    try:
                                        os.system('cls')
                                        print("╔══════════════╗")
                                        print("║ PostTest4App ║")
                                        print("╚══════════════╝")
                                        print(" LUAS LINGKARAN")
                                        jariJariLingkaran = float(input(" \u2022 Jari-jari = "))
                                        luasLingkaran = math.pi * jariJariLingkaran ** 2
                                        pembulatan = int(luasLingkaran) + 0.5
                                        if luasLingkaran >= pembulatan:
                                            hasilPembulatan = int(luasLingkaran) + 1
                                            print(" \u2022 Luas =", "{:.4}".format(luasLingkaran))
                                            print(" \u2022 Luas dibulatkan =", hasilPembulatan)
                                        else:
                                            print(" \u2022 Luas =", "{:.4}".format(luasLingkaran))
                                        input(" Tekan ENTER untuk kembali ke menu")
                                        os.system('cls')
                                        break
                                    except ValueError:
                                        print("\033[2;31m Masukkan angka dengan benar!\033[0;0m")
                                        input(" Tekan ENTER untuk melanjutkan")
                                        os.system('cls')
                                break        
                            # LUAS SEGITIGA
                            elif menuLuas == 4:
                                while True:
                                    try:
                                        os.system('cls')
                                        print("╔══════════════╗")
                                        print("║ PostTest4App ║")
                                        print("╚══════════════╝")
                                        print(" LUAS SEGITIGA")
                                        print(" 1. Jika diketahui alas dan tinggi")
                                        print(" 2. Jika diketahui ketiga sisi")
                                        menuSegitiga = int(input(" Masukkan pilihan: "))
                                        # SEGITIGA JIKA DIKETAHUI ALAS DAN TINGGI
                                        if menuSegitiga == 1:
                                            os.system('cls')
                                            while True:
                                                try:
                                                    print("╔══════════════╗")
                                                    print("║ PostTest4App ║")
                                                    print("╚══════════════╝")
                                                    print(" LUAS SEGITIGA JIKA DIKETAHUI ALAS DAN TINGGI")
                                                    alasSegitiga = float(input(" \u2022 Alas = "))
                                                    tinggiSegitiga = float(input(" \u2022 Tinggi = "))
                                                    luasSegitiga1 = alasSegitiga * tinggiSegitiga / 2
                                                    pembulatan = int(luasSegitiga1) + 0.5
                                                    if luasSegitiga1 >= pembulatan:
                                                        hasilPembulatan = int(luasSegitiga1) + 1
                                                        print(" \u2022 Luas =", "{:.4}".format(luasSegitiga1))
                                                        print(" \u2022 Luas dibulatkan =", hasilPembulatan)
                                                    else:
                                                        print(" \u2022 Luas =", "{:.4}".format(luasSegitiga1))
                                                    input(" Tekan ENTER untuk kembali ke menu")
                                                    os.system('cls')
                                                    break
                                                except ValueError:
                                                    print("\033[2;31m Masukkan angka dengan benar!\033[0;0m")
                                                    input(" Tekan ENTER untuk melanjutkan")
                                                    os.system('cls')
                                            break
                                        # SEGITIGA JIKA DIKETAHUI KEITGA SISI
                                        elif menuSegitiga == 2:
                                            os.system('cls')
                                            while True:
                                                try:
                                                    while True:
                                                        os.system('cls')
                                                        print("╔══════════════╗")
                                                        print("║ PostTest4App ║")
                                                        print("╚══════════════╝")
                                                        print(" LUAS SEGITIGA JIKA DIKETAHUI KETIGA SISI")
                                                        sisiSegitiga_a = float(input(" \u2022 Sisi a = "))
                                                        sisiSegitiga_b = float(input(" \u2022 Sisi b = "))
                                                        sisiSegitiga_c = float(input(" \u2022 Sisi c = "))
                                                        if sisiSegitiga_a + sisiSegitiga_b <= sisiSegitiga_c or sisiSegitiga_a + sisiSegitiga_c <= sisiSegitiga_b or sisiSegitiga_b + sisiSegitiga_c <= sisiSegitiga_a:
                                                            print("\033[2;31m Sisi terpanjang tidak boleh lebih besar atau sama dengan jumlah dari dua sisi lainnya\033[0;0m")
                                                            input(" Tekan ENTER untuk melanjutkan")
                                                        else:
                                                            semiPerimeter = (sisiSegitiga_a + sisiSegitiga_b + sisiSegitiga_c) / 2
                                                            luasSegitiga2 = sqrt(semiPerimeter * (semiPerimeter - sisiSegitiga_a) * (semiPerimeter - sisiSegitiga_b) * (semiPerimeter - sisiSegitiga_c))
                                                            pembulatan = int(luasSegitiga2) + 0.5
                                                            if luasSegitiga2 >= pembulatan:
                                                                hasilPembulatan = int(luasSegitiga2) + 1
                                                                print(" \u2022 Luas =", "{:.4}".format(luasSegitiga2))
                                                                print(" \u2022 Luas dibulatkan =", hasilPembulatan)
                                                            else:
                                                                print(" \u2022 Luas =", "{:.4}".format(luasSegitiga2))
                                                            input(" Tekan ENTER untuk kembali ke menu")
                                                            os.system('cls')
                                                            break
                                                    break
                                                except ValueError:
                                                    print("\033[2;31m Masukkan angka dengan benar!\033[0;0m")
                                                    input(" Tekan ENTER untuk melanjutkan")
                                                    os.system('cls')
                                            break        
                                        else:
                                            print("\033[2;31m Masukkan pilihan dengan benar!\033[0;0m")
                                            input(" Tekan ENTER untuk melanjutkan")
                                            os.system('cls')  
                                    except ValueError:
                                        print("\033[2;31m Masukkan pilihan dengan benar!\033[0;0m")
                                        input(" Tekan ENTER untuk melanjutkan")
                                        os.system('cls')
                                break        
                            # LUAS TRAPESIUM
                            elif menuLuas == 5:
                                while True:
                                    try:
                                        os.system('cls')
                                        print("╔══════════════╗")
                                        print("║ PostTest4App ║")
                                        print("╚══════════════╝")
                                        print(" LUAS TRAPESIUM")
                                        print(" 1. Jika diketahui sisi atas, sisi bawah, dan tinggi")
                                        print(" 2. Jika diketahui sisi atas, sisi bawah, dan sisi miring")
                                        menuTrapesium = int(input(" Masukkan pilihan: "))
                                        # TRAPESIUM JIKA DIKETAHUI SISI ATAS< SISI BAWAH, DAN TINGGI
                                        if menuTrapesium == 1:
                                            os.system('cls')
                                            while True:
                                                try:
                                                    print("╔══════════════╗")
                                                    print("║ PostTest4App ║")
                                                    print("╚══════════════╝")
                                                    print(" LUAS TRAPESIUM JIKA DIKETAHUI SISI ATAS< SISI BAWAH, DAN TINGGI")
                                                    sisiAtasTrapesium1 = float(input(" \u2022 Sisi atas = "))
                                                    sisiBawahTrapesium1 = float(input(" \u2022 Sisi bawah = "))
                                                    tinggiTrapesium1 = float(input(" \u2022 Tinggi = "))
                                                    luasTrapesium1 = (sisiAtasTrapesium1 + sisiBawahTrapesium1) * tinggiTrapesium1 / 2
                                                    pembulatan = int(luasTrapesium1) + 0.5
                                                    if luasTrapesium1 >= pembulatan:
                                                        hasilPembulatan = int(luasTrapesium1) + 1
                                                        print(" \u2022 Luas =", "{:.4}".format(luasTrapesium1))
                                                        print(" \u2022 Luas dibulatkan =", hasilPembulatan)
                                                    else:
                                                        print(" \u2022 Luas =", "{:.4}".format(luasTrapesium1))
                                                    input(" Tekan ENTER untuk kembali ke menu")
                                                    os.system('cls')
                                                    break
                                                except ValueError:
                                                    print("\033[2;31m Masukkan angka dengan benar!\033[0;0m")
                                                    input(" Tekan ENTER untuk melanjutkan")
                                                    os.system('cls')
                                            break
                                        # TRAPESIUM JIKA DIKETAHUI SISI ATAS< SISI BAWAH, DAN SISI MIRING
                                        elif menuTrapesium == 2:
                                            os.system('cls')
                                            while True:
                                                try:
                                                    while True:
                                                        try:
                                                            print("╔══════════════╗")
                                                            print("║ PostTest4App ║")
                                                            print("╚══════════════╝")
                                                            print(" LUAS TRAPESIUM JIKA DIKETAHUI SISI ATAS, SISI BAWAH, DAN SISI MIRING")
                                                            print(" 1. Trapesium sama kaki")
                                                            print(" 2. Trapesium siku-siku")
                                                            subMenuTrapesium = int(input(" Masukkan pilihan: "))
                                                            # TRAPESIUM SAMA KAKI
                                                            os.system("cls")
                                                            while True:
                                                                try:
                                                                    if subMenuTrapesium == 1:
                                                                        print("╔══════════════╗")
                                                                        print("║ PostTest4App ║")
                                                                        print("╚══════════════╝")
                                                                        print(" LUAS TRAPESIUM SAMA KAKI JIKA DIKETAHUI SISI ATAS, SISI BAWAH, DAN SISI MIRING")
                                                                        sisiAtasTrapesium2_1 = float(input(" \u2022 Sisi atas = "))
                                                                        sisiBawahTrapesium2_1 = float(input(" \u2022 Sisi bawah = "))
                                                                        sisiMiringTrapesium2_1 = float(input(" \u2022 Sisi miring = "))
                                                                        luasTrapesium2_1 = sqrt(sisiMiringTrapesium2_1**2 - (abs(sisiAtasTrapesium2_1 - sisiBawahTrapesium2_1) / 2)**2)
                                                                        pembulatan = int(luasTrapesium2_1) + 0.5
                                                                        if luasTrapesium2_1 >= pembulatan:
                                                                            hasilPembulatan = int(luasTrapesium2_1) + 1
                                                                            print(" \u2022 Luas =", "{:.4}".format(luasTrapesium2_1))
                                                                            print(" \u2022 Luas dibulatkan =", hasilPembulatan)
                                                                        else:
                                                                            print(" \u2022 Luas =", "{:.4}".format(luasTrapesium2_1))
                                                                        input(" Tekan ENTER untuk kembali ke menu")
                                                                        os.system('cls')
                                                                    break
                                                                except ValueError:
                                                                    print("\033[2;31m Masukkan angka dengan benar!\033[0;0m")
                                                                    input(" Tekan ENTER untuk melanjutkan")
                                                                    os.system('cls')
                                                            # TRAPESIUM SIKU-SIKU
                                                            while True:
                                                                try:
                                                                    if subMenuTrapesium == 2:
                                                                        print("╔══════════════╗")
                                                                        print("║ PostTest4App ║")
                                                                        print("╚══════════════╝")
                                                                        print(" LUAS TRAPESIUM SIKU-SIKU JIKA DIKETAHUI SISI ATAS, SISI BAWAH, DAN SISI MIRING")
                                                                        sisiAtasTrapesium2_2 = float(input(" \u2022 Sisi atas = "))
                                                                        sisiBawahTrapesium2_2 = float(input(" \u2022 Sisi bawah = "))
                                                                        sisiMiringTrapesium2_2 = float(input(" \u2022 Sisi miring = "))
                                                                        luasTrapesium2_2 = sqrt(sisiMiringTrapesium2_2**2 - (abs(sisiAtasTrapesium2_2 - sisiBawahTrapesium2_2))**2)
                                                                        pembulatan = int(luasTrapesium2_2) + 0.5
                                                                        if luasTrapesium2_2 >= pembulatan:
                                                                            hasilPembulatan = int(luasTrapesium2_2) + 1
                                                                            print(" \u2022 Luas =", "{:.4}".format(luasTrapesium2_2))
                                                                            print(" \u2022 Luas dibulatkan =", hasilPembulatan)
                                                                        else:
                                                                            print(" \u2022 Luas =", "{:.4}".format(luasTrapesium2_2))
                                                                        input(" Tekan ENTER untuk kembali ke menu")
                                                                        os.system('cls')
                                                                    break
                                                                except ValueError:
                                                                    print("\033[2;31m Masukkan angka dengan benar!\033[0;0m")
                                                                    input(" Tekan ENTER untuk melanjutkan")
                                                                    os.system('cls')
                                                            break
                                                        except ValueError:
                                                            print("\033[2;31m Masukkan pilihan dengan benar!\033[0;0m")
                                                            input(" Tekan ENTER untuk melanjutkan")
                                                            os.system('cls')
                                                    break
                                                except ValueError:
                                                    print("\033[2;31m Masukkan angka dengan benar!\033[0;0m")
                                                    input(" Tekan ENTER untuk melanjutkan")
                                                    os.system('cls')
                                            break
                                        else:
                                            print("\033[2;31m Masukkan pilihan dengan benar!\033[0;0m")
                                            input(" Tekan ENTER untuk melanjutkan")
                                            os.system('cls')  
                                    except ValueError:
                                        print("\033[2;31m Masukkan pilihan dengan benar!\033[0;0m")
                                        input(" Tekan ENTER untuk melanjutkan")
                                        os.system('cls')   
                                break            
                            else:
                                print("\033[2;31m Masukkan pilihan dengan benar!\033[0;0m")
                                input(" Tekan ENTER untuk melanjutkan")
                                os.system('cls')  
                        except ValueError:
                            print("\033[2;31m Masukkan pilihan dengan benar!\033[0;0m")
                            input(" Tekan ENTER untuk melanjutkan")
                            os.system('cls')
                # MENU VOLUME
                elif menuUtama == 2:
                    while True:
                        try:
                            os.system('cls')
                            print("╔══════════════╗")
                            print("║ PostTest4App ║")
                            print("╚══════════════╝")
                            print(" MENCARI VOLUME")
                            print(" 1. Kubus")
                            print(" 2. Balok") 
                            print(" 3. Bola")
                            print(" 4. Kerucut")
                            menuVolume = int(input(" Masukkan pilihan: "))
                            # VOLUME KUBUS
                            if menuVolume == 1:
                                while True:
                                    try:
                                        os.system('cls')
                                        print("╔══════════════╗")
                                        print("║ PostTest4App ║")
                                        print("╚══════════════╝")
                                        print(" VOLUME KUBUS")
                                        sisiKubus = float(input(" \u2022 Sisi = "))
                                        volumeKubus = sisiKubus ** 3
                                        pembulatan = int(volumeKubus) + 0.5
                                        if volumeKubus >= pembulatan:
                                            hasilPembulatan = int(volumeKubus) + 1
                                            print(" \u2022 Luas =", "{:.4}".format(volumeKubus))
                                            print(" \u2022 Luas dibulatkan =", hasilPembulatan)
                                        else:
                                            print(" \u2022 Luas =", "{:.4}".format(volumeKubus))
                                        input(" Tekan ENTER untuk kembali ke menu")
                                        os.system('cls')
                                        break
                                    except ValueError:
                                        print("\033[2;31m Masukkan angka dengan benar!\033[0;0m")
                                        input(" Tekan ENTER untuk melanjutkan")
                                        os.system('cls')
                                break
                            # VOLUME BALOK
                            elif menuVolume == 2:
                                while True:
                                    try:
                                        os.system('cls')
                                        print("╔══════════════╗")
                                        print("║ PostTest4App ║")
                                        print("╚══════════════╝")
                                        print(" VOLUME BALOK")
                                        panjangBalok = float(input(" \u2022 Panjang = "))
                                        lebarBalok = float(input(" \u2022 Lebar = "))
                                        tinggiBalok = float(input(" \u2022 Tinggi = "))
                                        volumeBalok = panjangBalok * lebarBalok * tinggiBalok
                                        pembulatan = int(volumeBalok) + 0.5
                                        if volumeBalok >= pembulatan:
                                            hasilPembulatan = int(volumeBalok) + 1
                                            print(" \u2022 Luas =", "{:.4}".format(volumeBalok))
                                            print(" \u2022 Luas dibulatkan =", hasilPembulatan)
                                        else:
                                            print(" \u2022 Luas =", "{:.4}".format(volumeBalok))
                                        input(" Tekan ENTER untuk kembali ke menu")
                                        os.system('cls')
                                        break
                                    except ValueError:
                                        print("\033[2;31m Masukkan angka dengan benar!\033[0;0m")
                                        input(" Tekan ENTER untuk melanjutkan")
                                        os.system('cls')
                                break
                            # VOLUME BOLA
                            elif menuVolume == 3:
                                while True:
                                    try:
                                        os.system('cls')
                                        print("╔══════════════╗")
                                        print("║ PostTest4App ║")
                                        print("╚══════════════╝")
                                        print(" VOLUME BOLA")
                                        jariJariBola = float(input(" \u2022 Jari-jari = "))
                                        volumeBola = math.pi * jariJariBola ** 3 * 4 / 3
                                        pembulatan = int(volumeBola) + 0.5
                                        if volumeBola >= pembulatan:
                                            hasilPembulatan = int(volumeBalok) + 1
                                            print(" \u2022 Luas =", "{:.4}".format(volumeBola))
                                            print(" \u2022 Luas dibulatkan =", hasilPembulatan)
                                        else:
                                            print(" \u2022 Luas =", "{:.4}".format(volumeBola))
                                        input(" Tekan ENTER untuk kembali ke menu")
                                        os.system('cls')
                                        break
                                    except ValueError:
                                        print("\033[2;31m Masukkan angka dengan benar!\033[0;0m")
                                        input(" Tekan ENTER untuk melanjutkan")
                                        os.system('cls')
                                break
                            # VOLUME KERUCUT
                            elif menuVolume == 4:
                                while True:
                                    try:
                                        os.system('cls')
                                        print("╔══════════════╗")
                                        print("║ PostTest4App ║")
                                        print("╚══════════════╝")
                                        print(" VOLUME KERUCUT")
                                        jariJariKerucut = float(input(" \u2022 Jari-jari = "))
                                        tinggiKerucut = float(input(" \u2022 Tinggi = "))
                                        volumeKerucut = tinggiKerucut * math.pi * jariJariKerucut ** 2 / 3
                                        pembulatan = int(volumeKerucut) + 0.5
                                        if volumeKerucut >= pembulatan:
                                            hasilPembulatan = int(volumeKerucut) + 1
                                            print(" \u2022 Luas =", "{:.4}".format(volumeKerucut))
                                            print(" \u2022 Luas dibulatkan =", hasilPembulatan)
                                        else:
                                            print(" \u2022 Luas =", "{:.4}".format(volumeKerucut))
                                        input(" Tekan ENTER untuk kembali ke menu")
                                        os.system('cls')
                                        break
                                    except ValueError:
                                        print("\033[2;31m Masukkan angka dengan benar!\033[0;0m")
                                        input(" Tekan ENTER untuk melanjutkan")
                                        os.system('cls')
                                break
                            else:
                                print("\033[2;31m Masukkan pilihan dengan benar!\033[0;0m")
                                input(" Tekan ENTER untuk melanjutkan")
                                os.system('cls')  
                        except ValueError:
                            print("\033[2;31m Masukkan pilihan dengan benar!\033[0;0m")
                            input(" Tekan ENTER untuk melanjutkan")
                            os.system('cls')  
                # LOG OUT
                elif menuUtama == 3:
                    while True:
                        os.system('cls')
                        print("╔══════════════╗")
                        print("║ PostTest4App ║")
                        print("╚══════════════╝")
                        print(" Anda yakin ingin Log out?")
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
                else:
                    print("\033[2;31m Masukkan pilihan dengan benar!\033[0;0m")
                    input(" Tekan ENTER untuk melanjutkan")
                    os.system('cls')
            except ValueError:
                print("\033[2;31m Masukkan pilihan dengan benar!\033[0;0m")
                input(" Tekan ENTER untuk melanjutkan")
                os.system('cls')
    # LOGIN USERNAME SALAH
    elif username != "farrel_praktikan" and password == "pengenSekelompokSamaSirkel":
        print("\033[2;31m Username Anda salah\033[0;0m")
        input(" tekan ENTER untuk melanjutkan")
    # LOGIN PASSWORD  SALAH
    elif username == "farrel_praktikan" and password != "pengenSekelompokSamaSirkel":
        print("\033[2;31m Password Anda salah\033[0;0m")
        input(" tekan ENTER untuk melanjutkan")
    # LOGIN USERNAME DAN PASSWORD SALAH
    else:
        print("\033[2;31m Username dan password Anda salah\033[0;0m")
        input(" tekan ENTER untuk melanjutkan")