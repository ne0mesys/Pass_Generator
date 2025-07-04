# 🔐 Password_Gen (GUI) by ne0mesys
This is software is a password generator, written in Python, that allows users to feel safer due to the creation of a more secure password containing special characters. This software is helped by a Graphical 
User Interface display, that allows users to access to it easier. 

The GUI is made up with the library **CustomTkinter** and it uses its stylish widgets, that enhances the program. This software uses the following widgets: *Buttons*, *Labels*, *Switches* & *Entries*.

You are welcome to taste it, donwload it and improve it yourselves! However, REMEMBER to stay tunned for upcoming updates...

This stool serves as a Cybersecurity Tool (Blue Team), which helps users to feel safer. 

By ne0mesys

<p align="center">
  <img src="https://github.com/user-attachments/assets/0155d495-2dfe-45aa-b05c-a869ac3a47e3" alt="Password Generator Screenshot" />
</p>

## Requirements 

### For Linux

Python 3 is required to run this software. In case you don't have it installed, you can find the installation instructions below: 
```
sudo apt update && sudo apt upgrade
sudo apt install python3
```

The ***CustomTkinter*** library is required. If it's not installed, use one of the following methods: 
 
**Option 1 - System-wide installation:**
```
pip3 install customtkinter
```
**Option 2 - Within a virtual environment:**
```
python3 -m venv venv
source venv/bin/activate
pip3 install customtkinter 
```

### For Arch Linux:

Here's a short documentation about how to install the requirements for Arch Linux users:

First, verify whether you have Python installed or not: 
```
python --version
```
or 
```
python3 --version
```

**Step 1) Python Installation**

If you have **Python** installed, proceed to the next step.

if you **DON'T** have it, install it using these commands:
```
sudo pacman -S python
sudo pacman -S python-pip
```

**Step 2) CustomTkinter Installation**

if you have **CustomTkinter** installed, you don't have to do this step.

if you **DON'T** have it, install it using these commands:

**Option 1 - System-wide installation:**

```
pip3 install customtkinter
```

**Option 2 - Within a virtual environment:**

```
python3 -m venv venv
source venv/bin/activate
pip3 install customtkinter 
```

### For Windows

You will need Python 3 and the **CustomTkinter** library:

[Download Python 3 for Windows](https://www.python.org/downloads/windows/)

Open Command Prompt and run:
```
pip install customtkinter
```

## Installation 

### For Linux 

Here's a short documentation about how to install the software for Linux users: 
```
sudo apt install git 
sudo git clone https://github.com/ne0mesys/PyDictionary.git
cd PyDictionary
```

### For Arch Linux

Here's a short documentation about how to install the software for Arch Linux users:
```
sudo pacman -S git
sudo git clone https://github.com/ne0mesys/PyDictionary.git
cd PyDictionary
```

### For Windows

Download the **password_generator.exe** file.

## Execution

### For Windows

*Right-click* over the **password_generator.exe** file, and it will open with the Python 3 software. 

### For Linux & Arch Linux

Once we are in the same folder of the software, we can proceed to enable its execution for Linux users. 

The software includes the Shebang line  ``` #!/usr/bin/env python3 ``` which allows the user to execute it directly, here's a quick guide about the two different ways to execute the software:
* Firstly, we give execution permissions to the file: 
```
sudo chmod +x password_generator.py
```

* Secondly, we execute the program:

```
./password_generator.py
python3 password_generator.py
```

## Author:

* Ne0mesys

Feel free to open an Issue...
```
E-Mail at: ne0mesys.acc@gmail.com
```
