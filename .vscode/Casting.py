# casting : merubah satu type ke tipe yg lain
data_int = 9
print('data =', data_int, 'type =', type(data_int))

# INTEGER
print('====INTEGER====')
data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int)
print('data =', data_float, 'type =', type(data_float))
print('data =', data_str, 'type =', type(data_str))
print('data =', data_bool, 'type =', type(data_bool))

# FLOAT
print('====FLOAT====')
data_float = 9.5
print('data =', data_float, 'type =', type(data_float))

data_int = int(data_float)  # akan dibulatkan ke bawah
data_str = str(data_float)
data_bool = bool(data_float)  # akan false jika bilangan nol
print('data =', data_int, 'type =', type(data_int))
print('data =', data_str, 'type =', type(data_str))
print('data =', data_bool, 'type =', type(data_bool))

# BOOLEAN
print('====BOOLEAN====')
data_bool = False
print('data =', data_bool, 'type =', type(data_bool))

data_int = int(data_bool)  # akan dibulatkan ke bawah
data_str = str(data_bool)
data_float = float(data_bool)  # akan false jika bilangan nol
print('data =', data_int, 'type =', type(data_int))
print('data =', data_str, 'type =', type(data_str))
print('data =', data_float, 'type =', type(data_float))

# STRING
print('====STRING====')
data_str = '10'   # harus angka klo string jadinya error
print('data =', data_str, 'type =', type(data_str))

# string tidak bisa dijadikan integer , stringnya harus angka
data_int = int(data_str)
data_float = float(data_str)   # stringnya harus angka
data_bool = bool(data_str)  # akan false ika bilangan nol ( atau kosong)
print('data =', data_int, 'type =', type(data_int))
print('data =', data_float, 'type =', type(data_float))
print('data =', data_bool, 'type =', type(data_bool))
