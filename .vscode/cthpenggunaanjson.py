import json

# Mengubah objek Python menjadi JSON
data = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
json_data = json.dumps(data)
print(json_data)

# Mengubah JSON menjadi objek Python
json_data = '{"name": "John", "age": 30, "city": "New York"}'
data = json.loads(json_data)
print(data["name"])

# Menulis objek Python ke file JSON
data = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
with open("data.json", "w") as json_file:
    json.dump(data, json_file)

# Membaca file JSON dan mengembalikan objek Python
with open("data.json", "r") as json_file:
    data = json.load(json_file)
print(data)
