Writing with Sphinx
===================

..  include::   /references.inc

I use Sphinx for all my technical writing. Sphinx_ is a Python standard
package, used to document Python iteslf, and I have used it for quite along
time in my teaching.

Installing Sphinx
-----------------

Installation is simple. With a proper Python setup (see
:doc:`../Languages/Python/InstallingPythonOnMac` for details), all you need to
do is this:

..  code-block:: text

    pip install sphinx
    pip install cloud-sptheme

Sphinx supports themes, and I currently use the "cloud" theme. 

Creating a new document
-----------------------

Once Sphinx is installed, we can create a new document for a project:

..  code-block:: text

    mkdir -p newproject/docs
    cd newproject/docs
    sphinx-quickstart 

You will be asked a few questions about the project. I usually answer these
using the defaults. I then tune things up as I get the project going.

