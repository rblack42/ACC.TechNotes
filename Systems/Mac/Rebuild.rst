Rebuilding a Mac
################

I try to keep my systems in a state where I can rebuild them any time I wish to
do so. To allow this, I need to have a good backup system in place. That will
protect my data so that a rebuild will not result in loss of important stuff.
My current rebuild process for my Mac systems will restore the system to a
clean version of Mountain Lion.

Rebuild USB
***********

I have set up an 8GB USB Flash drive with a bootable copy of OS-X 10.8.5
(Mountain Lion). The rebuild process starts by powering the target system down.

Boot from the USB drive
=======================

Plug in the bootable USB drive, then power the system up while holding down the
:menuselection:`Option` key. The system will display a menu with options on
what you want to do next.

Erase the current drive
=======================

To ensure we get a clean installation, we need to erase the current contents of
the primary disk drive. 

On the boot menu, you should see an entry named :menuselection:`Disk Utility`.
Click on this selection, then select the primary hard drive from the list of
devices located. Then click on the :menuselection:`Erase` tab. Using the
default settings, click on :menuselection:`Erase`. When this step completes,
the drive should be labeled "Untitled".

Exit the :program:`Disk Utility` application, you shoud see the original boot
menu again.

Install the OS
==============

Next, select :menuselection:`Reinstall OS X`. This will start the normal OS
intallation. This can take several minutes. First the files will be copied from
the USB to the system hard disk. Once that phase has been completed, the OS
installer will begin. There are a few points in this process where user input
is required. 

    * Language
    * Keyboard
    * Network (with security password)

You will also be asked if you want to transfer data from another syste, I do
not do this.

I do enable location services in case my latop gets stolen. I might be able to
find it if the thief is not too bright.

Next, provide your AppleId data

These days, I set up iCloud to synchronize my personal data like contact lists,
and calendars.

Basic system configuration
**************************

Once the new system has been set up, it is ready to configure for the work I
need to do on it. Basically, this will require installing a few tools, most of
which are open source (free). I am working hard to autmate this entire process,
so notes on doing that are available in another document:
:doc:`ConfiguringMacs`
