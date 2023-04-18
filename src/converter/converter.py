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


"""
   Сравненивает даты последнего изменения исходного файла 
   и преобразованного, если тот существует

   Parameters
   ----------
   full_path : str
         полный путь до исходного файла
   new_path : str
         полный путь до преобразованного файла

   Return
   ----------
   True : bool
         Если файл требует преобразования
   False : bool
         Если файл не требует преобразования
"""
def file_changed(full_path, new_path):
    
    if not os.path.exists(new_path):
        return True
    return os.path.getmtime(full_path) > os.path.getmtime(new_path)


"""
   Перебирает исходную директорию и передает файлы
   указанного формата в соответствующий модуль преобразования

   Parameters
   ----------
   pathFrom : str
         исходная директория
   pathTo : str
         директория для сохранения
   type_f : str
         тип файла для преобразования
"""
def find_files(pathFrom, pathTo, type_f):

    for rootdir, dirs, files in os.walk(pathFrom):
        for f in files:       
            if not (f.split('.')[-1]) == type_f:
                continue

            full_path = os.path.join(rootdir, f)
            new_type_f = 'md' if type_f == 'xml' else 'html'
            new_path = full_path.replace(pathFrom, pathTo).replace(type_f, new_type_f)

            if not file_changed(full_path, new_path):
                print(f'File {full_path} does not need to be converted')
                continue
                
            if type_f == 'md':
                fromMd.ConvHtml(full_path, new_path)
            else:
                fromXml.ConvMD(full_path, new_path)


"""
   Проверяет правильность введенных данных и
   вызывает функцию поиска файлов указанного формата
"""
def main():
    
    args = parser.parse_args()
    
    pathFrom = args.directory[0]
    pathTo = args.directory[0]

    if not os.path.exists(pathFrom):
        print(f'Object {pathFrom} not found')
        return

    if args.another:
        pathTo = args.another[0]

        if not os.path.exists(pathTo):
            print(f'Object {pathTo} not found')
            return
    
    if (args.xml and args.markdown) or (not args.xml and not args.markdown):
        print("Enter one type: -x or -m")
        return

    pathFrom = pathFrom.replace('/', '\\')
    pathTo = pathTo.replace('/', '\\')
    if args.xml:
        find_files(pathFrom, pathTo, 'xml')
    else:
        find_files(pathFrom, pathTo, 'md')


"""
   Проверка, что программа была запущена
"""
if __name__ == "__main__":
    main()
