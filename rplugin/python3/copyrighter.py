# In The Name Of God
# ========================================
# [] File Name : copyrighter.py
#
# [] Creation Date : 02-05-2015
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================

import neovim
import configparser
import os
import datetime
from collections import namedtuple

User = namedtuple('User', ['name', 'email'])


@neovim.plugin
class CopyrighterPlugin:
    def __init__(self, nvim):
        # NVIM instance
        self.nvim = nvim

        # Configurations (config.ini)
        self.headers = {}
        cnfg_path = os.path.join(os.path.dirname(__file__), '../../conf')
        cnfg = configparser.ConfigParser()
        cnfg.read(os.path.join(cnfg_path, "config.ini"))
        for section in cnfg.sections():
            for extension in cnfg[section]['Extension'].split(' '):
                header = open(
                        os.path.join(cnfg_path, cnfg[section]['File']),
                        'r')
                self.headers[extension] = header

    def _context(self, srcfile: str):
        '''
        Fills context for creating header
        '''

        context = {}
        context['user'] = User(name=self.nvim.eval('g:header_name'),
                                email=self.nvim.eval('g:header_email'))
        context['file'] = os.path.basename(srcfile)
        context['time'] = datetime.datetime.now()

        return context


    @neovim.command('Header', eval='@%')
    def header_command(self, srcfile: str, sync=True):
        '''
        Provides header in existing file
        '''
        if os.path.splitext(srcfile)[-1] in self.headers:
            extention_header = self.headers[os.path.splitext(srcfile)[-1]]

            context = self._context(srcfile)

            lines = [l.format(**context) for l in
                     extention_header.read().splitlines()]
            self.nvim.current.buffer.append(lines, 0)

            extention_header.seek(0)

    @neovim.autocmd('BufNewFile', pattern=r'*',
                    eval='expand("<afile>")', sync=True)
    def on_bufnew(self, srcfile: str):
        '''
        Provides header in the buffer of filename
        based on it's extention.
        '''
        if os.path.splitext(srcfile)[-1] in self.headers:
            extention_header = self.headers[os.path.splitext(srcfile)[-1]]

            context = self._context(srcfile)

            i = 1
            for line in extention_header.read().splitlines():
                line = line.format(**context)
                self.nvim.current.buffer[-1] = line
                self.nvim.current.buffer.append('')
                i += 1
            extention_header.seek(0)
            self.nvim.current.window.cursor = (i, 0)
