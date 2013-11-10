Installing HomeBrew on Mac
##########################

..  include::   /references.inc

One of the best tools for installing software on a Mac is the HomeBrew_ system. HomeBrew_ is a Ruby_ based program that uses a "formula" to define how to download and install a large number of popular programs. HomeBrew_ will manage compiling many of these packages from source code, making sure that everything on your system is up to date and works well. 

Installing
**********

HomeBrew_ is a Ruby_ program, so we need a recent version of RUby on the Mac.
Fortunately, the default installation of Mac OS-X has Ruby_ installed:

..  code-block:: text
    :emphasize-lines: 1

    ruby --verison
    ruby 1.8.7 (2012-02-08 patchlevel 358) [universal-darwin12.0]

This command will install HomeBrew_:

..  code-block:: text

    ruby -e "$(curl -fsSL https://raw.github.com/mxcl/homebrew/go)"

Setting the system path
***********************

HomeBrew_ installed packages as a normal user (it does not need ``sudo`` for
most commands). All packages are installed under ``/usr/local/Cellar`` (where
else would you keep your "brew"?), then symlinked into ``/usr/local/bin``. We
need to make sure the packages installed by HomeBrew_ are chosen before any
default versions installed on your system. To make this happen we need to add a
line to your ``.bash_profile`` file in your home directory. 

..  note::
    
    This file is not present by default on the Mac. Just create it with a text
    editor.

..  code-block:: text

    xport PATH="/usr/local/bin:$PATH"

Updating the system
*******************

With HomeBrew_ installed, you will need to update your system so the tool can find the most current packages. This should be done periodically, especially before installing a new package:

..  code-block:: text

    brew update

Cheking the installation
************************

ANother good thing to do periodically is to make sure HomeBrew_ is happy witht he setup on your system. RUn this:

..  code-block:: text

    brew doctor

If any issues are reported, it is a good idea to resolve them right away. Most issues can be figured out with a bit of "Googling"
