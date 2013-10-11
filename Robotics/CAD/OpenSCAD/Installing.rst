###################
Installing OpenSCAD
###################

..  include::   /references.inc

OpenSCAD_ runs on all major platforms. Installation is pretty simple.

***********
Mac Install
***********

Download the ``.dmg`` file from the project website:

* `OpenSCAD-2013.06.dmg <https://openscad.googlecode.com/files/OpenSCAD-2013.06.dmg>`_

Install as usual. You will ``double-click`` on the file name to unpack the ``.dmg`` file, then drag the ``.app`` file into the Applications folder. After that, do this from the command prompt:

..  code-block:: text

    sudo ln -s /Applications/OpenSCAD.app/Contents/MacOS/OpenSCAB /usr/local/bin/openscad

You should be able to run the tool from the command line:

..  code-block:: text

    openscad --version
    OpenSCAD version 2013.06 

If you see this, all is well. Go to the :ref:`testing-openscad` page
