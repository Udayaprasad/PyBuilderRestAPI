# PyBuilderRestAPI

## Steps to Run the Project:-


```
 Create one shell script in your favourite directory and Copy the contents of *run_me.sh* and issue the below command.
 
 sh run_me.sh
 
 ```
 
 ## Script output:-
 
 
 ```
 IM-LP-589:temp uvakalapudi$ sh runn.sh 

 ############# Start Git Cloning Operation ############# 

Cloning into 'PyBuilderRestAPI'...
remote: Enumerating objects: 30, done.
remote: Counting objects: 100% (30/30), done.
remote: Compressing objects: 100% (21/21), done.
remote: Total 30 (delta 8), reused 26 (delta 7), pack-reused 0
Unpacking objects: 100% (30/30), done.

 ############# Change Directory to PyBuilderRestAPI ############# 


 ############# Create Virtual Environment mypyenv ############# 


 ############# Activate mypyenv Environment ############# 


 ############# Install pybuilder package ############# 

Collecting pybuilder
  Using cached https://files.pythonhosted.org/packages/c0/23/57ef070a20ca2ff7852371056a57fef2d95d74b1b99e01bb7200dc7e80e5/pybuilder-0.11.17-py3-none-any.whl
Requirement already satisfied: pip<11dev,>=7.1 in ./mypyenv/lib/python3.6/site-packages (from pybuilder)
Collecting tblib (from pybuilder)
  Using cached https://files.pythonhosted.org/packages/6d/b1/32dd1c3e6f68856d9596abc649eae40ca914192b3f0f39fce91cf6747d90/tblib-1.5.0-py2.py3-none-any.whl
Collecting setuptools~=39.0.0 (from pybuilder)
  Using cached https://files.pythonhosted.org/packages/20/d7/04a0b689d3035143e2ff288f4b9ee4bf6ed80585cc121c90bfd85a1a8c2e/setuptools-39.0.1-py2.py3-none-any.whl
Collecting tailer (from pybuilder)
  Using cached https://files.pythonhosted.org/packages/dd/05/01de24d6393d6da0c27857c76b0f9ae97b42cd6102bbdf76cce95e031295/tailer-0.4.1.tar.gz
Collecting wheel~=0.31 (from pybuilder)
  Using cached https://files.pythonhosted.org/packages/00/83/b4a77d044e78ad1a45610eb88f745be2fd2c6d658f9798a15e384b7d57c9/wheel-0.33.6-py2.py3-none-any.whl
Installing collected packages: tblib, setuptools, tailer, wheel, pybuilder
  Found existing installation: setuptools 28.8.0
    Uninstalling setuptools-28.8.0:
      Successfully uninstalled setuptools-28.8.0
  Running setup.py install for tailer ... done
Successfully installed pybuilder-0.11.17 setuptools-39.0.1 tailer-0.4.1 tblib-1.5.0 wheel-0.33.6
You are using pip version 9.0.1, however version 19.3.1 is available.
You should consider upgrading via the 'pip install --upgrade pip' command.

 ############# Install and Build Project specific Libraries ############# 

PyBuilder version 0.11.17
Build started at 2019-11-30 11:57:41
------------------------------------------------------------
[INFO]  Building PyBuilderRestAPI version 1.0
[INFO]  Executing build in /Users/uvakalapudi/Desktop/pybuilderproject/temp/PyBuilderRestAPI
[INFO]  Going to execute task install_dependencies
[INFO]  Installing all dependencies
[INFO]  Processing batch dependency 'Flask==1.1.1'
[INFO]  Processing batch dependency 'configparser==4.0.2'
[INFO]  Processing batch dependency 'parameterized==0.7.1'
[INFO]  Processing batch dependency 'requests==2.22.0'
[INFO]  Processing batch dependency 'urllib3==1.25.7'
------------------------------------------------------------
BUILD SUCCESSFUL
------------------------------------------------------------
Build Summary
             Project: PyBuilderRestAPI
             Version: 1.0
      Base directory: /Users/uvakalapudi/Desktop/pybuilderproject/temp/PyBuilderRestAPI
        Environments: 
               Tasks: install_dependencies [3824 ms]
Build finished at 2019-11-30 11:57:44
Build took 3 seconds (3843 ms)

 ############# Start the WebService ############# 


 ############# Perform Project Build and run the unit testcases ############# 

PyBuilder version 0.11.17
Build started at 2019-11-30 11:57:45
------------------------------------------------------------
[INFO]  Building PyBuilderRestAPI version 1.0
[INFO]  Executing build in /Users/uvakalapudi/Desktop/pybuilderproject/temp/PyBuilderRestAPI
[INFO]  Going to execute task publish
[INFO]  Installing plugin dependency flake8
[INFO]  Installing plugin dependency pypandoc
 * Serving Flask app "WebServiceExercise" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
[INFO]  Installing plugin dependency unittest-xml-reporting
[INFO]  Running unit tests
[INFO]  Executing unit tests from Python modules in /Users/uvakalapudi/Desktop/pybuilderproject/temp/PyBuilderRestAPI/src/unittest/python
127.0.0.1 - - [30/Nov/2019 11:57:50] "GET /quotes/movie/5cd95395de30eff6ebccde5b/character/5cd99d4bde30eff6ebccfea0 HTTP/1.1" 200 -
127.0.0.1 - - [30/Nov/2019 11:57:51] "GET /quotes/movie/5cd95395de30eff6ebccde5b/character/5cd99d4bde30eff6ebccfe07 HTTP/1.1" 200 -
127.0.0.1 - - [30/Nov/2019 11:57:53] "GET /quotes/movie/5cd95395de30eff6ebccde5d/character/5cd99d4bde30eff6ebccfe9e HTTP/1.1" 200 -
127.0.0.1 - - [30/Nov/2019 11:57:53] "GET /quotes/movie/5cd95395de30eff6ebccde5/character/5cd99d4bde30eff6ebccfe9e HTTP/1.1" 200 -
[INFO]  Executed 4 unit tests
[INFO]  All unit tests passed.
[INFO]  Building distribution in /Users/uvakalapudi/Desktop/pybuilderproject/temp/PyBuilderRestAPI/target/dist/PyBuilderRestAPI-1.0
[INFO]  Copying scripts to /Users/uvakalapudi/Desktop/pybuilderproject/temp/PyBuilderRestAPI/target/dist/PyBuilderRestAPI-1.0/scripts
[INFO]  Writing setup.py as /Users/uvakalapudi/Desktop/pybuilderproject/temp/PyBuilderRestAPI/target/dist/PyBuilderRestAPI-1.0/setup.py
[INFO]  Building binary distribution in /Users/uvakalapudi/Desktop/pybuilderproject/temp/PyBuilderRestAPI/target/dist/PyBuilderRestAPI-1.0
------------------------------------------------------------
BUILD SUCCESSFUL
------------------------------------------------------------
Build Summary
             Project: PyBuilderRestAPI
             Version: 1.0
      Base directory: /Users/uvakalapudi/Desktop/pybuilderproject/temp/PyBuilderRestAPI
        Environments: 
               Tasks: prepare [3446 ms] compile_sources [0 ms] run_unit_tests [4366 ms] package [3 ms] run_integration_tests [0 ms] verify [0 ms] publish [635 ms]
Build finished at 2019-11-30 11:57:53
Build took 8 seconds (8466 ms)

 ############# Project Completed ############# 
 ```
