import json

with open("file.json", "r") as file:
    data = json.load(file)  # Загружает JSON из файла в виде словаря (dict)

#📤 Запись JSON в файл
with open("file.json", "w") as file:
    json.dump(data, file, indent=4)  # Записывает словарь (dict) в JSON-файл с отступами
#🔄 Преобразование JSON-строки в словарь (dict)
json_string = '{"name": "Alice", "age": 25}'
data = json.loads(json_string)  # Преобразует строку JSON в словарь
print(data["name"])  # Alice
#🔄 Преобразование словаря (dict) в JSON-строку
data = {"name": "Alice", "age": 25}
json_string = json.dumps(data)  # Преобразует словарь в строку JSON
print(json_string)  # {"name": "Alice", "age": 25}
#📌 Дополнительные параметры json.dump() и json.dumps()
json.dump(data, file, indent=4, sort_keys=True)  # indent=4 (отступы), sort_keys=True (сортировка ключей)
json.dumps(data, indent=4, ensure_ascii=False)  # ensure_ascii=False для корректного отображения кириллицы
#🏷 Изменение JSON-данных
data["age"] = 30  # Меняем данные
data["city"] = "New York"  # Добавляем новый ключ
del data["name"]  # Удаляем ключ
#🔄 Чтение и обработка данных из JSON-файла (пример с массивом)
with open("sample.json", "r") as file:
    data = json.load(file)

for item in data["items"]:  # Проход по массиву в JSON
    print(item["name"], item["price"])  # Доступ к значениям

# import json 
# with open("example.json" , "r") as json_file:
#     data=json.load(json_file)
# def dict_to_js(did):
#     print(json.dumps(did))
# did={"name":"Assel" , "age":"18", "birth":"04.03.07"}
# a=did
# dict_to_js(did)
# with open("example.json", "w") as json_file:
#     json.dump(a, json_file)

