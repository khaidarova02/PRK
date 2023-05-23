import markdown
import markdownify
import io

def Conv_MD(full_path, new_path):
    try:
        try:
            # Открываем XML-файл
            with io.open(full_path, 'r', encoding="utf-8") as f:
                # Считываем XML-файл 
                input_string = f.read()
        except PermissionError:
            print ("Недостаточно прав для чтения файла")
        else:
            # Конвертируем в markdown
            output_string = markdown.markdown(input_string)
            output_string = markdownify.markdownify(output_string)
            #Записываем в файл
            with io.open(new_path, 'w', encoding="utf-8") as f:
                f.write(output_string)
    except Exception:
        print (f'File {full_path} cannot be converted')
