# Pertemuan 04 Seleksi Multi-Kondisi dan Validasi Input

Nama: Nailah Nur Fadilah  
NIM: 2225250163  
Kelas: 3E  

## Tujuan

Membangun program validasi dan klasifikasi dengan rantai if-elif-else.

## Cara Menjalankan

```bash
python3 praktik/validasi_klasifikasi_nilai.py
## Tabel Keputusan

| Kategori | Syarat | Contoh Masukan |
|---|---|---|
| A | Nilai akhir >= 85 | 90 |
| B | Nilai akhir >= 70 dan < 85 | 75 |
| C | Nilai akhir >= 60 dan < 70 | 60 |
| D | Nilai akhir >= 50 dan < 60 | 55 |
| E | Nilai akhir < 50 | 40 |
| Tidak memenuhi syarat kehadiran | Kehadiran < 80% | 75% |

## Hasil Pengujian

| Masukan | Keluaran Diharapkan | Keluaran Aktual | Status |
|---|---|---|---|
| Ujian 90, Tugas 80, Kehadiran 95 | Nilai akhir = 86.00; Predikat A; Lulus | - | - |
| Ujian 75, Tugas 70, Kehadiran 85 | Nilai akhir = 73.00; Predikat B; Lulus | - | - |
| Ujian 60, Tugas 60, Kehadiran 80 | Nilai akhir = 60.00; Predikat C; Lulus | - | - |
| Ujian 55, Tugas 50, Kehadiran 90 | Nilai akhir = 53.00; Predikat D; Belum lulus | - | - |
| Ujian 40, Tugas 30, Kehadiran 100 | Nilai akhir = 36.00; Predikat E; Belum lulus | - | - |
| Ujian 90, Tugas 90, Kehadiran 75 | Nilai akhir = 90.00; Tidak memenuhi syarat kehadiran | - | - |
| Ujian 105, Tugas 80, Kehadiran 90 | Nilai ujian di luar rentang | - | - |
| Ujian 80, Tugas -5, Kehadiran 90 | Nilai tugas di luar rentang | - | - |
| Ujian 80, Tugas 80, Kehadiran abc | Seluruh data harus berupa angka | - | - |

## Refleksi

Masukan tidak valid yang semula terlewat adalah masukan berupa teks pada data yang seharusnya berupa angka. Masukan tersebut ditangani menggunakan try-except ValueError sehingga program dapat menolak masukan dan menampilkan pesan bahwa seluruh data harus berupa angka.