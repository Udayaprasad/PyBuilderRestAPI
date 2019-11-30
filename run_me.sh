#!/bin/bash
rm -rf PyBuilderRestAPI
kill -9 $(lsof -t -i:5000)
pip install --upgrade pip
echo "\n ############# Start Git Cloning Operation ############# \n"
git clone https://github.com/Udayaprasad/PyBuilderRestAPI.git
echo "\n ############# Change Directory to PyBuilderRestAPI ############# \n"
cd PyBuilderRestAPI
echo "\n ############# Create Virtual Environment mypyenv ############# \n"
python -m venv mypyenv
echo "\n ############# Activate mypyenv Environment ############# \n"
source mypyenv/bin/activate
echo "\n ############# Install pybuilder package ############# \n"
pip install pybuilder
echo "\n ############# Install and Build Project specific Libraries ############# \n"
pyb install_dependencies
echo "\n ############# Start the WebService ############# \n"
python src/main/python/WebServiceExercise.py &
echo "\n ############# Perform Project Build and run the unit testcases ############# \n"
pyb -v
echo "\n ############# Project Completed ############# \n"
