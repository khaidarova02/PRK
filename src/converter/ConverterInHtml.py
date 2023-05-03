import markdown
import os

def ConvHtml(full_path, new_path): 
    if not os.access(full_path, os.R_OK): 
        print("Недостаточно прав для чтения файла")
        return
    # Читая sample.md и сохранение его содержимого в переменной markdown_string
    with open(full_path, 'r') as f:
        markdown_string = f.read()

    # Преобразование markdown (markdown_string) в HTML (html_string) с использованием метода markdown из пакета markdown.
    html_string = markdown.markdown(markdown_string)

    # Создание sample.html файл и запись в него HTML (html_string).
    with open(new_path, 'w') as f:
        f.write(html_string)
