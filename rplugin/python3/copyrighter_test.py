# In The Name Of God
# ========================================
# [] File Name : rplugin/python3/copyrighter_test.py
#
# [] Creation Date : 04-06-2018
#
# [] Created By : Parham Alvani <parham.alvani@gmail.com>
# =======================================
import json
import os
import tempfile

import neovim
import pytest

from copyrighter import CopyrighterPlugin

neovim.setup_logging("test")


@pytest.fixture
def vim():
    child_argv = os.environ.get('NVIM_CHILD_ARGV')
    listen_address = os.environ.get('NVIM_LISTEN_ADDRESS')
    if child_argv is None and listen_address is None:
        child_argv = '["nvim", "-u", "NONE", "--embed"]'

    if child_argv is not None:
        editor = neovim.attach('child', argv=json.loads(child_argv))
    else:
        editor = neovim.attach('socket', path=listen_address)

    editor.command("let &runtimepath.=','.escape(expand('<sfile>:p:h'), '\,')")

    return editor


def test_header(vim):
    fname = tempfile.mkstemp()[1]
    cp = CopyrighterPlugin(vim)

    vim.command('new')
    vim.command('edit {}'.format(fname))
    cp.on_bufnew(fname)
