def nilai_huruf(x) :
    batas_minimal_a = 85
    batas_minimal_b = 70
    batas_minimal_c = 55
    batas_minimal_d = 45

    if x >= batas_minimal_a:
        return "A"
    elif x >= batas_minimal_b :
        return "B"
    elif x >= batas_minimal_c :
        return "C"
    elif x >= batas_minimal_d :
        return "D"
    else :
        return "E"

def rata_rata(daftar_nilai) :
    total = 0
    for nilai in daftar_nilai :
        total = total + nilai
    
    print("Total nilai : "+ str(total))
    print("Jumlah data : "+ str(len(daftar_nilai)))
    return float(total) / float(len(daftar_nilai))
