#!/bin/bash
# In The Name Of God
# ========================================
# [] File Name : init.sh
#
# [] Creation Date : 22-11-2015
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
echo "Installing Copyrighter project :D"
cd copyrighter
if [ -d "$HOME/.copyrighter" ]; then
	sudo python3 setup.py install_scripts
else
	sudo python3 setup.py install_scripts
	python3 setup.py install_data
fi
if [ $? -eq 0 ]; then
	echo "Copyrighter has been installed successfully"
else
	echo "Copyrighter installation has been failed"
	exit
fi
python3 -c "import airspeed" 2> /dev/null
if [ $? -eq 0 ]; then
	exit
fi
cd ..
echo "Installing airspeed dependency"
if [[ "$OSTYPE" == "darwin"* ]]; then
	git clone https://github.com/purcell/airspeed.git
	cd airspeed
	sudo python3 setup.py install
	cd ..
	sudo rm -Rf airspeed
else
	sudo apt-get install --yes python3-pip
	sudo pip3 install setuptools
	git clone https://github.com/purcell/airspeed.git
	cd airspeed
	sudo python3 setup.py install
	cd ..
	sudo rm -Rf airspeed
fi
