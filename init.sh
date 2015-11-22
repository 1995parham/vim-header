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
python3 copyrighter/setup.py install

if [ $? ]; then
    echo "successful copyrighter installation"
fi
