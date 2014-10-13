Installing XCode on your Mac
############################

If you intend to do any programming on your Mac, and you probably do if you are
reading these notes, you should install XCode on your Mac. This free package
provides a complete programming environment that many software developers uuse
to build applications for the Mac platform. I rarely use XCode directly, but I
use the tools installed all the time.

Mac App Store
*************

Installing XCode is a time  consuming process, because you have to wait while
the program downloads over your Internet connection and this program is big!

Open up the Mac App Store application and enter "XCode" n the search box. Once
you find the current version, click on :menuselection:`Install`, then go off
and do something else for a while. The tool will download and install like
other things you have installed on your system. 

Once the program installation finishes, Open it up using the Mac
:program:`FInder` tool. XCode will be listed as a normal application. You can
also launch it from the Mac :program:`LaunchPad`. The program will ask you a
few simple questions to complete the setup.

Adding the Command Line Tools
*****************************

Next, with XCode running, click on :menuselection:`XCode --> Developer Tools
--> More Developer Tools` . You will see a web page open up asking you to sign
in. Use your normal Apple credentials to do this.

..  note::

    At one time, you had to register as a developer to get into this site, but
    I believe Apple now makes it available to everyone. If this is not true,
    please let me know and I will update this note. Registering is free, so if
    the system does not let you in, go ahead and sign up.

Select :menuselection:`Command Line Tools (OS X 10.9) for XCode` for your
version of OX-X. If you are not sure what version you have installed, click on
the :menuselection:`Apple Icon` at the top left corner of your screen and
select :menuselection:`About This Mac` to see a screen that will tell you what
your system is running.

When you select the tool version you want, the system will download an
installation file that ends in an extension of ``.dmg``. If this does not
automatically run when it downloads, find the file in your `Downloads` folder
and double-click on it to install the tools.

After this step, you should be able to open up a :program:`Terminal` program
and type in this:

..  code-block:: text

    $ c++ --version
    Apple LLVM version 6.0 (clang-600.0.51) (based on LLVM 3.5svn)
    Target: x86_64-apple-darwin13.4.0
    Thread model: posix
    MacBookPro2:~ rblack$ 

If you see something like this, your installation is complete. Now, go off and
build a great program!

