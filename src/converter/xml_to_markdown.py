'''Модуль для работы с ОС'''
import os
import io
import xmltodict
def Conv_MD(full_path, new_path):
    '''Функция для конвертации xml-файла в markdown-файл'''
    if os.access(full_path, os.R_OK): # Выполняем проверку прав на чтение
        with io.open(full_path,'r', encoding="utf-8") as xml_file: # Открываем XML-файл
        # Парсим XML-файл в словарь
            data_dict = xmltodict.parse(xml_file.read())

        # Создаем и открываем Markdown-файл для записи
        with io.open(new_path, 'w', encoding="utf8") as md_file:
            # Проходимся по элементам словаря и записываем соответствующие строки в Markdown-файл
            for key in data_dict:
                md_file.write(f"# {key}\n\n") # Заголовок наименования элемента
                for subkey, subvalue in data_dict[key].items():
                    md_file.write(f"**{subkey}:** {subvalue}\n") #Строка с наименованием и значением
                md_file.write("\n") # Добавляем пустую строку
    else:
        print("Недостаточно прав для чтения файла")
