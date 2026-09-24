sudut1 = float(input("Masukkan sudut 1: "))
sudut2 = float(input("Masukkan sudut 2: "))
sudut3 = float(input("Masukkan sudut 3: "))

jumlah = sudut1 + sudut2 + sudut3

if sudut1 <= 0 or sudut2 <= 0 or sudut3 <= 0:
    print("Masukan ditolak: semua sudut harus lebih dari 0.")
elif abs(jumlah - 180) > 1e-9:
    print("Masukan ditolak: jumlah ketiga sudut harus 180 derajat.")
else:
    sudut_terbesar = max(sudut1, sudut2, sudut3)

    if sudut_terbesar < 90:
        print("Segitiga lancip.")
    elif sudut_terbesar == 90:
        print("Segitiga siku-siku.")
    else:
        print("Segitiga tumpul.")