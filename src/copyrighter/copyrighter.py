#!/usr/bin/env python3
# In The Name Of God
# ========================================
# [] File Name : copyrighter.py
#
# [] Creation Date : 02-05-2015
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
__author__ = 'Parham Alvani'

# updates the copyright information for input files

import datetime
import os
import argparse
import configparser
import airspeed

context = {}

def __init__(self):
    self.c_header = airspeed.Template()
    self.sh_header = """#!/bin/
# In The Name Of God
# ========================================
# [] File Name : ${FILE}
#
# [] Creation Date : ${DATE}
#
# [] Created By : ${USER} (${EMAIL})
# =======================================
"""

    self.php_header = """<?php
/**
 * In The Name Of God
 * File: ${FILE}
 * User: ${USER} (${EMAIL})
 * Date: ${DATE}
 * Time: ${TIME}
 */
"""

    self.java_header = """/*
 * In The Name Of God
 * ========================================
 * [] File Name : ${FILE}
 *
 * [] Creation Date : ${DATE}
 *
 * [] Created By : ${USER} (${EMAIL})
 * =======================================
*/
/**
 * @author ${USER}
 */
"""

    self.vhdl_header = """--------------------------------------------------------------------------------
-- Author:        ${USER} (${EMAIL})
--
-- Create Date:   ${DATE}
-- Module Name:   ${FILE}
--------------------------------------------------------------------------------
"""

    self.spice_header = """**
* Author: ${USER} (${EMAIL})
* Create Date: ${DATE}
* File Name: ${FILE}
**
"""
    self.go_header = """
        // +========================================
        // | Author:        ${USER} (${EMAIL})
        // |
        // | Creation Date: ${DATE}
        // |
        // | File Name:     ${FILE}
        // +========================================
"""

    self.vim_header = """
" In The Name Of God
" Vim plugin file
" Last Change:	2015 Sep 24
" Maintainer:	Parham Alvani <parham.alvani@gmail.com>
"""


def header_parser(header: str) -> str:
    """

    :param header: VT header for merging
    :return: merged version of input header
    """
    new_header = str(header)
    new_header = new_header.replace("${TIME}", time.strftime("%H:%M"))
    return new_header


def update_source(srcfile: str, str_based: bool) -> None:
    """

    :param srcfile: name of target source file
    :return: nothing
    """
    options = {
        '.c': config.c_header,
        '.h': config.c_header,
        '.S': config.c_header,
        '.s': config.c_header,
        '.v': config.c_header,
        '.go': config.go_header,
        '.py': config.py_header,
        '.php': config.php_header,
        '.java': config.java_header,
        '.vhd': config.vhdl_header,
        '.sp': config.spice_header,
        '.js': config.c_header,
        '.sh': config.sh_header
    }
    if os.path.splitext(srcfile)[-1] in options:

        header = options[os.path.splitext(srcfile)[-1]]

        context['file'] = {'name': os.path.split(srcfile)[1], 'path': os.path.abspath(srcfile)}
        context['time'] = datetime.datetime.now()

        if not str_based:
            print("Updating %s" % srcfile)
            file_data = open(srcfile, "r").read()
            file = open(srcfile, "w")
            file.write(header + file_data)
        else:
            print(header)
        return


parser = argparse.ArgumentParser(description="Copyright advance header adder script")
parser.add_argument(
    'files',
    metavar='F',
    type=str,
    nargs='+',
    help='Target files')
parser.add_argument('--name', dest='name', type=str, default='', help="user.name")
parser.add_argument('--email', dest='email', type=str, default='', help="user.email")
parser.add_argument('--config-path', dest='cnfg_path', type=argparse.FileType('r'),
                    default=os.path.expanduser('~/.copyrighter/config.ini'))

args = parser.parse_args()

context['user'] = {'email': args.email, 'name': args.name}

cnfg_path = args.cnfg_path

cnfg = configparser.ConfigParser()
cnfg.read(cnfg_path)
for section in cnfg.sections():
    if section == 'user'

while len(args.files) > 0:
    filepath = args.files.pop()
    update_source(filepath, args.str_based)
exit()
