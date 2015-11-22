#!/bin/sh
# In The Name Of God
# ========================================
# [] File Name : init.sh
#
# [] Creation Date : 22-11-2015
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
echo "installing copyrighter project :D"
cd copyrighter
if [ -d "$HOME/.copyrighter"]; then
	python3 setup.py install_scripts
	python3 setup.py install_lib
else
	python3 setup.py install
fi
if [ $? ]; then
    echo "successful copyrighter installation"
fi
