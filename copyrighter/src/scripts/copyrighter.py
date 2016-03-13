#!/usr/bin/env python3
# In The Name Of God
# ========================================
# [] File Name : copyrighter.py
#
# [] Creation Date : 02-05-2015
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
__version__ = "2.1"
"""
Updates the copyright information for input files
"""

import argparse
import configparser
import datetime
import os

try:
    import airspeed
except ImportError:
    airspeed = None
    quit(0)

context = {}
headers = {}


def update_source(srcfile: str, str_based: bool) -> None:
    """

    :param srcfile: name of target source file
    :param str_based: print header on stdout :) if true
    :return: nothing
    """
    if os.path.splitext(srcfile)[-1] in headers:

        dest_header = headers[os.path.splitext(srcfile)[-1]]

        context['file'] = {'name': os.path.split(srcfile)[1],
                           'path': os.path.abspath(srcfile)}
        context['time'] = datetime.datetime.now()

        dest_header = dest_header.merge(context)

        if not str_based:
            print("Updating %s" % srcfile)
            file_data = open(srcfile, "r").read()
            file = open(srcfile, "w")
            file.write(dest_header + file_data)
        else:
            print(dest_header)
        return


parser = argparse.ArgumentParser(
    description="Copyright: Advance-Dummy source codes header generator")
parser.add_argument('--version', action='version',
                    version='%(prog)s {version}'.format(version=__version__))
parser.add_argument('files',
                    metavar='F',
                    type=str,
                    nargs='+',
                    help='Target files')
parser.add_argument('--name', dest='name', type=str,
                    default='', help="user.name")
parser.add_argument('--email', dest='email', type=str,
                    default='', help="user.email")
parser.add_argument('--string', dest='str_based', action='store_true',
                    default=False, help="Print header on stdout")
parser.add_argument('--config-path', dest='cnfg_path', type=str,
                    default=os.path.expanduser('~/.copyrighter/'))

args = parser.parse_args()

context['user'] = {'email': args.email, 'name': args.name}

cnfg_path = ""
if os.path.isdir(args.cnfg_path):
    cnfg_path = args.cnfg_path

cnfg = configparser.ConfigParser()
cnfg.read(os.path.join(cnfg_path, "config.ini"))
for section in cnfg.sections():
    if section == 'user':
        if context['user']['name'] == "":
            context['user']['name'] = cnfg['user']['Name']
        if context['user']['email'] == "":
            context['user']['email'] = cnfg['user']['email']
    else:
        for extension in cnfg[section]['Extension'].split(' '):
            header = open(os.path.join(cnfg_path,
                                       cnfg[section]['File']), 'r').read()
            headers[extension] = airspeed.Template(header)

while len(args.files) > 0:
    filepath = args.files.pop()
    update_source(filepath, args.str_based)
exit()
