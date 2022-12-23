import os

# PESAN PEMBUKA
os.system('cls')
print("Mohon isi biodata diri Anda")
input("tekan ENTER untuk melanjutkan")
os.system('cls')

# NAMA
nama = input("Nama lengkap: ")
os.system('cls')

# TEMPAT, TANGGAL LAHIR
ttl = input("Tempat, tanggal lahir: ")
os.system('cls')

# UMUR
while True:
    try:
        while True:
            umur = int(input("Umur: "))
            if umur >= 0:
                os.system('cls')
                break
            else:
                print("Masukkan umur dengan benar!")
                input("Tekan ENTER untuk melanjutkan")
                os.system('cls')
        break
    except ValueError:
        print("Masukkan umur dengan benar!")
        input("Tekan ENTER untuk melanjutkan")
        os.system('cls')

# TINGGI BADAN
while True:
    try:
        while True:
            tinggiBadan = float(input("Tinggi badan: "))
            if tinggiBadan >= 0:
                os.system('cls')
                break
            else:
                print("Masukkan tinggi badan dengan benar!")
                input("Tekan ENTER untuk melanjutkan")
                os.system('cls')
        break
    except ValueError:
        print("Masukkan tinggi badan dengan benar!")
        input("Tekan ENTER untuk melanjutkan")
        os.system('cls')

# BERAT BADAN
while True:
    try:
        while True:
            beratBadan = float(input("Berat badan: "))
            if beratBadan >= 0:
                os.system('cls')
                break
            else:
                print("Masukkan berat badan dengan benar!")
                input("Tekan ENTER untuk melanjutkan")
                os.system('cls')
        break
    except ValueError:
        print("Masukkan berat badan dengan benar!")
        input("Tekan ENTER untuk melanjutkan")
        os.system('cls')

# GOLONGAN DARAH
golonganDarah = input("Golongan darah: ")
os.system('cls')

# FAKULTAS
fakultas = input("Fakultas: ")
os.system('cls')

# PRODI
prodi = input("Prodi: ")
os.system('cls')

# NIM
while True:
    try:
        while True:
            nim = int(input("NIM: "))
            if nim >= 0:
                os.system('cls')
                break
            else:
                print("Masukkan NIM dengan benar!")
                input("Tekan ENTER untuk melanjutkan")
                os.system('cls')
        break
    except ValueError:
        print("Masukkan NIM dengan benar!")
        input("Tekan ENTER untuk melanjutkan")
        os.system('cls')

# TIGA DIGIT TERAKHIR NIM
while True:
    try:
        while True:
            tigaDigitNIM = int(input("tiga digit terakhir NIM: "))
            if tigaDigitNIM >= 0:
                nimMod2 = tigaDigitNIM % 2
                os.system('cls')
                break
            else:
                print("Masukkan tiga digit terakhir NIM dengan benar!")
                input("Tekan ENTER untuk melanjutkan")
                os.system('cls')
        break
    except ValueError:
        print("Masukkan tiga digit terakhir NIM dengan benar!")
        input("Tekan ENTER untuk melanjutkan")
        os.system('cls')


# KONFIRMASI
while True:
    print("=================================================")
    print("BIODATA DIRI")
    print('\u2022', "Nama lengkap              :", nama.title())
    print('\u2022', "Tempat, tanggal lahir     :", ttl.title())
    print('\u2022', "Umur                      :", umur, "tahun")
    print('\u2022', "Tinggi badan              :", tinggiBadan, "cm")
    print('\u2022', "Berat badan               :", beratBadan, "kg")
    print('\u2022', "Golongan darah            :", golonganDarah.upper())
    print('\u2022', "Fakultas                  :", fakultas.title())
    print('\u2022', "Prodi                     :", prodi.title())
    print('\u2022', "NIM                       :", nim, bool(nim))
    print('\u2022', "tiga digit terakhir NIM   :", tigaDigitNIM)
    print("=================================================")
    print("Biodata yang Anda masukkan sudah benar?")
    print("[Y] untuk selesai")
    print("[N] untuk mengganti biodata")
    lanjut = input("[Y/N]: ")

# TAMPILAN BIODATA
    if lanjut == "Y" or lanjut == "y":
        os.system('cls')
        print("=================================================")
        print("BIODATA DIRI")
        print('\u2022', "Nama lengkap              :", nama.title())
        print('\u2022', "Tempat, tanggal lahir     :", ttl.title())
        print('\u2022', "Umur                      :", umur, "tahun")
        print('\u2022', "Tinggi badan              :", tinggiBadan, "cm")
        print('\u2022', "Berat badan               :", beratBadan, "kg")
        print('\u2022', "Golongan darah            :", golonganDarah.upper())
        print('\u2022', "Fakultas                  :", fakultas.title())
        print('\u2022', "Prodi                     :", prodi.title())
        print('\u2022', "NIM                       :", nim, bool(nim))
        print('\u2022', "NIM modulus 2             :", nimMod2)
        print("=================================================")
        break

# ISI ULANG BIODATA
    elif lanjut == "N" or lanjut == "n":
        while True:
            os.system('cls')
            print("=================================================")
            print("1.  Nama lengkap              :", nama.title())
            print("2.  Tempat, tanggal lahir     :", ttl.title())
            print("3.  Umur                      :", umur, "tahun")
            print("4.  Tinggi badan              :", tinggiBadan, "cm")
            print("5.  Berat badan               :", beratBadan, "kg")
            print("6.  Golongan darah            :", golonganDarah.upper())
            print("7.  Fakultas                  :", fakultas.title())
            print("8.  Prodi                     :", prodi.title())
            print("9.  NIM                       :", nim, bool(nim))
            print("10. tiga digit terakhir NIM   :", tigaDigitNIM)
            print("=================================================")
            gantiBiodata = int(input("Masukkan nomor urut biodata yang ingin diganti: "))
            # NAMA
            if gantiBiodata == 1:
                os.system('cls')
                nama = input("Nama: ")
                os.system('cls')
                break
            # TEMPAT, TANGGAL LAHIR
            elif gantiBiodata == 2:
                os.system('cls')
                ttl = input("Tempat, tanggal lahir: ")
                os.system('cls')
                break
            # UMUR
            elif gantiBiodata == 3:
                os.system('cls')
                while True:
                    try:
                        while True:
                            umur = int(input("Umur: "))
                            if umur >= 0:
                                os.system('cls')
                                break
                            else:
                                print("Masukkan umur dengan benar!")
                                input("Tekan ENTER untuk melanjutkan")
                                os.system('cls')
                        break
                    except ValueError:
                        print("Masukkan umur dengan benar!")
                        input("Tekan ENTER untuk melanjutkan")
                        os.system('cls')
                break
            # TINGGI BADAN
            elif gantiBiodata == 4:
                os.system('cls')
                while True:
                    try:
                        while True:
                            tinggiBadan = float(input("Tinggi badan: "))
                            if tinggiBadan >= 0:
                                os.system('cls')
                                break
                            else:
                                print("Masukkan tinggi badan dengan benar!")
                                input("Tekan ENTER untuk melanjutkan")
                                os.system('cls')
                        break
                    except ValueError:
                        print("Masukkan tinggi badan dengan benar!")
                        input("Tekan ENTER untuk melanjutkan")
                        os.system('cls')
                break
            # BERAT BADAN
            elif gantiBiodata == 5:
                os.system('cls')
                while True:
                    try:
                        while True:
                            beratBadan = float(input("berat badan: "))
                            if beratBadan >= 0:
                                os.system('cls')
                                break
                            else:
                                print("Masukkan berat badan dengan benar!")
                                input("Tekan ENTER untuk melanjutkan")
                                os.system('cls')
                        break
                    except ValueError:
                        print("Masukkan berat badan dengan benar!")
                        input("Tekan ENTER untuk melanjutkan")
                        os.system('cls')
                break
            # GOLONGAN DARAH
            elif gantiBiodata == 6:
                os.system('cls')
                golonganDarah = input("Golongan darah: ")
                os.system('cls')
                break
            # FAKULTAS
            elif gantiBiodata == 7:
                os.system('cls')
                fakultas = input("Fakultas: ")
                os.system('cls')
                break
            # PRODI
            elif gantiBiodata == 8:
                os.system('cls')
                prodi = input("Prodi: ")
                os.system('cls')
                break
            # NIM
            elif gantiBiodata == 9:
                os.system('cls')
                while True:
                    try:
                        while True:
                            nim = int(input("NIM: "))
                            if nim >= 0:
                                os.system('cls')
                                break
                            else:
                                print("Masukkan NIM dengan benar!")
                                input("Tekan ENTER untuk melanjutkan")
                                os.system('cls')
                        break
                    except ValueError:
                        print("Masukkan NIM dengan benar!")
                        input("Tekan ENTER untuk melanjutkan")
                        os.system('cls')
                break
            # TIGA DIGIT TERAKHIR NIM
            elif gantiBiodata == 10:
                os.system('cls')
                while True:
                    try:
                        while True:
                            tigaDigitNIM = int(input("Tiga digit terakhir NIM: "))
                            if tigaDigitNIM >= 0:
                                nimMod2 = tigaDigitNIM % 2
                                os.system('cls')
                                break
                            else:
                                print("Masukkan tiga digit terakhir NIM dengan benar!")
                                input("Tekan ENTER untuk melanjutkan")
                                os.system('cls')
                        break
                    except ValueError:
                        print("Masukkan tiga digit terakhir NIM dengan benar!")
                        input("Tekan ENTER untuk melanjutkan")
                        os.system('cls')
                break
            else:
                print("Masukkan sesuai pilihan!")
                input("Tekan ENTER untuk melanjutkan")
                os.system('cls')
            os.system('cls')