# Operator Aritmatika
x = 10
y = 5
z = 3
a = 3

# operator : +
# operand : x dan y
print("x + y = "+ str(x + y))
print("x - y = "+ str(x - y))
print("x * y = "+ str(x * y))
print("x / y = "+ str(x / y))
print("x ** y = "+ str(x ** z))
print("x / z = "+ str(float(x) / float(z)))
print("x // y = "+ str(x // z))
print("x % y = "+ str(x % z))

print("===========================")
# Operator Relasional (perbandingan)
print("x > y = "+ str(x > y))
print("a > z = "+ str(a > z))
print("x < z = "+ str(x < z))
print("x <= z = "+ str(x <= z))
print("a >= z = "+ str(a >= z))
print("a == z = "+ str(a == z))
print("x == z = "+ str(x == z))
print("a != z = "+ str(a != z))
print("x != z = "+ str(x != z))

print("===========================")
# Operator Assignment (mengisi data ke variabel)
b = 5 # mengisi nilai 5 ke dalam variabel b
print("b : "+ str(b))
b+=1  # menambah 1 ke nilai variabel b
print("b : "+ str(b))
b/=3  # membagi 3 nilai b, hasilnya diisikan ke b lagi
print("b : "+ str(b))

print("===========================")
# Operator Logika

## Apakah a bilangan genap?
print("a genap ? "+ str(a % 2 == 0))

## Apakah b bilangan genap?
print("b genap ? "+ str(b % 2 == 0))

## Apakah a dan b bilangan genap?
print("a dan b genap ? "+ str((a % 2 == 0) and (b % 2 == 0)))

## Apakah a atau b bilangan genap?
print("a atau b genap ? "+ str((a % 2 == 0) or (b % 2 == 0)))

## Apakah a bukan bilangan genap?
print("a bukan genap ? "+ str(not(a % 2 == 0)))

print("===========================")
# Operator Membership
krs = ['Data Mining', 'Akuntansi Biaya', 'Fiqh Muamalah']
print("Apakah saya ikut mata kuliah Data Mining ? ")
print('Data Mining' in krs)
print("Apakah saya ikut mata kuliah Ekonometrika ? ")
print('Ekonometrika' in krs)
print("Apakah Fiqh Muamalah tidak ada di KRS saya ? ")
print('Fiqh Muamalah' not in krs)
print("Apakah Statistika tidak ada di KRS saya ? ")
print('Statistika' not in krs)