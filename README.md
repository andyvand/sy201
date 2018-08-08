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
### Updated: 08/08/18
See the commit logs for a complete list of changes.

### Contents:

[upnext](#upnext) | [classwork](#classwork) | [labs](#labs) | [referenceLib](#referenceLib) | [codeSamples](#codeSamples) | [tools](#tools)

<a name="upnext"></a>
#### *upnext*

Upcoming Reminders, Readings, Assignments and Extra Activities.  The most-recent version will be displayed here and previous versions will be archived in the `upnext` directory of the repository.

<hr>

- Reminders<p>

	None<p>

- Readings<p>

	None
	
- Assignments<p>
 
	None
	
- Extra Activities<p>

	None<p>

<hr>

[Contents](#top)

<a name="classwork"></a>
#### *classwork*

Handouts, stubbed code files, etc., used for in-class assignments.  Subdirectories may be added for individual assignments.

Class_Meeting | Name | Topic  
:-------------|:-----|:-------------
08/20/18 | `cw00` |Welcome and Course Introduction

[Contents](#top)

<a name="labs"></a>
#### *labs*

Handouts, stubbed code files, etc., used for labs.  Subdirectories may be added for individual assignments.

Directory_Name | Title | Topic  
:--------------|:------|:-------------
`tbd` | TBD | <hr>

[Contents](#top)

<a name="referenceLib"></a>
#### *referenceLib*

Library of references, documentation, setup guides and other resources.

File Name | Description
:---------|:-------------
`coursePolicy.pdf` | SY201 Course Policy.
`collaborationPolicy.pdf` | SY201 Collaboration Policy.
`section_leader.pdf` | Duties of the Section Leader / Assistant Section Leader.
`python3-methods.pdf` | A helpful reference of commonly used Python 3 methods.
`cmdlineRef.pdf` | A quick reference for Linux terminal commands.
`asymmetric_encryption.pdf` | A quick overview of Public Key Encryption and Certificate Signing.

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
