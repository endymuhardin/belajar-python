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
