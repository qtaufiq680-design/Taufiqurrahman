
# PROGRAM SISTEM PENILAIAN AKADEMIK

print("=================================================")
print("       SISTEM PENILAIAN AKADEMIK")
print("=================================================")


# Input jumlah mahasiswa
jumlah = int(input("Masukkan jumlah mahasiswa: "))


# Menyiapkan variabel
data_mahasiswa = []
jumlah_lulus = 0
jumlah_tidak_lulus = 0


# Perulangan untuk memasukkan data mahasiswa
for i in range(jumlah):
    print("\nData Mahasiswa ke-", i + 1)

    nama = input("Masukkan nama mahasiswa: ")
    nilai = float(input("Masukkan nilai mahasiswa: "))

    # Menentukan kategori nilai
    if nilai >= 85 and nilai <= 100:
        kategori = "A"
        keterangan = "Sangat Baik"
        jumlah_lulus += 1

    elif nilai >= 75 and nilai < 85:
        kategori = "B"
        keterangan = "Baik"
        jumlah_lulus += 1

    elif nilai >= 60 and nilai < 75:
        kategori = "C"
        keterangan = "Cukup"
        jumlah_lulus += 1

    elif nilai >= 0 and nilai < 60:
        kategori = "D"
        keterangan = "Tidak Lulus"
        jumlah_tidak_lulus += 1

    else:
        print("Nilai tidak valid! Masukkan nilai 0-100.")
        continue

    # Menyimpan data mahasiswa
    data_mahasiswa.append({
        "nama": nama,
        "nilai": nilai,
        "kategori": kategori,
        "keterangan": keterangan
    })

# Menampilkan hasil penilaian
print("\n=================================================")
print("          HASIL PENILAIAN")
print("===================================================")

for mahasiswa in data_mahasiswa:
    print("\nNama       :", mahasiswa["nama"])
    print("Nilai      :", mahasiswa["nilai"])
    print("Kategori   :", mahasiswa["kategori"])
    print("Keterangan :", mahasiswa["keterangan"])

# Menampilkan jumlah kelulusan
print("\n================================================")
print("           REKAPITULASI")
print("==================================================")
print("JUMLAH MAHASISWA     :", len(data_mahasiswa))
print("JUMLAH MAHASISWA LULUS:", jumlah_lulus)
print("JUMLAH TIDAK LULUS    :", jumlah_tidak_lulus)
print("==================================================")
print("          PROGRAM SELESAI")
print("==================================================")
