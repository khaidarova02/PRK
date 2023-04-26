import xmltodict
import os

def ConvMD(xml):
    # Выполняем проверку прав на чтение
    if os.access(xml, os.R_OK):
       # Открываем XML-файл
        with open(xml,'r') as xml_file:
            # Парсим XML-файл в словарь
            data_dict = xmltodict.parse(xml_file.read())

    # Создаем и открываем Markdown-файл для записи
        md = os.path.splitext(xml)[0]+".md"
        with open(md, 'w') as md_file:
            # Проходимся по элементам словаря и записываем соответствующие строки в Markdown-файл
            for key in data_dict:
                md_file.write(f"# {key}\n\n")  # Заголовок наименования элемента
                for subkey, subvalue in data_dict[key].items():
                    md_file.write(f"**{subkey}:** {subvalue}\n")  # Строка с наименованием и значением
                md_file.write("\n")  # Добавляем пустую строку между элементами
    else:
        print("Недостаточно прав для чтения файла")
