[![Build Status](https://travis-ci.org/StudentESE/myFirstPiP.svg?branch=master)](https://travis-ci.org/StudentESE/myFirstPiP)
# myFirstPiPy
Ignore this package ! It is simple showing progress of learning developing reusable python modules

# Steps to create your own PIP Module

Each file extended by ```.py``` becomes a python module as follows:

```
#!/usr/bin/python
def myMethod():
    msg = "Hello PiP"
    print ("MSG: {}".format(msg))
    return msg
myVariable = 123

```

If you want to use your file as a module
you simple have to import it:

```
#!/usr/bin/python
import myModule
myModule.myMethod()
```

Also possible:

```
#!/usr/bin/python
from myFirstPiPy import *
print ("myVariable: {}".format(myVariable))
myMethod()

```

#Share your PiP
To share your module as a PIP Package everyone can install by ```pip install yourPackageName```requires a bit more structure.
After registering on [PyPi.org](https://pypi.org) ([and the Test Space accont!](https://test.pypi.org/account/register/)) install an utility for publishing Python packages on PyPi:

```
pip install twine
```
## Setup.py
Create a directory structure as follows and add plain files as shown:

```
/myFirstPiPy
  /myFirstPiPy
    __init__.py
  setup.py
  LICENSE
  README.md
```
Within the ```__init__.py``` you can add python code to be executed while importing the module.
The `setup.py` requires a fixed structure you can copy and past here for customizing your needs:

```
import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name="myFirstPiPy",
    version="0.0.1",
    author="Daniel Bunzendahl",
    author_email="StudentDanBu@gmail.com",
    description="My first PiP",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/StudentESE/myFirstPiP",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
```
**Note:** You have to create a new Git Repository [here](https://github.com/new) and copy the URL

To generate the [wheel](https://pythonwheels.com) for native compilations and `tar.gz` for python module - just do:

```
cd myFirstPiPy
python setup.py sdist bdist_wheel
```
generates:

```
dist/
  myFirstPiPy-0.0.1-py-none-any.whl
  myFirstPiPy-0.0.1.tar.gz
```
## Testdrive and Upload
First we test how a submission would look like:

```
twine upload --skip-existing --repository-url https://test.pypi.org/legacy/ dist/* 
```
If the result looks good for you it is time to run

```
twine upload dist/*
```
Which will publish your first PiP Package.

**Note:** If you like to change files on Pypi, you need to change the version in `setup.py`. It is not possible to delete the project and reupload your local version (security reason!!)

# Testing
Now we like to go more professional and add [unittests](https://docs.python.org/3/library/unittest.html). So we add a directory where to add tests in multiple files. 

```
/myFirstPiP
  /myFirstPiP
    __init__.py
  /tests
    test_var.py
    test_method.py
  setup.py
  LICENSE
  README.md
```

All this files are executed by the command ```python -m unittest discover -s ./tests -p "test_*"```

## Writing Tests
Tests are Classes which subclasses ```unittest.TestCase```. Each Method named `test*` within such a class will be run. The following example shows how `test_var.py` or `test_method.py` could look like merged within one file.

```
import unittest
import __init__ as myModule
class TestMyMethod(unittest.TestCase):
    def test_myMethod(self):
        self.assertEqual(myModule.myMethod(), "Hello PiP")
    def test_myVariable(self):
        self.assertIs(myModule.myVariable, 123)
if __name__ == '__main__':
    unittest.main()
```

#Continuous Integration (CI)
A very interesting solution is Travis which runs tests on Github. To enable Travis CI you need a ```.travis.yml``` after generating a ```requirements.txt```from your ```virtualenv```.
##Virtual Environment
First we need a virtual environment with only pip packages installed are realy neccessary. Based on this the generating of the ```requirements.txt``` is created.

```
cd .. # below ./myFirstPiP
virtualenv myFirstModuleDependencies
source myFirstModuleDependencies/bin/activate
cd myFirstPiP
```
Install required packages and generate the ```requirements.txt```

```
pip freeze > requirements.txt
```
##Travis
Now we can write the `.travis.yml` as follows:

```
language: python
python:
  - "2.7"
  - "3.3"
  - "3.4"
  - "3.5"
  - "3.5-dev"  # 3.5 development branch
  - "3.6"
  - "3.6-dev"  # 3.6 development branch
  - "3.7-dev"  # 3.7 development branch
# command to install dependencies
install:
  - pip install -r requirements.txt
# command to run tests
script:
  - python -m unittest discover -s ./tests -p "test_*"
```

# Git
```
cd ..
git pull
git add .
git commit -m "Travis CI Testdrive"
git push origin master
```