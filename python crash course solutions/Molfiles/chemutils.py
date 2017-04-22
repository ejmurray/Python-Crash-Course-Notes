#!/bin/env python
#
# Chemical utilities:  molfile, SDfile and rxnfile reading, parsing and
# writing, plus elements file reading.
#
# Written dd. 29Nov2010 Martin A. Ott, Lhasa Limited, Leeds, UK
# Last update 23Jun2012 M.A. Ott
#
# Update history:
# 20120623: Removed automatic file name addition from parse_sdfile
# 20120328: Added scaling functionality
# 20111126: Added error check for one-membered ring
# 20110819: Added read_element_data
# 20110220: Added rxnfile read/parse/write functions
# 20110207: Modified to allow invalid/empty molfile version
# 20101207: Modified to allow zero-atom molfiles
#


from math import sqrt
from time import localtime, strftime, strptime
from types import ListType

from genutils import *


def read_elements(file_name):
    """Read periodic table and return elements."""
    #
    # Read file_name (containing a textual description of the periodic table
    # of the elements) and return the elements in the form of two dictionaries:
    # atomic symbol -> atomic number and atomic number -> atomic symbol.
    #
    top_element = 112
    (elem_file, err_msg) = try_open_file(file_name, 'r')
    if elem_file is None:
        (elem_file, err_msg) = try_open_file('H:\\%s' % file_name, 'r')
        if elem_file is None:
            plain_message('fatal', err_msg)
    lines = elem_file.readlines()
    elem_file.close()
    atomic_num, atomic_sym = {}, {}
    atomic_num['D'] = 1
    atomic_num['T'] = 1
    for line in lines:
        if line[0] == ' ':
            items = line.split()
            if len(items) != 9:
                return None, None
            num = get_int(items[0], None)
            if num is None:
                return None, None
            sym = items[1]
            if len(sym) < 1 or len(sym) > 2:
                return None, None
            atomic_num[sym] = num
            atomic_sym[num] = sym
            if num == top_element:
                break
    if top_element not in atomic_sym.keys():
        return None, None
    return atomic_num, atomic_sym


def read_element_data(file_name):
    """Read periodic table and return elements with their data."""
    #
    # Read file_name (containing a textual description of the periodic table
    # of the elements) and return the elements in the form of five dictionaries:
    # atomic number, atomic symbol, element name, atomic mass, element type,
    # and valency data.
    # All are keyed on atomic number except atomic number which is keyed on
    # atomic symbol. Element types are: [A]lkali metal, alkaline [E]arth metal,
    # [T]ransition metal, [R]are earth metal (= La/Ac), [P]oor metal, [M]etalloid,
    # and [N]on-metal.  The valency data for an element consist of a duple
    # (maximum number of valence el., number of valence el. of the free atom).
    #
    top_element = 112
    element_types = ['A', 'E', 'T', 'R', 'P', 'M', 'N']
    (elem_file, err_msg) = try_open_file(file_name, 'r')
    if elem_file is None:
        (elem_file, err_msg) = try_open_file('H:\\%s' % file_name, 'r')
        if elem_file is None:
            plain_message('fatal', err_msg)
    lines = elem_file.readlines()
    elem_file.close()
    atomic_num, atomic_sym, element_name, atomic_mass, element_type, \
    valency_data = {}, {}, {}, {}, {}, {}
    atomic_num['D'] = 1
    atomic_num['T'] = 1
    for line in lines:
        if line[0] == ' ':
            items = line.split()
            if len(items) != 9:
                return None, None, None, None, None, None
            num = get_int(items[0], None)
            if num is None:
                return None, None, None, None, None, None
            sym = items[1]
            if len(sym) < 1 or len(sym) > 2:
                return None, None, None, None, None, None
            atomic_num[sym] = num
            atomic_sym[num] = sym
            sym = items[2]
            if sym not in element_types:
                return None, None, None, None, None, None
            element_type[num] = sym
            mval = get_int(items[3], None)
            if mval < 2 or mval > 24:
                return None, None, None, None, None, None
            dval = get_int(items[4], None)
            if dval < 1 or dval > 17:
                return None, None, None, None, None, None
            valency_data[num] = (mval, dval)
            mass = get_real(items[7], None)
            if mass is None:
                return None, None, None, None, None, None
            atomic_mass[num] = mass
            sym = items[8]
            if len(sym) < 3 or len(sym) > 16:
                return None, None, None, None, None, None
            element_name[num] = sym
            if num == top_element:
                break
    if top_element not in atomic_sym.keys():
        return None, None, None, None, None, None
    return atomic_num, atomic_sym, element_name, atomic_mass, element_type, valency_data


def read_ctab(lines, line_0):
    """Read connection table section of a molfile."""
    #
    # Read connection table section of a molfile/SDfile from a list of lines
    # starting at line_0.  Return the connection table section and the number
    # of the last line read (should be the "M  END" line).
    # If something is (fatally) wrong, err_msg is returned non-empty.
    #
    err_msg, mol_file, line_no = '', [], line_0
    end_read, count, atom_num, bond_num = False, 0, -1, -1
    for line in lines[line_0:]:
        outl = line.rstrip()
        count += 1
        line_no += 1
        if count == 4 and len(outl) > 5:
            atom_num = get_int(outl[0:3], -1)
            bond_num = get_int(outl[3:6], -1)
        mol_file.append('%s\n' % outl)
        if outl == 'M  END':
            end_read = True
            break
    if not end_read:
        err_msg = 'Missing "M  END"'
    elif atom_num < 0 or bond_num < 0:
        err_msg = 'Bad number of atoms or bonds'
    elif atom_num == 0 and bond_num != 0:
        err_msg = 'Zero atoms but non-zero bonds'
    elif count < atom_num + bond_num + 5:
        err_msg = 'Too few lines for atoms/bonds'
    return err_msg, mol_file, line_no


def read_molfile(file_name):
    """Read molfile file_name and bail out if format is incorrect."""
    #
    # Read file file_name (supposed to contain one molfile) and return
    # a list of lines.  Check that the number of lines is consistent with
    # the number of atoms/bonds, that there is at least one atom, and
    # that the last line is "M  END".  Bail out if something is wrong.
    #
    (in_file, err_msg) = try_open_file(file_name, 'r')
    if in_file is None:
        plain_message('fatal', err_msg)
    plain_message('info', 'Reading %s' % file_name)
    lines = in_file.readlines()
    in_file.close()
    (err_msg, mol_file, line_no) = read_ctab(lines, 0)
    if err_msg != '':
        plain_message('fatal', '%s in %s' % (err_msg, file_name))
    if len(lines) > line_no:
        plain_message('warning', 'Data beyond "M  END" in %s' % file_name)
    return mol_file


def parse_molfile_line1(line):
    """Process the first (title) line of a molfile."""
    #
    # Obtain the molfile title (compound name) and any synonyms from the
    # first (title) line of a molfile.  Synonyms are supposed to be separated
    # by a semicolon.  The first synonym is taken to be the molfile title.
    #
    synonyms = []
    items = line.split(';')
    for itemp in items:
        item = itemp.strip()
        if item != '' and item not in synonyms:
            synonyms.append(item)
    return synonyms


def parse_molfile_line2(line):
    """Process the second line of a molfile."""
    #
    # Obtain the dimension (2D/3D) indicator and other fields (user, program
    # and date) from the second line in a molfile.  An attempt will be made
    # to correct a wrong alignment of the fields (specifically, when the
    # dimension indicator is one position too far to the left).
    #
    mdl_time_format = '%m%d%y%H%M'
    user = line[0:2].strip()
    prog = line[2:10].strip()
    date = line[10:20].strip()
    dime = line[20:22].strip()
    dimi = 2
    if dime == 'D':
        prog = line[2:9].strip()
        date = line[9:19].strip()
        dime = line[19:21].strip()
        plain_message('warning', 'Badly aligned dimension indicator')
    num = get_int(date, -1)
    if num >= 101000000:
        try:
            tim = strptime(date, mdl_time_format)
        except:
            tim = None
    else:
        tim = None
    if tim is None:
        plain_message('warning', 'Cannot parse date/time')
        date = strftime(mdl_time_format)
    else:
        date = strftime(mdl_time_format, tim)
    if dime == '3D':
        plain_message('info', 'Molecule is a 3D structure')
        dimi = 3
    elif dime != '2D':
        if dime == '':
            plain_message('warning', 'Missing dimension indicator - set at 2D')
        else:
            plain_message('warning', 'Invalid dimension indicator - set at 2D')
    return '%-2s%-8s%10s%1dD' % (user, prog, date, dimi)


def parse_molfile_line3(synonyms, line):
    """Process the third (comment) line of a molfile."""
    #
    # Obtain various values from the third (comment) line of a molfile.
    # Recognised are: CAS registry number (tagged by "#"), systematical name
    # (tagged by "+") and external ID string (tagged by "@").
    #
    tags = {'casreg': '#', 'extreg': '@', 'sysnam': '+'}
    new_syns = synonyms
    casregs = []
    extregs = []
    sysnames = []
    items = line.split(';')
    for itemp in items:
        item = itemp.strip()
        if item != '':
            if item[0] == tags['casreg']:
                (msg, casreg) = parse_casreg(item[1:])
                if casreg is None:
                    plain_message('warning', msg)
                else:
                    plain_message('info', 'CAS registry number: %s' % casreg)
                    if casreg not in casregs:
                        casregs.append(casreg)
            elif item[0] == tags['extreg']:
                if len(item) < 2:
                    plain_message('warning', 'Missing external ID string')
                else:
                    extreg = item[1:]
                    plain_message('info', 'External ID string: %s' % extreg)
                    if extreg not in extregs:
                        extregs.append(extreg)
            elif item[0] == tags['sysnam']:
                if len(item) < 2:
                    plain_message('warning', 'Missing systematical name')
                else:
                    sysname = item[1:]
                    plain_message('info', 'Systematical name: %s' % sysname)
                    if sysname not in sysnames:
                        sysnames.append(sysname)
                    if sysname not in new_syns:
                        new_syns.append(sysname)
            else:
                plain_message('warning', 'Unmarked string "%s" discarded' % item)
    if len(sysnames) > 1:
        plain_message('warning', 'More than one systematical name; kept first')
    return new_syns, casregs, extregs, sysnames


def parse_molfile(atomic_num, mol_file):
    """Parse mol_file and return a data structure with the info."""
    #
    # Take mol_file (a list of lines), parse the contents, and put the
    # information into a dictionary.
    #
    # Structure of the molecule dictionary:
    #    title
    #    abs_flag (0/1) (a.k.a. "chiral flag")
    #    dimens (2/3) (2D or 3D structure)
    #    atoms (list of dictionaries; see below)
    #    bonds (list of dictionaries; see below)
    # atoms:
    #    T atom_type
    #    C charge
    #    I isotope
    #    R radical
    #    V valence
    #    B bonds
    #    X x_co
    #    Y y_co
    #    Z z_co
    #    M map#
    # bonds:
    #    T bond_type
    #    1 atom_1
    #    2 atom_2
    #    S stereo
    #
    # Note that the error checking is not exhaustive.  The function bails out
    # fatally if something is wrong.
    #
    mdl_valency_0, rgroup_offset = 15, 155
    mol, atoms, bonds = {}, [], []
    mol['title'] = mol_file[0].strip()
    line = '%-22s' % mol_file[1].rstrip()
    mol['dimens'] = get_int(line[20:21], 0)
    if mol['dimens'] != 3:
        mol['dimens'] == 2
    line = '%-40s' % mol_file[3].rstrip()
    mf_version = line[34:39].strip()
    if mf_version == 'V3000':
        plain_message('fatal', 'Molfile version is V3000 - cannot parse')
    elif mf_version == '':
        plain_message('warning', 'No molfile version')
    elif mf_version != 'V2000':
        plain_message('warning', 'Bad molfile version "%s"' % mf_version)
    atom_num = get_int(line[0:3], -1)
    bond_num = get_int(line[3:6], -1)
    mol['abs_flag'] = get_int(line[12:15], 0)
    if atom_num < 0 or bond_num < 0:
        plain_message('fatal', 'Bad number of atoms or bonds')
    #
    # Read the atoms section.
    #
    for line in mol_file[4:4 + atom_num]:
        line = '%-52s' % line.rstrip()
        atom = {'B': [], 'I': 0, 'C': 0, 'R': 0, 'V': None}
        sym = line[31:33].strip()
        if sym == 'D' or sym == 'T':
            if sym == 'D':
                atom['I'] = 2
            else:
                atom['I'] = 3
            sym = 'H'
        if sym in atomic_num.keys():
            atom['T'] = atomic_num[sym]
        elif sym == 'R#':
            #
            # R group; the "atom type" will correspond to the actual R group number
            # (in fact rgroup_offset + number), which will be read from the property
            # line(s).
            #
            atom['T'] = None
        elif sym == 'Du':
            plain_message('warning', 'Dummy atom encountered')
            atom['T'] = -1
        else:
            plain_message('fatal', 'Unrecognised atom symbol "%s"' % sym)
        x = get_real(line[0:10], None)
        y = get_real(line[10:20], None)
        z = get_real(line[20:30], None)
        if x == None or y == None or z == None:
            plain_message('fatal', 'Bad coordinate in "%s"' % line[0:30])
        atom['X'] = int(10000.0 * x + 0.2)
        atom['Y'] = int(10000.0 * y + 0.2)
        atom['Z'] = int(10000.0 * z + 0.2)
        num = get_int(line[48:51], 0)
        if num > 0:
            if num == mdl_valency_0:
                atom['V'] = 0
            else:
                atom['V'] = num
        atom['M'] = get_int(line[60:63], 0)
        atoms.append(atom)
    #
    # Read the bonds section.
    #
    for line in mol_file[4 + atom_num:4 + atom_num + bond_num]:
        bond = {}
        atom_1 = get_int(line[0:3], 0)
        atom_2 = get_int(line[3:6], 0)
        if atom_1 < 1 or atom_1 > atom_num or atom_2 < 1 or atom_2 > atom_num:
            plain_message('fatal', 'Bad atom number(s) in bond')
        if atom_1 == atom_2:
            plain_message('fatal', 'One-membered ring')
        atom_1_t = atoms[atom_1 - 1]['T']
        atom_2_t = atoms[atom_2 - 1]['T']
        if (atom_1_t > 0 or atom_1_t == None) and \
                (atom_2_t > 0 or atom_2_t == None):
            bond['T'] = get_int(line[6:9], 0)
            if bond['T'] < 1 or bond['T'] > 4:
                plain_message('fatal', 'Bad bond type')
            bond['S'] = get_int(line[9:12], 0)
            if bond['S'] < 0 or bond['S'] > 6:
                plain_message('fatal', 'Bad bond stereo')
            if atom_2 > atom_1 or bond['T'] == 1 or bond['T'] == 6:
                bond['1'], bond['2'] = atom_1 - 1, atom_2 - 1
            else:
                bond['1'], bond['2'] = atom_2 - 1, atom_1 - 1
            bonds.append(bond)
        #
        # Read the rest, i.e., the properties section.
        #
    for line in mol_file[4 + atom_num + bond_num:]:
        if line[0] == 'M':
            tag = line[3:6]
            if tag == 'END':
                break
            if tag == 'CHG' or tag == 'RAD' or tag == 'ISO' or tag == 'RGP':
                count = get_int(line[6:9], -1)
                if count < 1 or count > 8:
                    plain_message('fatal', 'Bad number of property items')
                if len(line) < 8 * count + 9:
                    plain_message('fatal', 'Property line too short')
                itemstr = line[9:(8 * count + 9)]
                for num in range(count):
                    atom = get_int(itemstr[(8 * num):(8 * num + 4)], -1)
                    valu = get_int(itemstr[(8 * num + 4):(8 * num + 8)], None)
                    if atom == -1 or valu == None:
                        plain_message('fatal', 'Invalid property line')
                    #
                    # If atom is an R group, set its "atom type" to the R group number (+ offset).
                    #
                    if tag == 'RGP':
                        atoms[atom - 1]['T'] = valu + rgroup_offset
                    else:
                        atoms[atom - 1][tag[0]] = valu
            else:
                plain_message('warning', 'Line ignored "%s"' % line.strip())
        else:
            plain_message('warning', 'Line ignored "%s"' % line.strip())
        #
        # Put bond references in the atom connection data.  Note that this
        # information is redundant but allows faster manipulation.
        #
    num = 0
    for bond in bonds:
        atoms[bond['1']]['B'].append(num)
        atoms[bond['2']]['B'].append(num)
        num += 1
    mol['atoms'] = atoms
    mol['bonds'] = bonds
    return mol


def read_data(lines, line_0):
    """Read data section from an SDfile."""
    #
    # Read compound data from the data section of an SDfile from a list of
    # lines starting at line_0.  Return the data dictionary and the total
    # number of lines read from the SDfile.
    # If something is (fatally) wrong, err_msg is returned non-empty.
    #
    err_msg, mol_data, line_no = '', {}, line_0
    end_read = False
    while line_no < len(lines):
        line = lines[line_no]
        outl = line.rstrip()
        line_no += 1
        if len(outl) > 0:
            if outl == '$$$$':
                end_read = True
                break
            elif outl[0] == '>':
                tag = True
                items = outl.split('>')
                if len(items) < 3:
                    err_msg = 'Bad data tag "%s"' % outl
                    break
                loc = items[1].find('<')
                if loc < 0:
                    err_msg = 'Bad data tag "%s"' % outl
                    break
                field = items[1][loc + 1:]
            else:
                if field in mol_data.keys():
                    mol_data[field].append(outl.strip())
                else:
                    mol_data[field] = [outl.strip()]
    if err_msg != '' and not end_read:
        err_msg = 'Missing "$$$$"'
    return (err_msg, mol_data, line_no)


def parse_sdfile(atomic_num, file_name):
    """Read an SDfile and return its molfiles and data sections."""
    #
    # Read file file_name (supposed to contain an SDfile) and return the
    # molfile/data sections as two lists.  Bail out fatally if something
    # is wrong.
    #
    max_molfile = 10000
    mols, mol_datas = [], []
    (in_file, err_msg) = try_open_file(file_name, 'r')
    if in_file is None:
        plain_message('fatal', err_msg)
    plain_message('info', 'Reading %s' % file_name)
    lines = in_file.readlines()
    in_file.close()
    if len(lines) < 6:
        plain_message('fatal', 'Too few lines in %s' % file_name)
    molfile_no = 0
    line_no = 0
    while line_no < len(lines):
        if molfile_no == max_molfile:
            plain_message('warning', 'Reached structure #%d in %s; stopped' % \
                          (max_molfile + 1, file_name))
            break
        (err_msg, mol_file, line_no) = read_ctab(lines, line_no)
        if err_msg != '':
            plain_message('fatal', '%s in %s' % (err_msg, file_name))
        (err_msg, mol_data, line_no) = read_data(lines, line_no)
        if err_msg != '':
            plain_message('fatal', '%s in %s' % (err_msg, file_name))
        molfile_no += 1
        mols.append(parse_molfile(atomic_num, mol_file))
        mol_datas.append(mol_data)
    return mols, mol_datas


def read_rxnfile(file_name):
    """Read rxnfile and bail out if format is incorrect."""
    #
    # Read file file_name (supposed to contain one rxnfile) and return a list
    # of reactants and a list of products (as lists of lines i.e. molfiles).
    # Check the contents of each molfile.  Bail out if something is wrong.
    #
    reactants = []
    products = []
    flip = False
    (in_file, err_msg) = try_open_file(file_name, 'r')
    if in_file is None:
        plain_message('fatal', err_msg)
    plain_message('info', 'Reading %s' % file_name)
    lines = in_file.readlines()
    in_file.close()
    if len(lines) < 19:
        plain_message('fatal', 'Too few lines in %s' % file_name)
    if lines[0][0:4] != '$RXN':
        plain_message('fatal', 'No "$RXN" (line 1) in %s' % file_name)
    if lines[5][0:4] != '$MOL':
        plain_message('fatal', 'No "$MOL  (line 6)in %s' % file_name)
    reac_num = get_int(lines[4][0:3], -1)
    prod_num = get_int(lines[4][3:6], -1)
    if reac_num <= 0 or prod_num <= 0:
        plain_message('fatal', 'Zero reactants or products in %s' % file_name)
    curr_line = 5
    for count in range(reac_num):
        if lines[curr_line][0:4] != '$MOL':
            plain_message('fatal', 'Missing reactant in %s' % file_name)
        curr_line += 1
        if len(lines) < curr_line + 3:
            plain_message('fatal', 'Too few lines in %s' % file_name)
        (err_msg, mol_file, line_no) = read_ctab(lines[curr_line:], 0)
        if err_msg != '':
            plain_message('fatal', err_msg)
        reactants.append(mol_file)
        curr_line += line_no
    for count in range(prod_num):
        if lines[curr_line][0:4] != '$MOL':
            plain_message('fatal', 'Missing reactant in %s' % file_name)
        curr_line += 1
        if len(lines) < curr_line + 3:
            plain_message('fatal', 'Too few lines in %s' % file_name)
        (err_msg, mol_file, line_no) = read_ctab(lines[curr_line:], 0)
        if err_msg != '':
            plain_message('fatal', err_msg)
        products.append(mol_file)
        curr_line += line_no
    return reactants, products


def parse_rxnfile(atomic_num, reactants, products):
    """Parse reactants and products and them as structured data."""
    #
    # Take reactants and products (lists of lines), parse the contents, and
    # put the information into dictionaries.
    #
    new_reactants, new_products = [], []
    for molecule in reactants:
        new_reactants.append(parse_molfile(atomic_num, molecule))
    for molecule in products:
        new_products.append(parse_molfile(atomic_num, molecule))
    return new_reactants, new_products


def reset_coords(mol, scale):
    """Reset and optionally rescale the coordinates of mol."""
    #
    # Reset the coordinates of mol (simple translation).  The left lower
    # corner will be at (0,0).  If scale is true, then the coordinates will
    # be re-scaled such that the median bond length becomes 0.825.
    #
    new_mol = mol
    atom_num = len(mol['atoms'])
    #
    # Find lowest X and Y coordinates.
    #
    min_x, min_y = None, None
    for num in range(atom_num):
        (x_co, y_co) = (mol['atoms'][num]['X'], mol['atoms'][num]['Y'])
        if min_x is None or min_x > x_co:
            min_x = x_co
        if min_y is None or min_y > y_co:
            min_y = y_co
    if scale and len(mol['bonds']) > 0:
        bond_lengths = []
        for bond in mol['bonds']:
            atom_1, atom_2 = bond['1'], bond['2']
            x1 = float(mol['atoms'][atom_1]['X'])
            y1 = float(mol['atoms'][atom_1]['Y'])
            x2 = float(mol['atoms'][atom_2]['X'])
            y2 = float(mol['atoms'][atom_2]['Y'])
            bond_lengths.append((x1 - x2) ** 2 + (y1 - y2) ** 2)
        bond_lengths.sort()
        median = sqrt(bond_lengths[len(bond_lengths) / 2])
    else:
        median = 0.0
    if median == 0.0:
        for num in range(atom_num):
            new_mol['atoms'][num]['X'] = mol['atoms'][num]['X'] - min_x
            new_mol['atoms'][num]['Y'] = mol['atoms'][num]['Y'] - min_y
    else:
        if median > 8249.0 and median < 8251.0:
            factor = 1.0
        else:
            factor = 8250.0 / median
        for num in range(atom_num):
            new_mol['atoms'][num]['X'] = \
                int(0.5 + factor * (mol['atoms'][num]['X'] - min_x))
            new_mol['atoms'][num]['Y'] = \
                int(0.5 + factor * (mol['atoms'][num]['Y'] - min_y))
    return new_mol


def process_molfile(atomic_num, filename, mol_file, scale):
    """Process mol_file (having name filename)."""
    #
    # Take mol_file (a list of lines), set the left lower corner of the
    # atom coordinates at (0,0), and collect various data fields.  The
    # results are returned as a molecule and associated data dictionary.
    # The collected data fields are: "name" and "synonyms" containing the
    # name(s) of the compound; "filename" containing the file name of the
    # original molfile; "casreg" containing the CAS registry number (if
    # present); "extreg" containing an external ID string (if present);
    # and "sysname" containing its systematical name (if present).
    # The name is derived from the first (title) line of mol_file.  More
    # names, separated by ";", can be present and will end up as synonyms.
    # The CAS registry number, external ID string and systematical name are
    # expected in the comment line, tagged by "#", "@" and "+" respectively.
    # If scale is true, then the coordinates are re-scaled such that the
    # median bond length becomes 0.825.
    #
    mol_data = {'filename': filename}
    #
    # Find name and synonyms from the title (first) line.
    #
    synonyms = parse_molfile_line1(mol_file[0])
    #
    # Find CAS registry number, external ID string and systematical name
    # from the comment (third) line.
    #
    (synonyms, casregs, extregs, sysnames) = \
        parse_molfile_line3(synonyms, mol_file[2])
    name = ''
    if len(synonyms) != 0:
        name = synonyms[0]
    mol_file[0] = name
    #
    # Try to fix the second line (with the dimension (2D/3D) indicator).
    #
    mol_file[1] = parse_molfile_line2(mol_file[1])
    mol_file[2] = ''
    mol = parse_molfile(atomic_num, mol_file)
    #
    # Find lowest X and Y coordinates and set left lower corner to (0,0).
    #
    min_x, min_y = None, None
    for atom in mol['atoms']:
        x_co = atom['X']
        y_co = atom['Y']
        if min_x is None or min_x > x_co:
            min_x = x_co
        if min_y is None or min_y > y_co:
            min_y = y_co
    for atom in mol['atoms']:
        atom['X'] -= min_x
        atom['Y'] -= min_y
    if name != '':
        mol_data['name'] = name
    if len(synonyms) != 0:
        mol_data['synonyms'] = synonyms
    if len(casregs) != 0:
        mol_data['casreg'] = casregs
    if len(extregs) != 0:
        mol_data['extreg'] = extregs
    if len(sysnames) != 0:
        mol_data['sysname'] = sysnames[0]
    return reset_coords(mol, scale), mol_data


def racemic_inchi(inchi, synonyms):
    """Set '/s' layer in InChI to '/s3' for racemic compound."""
    #
    # Change the whole-molecule stereo layer (/s) in InChI from "2"
    # (relative) to "3" (racemic) if one of the synonyms indicate that
    # the racemate is intended.  If the information in the InChI is
    # "unexpected", the InChI won't be changed and a warning will be given.
    # An intended racemate is assumed when a synonym starts with one of
    # the following: "(+/-)-", "(+-)-", "DL-", "dl-", "rac-" or "racemo-".
    #
    new_inchi = inchi
    racemic = False
    for synonym in synonyms:
        if synonym[0:6] == '(+/-)-' or synonym[0:5] == '(+-)-' or \
                        synonym[0:3] == 'DL-' or synonym[0:3] == 'dl-' or \
                        synonym[0:4] == 'rac-' or synonym[0:7] == 'racemo-':
            racemic = True
    if not racemic:
        return new_inchi
    loc_s = inchi.find('/s')
    loc_t = inchi.find('/t')
    #
    # The case of a single undefined stereocentre requires more work because
    # the stereo (/s) layer will be absent altogether.  The SUU flag ensures
    # that the tetrahedral layer (/t) will be present which in this case will
    # contain a single centre with unknown or undefined configuration.
    #
    if loc_t < 0:
        plain_message('warning', 'racemic name for non-stereo compound %s' % synonyms[0])
        return new_inchi
    if loc_s < 0:
        section = inchi[loc_t + 2:]
        rest = ''
        racemic = '-/s3'
        loc_s = section.find('/')
        if loc_s > 0:
            plain_message('warning', 'Unexpected layer following /s for compound %s' % synonyms[0])
            return new_inchi
        loc_s = section.find(';')
        if loc_s > 0:
            if loc_s + 1 != len(section):
                plain_message('warning', 'Undefined stereo in multi-fragment compound %s' % synonyms[0])
                return new_inchi
            section = section[:-1]
            racemic = '-;/s3'
        loc_s = section.find(',')
        if loc_s > 0:
            if section.find('?') > 0 or section.find('u') > 0:
                plain_message('warning', 'racemic name for stereo-undefined compound %s' % synonyms[0])
            else:
                plain_message('warning', 'racemic name for meso compound %s' % synonyms[0])
            return new_inchi
        if get_int(section[:-1], 0) <= 0 or \
                (section[-1] != 'u' and section[-1] != '?'):
            plain_message('warning', 'Unexpected situation in InChI for compound %s' % synonyms[0])
            return new_inchi
        new_inchi = \
            '%s%s%s%s%s' % (inchi[:loc_t], '/t', section[:-1], racemic, rest)
        plain_message('info', 'InChI adjusted for racemic compound %s' % \
                      synonyms[0])
    elif inchi[loc_s + 2] == '1':
        plain_message('warning', 'racemic name for single enantiomer %s' % synonyms[0])
    else:
        new_inchi = \
            '%s%s%s' % (inchi[:loc_s + 2], '3', inchi[loc_s + 3:])
        plain_message('info', 'InChI adjusted for racemic compound %s' % synonyms[0])
    return new_inchi


def serial_molecule(atomic_sym, mol):
    """Convert molecule into a molfile section."""
    #
    # Convert molecule mol into a molfile section (list of lines).
    #
    mdl_valency_0, rgroup_offset = 15, 155
    line = '%s\n' % mol['title']
    mol_file = [line]
    tim = localtime()
    line = '%2s%-8s%02d%02d%02d%02d%02d%1dD\n' % ('', '-ISIS-', \
                                                  tim.tm_mon, tim.tm_mday, tim.tm_year % 100, tim.tm_hour, tim.tm_min, \
                                                  mol['dimens'])
    mol_file.append(line)
    mol_file.append('\n')
    line = '%3d%3d%3d%3d%3d%3d%3d%3d%3d%3d%3d V2000\n' % (len(mol['atoms']), len(mol['bonds']), 0, 0, \
            mol['abs_flag'], 0, 0, 0, 0, 0, 999)
    mol_file.append(line)
    prop = {}
    prop['ISO'] = []
    prop['CHG'] = []
    prop['RAD'] = []
    prop['RGP'] = []
    num = 0
    for atom in mol['atoms']:
        num += 1
        for kind in ['ISO', 'CHG', 'RAD']:
            if atom[kind[0]] != 0:
                prop[kind].append((num, atom[kind[0]]))
        if atom['T'] > rgroup_offset:
            sym = 'R#'
            prop['RGP'].append((num, atom['T'] - rgroup_offset))
        elif atom['T'] > 0:
            sym = atomic_sym[atom['T']]
        else:
            sym = 'Du'
        if atom['V'] is None:
            val = 0
        elif atom['V'] == 0:
            val = mdl_valency_0
        else:
            val = atom['V']
        mnr = atom['M']
        line = '%10.4f%10.4f%10.4f %-2s%3d%3d%3d%3d%3d%3d%3d%3d%3d%3d\n' % \
               (float(atom['X']) / 10000.0, float(atom['Y']) / 10000.0, \
                float(atom['Z']) / 10000.0, sym, 0, 0, 0, 0, 0, val, 0, 0, 0, mnr)
        mol_file.append(line)
    for bond in mol['bonds']:
        line = '%3d%3d%3d%3d\n' % \
               (bond['1'] + 1, bond['2'] + 1, bond['T'], bond['S'])
        mol_file.append(line)
    for kind in ['ISO', 'CHG', 'RAD', 'RGP']:
        for count in range((len(prop[kind]) + 7) / 8):
            num = len(prop[kind]) - 8 * count
            if num > 8:
                num = 8
            line = 'M  %3s%3d' % (kind, num)
            for item in prop[kind][8 * count:8 * count + num]:
                line = line + '%4d%4d' % item
            line = line + '\n'
            mol_file.append(line)
    mol_file.append('M  END\n')
    return mol_file


def write_molfile(file_name, atomic_sym, mol):
    """Write mol into new molfile file_name."""
    #
    # Create file file_name and write mol into it.
    #
    (out_file, err_msg) = try_open_file(file_name, 'w')
    if out_file is None:
        plain_message('fatal', err_msg)
    for line in serial_molecule(atomic_sym, mol):
        out_file.write(line)
    out_file.close()
    return


def write_sdfile_section(out_file, atomic_sym, mol, mol_data):
    """Write mol and mol_data to an SDfile section."""
    #
    # Write mol and mol_data to an SDfile section.  The data fields
    # are written in alphabetical order of the field name.
    #
    for line in serial_molecule(atomic_sym, mol):
        out_file.write(line)
    field_list = mol_data.keys()
    field_list.sort()
    for field in field_list:
        out_file.write('>  <%s>\n' % field)
        if type(mol_data[field]) == ListType:
            for item in mol_data[field]:
                out_file.write('%s\n' % item)
        else:
            out_file.write('%s\n' % mol_data[field])
        out_file.write('\n')
    out_file.write('$$$$\n')
    return


def write_rxnfile(file_name, atomic_sym, reactants, products):
    """Writes reactants and products to output rxnfile."""
    #
    # Writes reactants and products to output rxnfile with name file_name.
    #
    mdl_rxn_time_format = '%m%d%Y%H%M'
    (rxn_file, err_msg) = try_open_file(file_name, 'w')
    if rxn_file is None:
        plain_message('fatal', err_msg)
    plain_message('info', 'Writing %s' % file_name)
    tim = localtime()
    rxn_file.write('$RXN\n\n      %-8s %12s\n\n%3d%3d\n' % ('ISIS', \
                                                            strftime(mdl_rxn_time_format), len(reactants),
                                                            len(products)))
    for mol in reactants + products:
        rxn_file.write('$MOL\n')
        for line in serial_molecule(atomic_sym, mol):
            rxn_file.write(line)
    rxn_file.close()
    return
