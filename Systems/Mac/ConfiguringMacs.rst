Configuring Mac systems
#######################

..  include::   /references.inc

In an attempt to automate the installation of all software I need on a system,
I currently use Puppet_ to control the installation after the basic OS is on
the system.. Unfortunately, we have a chicken and egg problem here. We need to
install Puppet_ before we can automate the rest of the process. 

One solution is to manually get the system into a state where Puppet_ is
available, then use something like :program`Carbon Copy CLoner` to capture that
setup. This is the method I currently use. 


Exploring the current system
****************************

Open up a terminal on the new system and make sure a few basic tools are
installed:

..  code-block:: text
    :emphasize-lines: 1,3

    python --version
    Python 2.7.2
    ruby --version
    ruby 1.8.7 (2012-02-08 patchlevel 358) [universal-darwin12.0]



