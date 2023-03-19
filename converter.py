import argparse
import os

parser = argparse.ArgumentParser (prog='converter', description='File format conversion')
parser.add_argument('-d', '--directory', help='Input directory', nargs=1, required=True)
parser.add_argument('-x', '--xml', help='File type', action='store_true', required=False)
parser.add_argument('-m', '--markdown', help='File type', action='store_true', required=False)
parser.add_argument('-a', '--another', help='Output directory', nargs=1, required=False)
args = parser.parse_args()

def find_files(type_f):
    path=args.directory

    for p in path:
        for rootdir, dirs, files in os.walk(p):
            for f in files:       
                if((f.split('.')[-1]) == type_f):
                    print(os.path.join(rootdir, f))
                
if args.xml:
    find_files('xml')
elif args.markdown:
    find_files('md')
else:
    print("Enter one type")

