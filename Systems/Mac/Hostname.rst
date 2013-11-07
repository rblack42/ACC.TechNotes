Managing the hostname
#####################

Many tools need to refer to the hostname of a system. On the Mac, we can manage
the hostname setting using these commands:

Checking the current hostname
*****************************

The hostname on the system can be determined by using this command:

..  code-block:: text

    hostname

or

..  code-block:: text

    scutil --get HostName

Changing the hostname
*********************

To alter the hostname, do this:

..  code-block:: text

    sudo scutil --set HostName newname


