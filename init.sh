#!/bin/bash
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
python3 -c "import airspeed" 2> /dev/null
if [ $? -eq 0 ]; then
	exit
fi
cd ..
echo "installing airspeed dependency"
if [ "$OSTYPE" == "darwin"* ]; then
	pip3 install airspeed
else
	sudo apt-get install python3-pip
	git clone https://github.com/purcell/airspeed.git
	cd airspeed
	sudo python3 setup.py install
	cd ..
	sudo rm -Rf airspeed
fi
