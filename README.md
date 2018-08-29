## Resources for SY201, Fall AY2019

##### *Note: Your instructor will walk you through setting up your directory structure on the first day of class.*

<img style="float: left; border-style: none" src="https://drive.google.com/uc?id=1hApO6rkv3h3JJspLd7fef7B9JVD7UeMF" width=50%>
<p style="clear:both;" />

Type the commands below in a terminal session on your VM to create a clone of this repository.

*Note: `ubuntu:~$` is the prompt, not something you type. Also, any line beginning with hashtag (#) is a comment and not something you type.*

``` C
# Entering cd by itself ensures you are in your home directory.
ubuntu:~$ cd
ubuntu:~$ mkdir repo201
ubuntu:~$ cd repo201
# Note: the trailing space and period "." below are very important.  Also note
# that the prompt has changed to reflect my current working directory (repo201)
ubuntu:repo201$ git clone https://www.github.com/geozeke/sy104.git .
```
You're all set! Whenever you want to update your repository, just change to it and type: `git pull`

----

<a name="top"></a>
### Updated: 08/29/18
See the commit logs for a complete list of changes.

### Contents:

[upnext](#upnext) | [classwork](#classwork) | [programming](#programming) | [referenceLib](#referenceLib) | [codeSamples](#codeSamples) | [tools](#tools)

<a name="upnext"></a>
#### *upnext*

Upcoming Reminders, Readings, Assignments and Extra Activities.  The most-recent version will be displayed here and previous versions will be archived in the `upnext` directory of the repository.

<hr>

- Reminders<p>

	Evening EI will go as scheduled starting at 1900 in NI227 on Thrusday, 30 Aug.<p>

- Readings<p>

	By Friday, 31 Aug, Read *Liang*, sections 5.1 through 5.3 (Loops)
	
- Assignments<p>
 
	By 2359, on Tue 11 Sep, submit Programming Assignment 02 (`pa02`) into the Submitted Work folder in tcourt, in accordance with your instructor's directions.  The materials for Programming Assignment 02 are available in the `programming/pa02` directory.
	
- Extra Activities<p>

	None<p>

<hr>

[Contents](#top)

<a name="classwork"></a>
#### *classwork*

Handouts, stubbed code files, etc., used for in-class assignments.  Subdirectories may be added for individual assignments.

Class_Meeting | Name | Topic  
:-------------|:-----|:-------------
08/29/18 | `cw06` | Advanced output formatting and loops. Demo code includes: samples of various format types and simple loops.  The Python formatting reference sheet is available in the `referenceLib` directory of the repo.
08/28/18 | `cw05` | Exception handling using `try...except`. Demo code includes: a sample of `try...except`, exception handling for the adult / drinking age program, and an introduction to string formatting using `.format()`.  A pdf copy of the *Exception Handling* slides is also included.
08/27/18 | `cw04` | *Liang* sections 2.8, 2.9, 4.1 through 4.6, 4.11. More Boolean operations and a discussion of nested conditionals (`if...elif...else`).  Demo code includes: complex Boolean examples, nested conditionals using ages (adult / drinking age), and a simple ATM demo showing why the Python `eval()` function is risky, from a security standpoint.
08/24/18 | `cw03` | *Liang* sections 2.8, 2.9, 4.1 through 4.6, 4.11.  Modulo operator (`%`), integer division (`//`), logical operators (`and`, `or`, `not`) and conditionals (`if...else`).  Demo code and Magic Board notes are included.
08/22/18 | `cw02` | *Liang* sections 2.1 through 2.5.  This directory includes the demo code for the area of a circle as well as a pdf version of my notes from the "Magic Board."
08/21/18 | `cw01` | VM Tuneup and introduction to the python3 environment. This directory contains the code for our in-class demos `hello.py` and `calc.py`
08/20/18 | `cw00` | Welcome and Course Introduction.  My PowerPoint slides from the course introduction are available here.

[Contents](#top)

<a name="programming"></a>
#### *programming*

Handouts, stubbed code files, etc., used for your Programming Assignments.  Subdirectories will be added for individual assignments.

Directory_Name | Title | Topic  
:--------------|:------|:-------------
`pa02` | Port Lookup | For this assignment, you'll develop a program that will allow the user to lookup information about a particular port number.  In addition to the techniques learned in `pa01`, this assignment gives you practice with nested conditionals.  This directory includes a .pdf of the assignment, as well as an executable version of the finished program so you can see how it's supposed to operate.
`pa01` | Calculations and Conversions | Your first programming assignment will introduce you to the Python environment.  You'll practice input, output and using arithmetic operators.  This directory includes a .pdf of the assignment, as well as an executable version of the finished program so you can see how it's supposed to operate.

[Contents](#top)

<a name="referenceLib"></a>
#### *referenceLib*

Library of references, documentation, and other resources.

File Name | Description
:---------|:-------------
`syllabus.pdf` | SY201 Course Syllabus.
`coursePolicy.pdf` | SY201 Course Policy.
`collaborationPolicy.pdf` | SY201 Collaboration Policy.
`section_leader.pdf` | Duties of the Section Leader / Assistant Section Leader.
`python3-methods.pdf` | A helpful reference of commonly used Python 3 methods.
`cmdlineRef.pdf` | A reference for Linux terminal commands.
`asymmetric_encryption.pdf` | An overview of Public Key Encryption and Certificate Signing.
`pythonFormatting.pdf` | Reference sheet for formatted output in Python.

[Contents](#top)

<a name="codeSamples"></a>
#### *codeSamples*

A collection of coding tips and demonstrations for various topics in Python.

Category | File Name | Description
:--------|:----------|:-------------
Documentation | `template.py` | This file provides the template you should use for documenting the code you write for assignments in this class.
Flow | `tryexcept.py` | Demonstration of basic exception handling using `try-except` in Python.

[Contents](#top)

<a name="tools"></a>
#### *tools*

Tools, tips and other useful utilities for the course.

Tool_Name | Purpose
:---------| :------
`bashrc.txt` | This bashrc file tunes up the look and behavior of your Linux terminal windows.  To install it, open a terminal window and type: <font face="Courier New"><h4>cp ~/repo201/tools/bashrc.txt ~/.bashrc</h4></font> If you receive a message asking to overwrite the existing `.bashrc` file, type "y", followed by return. Close and reopen any existing terminal windows and the changes will take effect.

[Contents](#top)
