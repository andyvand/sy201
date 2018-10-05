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
### Updated: 10/03/18
See the commit logs for a complete list of changes.

### Contents:

[upnext](#upnext) | [classwork](#classwork) | [programming](#programming) | [referenceLib](#referenceLib) | [codeSamples](#codeSamples) | [tools](#tools)

<a name="upnext"></a>
#### *upnext*

Upcoming Reminders, Readings, Assignments and Extra Activities.  The most-recent version will be displayed here and previous versions will be archived in the `upnext` directory of the repository.

<hr>

- Reminders<p>

	Evening EI will go as scheduled tomorrow (10/04) in NI227 starting at 1900.
	
- Readings<p>

	None.
	
- Assignments<p>
 
	By 2359, on Tue 16 Oct, submit Programming Assignment 05 (`pa05`) into the Submitted Work folder in *tcourt* in accordance with your instructor's directions.  The materials for Programming Assignment 05 are available in the `repo201/programming/pa05` directory.
	
- Extra Activities<p>

	I recommend you work on the lesson in `~/repo201/classwork/cw25` as well as the puzzle I sent via e-mail.<p>

<hr>

[Contents](#top)

<a name="classwork"></a>
#### *classwork*

Handouts, stubbed code files, etc., used for in-class assignments.  Subdirectories may be added for individual assignments.

Class_Meeting | Name | Topic  
:-------------|:-----|:-------------
10/03/18 | `cw25` | Today's class was focused on a self-assessment exercise using File I/O and looping.  All the required files (including a README file) are in this directory.
10/02/18 | `cw24` | Today we introduced Programming Assignment 05 (Caesar Cipher) and spent time working on Programming Assignment 04 (Password Validator).  This directory is just a placeholder.
10/01/18 | `cw23` | Today we worked on building a general purpose function to prompt the user for a file name and return an open file handle based on a chosen mode (`"r"` or `"w"`).  This directory is just a placeholder.
09/28/18 | `cw22` | Today we spent time discussing pa04.  An updated version of the executable program and more test case files are available in the `~/repo201/programming/pa04` directory in the repo (use `git pull`).  Note: Your program does not have to handle the special case when the user enters a period (`.`) or a slash (`/`) for the file name.  This directory is just a placeholder.
09/26/18 | `cw21` | *Liang* section 6.1 – 6.5 (skip 6.3.1 *Call Stacks*).  Today we introduced functions.  Several examples were provided and are included in this directory.  A pdf copy of the class handout is also included.
09/25/18 | `cw20` | 6-week exam.  This directory is a placeholder.
09/24/18 | `cw19` | 6-week exam review (cont.).  This directory is a placeholder.
09/21/18 | `cw18` | 6-week exam review.  This directory is a placeholder.
09/19/18 | `cw17` | In this class we started working on a program to decrypt a version of the *Gettysburg Address*.  All the files necessary (including a README file) are located in this directory.
09/18/18 | `cw16` | *Liang*, section 3.3 (p. 67 - 72); 8.1, 8.2 (p. 242 - 253).  In this lab we continued advanced string processing techniques, and worked on a program to scan the `/etc/passwd` file; pull out certain fields; and print them to the screen using formatted output.  This directory contains a template source code file (`.py`).  It's mostly comments that are followed by this: `>> Your line of code here <<`.  If you follow the instructions in the comments and write each line of code specified, you should be able to complete the entire project.  Give it a try!  Also included in this directory is another Python file of advanced string handling techniques.
09/17/18 | `cw15` | *Liang*, section 3.3 (p. 67 - 72); 8.1, 8.2 (p. 242 - 253).  In this class we started learning about advanced string processing techniques.  Sample code from our classwork today is included in this directory.
09/14/18 | `cw14` | In this class we mapped-out the flow chart for completing `pa03`.  A .pdf copy of the flowchart is now available in `~/repo201/programming/pa03`.  This directory (`cw14`) is just a placeholder.
09/12/18 | `cw13` | In this class we continued work on the password cracking program.  The files for that project are in `cw12`.  This directory (`cw13`) is just a placeholder.
09/11/18 | `cw12` | In this class we continued work on the histogram generator for the *Gettysburg Address*, and introduced `pa03` (Password Stretching).  We also introduced the concepts of salting, hashing and stretching.  My hashing slides are included in this folder, along with the template for the password cracker, a file of hashes, and a README file.
09/10/18 | `cw11` | *Liang* sections 13.1 through 13.2.  Introduction to File I/O (Input/Output).  Using the *Gettysburg Address* in a text file, we introduced opening files, reading and processing data, and closing files.  This directory includes a README file and an executable file called `histogram` that counts the frequency of the letters in the `gettysburg.txt` file (also included).
09/07/18 | `cw10` | Loops Review.  We discussed what to watch out for when using `sys.exit()` along with `try...except`.  The example we used for this is called `try.py`.  We also worked on an imaginary Lottery game called `Pick-4`.  All files used in this class are in `cw10`, inclding a README file for `Pick-4`.
09/05/18 | `cw09` | More Loops!  Today we spent most of the class period working on the *Dice Rolling* program.  A README file and the executable version of the program are available in `cw09`.
09/04/18 | `cw08` | *Liang* sections 5.4 through 5.6. Nested Loops.  The code for Checkpoint 5.11 (on p. 146) is included and is setup so you can un-comment and run individual sections.  Also included is a README file for Checkpoint 5.11 to help you keep track of the looping variables while you examine how they work.
08/31/18 | `cw07` | More loops and conditionals. Demo code includes *for* loops using `range(a,b)` (which goes from `a` to `b - 1`) as well as ranging across a string (the *Hello World* example).  Sample code is also included for more complex *while* loops using exception handling, conditionals, user input, `break` statements, and formatted output.
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
`pa05` | Caesar Cipher | In this assignment you will create a program that encrypts and decrypts text files using a Caesar Cipher. This directory includes a .pdf of the assignment, as well as an executable version of the finished program and several test files so you can see how it's supposed to operate and test your own code.
`pa04` | Password Validation | In this assignment you will create a program that reads passwords from a file and determines if each one meets a minimum set of requirements for length and complexity.  The specifications for complexity are stored in a second (separate) file. This directory includes a .pdf of the assignment, as well as an executable version of the finished program and several test files so you can see how it's supposed to operate and test your own code.
`pa03` | Password Stretching | In this assignment you will create a program that performs password stretching; repeating a hashing algorithm a number of times to obfuscate a password. This directory includes a .pdf of the assignment, a .pdf of a high-level flowchart, and an executable version of the finished program so you can see how it's supposed to operate.
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
`asciiChart.pdf` | ASCII Chart for the base (0 - 127) and extended (128 - 255) sets.
`6wkExamReview.pdf` | Review packet for the 6-week exam.

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
`utils` | This is a directory you can use as a template to create your own custom Python library functions.  The included filed (`__init__.py`) must remain in the directory when you use it.  Copy the directory to a location of your choosing using: `cp -R ~/repo201/tools/utils .` (where "`.`" is your current working directory).
`bashrc.txt` | This bashrc file tunes up the look and behavior of your Linux terminal windows.  To install it, open a terminal window and type: <font face="Courier New"><h4>cp ~/repo201/tools/bashrc.txt ~/.bashrc</h4></font> If you receive a message asking to overwrite the existing `.bashrc` file, type "y", followed by return. Close and reopen any existing terminal windows and the changes will take effect.

[Contents](#top)
