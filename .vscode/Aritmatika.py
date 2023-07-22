# operasi aritmatika

a = 10
b = 3

# operasi tambah +
hasil = a + b
print(a, "+", b, "=", hasil)

# operasi pengurangan -
hasil = a - b
print(a, "-", b, "=", hasil)

# operasi perkalian *
hasil = a * b
print(a, "*", b, "=", hasil)

# operasi pembagian /  # klo bagusnya di pyhton pembagian akan otomatis hasilnya jadi float(ada komanya)
hasil = a / b
print(a, "/", b, "=", hasil)

# operasi modulus (sisa pembagian) %
hasil = a % b
print(a, "%", b, "=", hasil)

# operasi pangkat (eksponen)  **
hasil = a ** b
print(a, "**", b, "=", hasil)

# operasi floor division //
hasil = a // b
print(a, "//", b, "=", hasil)

# prioritas operasi, operational precedence
'''
  1.()
  2. exponen **
  3.perkalian dan teman teman */ ** % //
  4. pertambahan dan pengurangan +-
'''
x = 3
y = 2
z = 4

hasil = x ** y * (z + x) / y-y % z // x
print(x, '**', y, '*', z, '+', x, '/', y, '-', y, '%', z, '/ /', x, '=', hasil)

hasil = x + y * z
# jika ada kurung maka yg kurung akan diambil langkah pertama
print(x, '+', y, '*', z, '=', hasil)
hasil = (x+y)*z
print('(', x, '+', y, ')*', z, '=', hasil)
