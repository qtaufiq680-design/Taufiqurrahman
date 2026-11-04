jumlah = int(input("Jumlah mahasiswa (5-10): "))

if jumlah >= 5 and jumlah <= 10:
    total = 0

    for i in range(1, jumlah + 1):
        nilai = float(input(f"Masukkan nilai mahasiswa {i}: "))
        total += nilai

    rata_rata = total / jumlah

    print("Nilai rata-rata:", rata_rata)

else:
    print("Jumlah mahasiswa harus antara 5-10!")