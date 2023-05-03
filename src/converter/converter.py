# -----------------------------------------------------------
# Преобразователь XML->MD->HTML
#
# (C) 2023 Alisa Haidarova, PetrGU, Petrozavodsk, Russia
# License: GNU General Public License (GPL)
# Email: i.nesy.chav@gmail.com
# -----------------------------------------------------------

import argparse
import os

import ConverterInHtml as fromMd
import xml_to_markdown as fromXml

# Обозначение ключей
#
# -d, --directory    Выбор директории, из которой требуется преобразовать файлы
# -x, --xml          Преобразование из XML в MarkDown
# -m, --markdown     Преобразование из MarkDown в HTML
# -a, --another      Выбор директории, в которую требуется сохранить преобразованные файлы

parser = argparse.ArgumentParser (prog='converter', description='File format conversion')
parser.add_argument('-d', '--directory', help='Input directory', nargs=1, required=True)
parser.add_argument('-x', '--xml', help='File type', action='store_true', required=False)
parser.add_argument('-m', '--markdown', help='File type', action='store_true', required=False)
parser.add_argument('-a', '--another', help='Output directory', nargs=1, required=False)


def file_changed(src_path, dst_path):
    """
       Сравненивает даты последнего изменения исходного файла 
       и преобразованного, если тот существует

       Parameters
       ----------
       src_path : str
             исходный путь (включает название файла)
       dst_path : str
             путь назначения (включает название файла)

       Return
       ----------
       True : bool
             Если файл требует преобразования
       False : bool
             Если файл не требует преобразования
    """
    if not os.path.exists(dst_path):
        return True
    return os.path.getmtime(src_path) > os.path.getmtime(dst_path)


def find_files(src_dir, dst_dir, type_f):
    """
       Перебирает исходную директорию и передает файлы
       указанного формата в соответствующий модуль преобразования

       Parameters
       ----------
       src_dir : str
             исходная директория
       dst_dir : str
             директория назначения
       type_f : str
             тип файла для преобразования
    """
    for rootdir, dirs, files in os.walk(src_dir):
        for f in files:       
            if not (f.split('.')[-1]) == type_f:
                continue

            src_path = os.path.join(rootdir, f)
            new_type_f = 'md' if type_f == 'xml' else 'html'
            dst_path = src_path.replace(src_dir, dst_dir).replace(type_f, new_type_f)
            
            new_dir = rootdir.replace(src_dir, dst_dir)
            if not os.path.exists(new_dir):
                os.makedirs(new_dir)

            if not file_changed(src_path, dst_path):
                print(f'File {src_path} does not need to be converted')
                continue
                
            if type_f == 'md':
                fromMd.ConvHtml(src_path, dst_path)
            else:
                fromXml.Conv_MD(src_path, dst_path)


def main():
    """
       Проверяет правильность введенных данных и
       вызывает функцию поиска файлов указанного формата
    """
    
    args = parser.parse_args()
    
    src_dir = args.directory[0]
    dst_dir = args.directory[0]

    if not os.path.exists(src_dir):
        print(f'Object {src_dir} not found')
        return

    if args.another:
        dst_dir = args.another[0]

        if not os.path.exists(dst_dir):
            print(f'Object {dst_dir} not found')
            return
    
    if (args.xml and args.markdown) or (not args.xml and not args.markdown):
        print("Enter one type: -x or -m")
        return

    src_dir = src_dir.replace('/', '\\')
    dst_dir = dst_dir.replace('/', '\\')
    if args.xml:
        find_files(src_dir, dst_dir, 'xml')
    else:
        find_files(src_dir, dst_dir, 'md')


"""
   Проверка, что программа была запущена
"""
if __name__ == "__main__":
    main()
