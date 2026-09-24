teks_benar = input("Jumlah jawaban benar (0-20): ").strip()

try:
    benar = int(teks_benar)
except ValueError:
    print("Masukan ditolak: jumlah jawaban benar harus berupa bilangan bulat.")
else:
    if not (0 <= benar <= 20):
        print("Masukan ditolak: jumlah jawaban benar harus berada pada rentang 0 sampai 20.")
    else:
        persentase = (benar / 20) * 100

        if persentase >= 75:
            status = "Tuntas"
        else:
            status = "Belum tuntas"

        print(f"Persentase = {persentase:.2f}%")
        print(f"Status = {status}")