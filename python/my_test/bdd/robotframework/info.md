## docs
http://robotframework.org/

## install

pip install robotframework

## examples
### demoapp
#### install
pip install --user robotframework-selenium2library
#### run app
python demoapp/server.py

#### run testcases
robot login_tests
robot --variable BROWSER:Chrome login_tests