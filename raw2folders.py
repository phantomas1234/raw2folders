#!/usr/bin/env python

import os
import sys
import shutil
import glob
from optparse import OptionParser

usage = "usage: %prog [options]"
parser = OptionParser(usage=usage)


parser.add_option("-i", "--input", dest="input_directory", default=".",
                  help="directory containing *.raw files (for example 5-3-2014_1000 uM Muconic aci_1001 + [73.04] - [44.65 - 45.35].raw)", metavar="PATH")
parser.add_option("-o", "--output", dest="output_directory", default=".",
                  help="where to put folders and files from processed *.raw files", metavar="PATH")
parser.add_option("-v", "--verbose", action="store_true", dest="verbose")

(options, args) = parser.parse_args()

if not os.path.exists(options.output_directory):
    os.mkdir(options.output_directory)

for path in glob.glob(os.path.join(options.input_directory, '*.raw')):
    if options.verbose:
        print "Processing", path
    basename = os.path.basename(path)
    (new_file, folder) = basename.split(' + ')
    folder = folder.replace('.raw', '')
    folder = os.path.join(options.output_directory, folder)
    if not os.path.exists(folder):
        os.mkdir(folder)
    final_destination = os.path.join(folder, new_file+'.raw')
    if options.verbose:
        print "Copying to", final_destination
    shutil.copy(path, final_destination)