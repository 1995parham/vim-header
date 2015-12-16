from distutils.core import setup
import os

# Just someone, someone tell WTF :)
headers = []
for header in os.listdir('conf/header/'):
    headers.append(os.path.join('conf/header/', header))

setup(
    name='copyrighter',
    version='2.0',
    scripts=['src/scripts/copyrighter.py'],
    data_files=[
        (os.path.expanduser("~/.copyrighter"), ["conf/config.ini"]),
        (os.path.expanduser("~/.copyrighter/header"), headers)
    ],
    url='https://github.com/1995parham/vim-header',
    license='GPLv2',
    author='Parham Alvani',
    author_email='parham.alvani@gmail.com',
    description='Advance-Dummy source codes header generator',
    install_requires=['airspeed']
)
