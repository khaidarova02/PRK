import argparse
import os

import ConverterInHtml as fromMd
import xml_to_markdown as fromXml


parser = argparse.ArgumentParser (prog='converter', description='File format conversion')
parser.add_argument('-d', '--directory', help='Input directory', nargs=1, required=True)
parser.add_argument('-x', '--xml', help='File type', action='store_true', required=False)
parser.add_argument('-m', '--markdown', help='File type', action='store_true', required=False)
parser.add_argument('-a', '--another', help='Output directory', nargs=1, required=False)


def get_change_file(full_path, new_path):
    
    if not os.path.exists(new_path):
        return True
    return os.path.getmtime(full_path) > os.path.getmtime(new_path)


def find_files(pathFrom, pathTo, type_f):

    for rootdir, dirs, files in os.walk(pathFrom):
        for f in files:       
            if not (f.split('.')[-1]) == type_f:
                continue

            full_path = os.path.join(rootdir, f)
            new_type_f = 'md' if type_f == 'xml' else 'html'
            new_path = full_path.replace(pathFrom, pathTo).replace(type_f, new_type_f)

            if not get_change_file(full_path, new_path):
                print(f'File {os.path.join(rootdir, f)} does not need to be converted')
                continue
                
            if type_f == 'md':
                fromMd.ConvHtml(full_path, new_path)
            else:
                fromXml.converter(full_path, new_path)


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


if __name__ == "__main__":
    main()
