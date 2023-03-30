import markdown
import os

def ConvHtml(file):
    # Читая sample.md и сохранение его содержимого в переменной markdown_string
    with open(file, 'r') as f:
        markdown_string = f.read()

    # Преобразование markdown (markdown_string) в HTML (html_string) с использованием метода markdown из пакета markdown.
    html_string = markdown.markdown(markdown_string)

    # Создание sample.html файл и запись в него HTML (html_string).
    file2 = os.path.splitext(file)[0]+".html"
    with open(file2, 'w') as f:
        f.write(html_string)
