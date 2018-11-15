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
  
If the json file is empty, there is no output on the console's stdout
```
(hbnb) all
(hbnb)
```
If the json file was reloaded with objects already in it, the console will show all instances of every class
```
(hbnb) all
["[Place] (862752c6-b7b3-43bb-91c3-59554a0fb41a) {'created_at': datetime.datetime(2018, 11, 15, 3, 49, 38, 641434), 'id': '862752c6-b7b3-43bb-91c3-59554a0fb41a', 'updated_at': datetime.datetime(2018, 11, 15, 3, 49, 38, 641458)}", "[BaseModel] (c180b06f-49eb-4fea-9b34-b49f1ddc0e82) {'created_at': datetime.datetime(2018, 11, 15, 3, 49, 34, 471458), 'id': 'c180b06f-49eb-4fea-9b34-b49f1ddc0e82', 'updated_at': datetime.datetime(2018, 11, 15, 3, 49, 34, 471485)}", "[City] (3770d0cc-7d49-452c-833f-21fb275c5998) {'created_at': datetime.datetime(2018, 11, 15, 3, 49, 22, 329061), 'id': '3770d0cc-7d49-452c-833f-21fb275c5998', 'updated_at': datetime.datetime(2018, 11, 15, 3, 49, 22, 329087)}", "[State] (81d41258-7c0c-47f3-b3d5-a078b66f0a9c) {'created_at': datetime.datetime(2018, 11, 15, 3, 49, 24, 226780), 'id': '81d41258-7c0c-47f3-b3d5-a078b66f0a9c', 'updated_at': datetime.datetime(2018, 11, 15, 3, 49, 24, 226806)}", "[Place] (a2c9a0c6-0d94-4bf5-ba32-357ee73f08fb) {'created_at': datetime.datetime(2018, 11, 15, 3, 49, 15, 310153), 'id': 'a2c9a0c6-0d94-4bf5-ba32-357ee73f08fb', 'updated_at': datetime.datetime(2018, 11, 15, 3, 49, 15, 310179)}", "[Amenity] (dc5d752b-d403-4c7d-aaa0-5f7a2dcaeb1d) {'created_at': datetime.datetime(2018, 11, 15, 3, 49, 43, 611294), 'id': 'dc5d752b-d403-4c7d-aaa0-5f7a2dcaeb1d', 'updated_at': datetime.datetime(2018, 11, 15, 3, 49, 43, 611319)}", "[Amenity] (570bfab8-f90c-4e46-90f2-961955754450) {'created_at': datetime.datetime(2018, 11, 15, 3, 49, 18, 286804), 'id': '570bfab8-f90c-4e46-90f2-961955754450', 'updated_at': datetime.datetime(2018, 11, 15, 3, 49, 18, 286831)}", "[BaseModel] (3280b43e-486a-4484-badc-5915e9756bc9) {'created_at': datetime.datetime(2018, 11, 15, 3, 49, 27, 763802), 'id': '3280b43e-486a-4484-badc-5915e9756bc9', 'updated_at': datetime.datetime(2018, 11, 15, 3, 49, 27, 763839)}", "[Review] (50168e1f-2874-4a5e-94b2-8348f371fb57) {'created_at': datetime.datetime(2018, 11, 15, 3, 49, 57, 274072), 'id': '50168e1f-2874-4a5e-94b2-8348f371fb57', 'updated_at': datetime.datetime(2018, 11, 15, 3, 49, 57, 274098)}"]
```
If you want to narrow down the output to a specific class
```
(hbnb) all BaseModel
["[BaseModel] (c180b06f-49eb-4fea-9b34-b49f1ddc0e82) {'created_at': datetime.datetime(2018, 11, 15, 3, 49, 34, 471458), 'id': 'c180b06f-49eb-4fea-9b34-b49f1ddc0e82', 'updated_at': datetime.datetime(2018, 11, 15, 3, 49, 34, 471485)}", "[BaseModel] (3280b43e-486a-4484-badc-5915e9756bc9) {'created_at': datetime.datetime(2018, 11, 15, 3, 49, 27, 763802), 'id': '3280b43e-486a-4484-badc-5915e9756bc9', 'updated_at': datetime.datetime(2018, 11, 15, 3, 49, 27, 763839)}"]
```

### create
* Creates a new instance of 'class-name', prints the id of instance, and saves the instance to the json file.

* Usage
  * Valid Class Names: ['BaseModel', 'User', 'Place', 'State', 'City', 'Amenity', 'Review']
  * Usage: `(hbnb) create <valid class name>`

* Possible errors that can print:
  * **class name missing **: prints when a class name is not given to create
  * ** class doesn't exist **: prints when an invalid class name is given to create
  
  
* Example Output:
```
(hbnb) create BaseModel
220efcfc-f4ee-4eeb-92c5-7976ec2a6a89
(hbnb) create Place
110619ac-fd6e-4ef8-b0ea-fdf7825b29da
(hbnb) create State
26dcfe18-6102-4692-a2a1-0166f494ff69
(hbnb) create Review
0fb056a9-3a05-4b5b-9726-fb1f474f4318
```
  
  
### destroy
* Deletes an instance based on 'class name' and 'id'. Saves the deletion to the json file.

* Valid Class Names: ['BaseModel', 'User', 'Place', 'State', 'City', 'Amenity', 'Review']
* Usage: `(hbnb) destroy <class name> <id>`

* Common errors that can print:
  * ** class name missing **: e.g (hbnb) destroy
  * ** class doesn't exist **: prints when an invalid class name was given to destroy
  * ** instance id missing **: prints when an ID was not typed after a valid class name
  * ** no instance found **: when an instance of a valid class name doesn't exist for id
  
* Example Output:
```
(hbnb) all BaseModel
["[BaseModel] (220efcfc-f4ee-4eeb-92c5-7976ec2a6a89) {'created_at': datetime.datetime(2018, 11, 15, 3, 27, 0, 1682), 'id': '220efcfc-f4ee-4eeb-92c5-7976ec2a6a89', 'updated_at': datetime.datetime(2018, 11, 15, 3, 27, 0, 1707)}"]
(hbnb)
(hbnb) destroy BaseModel 220efcfc-f4ee-4eeb-92c5-7976ec2a6a89
(hbnb)
(hbnb) all BaseModel
(hbnb)
```
As you can see, the instance was deleted. `all BaseModel` shows instances that are currently stored in the json file
  
### show
* prints the string representation of an instance based on the class name and id

* Valid Class Names: ['BaseModel', 'User', 'Place', 'State', 'City', 'Amenity', 'Review']
* Usage: `(hbnb) show <class name> <valid id>`

* Possible errors that can print:
  * ** class name missing **: prints when a class name is not given to show
  * ** class doesn't exist **: prints when an invalid class name is given
  * ** instance id missing **: prints if the id wasn't typed in after a valid class name
  * ** no instance found **: prints when a bad ID is typed after a valid class name
  
* Example Output:
Let's create 3 instances
```
(hbnb) all
["[Amenity] (2b37982f-bba2-447a-b658-81243650f0fd) {'created_at': datetime.datetime(2018, 11, 15, 3, 34, 43, 263564), 'id': '2b37982f-bba2-447a-b658-81243650f0fd', 'updated_at': datetime.datetime(2018, 11, 15, 3, 34, 43, 263590)}", "[Amenity] (6f727d54-dd8f-4bb8-8796-c12b4d60e018) {'created_at': datetime.datetime(2018, 11, 15, 3, 34, 51, 482912), 'id': '6f727d54-dd8f-4bb8-8796-c12b4d60e018', 'updated_at': datetime.datetime(2018, 11, 15, 3, 34, 51, 482937)}", "[Amenity] (5c47c464-47f3-4bd7-96d3-1c87338ddad0) {'created_at': datetime.datetime(2018, 11, 15, 3, 34, 57, 622834), 'id': '5c47c464-47f3-4bd7-96d3-1c87338ddad0', 'updated_at': datetime.datetime(2018, 11, 15, 3, 34, 57, 622861)}"]
```
Let's use that information to display the second instance of Amenity
```
(hbnb) show Amenity 6f727d54-dd8f-4bb8-8796-c12b4d60e018
[Amenity] (6f727d54-dd8f-4bb8-8796-c12b4d60e018) {'created_at': datetime.datetime(2018, 11, 15, 3, 34, 51, 482912), 'id': '6f727d54-dd8f-4bb8-8796-c12b4d60e018', 'updated_at': datetime.datetime(2018, 11, 15, 3, 34, 51, 482937)}
```
  
### update
* Updates an instance of 'class name' and 'id' with an attribute and value. Saves the change to the json file.

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
  
Let's create an instance of Place and update it with an attribute called 'rooms'
```
(hbnb) create Place
333ef6ff-3ffd-4124-8349-940d43c89e72
(hbnb) update Place 333ef6ff-3ffd-4124-8349-940d43c89e72 rooms 5
(hbnb)
(hbnb)
(hbnb) show Place 333ef6ff-3ffd-4124-8349-940d43c89e72
[Place] (333ef6ff-3ffd-4124-8349-940d43c89e72) {'id': '333ef6ff-3ffd-4124-8349-940d43c89e72', 'created_at': datetime.datetime(2018, 11, 15, 3, 39, 41, 148125), 'updated_at': datetime.datetime(2018, 11, 15, 3, 39, 41, 148149), 'rooms': '5'}
```



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
```
├── AUTHORS
├── console.py
├── file.json
├── models
│   ├── amenity.py
│   ├── base_model.py
│   ├── city.py
│   ├── engine
│   │   ├── file_storage.py
│   │   ├── __init__.py
│   ├── __init__.py
│   ├── place.py
│   ├── review.py
│   ├── state.py
│   └── user.py
├── README.md
└── tests
    ├── __init__.py
    └── test_models
        ├── __init__.py
        ├── test_amenity.py
        ├── test_base_model.py
        ├── test_city.py
        ├── test_engine
        │   ├── __init__.py
        │   └── test_file_storage.py
        ├── test_place.py
        ├── test_review.py
        ├── test_state.py
        └── test_user.py
```

# Authors
Hemant Heer  
Heindrick Cheung
