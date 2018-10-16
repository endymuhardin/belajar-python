daftar_nilai = [80, 75, 55, 60, 86, 90, 45, 65]

batas_minimal_a = 85
batas_minimal_b = 70
batas_minimal_c = 55
batas_minimal_d = 45

# tentukan nilai huruf dari daftar nilai di atas
x = daftar_nilai[0]
print(x)
if x >= batas_minimal_a :
  print("Nilai : A")
elif x >= batas_minimal_b :
  print("Nilai : B")
elif x >= batas_minimal_c :
  print("Nilai : C")
elif x >= batas_minimal_d :
  print("Nilai : D")
else :
  print("Nilai : E")