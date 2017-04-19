#!/bin/env python
#
# General utilities:  messages, string-to-number conversions and others.
#
# Written dd. 26Nov2010 Martin A. Ott, Lhasa Limited, Leeds, UK
# Last update 23Jun2012 M.A. Ott
#
# Update history:
# 20120623: Renamed variable called "str"
# 20110819: Made uniqname to work
# 20110220: Added handling of options with restricted values
# 20110207: Added check_ascii
#


from os import getenv, getpid
from os.path import isfile
import sys
from time import localtime
from types import *


def plain_message(sever, msg):
    """Print message and bail out for severe case."""
    #
    # Print message msg and bail out if sever is fatal (or worse!).
    #
    the_text = msg.strip()
    if sever in ['info', 'debug', 'warning', 'error']:
        if sever == 'info':
            print(the_text)
        else:
            print('%s:  %s' % (sever.upper(), the_text))
    elif sever == 'fatal':
        print('\nFATAL ERROR:  %s\n' % the_text)
        sys.exit()
    elif sever == 'bug':
        print('\nPROGRAM ERROR:  %s\n' % the_text)
        sys.exit()
    else:
        print('\nPROGRAM ERROR:  %s\n' % 'bad severity; message ignored')
        sys.exit()
    return None


def get_int(value, default_value):
    """Convert string to signed integer number using default value."""
    #
    # Convert value to signed integer number, using default_value if the
    # conversion is unsuccessful.  Real values are not converted.
    #
    if isinstance(value, IntType):
        return value
    elif isinstance(value, StringType):
        neg = False
        val = value.strip()
        if len(val) > 0:
            if '+-'.find(val[0]) >= 0:
                if val[0] == '-':
                    neg = True
                val = val[1:]
            if val.isdigit():
                if neg:
                    return 0 - int(val)
                else:
                    return int(val)
    return default_value


def get_real(value, default_value):
    """Convert string to signed real number using default value."""
    #
    # Convert value to signed real number, using default_value if the
    # conversion is unsuccessful.  Integer values are converted.
    #
    if isinstance(value, FloatType):
        return value
    if isinstance(value, IntType):
        return float(value)
    elif isinstance(value, StringType):
        negat = False
        value = value.strip()
        if len(value) > 0:
            if '+-'.find(value[0]) >= 0:
                if value[0] == '-':
                    negat = True
                value = value[1:]
            loc = value.find('.')
            if loc < 0:
                ok = value.isdigit()
            elif loc == 0:
                ok = value[1:].isdigit()
            else:
                ok = value[:loc].isdigit() and value[loc + 1:].isdigit()
            if ok:
                if negat:
                    return - float(value)
                else:
                    return float(value)
    return default_value


def check_ascii(string_value):
    """Check string_value for non-ASCII characters."""
    #
    # Check string_value for non-ASCII characters (not in 0-127 range).
    # Returns True if the string is valid ASCII (0-127), False otherwise.
    #
    valid = False
    try:
        valid = unicode(string_value, 'ascii')
    except UnicodeError:
        # xxx = unicode (string_value, 'utf-8')
        valid = False
    else:
        valid = True
    return valid


def fuzzify(value):
    """Return the "fuzzified" version of string value."""
    #
    # Return the "fuzzified" version of string value, keeping only
    # the letters and digits, and converting all letters to upper case.
    # Any whitespace is converted to single spaces.
    #
    # del_chars = '\*\'\\!"#$%&()+,-./:;<=>?@[]^_`{|}~0123456789'
    del_chars = '\*\'\\!"#$%&()+,-./:;<=>?@[]^_`{|}~'
    new_value = value.translate(None, del_chars)
    items = new_value.upper().split()
    return ' '.join(items)


def get_keyword(keyword_list, abbr_keyword):
    """Look up (abbreviated) abbr_keyword in keyword_list."""
    #
    # Look up abbr_keyword (which may be abbreviated) in keyword_list.
    # Note that keywords should not contain a slash ("/") - this is not
    # checked.  The function is case-sensitive.  If abbr_keyword does
    # not match exactly any keyword from keyword_list then it (as an
    # abbreviation) should not match more than one (it would be ambiguous).
    # The function returns an error message (empty if successful) and the
    # found keyword (None if not successful).
    #
    err_msg, keyword = '', None
    if abbr_keyword in keyword_list:
        keyword = abbr_keyword
    else:
        keyword_string = '/' + '/'.join(keyword_list)
        loc = keyword_string.find('/%s' % abbr_keyword)
        if loc < 0:
            err_msg = 'Unrecognised'
        elif keyword_string[loc + 1:].find('/%s' % abbr_keyword) >= 0:
            err_msg = 'Ambiguous'
        else:
            items = keyword_string[loc + 1:].split('/')
            keyword = items[0]
    return err_msg, keyword


def parse_commandline(sysargv, argum_list, argum_dict, option_dict):
    """Parse command line arguments including options."""
    #
    # Parse command line arguments including options.  The available
    # arguments and options are given as dictionaries (with default values)
    # keyed on the argument/option names.
    # The arguments are given as a list as well since they come in order on
    # the command line (whereas options are named).  Arguments which have
    # a default value of "None" are mandatory; otherwise they are optional.
    # Obviously, a mandatory argument cannot be followed by an optional one
    # but this is not checked.
    # Options should start with a slash ("/") and can have a value (e.g.,
    # "/output=result.txt").  In the absence of a value, the value "True"
    # is assigned.  For a "boolean" option, a value is not allowed: its
    # presence means "True", the default value being "False" (in fact, the
    # default value _must_ be "False").  The parse results are returned as
    # updated argument/option dictionaries.  If something is incorrect,
    # err_msg is returned non-empty.
    #
    err_msg, argum_read, option_read, argum_no = '', {}, {}, 0
    for argum in sysargv:
        if len(argum) > 0:
            if argum[0] == '/':
                #
                # Option.
                #
                value = True
                items = argum[1:].split('=')
                if len(items) > 2:
                    err_msg = 'Bad option "%s"' % argum
                    break
                elif len(items) == 2:
                    value = items[1]
                item = items[0].lower()
                if len(item) == 0 or item.find('/') >= 0:
                    err_msg = 'Bad option "%s"' % argum
                    break
                (err_msg, option) = get_keyword(option_dict.keys(), item)
                if option is None:
                    err_msg = '%s option "%s"' % (err_msg, argum)
                    break
                if option in option_read.keys():
                    err_msg = 'Duplicate option "/%s"' % option
                    break
                values = option_dict[option]
                if values is False:
                    if value is not True:
                        err_msg = 'Option "%s" does not take value' % option
                        break
                elif value is True:
                    err_msg = 'Option "/%s" should have a value' % option
                    break
                elif value == '':
                    err_msg = 'Empty value for option "/%s"' % option
                    break
                elif isinstance(values, ListType):
                    item = value
                    (err_msg, value) = get_keyword(values, item)
                    if value is None:
                        err_msg = '%s value "%s" for option "/%s"' % \
                                  (err_msg, item, option)
                        break
                option_read[option] = value
            else:
                #
                # Argument.
                #
                if argum_no == len(argum_list):
                    err_msg = 'Too many arguments'
                    break
                argum_read[argum_list[argum_no]] = argum
                argum_no += 1
    if err_msg == '':
        for argum in argum_read.keys():
            argum_dict[argum] = argum_read[argum]
        for argum in argum_dict.keys():
            if argum_dict[argum] is None:
                err_msg = 'Mandatory argument(s) missing'
                break
        for option in option_dict.keys():
            if option in option_read.keys():
                option_dict[option] = option_read[option]
            elif isinstance(option_dict[option], ListType):
                option_dict[option] = None
    return err_msg, argum_dict, option_dict


def parse_filename(file_name, ext):
    """Add file extension ext to file_name if not already present."""
    #
    # Add file extension ext to file_name if it is not already present.
    #
    ext_len = len(ext)
    if file_name[-ext_len:] != ext:
        return file_name + ext
    return file_name


def try_open_file(file_name, mode):
    """Attempt to open file file_name and return file handle."""
    #
    # Attempt to open file file_name with mode (either 'r' (read) or 'w' (write)).
    # Return file handle if successful, return file handle and empty message,
    # otherwise None and an appropriate error message.
    #
    mode_str = None
    if mode != 'r' and mode != 'w':
        plain_message('bug', 'Invalid file open mode "%s"' % mode)
    if mode == 'r' and not isfile(file_name):
        return None, 'File "%s" does not exist' % file_name
    try:
        handle = open(file_name, mode)
    except:
        if mode == 'r':
            mode_str = 'read'
        else:
            mode_str = 'writ'
    if mode_str != None:
        return None, 'Cannnot open file %s for %sing' % (file_name, mode_str)
    return handle, ''


def uniqname():
    """Builds a unique file name."""
    #
    # Builds a unique name (typically for use as a file name).
    # Don't call this function more than once per second!
    #
    all_digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digits = []
    radix = 36
    tim = localtime()
    num = ((tim.tm_yday * 24 + tim.tm_hour) * 60 + tim.tm_min) * 60 + tim.tm_sec
    while num != 0:
        dig = num % radix
        digits.append(all_digits[dig])
        num = num / radix
    if digits is []:
        digits = ['0']
    digits.reverse()
    user = getenv('USER')
    if user is None:
        user = ''
    else:
        user = user.strip()
    if user == '':
        user = getenv('REMOTE_USER')
        if user is None:
            user = ''
        else:
            user = user.strip()
        if user == '':
            user = 'nn'
    strng = '%s_%x_%s' % (user, getpid(), ''.join(digits))
    return strng.lower()


def get_inchi_program(option_dict):
    """Get the InChI program and its command line options."""
    #
    # Get the InChI program (the name of the executable) and its command
    # line options (as a list of strings).  Note that InChI command line
    # options are supposed to have been transmitted through command line
    # options to the calling script.
    #
    inchi_prog = None
    inchi_progs = ['C:\Program Files\InChI103\inchi-1.exe',
                   'C:\Program Files\InChI102\cInChI-1.exe',
                   'C:\Program Files\InChI\InChI-1\cInChI-1.exe'
                   ]
    for item in inchi_progs:
        if isfile(item):
            inchi_prog = item
            break
    if inchi_prog == None:
        return (None, None, 'No InChI program found')
    inchi_flags = ['/AuxNone', '/NoLabels']
    version1 = inchi_prog.find('10') < 0
    version103 = inchi_prog.find('103') > 0
    if not version103:
        inchi_flags.append('/NEWPS')
    if option_dict['key']:
        if version1:
            return (None, None, 'InChI program does not support InChIKey')
        inchi_flags.append('/Key')
    if option_dict['fixedh']:
        inchi_flags.append('/FixedH')
    if option_dict['fixsp3bug'] or option_dict['fb']:
        if version103:
            plain_message('error', 'InChI program does not support FixSP3Bug/FB')
        else:
            inchi_flags.append('/FixSp3Bug')
    if option_dict['recmet']:
        inchi_flags.append('/RecMet')
    if option_dict['sasxyz']:
        if version103:
            plain_message('error', 'InChI program does not support SAsXYZ')
        else:
            inchi_flags.append('/SAsXYZ')
    if option_dict['sluud']:
        if not version103:
            plain_message('error', 'InChI program does not support SLUUD')
        else:
            inchi_flags.append('/SLUUD')
    if option_dict['snon']:
        inchi_flags.append('/SNon')
    if option_dict['spxyz']:
        if version103:
            plain_message('error', 'InChI program does not support SPXYZ')
        else:
            inchi_flags.append('/SPXYZ')
    if option_dict['sucf']:
        inchi_flags.append('/SUCF')
    if option_dict['suu']:
        inchi_flags.append('/SUU')
    return (inchi_prog, inchi_flags, '')


def check_casreg(part0, part1, part2):
    """Check validity of CAS registry number and return it."""
    #
    # Check validity of CAS registry number by applying the CAS checksum
    # algorithm.  The CAS number is specified as "part0-part1-part2";
    # these numbers should already have been checked for being in the
    # correct range.  If the CAS registry number is valid, it is returned
    # as a string otherwise None is returned.
    #
    casreg, cksum, count, numbr = None, 0, 0, 100 * part0 + part1
    while numbr != 0:
        count += 1
        digit, numbr = numbr % 10, numbr / 10
        cksum += count * digit
    if cksum % 10 == part2:
        casreg = '%d-%02d-%01d' % (part0, part1, part2)
    return casreg


def parse_casreg(string):
    """Parse string to yield a valid CAS registry number."""
    #
    # Parse string to yield a valid CAS registry number.
    #
    msg, casreg = '', None
    parts = string.split('-')
    if len(parts) > 2:
        part0 = parts[0].strip()
        part1 = parts[1].strip()
        part2 = parts[2].strip()
        if len(part0) > 0 and len(part0) < 9 and \
                        len(part1) == 2 and len(part2) > 0:
            part0 = get_int(part0, -1)
            part1 = get_int(part1, -1)
            part2 = get_int(part2[0:1], -1)
            if part0 != -1 and part1 != -1 and part2 != -1:
                casreg = check_casreg(part0, part1, part2)
                if casreg is None:
                    msg = 'Checksum error in CAS registry number: %s' % string
            else:
                msg = 'Not a CAS registry number: %s' % string
    elif string != '':
        msg = 'Not a CAS registry number: %s' % string
    else:
        msg = 'Empty CAS registry number'
    return msg, casreg
