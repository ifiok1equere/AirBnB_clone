# 0x00. AirBnB clone - The console Project

## Description

### Write a command interpreter to manage your AirBnB objects.

This is the first of many steps to building a fully functional web application: it's called the AirBnB clone.
This first step is very important because it forms the basis for other projects to follow: HTML/CSS templating, database storage, API, front-end integration…

One project is linked with the other and will help to:
	* put in place a parent class (called `BaseModel`) to take care of the initialization, serialization and deserialization of your future instances
	* create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
	* create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
	* create all unittests to validate all our classes and storage engine
	* create the first abstracted storage engine of the project: File storage.

## How about the command interpreter?
It is just like the shell except that it is limited to a specific use-case. 
In this case, we want to be able to manage the objects that will be created in
this project as detailed below:
	* Create a new object (ex: a new User or a new Place)
	* Retrieve an object from a file, a database etc…
	* Do operations on objects (count, compute stats, etc…)
	* Update attributes of an object
	* Destroy an object

### Project Requirements
#### Python Scripts
* Allowed editors: `vi`, `vim`, `emacs`
* All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
* All your files should end with a new line
* The first line of all your files should be exactly `#!/usr/bin/python3`
* A `README.md` file, at the root of the folder of the project, is mandatory
* Your code should use the pycodestyle (version `2.8.*`)
* All your files must be executable
* The length of your files will be tested using wc
* All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
* All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
* All your functions (inside and outside a class) should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
* A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

#### Python Unit Tests
* Allowed editors: `vi`, `vim`, `emacs`
* All your files should end with a new line
* All your test files should be inside a folder `tests`
* You have to use the unittest module
* All your test files should be python files (extension: `.py`)
* All your test files and folders should start by `test_`
* Your file organization in the tests folder should be the same as your project
* e.g., For `models/base_model.py`, unit tests must be in: `tests/test_models/test_base_model.py`
* e.g., For `models/user.py`, unit tests must be in: `tests/test_models/test_user.py`
* All your tests should be executed by using this command: `python3 -m unittest discover tests`
* You can also test file by file by using this command: `python3 -m unittest tests/test_models/test_base_model.py`
* All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
* All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
* All your functions (inside and outside a class) should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
* We strongly encourage you to work together on test cases, so that you don’t miss any edge case

## How to use the command interpreter:
### The interpreter can be used in two modes:
- Interactive mode
- Non-Interactive mode

##### In interactive mode
* How to start it/use it/examples
```
	$ ./console.py
	(hbnb)
	help

	Documented commands (type help <topic>):
	========================================
	EOF  help  quit

	(hbnb)
	(hbnb)
	(hbnb) quit
	$
```

##### In non-interactive mode
* How to start it/use it/examples
```
	$ echo "help" | ./console.py
	(hbnb)

	Documented commands (type help <topic>):
	========================================
	EOF  help  quit
	(hbnb) 
	$
	$ cat test_help
	help
	$
	$ cat test_help | ./console.py
	(hbnb)

	Documented commands (type help <topic>):
	========================================
	EOF  help  quit
	(hbnb)
	$
```

All tests should also pass in non-interactive mode: `$ echo "python3 -m unittest discover tests" | bash`
