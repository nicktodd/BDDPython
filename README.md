# BDDPython

## Required libraries
pip install behave
pip install selenium
pip install pyhamcrest

## Chromedriver
download latest chromedriver from https://chromedriver.storage.googleapis.com/index.html?path=2.40/
v94 as of Oct 2021  https://chromedriver.storage.googleapis.com/index.html?path=94.0.4606.61/

Extract chromedriver and place file in the PATH. On windows, you can run the following command from a terminal at the root of the project

```
PATH=%PATH%;.\
```

## Running a Test
To run the tests, type behave at the command line

```
behave -i insurance.feature

behave -i StudentWebsite.feature
```