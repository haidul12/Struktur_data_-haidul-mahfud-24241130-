# ===============================================
# KELOMPOK 5
# 1. Nama: Helmiati (24241120)
# 2. Nama: Haidul Mahfud (24241130)
# ===============================================

print("="*45)
print("         PROGRAM GABUNGAN TUGAS 1 - 8         ")
print("="*45)

# =======================
# TUGAS 1 - Tabel Kebenaran
# =======================
print("\n# TUGAS 1 - TABEL KEBENARAN LOGIKA P DAN Q\n")
print(f"{'P':^5} {'Q':^5} {'NOT P':^7} {'P AND Q':^9} {'P OR Q':^8} {'P XOR Q':^10} {'P → Q':^7} {'P ↔ Q':^7}")

for P in [True, False]:
    for Q in [True, False]:
        not_p = not P
        and_pq = P and Q
        or_pq = P or Q
        xor_pq = P != Q
        impl_pq = (not P) or Q
        biimpl_pq = P == Q
        print(f"{P!s:^5} {Q!s:^5} {not_p!s:^7} {and_pq!s:^9} {or_pq!s:^8} {xor_pq!s:^10} {impl_pq!s:^7} {biimpl_pq!s:^7}")

# =======================
# TUGAS 2 - Operasi Logika
# =======================
print("\n# TUGAS 2 - OPERASI LOGIKA\n")

x = True
z = not x
print("Nilai dari z = not", x, "->", z)

print("\n********** AND ***********")
for x in [True, False]:
    for y in [True, False]:
        z = x and y
        print(x, "and", y, "=", z)

print("\n********** OR ***********")
for x in [True, False]:
    for y in [True, False]:
        z = x or y
        print(x, "or", y, "=", z)

# =======================
# TUGAS 3 - Konversi Nilai Mahasiswa
# =======================
print("\n# TUGAS 3 - KONVERSI NILAI MAHASISWA\n")

mahasiswa = [
    {"nama": "helmiati", "nilai": 100},
    {"nama": "haidul mahfud", "nilai": 80}
]

def konversi_nilai(nilai):
    if nilai >= 85:
        return 'A'
    elif nilai >= 75:
        return 'B'
    elif nilai >= 60:
        return 'C'
    elif nilai >= 50:
        return 'D'
    else:
        return 'E'

print(f"{'Nama':<15} {'Nilai':<10} {'Huruf':<6}")
print("-" * 35)
for mhs in mahasiswa:
    nilai_angka = mhs['nilai']
    nilai_huruf = konversi_nilai(nilai_angka)
    print(f"{mhs['nama']:<15} {nilai_angka:<10} {nilai_huruf:<6}")

# =======================
# TUGAS 4 - Ternary Umur
# =======================
print("\n# TUGAS 4 - KATEGORI UMUR (TERNARY)\n")

umur = int(input("Masukkan umur Anda: "))
kategori = "Dewasa" if umur >= 18 else "Anak-anak"
print(f"Anda termasuk {kategori}.")

# =======================
# TUGAS 5 - Hitung Huruf & Validasi
# =======================
print("\n# TUGAS 5 - HITUNG HURUF DAN VALIDASI PASSWORD\n")

# Input teks
teks = input("Masukkan teks (misalnya: bima soromandi a): ")
teks_bersih = teks.replace(" ", "").lower()

print("Jumlah kemunculan setiap huruf:")
for huruf in sorted(set(teks_bersih)):
    jumlah = teks_bersih.count(huruf)
    print(f"Huruf '{huruf}' muncul {jumlah} kali")

# Tempat tinggal
tempat_tinggal = input("Masukkan tempat tinggal anda: ")
print("Jumlah huruf pada tempat tinggal:", len(tempat_tinggal))

# Password
password = input("Masukkan password: ")
print("Jumlah huruf pada password:", len(password))
if len(password) < 8:
    print("Password kurang panjang")
else:
    print("Password diterima")

# =======================
# TUGAS 6 - Operasi List
# =======================
print("\n# TUGAS 6 - OPERASI DATA PADA LIST\n")

number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

def tampilkan_data_terakhir(data):
    return data[-1]

def tampilkan_data_pertama(data):
    return data[0]

def tampilkan_data_ke3_sampai_ke6(data):
    return data[2:6]

print("=== HASIL APLIKASI DATA ===")
print("A. Data terakhir       :", tampilkan_data_terakhir(number))
print("B. Data pertama        :", tampilkan_data_pertama(number))
print("C. Data ke-3 sampai ke-6:", tampilkan_data_ke3_sampai_ke6(number))

# =======================
# TUGAS 7 - Pemisahan Domain
# =======================
print("\n# TUGAS 7 - PEMISAHAN DOMAIN WEBSITE\n")

alamat = input("Masukkan nama domain anda (contoh: helmiati.net): ")
nama, domain = alamat.split(".")
print("Nama domain:", nama)
print("Domain yang anda gunakan:", domain)

# =======================
# TUGAS 8 - Ambil Digit Koma
# =======================
print("\n# TUGAS 8 - AMBIL DIGIT DI BELAKANG KOMA\n")

harga_normal = 15.5935
harga_diskon = 16.45987
harga_retail = 14.96884

satu_digit_normal = int((harga_normal * 10) % 10)
satu_digit_diskon = int((harga_diskon * 10) % 10)
satu_digit_retail = int((harga_retail * 10) % 10)

dua_digit_normal = int((harga_normal * 100) % 100)
dua_digit_diskon = int((harga_diskon * 100) % 100)
dua_digit_retail = int((harga_retail * 100) % 100)

print("Satu digit di belakang koma:")
print("harga_normal :", satu_digit_normal)
print("harga_diskon :", satu_digit_diskon)
print("harga_retail :", satu_digit_retail)

print("\nDua digit di belakang koma:")
print("harga_normal :", dua_digit_normal)
print("harga_diskon :", dua_digit_diskon)
print("harga_retail :", dua_digit_retail)