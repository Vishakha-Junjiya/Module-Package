# 🛠️ Multi-Utility Toolkit Using Python

## 📌 Project Overview

The **Multi-Utility Toolkit** is a Python-based project developed using the concepts of **Modules and Packages**. It provides multiple useful operations through a single menu-driven application.

The project is divided into separate modules to make the code organized, reusable, easy to understand, and maintainable. Each module is responsible for performing a specific set of operations, such as date and time operations, mathematical calculations, random data generation, UUID generation, and file operations.

The project also demonstrates dynamic module importing and the use of Python's built-in `dir()` function to explore module attributes.

This project helps demonstrate the practical implementation of modular programming in Python.

---

## 🎯 Project Objectives

The main objectives of this project are:

* To understand the concepts of Python modules and packages.
* To divide a large program into smaller, reusable modules.
* To implement a menu-driven application.
* To perform date and time operations using Python.
* To perform mathematical calculations using the `math` module.
* To generate random numbers, lists, passwords, and OTPs.
* To generate unique identifiers using UUID.
* To perform file operations using a custom module.
* To explore module attributes using the `dir()` function.
* To understand dynamic module importing.
* To improve code reusability, readability, and maintainability.

---

## ⚙️ Functional Requirements

The application provides the following features:

### 1. Date and Time Operations

This module provides different date and time utilities.

**Features:**

* Display the current date and time.
* Calculate the difference between two dates.
* Display dates in a custom format.
* Measure elapsed time using a stopwatch.
* Run a countdown timer.

### 2. Mathematical Operations

This module performs mathematical calculations using Python's built-in `math` module and mathematical formulas.

**Features:**

* Calculate the factorial of a number.
* Calculate compound interest.
* Perform trigonometric operations.
* Calculate the area of a circle.
* Calculate the area of a rectangle.
* Calculate the area of a triangle.

### 3. Random Data Generation

This module generates random values using Python's `random` module.

**Features:**

* Generate a random number.
* Generate a random list.
* Generate a random password.
* Generate a random OTP.

### 4. UUID Generation

This module generates a universally unique identifier using Python's `uuid` module.

**Features:**

* Generate a UUID using UUID version 4.
* Display the generated unique identifier.

### 5. File Operations

This module contains custom file-operation functionality.

**Features:**

* Access file-operation functionality through a separate module.
* Keep file-related operations separate from the main program.
* Reuse file-operation functions through imports.

*Note: The exact file operations depend on the functions implemented in `Module/file_operation.py`.*

### 6. Explore Module Attributes

This feature demonstrates how to explore Python module attributes dynamically.

**Features:**

* Import a module dynamically.
* Use the `dir()` function to display the module's available attributes.
* Understand the attributes and functions provided by a module.

### 7. Exit

The user can select the Exit option to terminate the application.

---

## 🗂️ Project Structure

```text
project_7/
│
├── Module/
│   ├── __init__.py
│   ├── Operation.py
│   └── file_operation.py
│
├── Main.py
├── sample.txt
├── modula_&_package.jpg
└── README.md
```

### File Description

| File / Folder              | Description                                                                               |
| -------------------------- | ----------------------------------------------------------------------------------------- |
| `Main.py`                  | The main program that displays the menu and calls the selected operations.                |
| `Module/`                  | A package containing the project's custom Python modules.                                 |
| `Module/__init__.py`       | Identifies the directory as a Python package.                                             |
| `Module/Operation.py`      | Contains date and time, mathematical, random data, UUID, and module-attribute operations. |
| `Module/file_operation.py` | Contains custom file-operation functionality.                                             |
| `sample.txt`               | A sample text file for file-related tasks, if used by the implemented operations.         |
| `modula_&_package.jpg`     | An image related to the project's modules and packages topic.                             |
| `README.md`                | Contains project documentation and instructions.                                          |

---

## 🏗️ Project Architecture

The project follows a modular architecture in which each module handles a specific responsibility.

### Main Program — `Main.py`

The main program acts as the entry point of the application. It displays the menu, accepts the user's choice, and calls the appropriate module function.

### Operation Module — `Module/Operation.py`

This module contains the primary utility functions, including:

* Date and time operations
* Mathematical operations
* Random data generation
* UUID generation
* Module attribute exploration

### File Operation Module — `Module/file_operation.py`

This module separates file-related functionality from the main program, helping improve organization and code reusability.

### Package — `Module/`

The `Module` directory groups related Python files into one package. This allows the main program to import the required functions from different files.

---

## 🔄 Application Workflow

1. The application starts by executing `Main.py`.
2. The welcome message is displayed.
3. The user is shown a menu containing seven options.
4. The user selects an operation.
5. The main program calls the corresponding module or function.
6. The selected operation performs its task and displays the result.
7. The menu appears again so the user can select another operation.
8. The application terminates when the user selects Exit.

---

## 💻 Technologies and Tools Used

| Technology / Tool  | Purpose                                        |
| ------------------ | ---------------------------------------------- |
| Python 3           | Main programming language                      |
| `datetime`         | Working with dates and times                   |
| `time`             | Stopwatch and countdown operations             |
| `math`             | Mathematical and trigonometric calculations    |
| `random`           | Generating random values and data              |
| `uuid`             | Generating unique identifiers                  |
| `string`           | Supporting character-based operations, if used |
| `__import__()`     | Dynamically importing a module                 |
| `dir()`            | Exploring module attributes                    |
| Python Modules     | Separating functionality into different files  |
| Python Packages    | Organizing related modules                     |
| Visual Studio Code | Writing and managing Python code               |
| Git                | Version control                                |
| GitHub             | Hosting and sharing the project repository     |

---

## 📚 Python Concepts Demonstrated

This project demonstrates the following Python concepts:

* Modules and packages
* Import statements
* Custom module creation
* Function definition and function calls
* Menu-driven programming
* Conditional statements
* Loops
* User input and output
* Date and time handling
* Mathematical calculations
* Random data generation
* UUID generation
* File handling concepts
* Dynamic importing
* Built-in functions such as `dir()`
* Code reusability and modular programming

---

## 🔗 Module Importing

The main program imports the required functions from the custom modules.

Example:

```python
from Module.Operation import (
    datetime_timeop,
    math_operation,
    random_data,
    uuid_operation,
    module_attribute
)

from Module.file_operation import file_op
```

This approach allows the main program to access functions defined in separate files without placing all the code in a single Python file.

It also demonstrates how custom modules can be organized inside a package.

---

## 🔍 Dynamic Module Exploration

The project demonstrates dynamic importing using Python's `__import__()` function and module inspection using `dir()`.

The `__import__()` function can import a module based on its name, while `dir()` returns a list of names defined by the module, including its available attributes and functions.

These concepts help users understand how Python modules can be imported and explored programmatically.

---

## ▶️ How to Run the Project

### Prerequisites

* Python 3 installed on your computer.
* A code editor such as Visual Studio Code.
* Basic knowledge of running Python programs.

### Steps

**Step 1: Download or clone the project**

If the project is hosted on GitHub, clone the repository using:

```bash
git clone <your-github-repository-url>
```

Replace the placeholder with your actual repository URL.

**Step 2: Open the project folder**

Open the `project_7` folder in Visual Studio Code or another Python editor.

**Step 3: Check the project structure**

Make sure that `Main.py` and the `Module` folder are in the correct locations.

**Step 4: Run the main program**

Open the terminal in the project directory and execute:

```bash
python Main.py
```

If your system uses the `py` command, you can run:

```bash
py Main.py
```

**Step 5: Select an operation**

Choose an option from the displayed menu and follow the instructions shown on the screen.

---

## 🧪 Sample Menu

```text
Welcome to Multi-Utility Toolkit

Choose an option:

1. Datetime and Time Operations
2. Mathematical Operations
3. Random Data Generation
4. Generate Unique Identifiers (UUID)
5. File Operation (Custom Module)
6. Explore Module Attributes
7. Exit

Enter your choice:
```

The exact output may vary depending on the selected operation and the input entered by the user.

---

## 🌟 Advantages of the Project

* **Modular Design:** The program is divided into separate modules.
* **Code Reusability:** Functions can be imported and reused where needed.
* **Easy Maintenance:** Each module can be updated independently.
* **Improved Readability:** Related functions are grouped together.
* **Easy Expansion:** New operations can be added as separate functions or modules.
* **Practical Learning:** Demonstrates important Python programming concepts.
* **Organized Structure:** Related files are grouped into a package.

---

## 🚀 Future Enhancements

The project can be improved in the future by adding:

* More mathematical operations.
* Additional date and time utilities.
* Stronger password-generation options.
* Improved input validation and error handling.
* More file-management operations.
* A graphical user interface (GUI).
* Automated unit tests.
* Improved documentation and usage examples.

---

## 🧑‍💻 Author

**Vishakha Junjiya**

Python Project — Modules and Packages

---

## 📌 Conclusion

The **Multi-Utility Toolkit** demonstrates how Python modules and packages can be used to develop an organized and reusable application.

By combining date and time utilities, mathematical calculations, random data generation, UUID generation, file operations, and module exploration, the project provides practical experience with multiple Python features.

The project also highlights the importance of modular programming in making applications easier to understand, maintain, and expand.

---

## 🔧 Version Control with Git

Git can be used to track changes made to the project and maintain its development history.

Useful Git commands include:

```bash
git init
git status
git add .
git commit -m "Initial commit"
```

To check the current state of the repository, use:

```bash
git status
```

To record changes, use `git add` followed by `git commit`.

---

## 🌐 Project Hosting with GitHub

GitHub can be used to store the project online, maintain a repository, and share the source code with others.

After configuring the repository and connecting it to the appropriate remote URL, changes can be uploaded using:

```bash
git add .
git commit -m "Update project documentation"
git push
```

Make sure the GitHub remote and branch are configured correctly before running `git push`.

---

**Thank you for checking out the Multi-Utility Toolkit!** 🐍
