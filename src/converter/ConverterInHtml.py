import markdown
import os


def convHtml(full_path, new_path): 
    # проверка на права доступа
    if not os.access(full_path, os.R_OK): 
        print("Недостаточно прав для чтения файла")
        return

    try:
        # Чтение файла и сохранение его содержимого в переменной markdown_string
        with open(full_path, 'r', encoding="utf-8") as f:
            markdown_string = f.read()

        # Преобразование markdown в HTML 
        # с использованием метода markdown из пакета markdown.
        html_string = markdown.markdown(markdown_string)

    except Exception:
        print (f'File {full_path} cannot be converted')
        return

    # Открываем файл с блоком div
    with open('header.html', 'r', encoding="utf-8") as f:
        header = f.read()
    
    pos = header.find('<main>')
    html_string = header[:pos] + html_string + header[pos:]

    # Создание файла и запись в него HTML (html_string).
    with open(new_path, 'w', encoding="utf-8") as f:
        f.write(html_string)
