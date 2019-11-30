#!/bin/bash
echo "############# Start Git Cloning Operation ############# \n"
git clone https://github.com/Udayaprasad/PyBuilderRestAPI.git
echo "############# Change Directory to PyBuilderRestAPI ############# \n"
cd PyBuilderRestAPI
"############# Create Virtual Environment mypyenv ############# \n"
python -m venv mypyenv
"############# Activate mypyenv Environment ############# \n"
source mypyenv/bin/activate
"############# Install pybuilder package ############# \n"
pip install pybuilder
"############# Install and Build Project specific Libraries ############# \n"
pyb install_dependencies
"############# Start the WebService ############# \n"
python src/main/python/WebServiceExercise.py &
"############# Perform Project Build and run the unit testcases ############# \n"
pyb -v
