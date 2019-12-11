.. _install:

Installing BlenderQ
===================

:ref:`Go Home <index>`

Dependencies
------------

Ensure that you have the dependencies installed with:

``sudo apt-get install git python3 python3-tk``

for Debian based systems (Ubuntu, Debian, etc), or

```sudo yum install git python3 python3-tk``

for Redhat and CentOS.

Other operating systems will need to install `Git <https://git-scm.com/>`__, `Python <https://www.python.org/>`__, and `Tkinter <https://wiki.python.org/moin/TkInter>`__ per their individual instructions.

Getting BlenderQ
----------------

Using a terminal or git bash:

``git clone https://github.com/AO-StreetArt/BlenderQ.git``

And execute BlenderQ with:

``python3 blenderq.py``

Configuring BlenderQ
--------------------

Before using BlenderQ, we have to tell it where to find the Blender executable.

Open the text file, 'config.ini'.  Change the 'blender.location' value to the location of the executable on your computer.

Next
----

Now that you've got BlenderQ installed, go ahead and check out the :ref:`Use Page <use>`
