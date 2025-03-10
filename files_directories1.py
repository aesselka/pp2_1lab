import os
from pathlib import Path
import shutil

# Создать директорию
os.mkdir("example_directory")  # Создает одну директорию

# Создать вложенные директории
os.makedirs("example_directory/nested_folder")  # Создает директории рекурсивно

# Перечислить содержимое директории
print(os.listdir("example_directory"))  # Возвращает список файлов и папок

# Проверить, существует ли файл или директория
print(os.path.exists("example_directory"))  # True, если существует

# Проверить, является ли путь файлом
print(os.path.isfile("example_directory/example.txt"))  # True, если это файл

# Проверить, является ли путь директорией
print(os.path.isdir("example_directory"))  # True, если это директория

# Получить абсолютный путь
print(os.path.abspath("example_directory"))  # Возвращает полный путь

# Удалить пустую директорию
os.rmdir("example_directory/nested_folder")  # Удаляет только пустые директории

# Удалить директорию и всё её содержимое
shutil.rmtree("example_directory")  # Удаляет директорию и все файлы внутри

# Создать файл и записать в него данные
with open("example.txt", "w") as file:
    file.write("Привет, мир!")  # Запись текста в файл

# Прочитать файл
with open("example.txt", "r") as file:
    print(file.read())  # Чтение всего содержимого файла

# Переименовать файл
os.rename("example.txt", "new_example.txt")  # Переименовывает файл

# Удалить файл
os.remove("new_example.txt")  # Удаляет файл

# Получить информацию о файле
file_stats = os.stat("example.txt")  # Возвращает информацию о файле
print(f"Размер: {file_stats.st_size} байт")  # Размер файла
print(f"Дата изменения: {file_stats.st_mtime}")  # Время последнего изменения

# Рекурсивный поиск файлов по расширению
for root, _, files in os.walk("example_directory"):
    for file in files:
        if file.endswith(".txt"):  # Ищет файлы с расширением .txt
            print(os.path.join(root, file))  # Полный путь к файлу


import os
def list_content(path):
    os.mkdir(path)
    all_items = os.listdir(path)
    directories = [item for item in all_items if os.path.isdir(os.path.join(path, item))]
    print("Directories:", directories)
path = "test_dir" 
list_content(path)