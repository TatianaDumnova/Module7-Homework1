# ДЗ по теме "Режимы открытия файлов"

# Создайте в директории проекта текстовый файл с раширением txt
# Добавьте в этот файл следующий текст
# Создайте переменную с этим файлом
# Распечатайте содержимое текстового файла в консоль
# Закройте файл

# Вариант № 1
from pprint import pprint

file_name = 'byron.txt'
file = open(file_name, mode='rb')
file_content = file.read()
pprint(file_content)
file.close()

#Вариант № 2:

file_name = 'byron.txt'
file = open(file_name, mode='r')
file_content = file.read()
print(file_content)
file.close()
