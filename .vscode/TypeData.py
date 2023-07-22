# type data = macam macam data yg bisa kita pakai di python atau codingan lain

# type data apa saja yg ada di python

# 1. angka satuan pokoknya yg nggk ada komanya (integer)
from ctypes import c_double, c_char, c_long
data_integer = 15
print('data :', data_integer)
print('-bertipe :', type(data_integer))

# 2. angka dengan koma (float)
data_float = 1.5
print('data :', data_float)
print('-bertipe :', type(data_float))

# 3. kumpulan karakter (string)
data_string = 'string'
print('data :', data_string)
print('-bertipe :', type(data_string))

# 4. binear true /false (boolean)
data_bool = True
print('data :', data_bool)
print('-bertipe :', type(data_bool))

# type data khusus

# bilangan kompleks
data_complex = complex(5, 6)
print('data :', data_complex)
print('-bertipe :', type(data_complex))

# type data dari bahasa c

data_c_double = c_double(10.5)
print('data :', data_c_double)
print('-bertipe :', type(data_c_double))
