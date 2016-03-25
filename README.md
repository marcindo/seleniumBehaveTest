# seleniumBehave

This is a sample test framework which uses BDD to test web pages, and was written as a part of job application.
It uses behave framework which is essentially  cucumber clone for python and selenium webdriver to control web pages 

### Setup
For those unfamiliar with python:
- First install python, >2.7 is a must, code was tested with both 2.7 and 3.3 versions
- Then get pip by running get-pip.py from [here](https://bootstrap.pypa.io/get-pip.py)

- Make sure that pip is added to system path.
- Then clone this repo and go to the main directory, run:

<pre>pip install -r requirements.txt</pre>
In case of some access errors try to use sudo on Mac or run cmd as administrator on windows

Browser used to run test is hardcoded as Firefox for now, so make sure it is installed, newest version will do.
However, test code was also tested on Chrome, due to the usage of selenium action chains it will **not work** on Safari

### Running code
Very simple - just type 
<pre>behave</pre>
in terminal, or alternatively run test_runner.py (really, it does exact same thing)

###Code organization
Main code is stored in *features* directory. There are some highlevel level behave files
- .features file which stores business logic level test description written in BDD friendly format
- environment.py which stores environment setup for behave and takes care of logging
- test code in steps/selenium-test.py with test steps, each step calls one method which in turn call for page objects methods

Actual stuff is done at lower level using my own version of Page Object Pattern stored in *pages*, it consist of three elements:
- page objects stored in pages.py

	Every page accessed during test is a separate object and features,
	- real elements present on the page imported as its attributes.
	- private functions for manipulating those elements, usually they just call for one function of the element, unless it makes sense to call multiple elements at once or do some stuff to the arguments
	- higher level functions that call for the private methods and are called in turn by test functions.
	The advantage of this structure is that it's very easy to read what each test method actually does on the page, as well as what actions are available for each page
- generic elements stored in element/basic_elements.py

	In fact they're more like generic element types, and all selenium function calls are separated here. Each basic element has typically one function that is used to interact with it (i.e. fill text box, press button)
	Each real element will then inherit one of these basic types and gain access to the specific method for interaction, and provide it's own locator for this function.
	Sometimes one of the elements won't work with typical selenium implementation, to workaround it some element-specific changes or selenium tricks need to be implemented instead. With this approach, it's possible 
	to just create new basic element, and let that troublesome element use it as its parent.
	The advantage is that one can easily provide modified methods for some elements without modyfing working methods for other elements. Also it is much easier to keep track why and for what elements new changes
	were implemented.
- real elements stored in additional modules under *elements* directory
	They're simple objects that inherit basic element types and have just one attribute - their locator. One exception are some elements that interact with another and could be treated as one entity - these have additional locator
	One example of such element is text box that also need one element picked from dropdown list to work properly

So in short - each real element is an object that holds its locator and inherits typically one method from basic element object and is stored by corresponding page object.

In the framework business logic level test logic, environment setup, highlevel test code, web pages with their actions, low level selenium methods and elements locators all all separated from each other, which allows easy debugging and change adaptation
 
###Test results
Behave will print test results in nice easy-to-read format if run from command line, of if test-runner.py is run in some IDE.
On top of that each test run will generate folder in *logs* with test start date as its name. Inside this log directory a text log file and screenshots from browser made after each step and failure are stored.  