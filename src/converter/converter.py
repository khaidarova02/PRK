import argparse
import os


parser = argparse.ArgumentParser (prog='converter', description='File format conversion')
parser.add_argument('-d', '--directory', help='Input directory', nargs=1, required=True)
parser.add_argument('-x', '--xml', help='File type', action='store_true', required=False)
parser.add_argument('-m', '--markdown', help='File type', action='store_true', required=False)
parser.add_argument('-a', '--another', help='Output directory', nargs=1, required=False)
args = parser.parse_args()


def get_change_file(path_f, name_f, type_f):
    new_f = os.path.join(path_f, name_f)

    if args.another:
        old_path = args.directory[0]
        new_path = args.another[0]
        path_f = path_f.replace(old_path, new_path)

    type_f = 'xml' if type_f == 'md' else 'md'
    name_f = name_f.split('.')[0] + type_f

    path_f = os.path.join(path_f, name_f)
    if os.path.exists(path_f):
        return os.path.getmtime(path_f) < os.path.getmtime(new_f)
    else:
        return True


def find_files(type_f):
    path = args.directory[0]
    
    if os.path.exists(p):
        for rootdir, dirs, files in os.walk(p):
            for f in files:       
                if (f.split('.')[-1]) == type_f:
                    if readable(f):
                        if get_change_file(rootdir, f, type_f):
                            print(os.path.join(rootdir, f))
                        else:
                            print(f'File {f} does not need to be converted')
                    else:
                        print(f'File {f} cannot be read')
    else:
        print(f'Object {p} not found')


def get_type_files():

    if args.xml:
        find_files('xml')
    elif args.markdown:
        find_files('md')
    else:
        print("Enter one type")


if __name__ == "__main__":
    get_type_files()

