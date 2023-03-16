# meminta pengguna untuk memasukkan jumlah bilangan
jumlah_bilangan = int(input("Masukkan jumlah bilangan: "))

# meminta pengguna untuk memasukkan bilangan
bilangan_list = []
for i in range(jumlah_bilangan):
    bilangan = float(input("Masukkan bilangan ke-{}: ".format(i+1)))
    bilangan_list.append(bilangan)

# menghitung rata-rata
jumlah = sum(bilangan_list)
rata_rata = jumlah / len(bilangan_list)

# menampilkan hasil rata-rata
print("Rata-rata dari bilangan", bilangan_list, "adalah", rata_rata)

# mencari nilai maksimum dan minimum
nilai_max = max(bilangan_list)
nilai_min = min(bilangan_list)

# menampilkan hasil nilai maksimum dan minimum
print("Nilai maksimum dari bilangan", bilangan_list, "adalah", nilai_max)
print("Nilai minimum dari bilangan", bilangan_list, "adalah", nilai_min)