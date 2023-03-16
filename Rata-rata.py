import timeit

# meminta pengguna untuk memasukkan jumlah bilangan
jumlah_bilangan = int(input("Masukkan jumlah bilangan: "))

# meminta pengguna untuk memasukkan bilangan
bilangan_list = []
for i in range(jumlah_bilangan):
    bilangan = float(input("Masukkan bilangan ke-{}: ".format(i+1)))
    bilangan_list.append(bilangan)

# menghitung rata-rata
start_time = timeit.default_timer()

jumlah = sum(bilangan_list)
rata_rata = jumlah / len(bilangan_list)

end_time = timeit.default_timer()
total_waktu = (end_time - start_time) * 1000

# menampilkan hasil rata-rata dan waktu yang dibutuhkan
print("Rata-rata dari bilangan", bilangan_list, "adalah", rata_rata)
print("Waktu yang dibutuhkan untuk menghitung rata-rata adalah", total_waktu, "milisecond")
