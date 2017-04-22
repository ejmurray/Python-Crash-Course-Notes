#!/bin/env python
#
# Collects all molfiles in a directory (the only and optional argument)
# and concatenates them in one SDfile.  The default directory to be
# processed is the current directory, and the output file is produced
# in the current directory.  Note that only files whose name ends in ".mol"
# are processed.
#
# The name of each individual molfile is added to its data section in the
# SDfile as a data field tagged by "filename".  If the CAS registry number
# is present in the comment line (and tagged using "#", e.g. "#50-00-0")
# it is added as a data field tagged by "casreg".
#
# Three options are available:
# /output=<filename> to specify the name of the SDfile (default is "out.sdf");
# /copyname (boolean) to copy the molfile name to its title (1st) line.
# /scale (boolean) to set the median bond length to 0.825.
#
# Two "corrections" are made to the molfile sections:
# The coordinates are shifted to put the left lower corner at (0,0)(for
# better display in ChemFileBrowser) and the second line (containing the
# dimension indicator) is corrected if necessary (because of bad Vitic
# output).  The last line is checked (it should read "M  END") and the
# numbers of atoms and bonds are also checked for internal consistency -
# however, no further sanity checking is performed.
#
# Usage:
#    mol2sdf.py  [ <options> ]  [ <directory> ]
#
# Options:
#    /output=<filename>:
#       to specify the name of the SDfile (default is "out.sdf");
#
#    /copyname:
#       (boolean) to copy the molfile name to its title (1st) line;
#
#    /scale:
#       (boolean) to set the median bond length to 0.825.
#
# Written dd. 14May2008 Martin A. Ott, Lhasa Limited, Leeds, UK
# Last update 09Jun2012 M.A. Ott
#
# Update history:
# 20120609: Added scaling functionality & option
# 20110223: Added copyname file option
# 20101129: Split out general and chemical functions
# 20101124: Added output file option
# 20081222: Split read_ctab from read_molfile
# 20080725: Added transfer of CAS reg from comment line to data field
# 20080716: Shifted atom coordinates for better display in ChemFileBrowser
# 20080716: Added checks for number of atoms and bonds in read_molfile
#


from os import listdir
from os.path import isfile
from sys import argv

from genutils import *
from chemutils import read_elements, read_molfile, process_molfile, \
    write_sdfile_section

#
# Main program.
#
argum_list = ['self', 'directory']
argum_dict = {'self': '', 'directory': '.'}
option_dict = {'output': 'out.sdf', 'copyname': False, 'scale': False}
(err_msg, argum_dict, option_dict) = \
    parse_commandline(argv, argum_list, argum_dict, option_dict)
if err_msg != '':
    plain_message('info', 'Usage:  mol2sdf.py  [ <options> ]  [ <directory> ]')
    plain_message('fatal', err_msg)
dir_name = argum_dict['directory']
file_name = option_dict['output']
if len(file_name) < 4 or \
        (file_name[-3:] != '.sd' and file_name[-4:] != '.sdf'):
    file_name = '%s.sdf' % file_name
(atomic_num, atomic_sym) = read_elements('elements.txt')
(out_file, err_msg) = try_open_file(file_name, 'w')
if out_file == None:
    plain_message('fatal', err_msg)
num = 0
file_names = listdir(dir_name)
file_names.sort()
for file_name in file_names:
    if file_name[-4:] == '.mol':
        full_name = '%s\%s' % (dir_name, file_name)
        if isfile(full_name):
            mol_file = read_molfile(full_name)
            (mol, mol_data) = process_molfile(atomic_num, file_name, mol_file, \
                                              option_dict['scale'])
            if option_dict['copyname']:
                mol['title'] = file_name
            write_sdfile_section(out_file, atomic_sym, mol, mol_data)
            num += 1
out_file.close()
plain_message('info', 'Collected %d molfile(s)' % num)
