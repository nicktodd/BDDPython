# BDDPython

## Required libraries
pip install behave
pip install selenium
pip install pyhamcrest

## Chromedriver

The URL for chrome drivers is now. You can identify the current driver on this page.
https://googlechromelabs.github.io/chrome-for-testing/#stable

Extract chromedriver and place file in the PATH. On windows, you can run the following command from a terminal at the root of the project

```
PATH=%PATH%;.\
export PATH=$PATH:.
```

## Running a Test
To run the tests, type behave at the command line

```
This feature does not go near the internet so can be executed without the chrome driver
behave -i SpeakingClock.feature

This feature uses the metacritic test Lambda (which now fakes the result at 89%)
behave -i gamereview.feature


This feature tests the student find my machine web site
behave -i StudentWebsite.feature

The insurance feature is no longer live.
behave -i insurance.feature

```