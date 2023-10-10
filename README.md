# AirBnB Clone Project

This project is the initial step in creating an AirBnB clone, a full web application. The primary goal of this step is to develop a command interpreter to manage AirBnB objects.

## Command Interpreter

The command interpreter is a crucial component that allows you to manage objects in the AirBnB project. It enables you to:

- Create new objects (e.g., User, Place)
- Retrieve objects from various sources (files, databases)
- Perform operations on objects (e.g., counting, computing statistics)
- Update attributes of objects
- Delete objects

## Learning Objectives

By the end of this project, you will be able to:

- Create a Python package
- Develop a command interpreter in Python using the cmd module
- Implement unit testing in a large project
- Serialize and deserialize a class
- Read and write JSON files
- Manage datetime
- Work with UUID
- Understand and use *args and **kwargs
- Handle named arguments in a function

## Requirements

### Python Scripts

- Editors allowed: vi, vim, emacs
- All files will be interpreted/compiled on Ubuntu 20.04 LTS using Python3 (version 3.8.5)
- Files should end with a new line
- The first line of all files should be `#!/usr/bin/python3`
- A README.md file at the root of the project folder is mandatory
- Code should follow PEP 8 style guidelines (use pycodestyle version 2.8.*)
- All files must be executable
- Modules, classes, and functions should have documentation explaining their purpose

### Python Unit Tests

- Editors allowed: vi, vim, emacs
- All test files should end with a new line
- Test files should be inside a folder named `tests`
- Use the `unittest` module for testing
- Test files should have a `.py` extension
- Test files and folders should start with `test_`
- Your file organization in the `tests` folder should match your project's structure
- Tests should be executed using the command: `python3 -m unittest discover tests`

## How to Use

To use the command interpreter, run `./console.py` in interactive mode. You can enter commands and interact with the application.

```bash
$ ./console.py
(hbnb) help
Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
```

You can also use non-interactive mode by piping commands into the interpreter:

```bash
$ echo "help" | ./console.py
(hbnb)
```

## Examples

For detailed examples and usage instructions, please refer to the project's documentation.

## Copyright and Plagiarism

- Solutions for the tasks should be developed independently to meet the learning objectives.
- Plagiarism is strictly forbidden, and any form of publishing project content is not allowed.

**Note:** This README provides a brief overview. For more detailed instructions and information, please refer to the project's documentation and resources.
