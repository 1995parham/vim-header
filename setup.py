from distutils.core import setup
import os

setup(
    name='copyrighter',
    version='2.0',
    packages=['copyrighter'],
    package_dir={'copyrighter': 'src/copyrigher'},
    data_files=[(os.path.expanduser("~/.copyrighter"), "conf/config.ini")],
    url='https://github.com/1995parham/vim-header',
    license='GPLv2',
    author='Parham Alvani',
    author_email='parham.alvani@gmail.com',
    description='Advance-Dummy source codes header generator'
)
