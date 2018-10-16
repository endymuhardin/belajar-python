daftar_nilai = [80, 75, 55, 60, 86, 90, 45, 65]

batas_minimal_a = 85
batas_minimal_b = 70
batas_minimal_c = 55
batas_minimal_d = 45

# tentukan nilai huruf dari daftar nilai di atas
for x in daftar_nilai :
  if x >= batas_minimal_a :
    print(str(x) + " : A")
  elif x >= batas_minimal_b :
    print(str(x) + " : B")
  elif x >= batas_minimal_c :
    print(str(x) + " : C")
  elif x >= batas_minimal_d :
    print(str(x) + " : D")
  else :
    print(str(x) + " : E")