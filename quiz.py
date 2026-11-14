# Program Quiz Algoritma Python
# Input, Percabangan, dan Perulangan While

print("=== PROGRAM UJIAN MATEMATIKA ===")

# Input nama mahasiswa
nama = input("Masukkan nama mahasiswa: ")

# Menentukan target nilai
if nama.lower() == "andi":
    target = 70
elif nama.lower() == "budi":
    target = 75
elif nama.lower() == "citra":
    target = 80
else:
    print("Nama mahasiswa tidak terdaftar!")
    exit()

print("\nNama Mahasiswa :", nama)
print("Target Nilai   :", target)

# Proses ujian maksimal 3 kali
percobaan = 1
lulus = False

while percobaan <= 3:
    nilai = int(input(f"\nMasukkan nilai ujian ke-{percobaan}: "))

    if nilai >= target:
        lulus = True
        break
    else:
        print("Nilai belum mencapai target.")
        print("Silakan mengikuti remedial.")

    percobaan += 1

# Menampilkan hasil akhir
print("\n=== HASIL UJIAN ===")

if lulus:
    print(nama, "berhasil lulus!")
    print("Jumlah percobaan:", percobaan)
else:
    print(nama, "tidak lulus!")
    print("Sudah melakukan 3 kali percobaan.")

print("Program selesai.")