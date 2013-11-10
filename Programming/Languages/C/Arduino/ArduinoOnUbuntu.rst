Arduino on Ubuntu
#################

..  include::   /references.inc

In this note, we will set up a Ubuntu_ server so we can write code that can be
run on Arduino_ or Teensy2 boards.

Installing the tools
********************

This part is simple:

..  code-block:: text

    sudo apt-get install arduino arduino-code

Checking the installation
*************************

We need to make sure the new tools are in place:

..  code-block:: text
    :emphasize-lines: 1

    avr-gcc --version
    avr-gcc (GCC) 4.5.3
    Copyright (C) 2010 Free Software Foundation, Inc.
    This is free software; see the source for copying conditions.  There is NO
    warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

Compiling a test program
************************

To verify that we can write code as needed, here is a small texst program (as
in "Hello, World!", microcontroller style!) 

..  literalinclude::    code/blink.c

Compile it with this ``Makefile``:

..  literalinclude::    code/Makefile

We can install it by plugging in the Arduino and running this:

..  code-block:: text

    make install

With any luck, the LED on the Arduino should start blinking!
