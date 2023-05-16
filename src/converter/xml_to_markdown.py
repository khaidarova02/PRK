import io
import xmltodict

def Conv_MD(full_path, new_path):
    try:
        try:
            # Открываем XML-файл
            with io.open(full_path,'r', encoding="utf-8") as xml_file: # Открываем XML-файл
        # Парсим XML-файл в словарь
                data_dict = xmltodict.parse(xml_file.read())
        except PermissionError:
            print ("Недостаточно прав для чтения файла")
        else:
            with io.open(new_path, 'w', encoding="utf8") as md_file:
                for key in data_dict:
                    md_file.write(f"# {key}\n\n") # Заголовок наименования элемента
                    for subkey, subvalue in data_dict[key].items():
                        md_file.write(f"**{subkey}:** {subvalue}\n") #Строка с наименованием и значением
                    md_file.write("\n") # Добавляем пустую строку
    except Exception:
        print (f'File {full_path} cannot be converted')
