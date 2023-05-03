import markdown
import os

def ConvHtml(full_path, new_path): 
    # проверка на права доступа
    if not os.access(full_path, os.R_OK): 
        print("Недостаточно прав для чтения файла")
        return

    # Чтение файла и сохранение его содержимого в переменной markdown_string
    with open(full_path, 'r') as f:
        markdown_string = f.read()

    # Преобразование markdown (markdown_string) в HTML (html_string) с использованием метода markdown из пакета markdown.
    html_string = markdown.markdown(markdown_string)

     # Создание файла и запись в него HTML (html_string).

    with open(new_path, 'w') as f:
        f.write(html_string)
