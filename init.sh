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
if [ -d "$HOME/.copyrighter" ]; then
	sudo python3 setup.py install_scripts
else
	sudo python3 setup.py install_scripts
	python3 setup.py install_data
fi
if [ $? ]; then
    echo "copyrighter has been installed successfully"
fi
python3 -c "import airspeed"
if [ $? ]; then
	exit
fi
cd ..
echo "installing airspeed dependency"
git clone https://github.com/purcell/airspeed.git
cd airspeed
sudo python3 setup.py install
cd ..
sudo rm -Rf airspeed
