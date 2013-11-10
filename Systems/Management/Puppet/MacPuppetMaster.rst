Configuring a Puppet Master on Mac
##################################

..  include::   /references.inc

As part of learning how to use Puppet_ to manage my Mac systems, this note will
cover creating a Puppet Master server in a :term:`virtual machine`. This setup
will eventually be deployed to one of my :term:`VPS` systems.

Installing VirtualBox
*********************

The latest installer for VirtualBox is available from their website:
    
    * http://download.virtualbox.org/virtualbox/4.3.2/VirtualBox-4.3.2-90405-OSX.dmg

Download and run this file to install the basic system on the development
system.

Installing Vagrant
==================

While we could create a conventional Ubuntu_ installation using the available
``.iso`` file, it will be more convenient to use Vagrant_ to set up our server. 

    * http://files.vagrantup.com/packages/a40522f5fabccb9ddabad03d836e120ff5d14093/Vagrant-1.3.5.dmg

Insall as usual.

Create the Ubuntu Server
========================

The Puppet Master will be installed in a Ubuntu_ server. We will set up this
server using a standard Vagrant_ "box", which is a preconfigured :term:`virtual
machine` customized to support Vagrant_.

To get this started, we need to set up a new project with Vagrant_.

..  code-block:: text

    vagrant init precise64 http://files.vagrantup.com/precise64.box
    vagrant up

Vagrant_ stores the basic "box" files under ``~/vagrant.d`` on your system. If
the image is not available locally, the first time you launch this image, it
will be downloaded. After that, the local image will be used.

Once the server is running, you can access it using this:

..  code-block:: text

    vagrant ssh

You will be logged in as a user named ``vagrant``, with ``sudo`` privileges.
That means we can manually install software on this system, or we ca use
Puppet_ to do the work for us.

..  note::

    The first time I tried this on my system, I was loading the latest versions
    of both VirtualBox and Vagrant. The available "box" was not up to date yet,
    so the first time I booted this server up, it complained about out-of-date
    guest additions. To fix this, open the :term:`VM` using VirtualBox directly,
    and update the guest additions.

Log into the server
-------------------


