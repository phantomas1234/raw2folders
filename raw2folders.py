#!/usr/bin/env python

__author__ = 'Nikolaus Sonnenschein'
__version__ = '0.0.3'

import os
import sys
import shutil
import glob
from argparse import ArgumentParser


parser = ArgumentParser()

parser.add_argument("input_directory", default=".",
                  help="directory containing *+*.* files (for example 5-3-2014_1000 uM Muconic aci_1001 + [73.04] - [44.65 - 45.35].raw)")
parser.add_argument("output_directory", default=".",
                  help="where to put folders and files from processed *+*.* files in addition to CSV file containing all processed files")
parser.add_argument("-v", "--verbose", action="store_true", dest="verbose", help='set for verbose output')

if len(sys.argv)==1:
    parser.print_help()
    sys.exit(1)

args = parser.parse_args()
if not os.path.exists(args.output_directory):
    os.mkdir(args.output_directory)

files_for_csv = set()
for path in glob.glob(os.path.join(args.input_directory, '*+*.*')):
    file_path_no_extension, file_extension = os.path.splitext(path)
    if args.verbose:
        print "Processing", path
    basename = os.path.basename(file_path_no_extension)
    (new_file, folder) = basename.split(' + ')
    # replace \s -> _ and . -> -
    new_file = new_file.replace(' ', '_').replace('.', '-')
    files_for_csv.add(new_file + file_extension)
    folder = os.path.join(args.output_directory, folder)
    if not os.path.exists(folder):
        os.mkdir(folder)
    final_destination = os.path.join(folder, new_file+file_extension)
    if args.verbose:
        print "Copying to", final_destination
    shutil.copy(path, final_destination)
with open(os.path.join(args.output_directory,'processed_files.csv'), 'w') as fhandle:
    for file in files_for_csv:
        fhandle.write(file + "\n")
