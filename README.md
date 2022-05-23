# QA_Automation_Test_Wefox

##Requirements
platform win32 
Python == 3.9.4, pytest-6.2.3, py-1.10.0, pluggy-0.13.1
webdriver-manager == 3.7.0,
selenium == 3.141.0

##Dependencies
Python 3.9.4 + pytest 6.2.3, webdriver-manager 3.7.0, selenium 3.141.0

##Execution:
The app supports different platform to be executed:

```sh
py.test -s -v ./QA_Automation_Test_Wefox/tests/books/searchBook_test.py --browser chrome --titleToSearch 'Programming JavaScript Applications' --baseUrl 'https://demoqa.com/books' 
```
 
