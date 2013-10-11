#######################
3D Printing with Slic3r
#######################

..  include::   /references.inc

Modeling 3D objects involves creating them using some kind of CAD program, then
exporting the drawings of the object in some standard file format. To print the
object on a 3D printer, the model needs to be "sliced" into thin layers, and
the printer instructed to "draw" over those layers, depositing the printing
material on the surface of the object as it is being printer, layer by layer.

The tool I an currently using to create the basic 3D model is OpenSCAD. The
slicing tool is Slic3r_

***********
Downloading
***********

The file I installed for my Mac was located on the download area of the project
home page. The file I downloaded is this:

* `slic3r-osx-uni-0-9-10.dmg <http://dl.slic3r.org/mac/slic3r-osx-uni-0-9-10b.dmg>`_

This file is a standard Mac disk image that you install by double clicking
using the ``Finder`` tool. Once the image is unpacked, move the program
``.app`` file into the Applications folder and you are done.

Next, we need to create a link tot he executable file so we can run the program
from the command line:

..  code-block:: text

    sudo ln -s /Applications/Slic3r.app/Contents/MacOS/slic3r /usr/local/bin/slic3r 

**************
Testing Slic3r
**************

Now that we can run the program from the command line, we need to make sure it
runs on a simple test case.

