Puppet 3 on Mac
###############

..  include::   /references.inc

In this note, I will go over how I set up my current Puppet_ installation.
Since I had been experimenting with Puppet_ 2.7 for some time, I started off by
removing all old Puppet files. 

Uninstalling Puppet
*******************

There is no uninstaller for Puppet_, so the files that need to be removed are
these:

..  code-block:: text

    sudo rm /usr/bin/puppet*
    sudo rm /usr/sbin/puppet*

Also, remove these directories:

..  code-block:: text

    sudo rm -rf /private/etc/puppet
    sudo rm -rf /usr/share/doc/puppet

And finally, remove the Puppet_ user:

..  code-block:: text

    sudo dscl . delete /Users/puppet

Last step is to remove the packages from the system:

..  code-block:: text

    sudo pkgutil --forget com.puppetlabs.puppet

Reboot after these steps.

Installing Puppet 3
*******************

Puppet_ for the Mac is available as a ``.dmg`` file. Download a copy using
:program:`wget`:

..  code-block:: text

    cd ~/Downloads
    wget https://downloads.puppetlabs.com/mac/puppet-3.3.1.dmg


Run the installer and let it do its thing. Once this step is complete, we have
a bit of configuration to do.

We need to create a ``puppet`` group and user to run the programs when we set
up automatic sessions to keep the system up to date:

..  code-block:: text

    sudo puppet resource group puppet ensure=present
    sudo puppet resource user puppet ensure=present gid=puppet shell='/sbin/nologin'

Checking the basic installation
*******************************

Now, verify that Puppet_ is installed correctly:

..  code-block:: text
    :emphasize-lines: 1

    puppet --version
    3.3.1

Create a test manifest
======================

Open up an editor and create a simple file named ``site.pp``:

..  code-block:: text

    file { '/tmp/hello':
        content => "Hello, World!\n",
    }

Next, apply this manifest by doing this:

..  code-block:: text
    :emphasize-lines: 1

    puppet apply site.pp
    Notice: Compiled catalog for macbookpro2.austincc.edu in environment production in 0.05 seconds
    Notice: /Stage[main]//File[/tmp/hello]/ensure: defined content as '{md5}bea8252ff4e80f41719ea13cdf007273'
    Notice: Finished catalog run in 0.06 seconds

Verify that puppet is on control
================================

Puppet will make sure that the configuration you have defined stays in place,
even if things change:

..  code-block:: text

    echo Goodbye World > /tmp/hello
    puppet apply site.pp
    Notice: Compiled catalog for macbookpro2.austincc.edu in environment production in 0.05 seconds
    Notice: /Stage[main]//File[/tmp/hello]/content: content changed '{md5}a03b6c0006b4d8a6114db27bd363fbc5' to '{md5}bea8252ff4e80f41719ea13cdf007273'
    Notice: Finished catalog run in 0.07 seconds
    MacBookPro2:puppet3 rblack$ cat /tmp/hello
    Hello, World!

Since system administrators are in the habit of modifying files they work with,
it is a good idea to add comments ot files being managed by Puppet_ so they
unwary admin type will know their modifications may get wiped out the next time
Puppet_ runs!

Organizing manifest files
*************************

On my Macbook, I keep all system related files in a central directory named
/USers/rblack/_system. I keep all Puppet_ related files in a subdirectory under
that location:

..  code-block:: text

    mkdir ~/_system/puppet

..  note::

    Why the underscore in my system directory? I like to make that name appear
    first when I view directories using :program:`Finder`, or type :command:`ls` at
    the :term:`command prompt`.

The Puppet_ recommented organization of the ``puppet`` directory places the
site manifest under a ``manifests`` subdirectory. So, we should do this:

,,  code-block:: text

    cd ~/_system/puppet
    mkdir manifests
    mv site.pp manifests

Check that things still work by doing this:

..  code-block:: text
    :emphasize-lines: 1

    puppet apply manifests/site.pp 
    Notice: Compiled catalog for macbookpro2.austin.rr.com in environment production in 0.03 seconds
    Notice: Finished catalog run in 0.06 seconds


Next, we build a manifest for the current machine (a ``node`` in puppet
terminology). Puppet scans the directory tree we are building checking
manifests for configuration settings If the configuration file is named
``node.pp``, the name of the node defined in that file is matched against the
hostname on the machine running the puppet command. If they match, those rules
are applied. Since we are working on a system with a local hostname of
``MacBookPro2``, we build a node.pp file as follows:

..  literalinclude::    /../puppet3/manifests/nodes.pp

Modify the ``sites.pp`` file so it contains this:

..  code-block:: text

    import node.pp


