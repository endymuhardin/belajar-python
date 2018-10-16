# list, urutan dijamin
nama_hari = ['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Ahad']
print (nama_hari)

# mulai hitung dari 0, bukan dari 1
print ("Hari ke 1 : " + nama_hari[0]) 
print ("Hari ke 2 : " + nama_hari[1]) 

# jumlah data dalam list
jumlah_hari = len(nama_hari) # tipe data : integer
print ("Jumlah hari : " + str(jumlah_hari)) # konversi jadi string, supaya bisa digabungkan

# mengetahui posisi index suatu data
print ("Hari Jumat ada di posisi : " + str(nama_hari.index('Jumat')))

# Awalnya, yang hadir baru 3 orang
kehadiran = ["Ahmad", "Adi", "Budi"] 
print ("Siswa yang sudah hadir : ")
print (kehadiran)

# Menambah satu data ke dalam list
kehadiran = kehadiran + ["Haffizh"]
print ("Siswa yang sudah hadir : ")
print (kehadiran)

# Menambah 2 data
kehadiran = kehadiran + ["Wahyu", "Nurul"]
print ("Siswa yang sudah hadir : ")
print (kehadiran)

# Menghapus data
kehadiran.remove("Adi")
print ("Siswa yang sudah hadir : ")
print (kehadiran)
