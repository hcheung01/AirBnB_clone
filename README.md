# AirBnb Clone

## Purpose
To build a command interpreter that can:
- Create new objects
- Retrieve objects from a file, database
- Do operations on these objects
- Update the attributes of an object
- Destroy objects

## How do I start it?
`git clone <repo-name>`\
`cd AirBnB_clone`\
`./console.py`

## Usage
Available commands:

### all
*Print a list of instances(string representations) that match the class name. If a class name wasn't provided, it prints all instances in the json file

* Usage:
  * Valid Class Names: ['BaseModel', 'User', 'Place', 'State', 'City', 'Amenity', 'Review'] \
  * (hbnb) `all`......prints all instances in the json file \
  * (hbnb) `all <valid class name>`....prints instances of that class

* Common errors:
  * ** class doesn't exist **:  prints when an invalid class name was given to all

### create
* Creates a new instance of <class-name>, prints the id of instance, and saves the instance to the json file.

* Usage
  * Valid Class Names: ['BaseModel', 'User', 'Place', 'State', 'City', 'Amenity', 'Review']
  * Usage: `(hbnb) create <valid class name>`

* Possible errors that can print:
  * **class name missing **: prints when a class name is not given to create
  * ** class doesn't exist **: prints when an invalid class name is given to create
  
  
### destroy
* Deletes an instance based on <class name> and <id>. Saves the deletion to the json file.

* Valid Class Names: ['BaseModel', 'User', 'Place', 'State', 'City', 'Amenity', 'Review']
* Usage: `(hbnb) destroy <class name> <id>`

* Common errors that can print:
  * ** class name missing **: e.g (hbnb) destroy
  * ** class doesn't exist **: prints when an invalid class name was given to destroy
  * ** instance id missing **: prints when an ID was not typed after a valid class name
  * ** no instance found **: when an instance of a valid class name doesn't exist for id
  
### show
* prints the string representation of an instance based on the class name and id

* Valid Class Names: ['BaseModel', 'User', 'Place', 'State', 'City', 'Amenity', 'Review']
* Usage: `(hbnb) show <class name> <valid id>`

* Possible errors that can print:
  * ** class name missing **: prints when a class name is not given to show
  * ** class doesn't exist **: prints when an invalid class name is given
  * ** instance id missing **: prints if the id wasn't typed in after a valid class name
  * ** no instance found **: prints when a bad ID is typed after a valid class name
  
### update
* Updates an instance of <class name> and <id> with an attribute and value. Saves the change to the json file.

* You cannot update 'id', 'created_at', 'updated_at'
* The command ignores everything after the first attribute-value pair

* Valid Class Names: ['BaseModel', 'User', 'Place', 'State', 'City', 'Amenity', 'Review']
* Usage: `(hbnb) update <class name> <id> <attribute> <value>`

* Common errors that can print:
  * ** class name missing **: e.g (hbnb) update
  * ** class doesn't exist **: prints when an invalid class name was given to update
  * ** instance id missing **: prints when an ID was not typed after a valid class name
  * ** no instance found **: when an instance of a valid class name doesn't exist for id
  * ** attribute name missing **: prints when an attribute name wasn't typed in after id
  * ** value missing **: prints when the value wasn't typed after a valid attribute





# Technical Requirements
- All modules have documentation: can be verified with `python3 -c 'print(__import__("my_module").__doc__)'`
- All classes have documentation: can be verified with `python3 -c 'print(__import__("my_module").MyClass.__doc__)`
- All functions inside and outside of a class have documentation: to verify `python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`

## Scripts
- Code is PEP 8 (version 1.7) compliant

## Tests
- Uses the unittest module
- Output from tests should be free of errors
- All tests should execute using: `python3 -m unittest discover tests` from the directory that contains the tests/ directory
- Individual tests can be run by specifying the full path to the file: e.g. `python3 -m unittest tests/test_models/test_base_model.py`

# Repo hierarchy
Import output from tree when close to deadline

# Authors
Hemant Heer  
Heindrick Cheung
