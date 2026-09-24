bilangan = int(input("Masukkan bilangan: "))

if bilangan < 0:
    kategori = "bilangan negatif"
elif bilangan == 0:
    kategori = "nol"
elif bilangan % 2 == 0:
    kategori = "bilangan positif genap"
else:
    kategori = "bilangan positif ganjil"

print(f"{bilangan} adalah {kategori}.")