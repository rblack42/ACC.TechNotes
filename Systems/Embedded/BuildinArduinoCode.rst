How Arduino build a program
###########################

When the Arduino IDE compiles a :term:`sketch` it actually builds a
conventional C/C++ program by linking in a bunch of standard files on your
system. We can discover exactly how this works by turning on a more verbose
messaging system in the IDE. 

Navigate to :menuselection:`Arduino --> Preferences``. Look for the line with
two check-boxes that control verbosity during compilation and uploading of code
to the board. With these two boxes checked, re-compile your example code and
upload it tot the board. The output you see in this window is, well, verbose! Rather than just dump all of that material into this note, I am going to edit it and explain what you will see.

What is happening here
**********************

Like most IDE systems, basically, the tool is issuing commands to the operating system that run installed programs and pass in a bunch of parameters to those programs. IN our case, the primary program being run is the C/C++ compiler that will initially compile your program code into an :term:`object file`, which is basically a new form of your program closer to the actual :term:`machine language` that your computer's processor understands. These :term:`object files` have holes in them, places where your code references something in some other file. In a later step, your :term:`object file` will be merged with other :term:`object files` to construct a real :term:`executable` file thta can actually be loaded and run on a real computer.

Where are the Arduino tools
===========================

Many of the output lines you will see when verifying your Arduino_ "sketch"
begin with the full :term:`path` to the program the IDE is running. On my
MacBook Pro, this path looks like this:

..  code-block:: text

    /Applications/Arduino.app/Contents/Resources/Java/hardware/tools/avr/bin

This is the directory on my system where are of the real C/C++ tools for the
Arduino_ are located. 

..  note::
   
    Notice how Apple packages an "application". It is basically a directory
    containing a bunch of other things needed to manage thiat application. This
    is nice in that you can remove the application and everything about it by
    removing one directory from your system    


The final part of the first output like is the actual :term:`command: being
given to the :term:`operating system`. In this case, we are launching the
``avr-g++`` program on our computer. This program is actually a management
program that controls the process of compiling a C++ program. The Arduino_
tools are identical to those used in the LInux world to compile C++ programs
for the Pentium processor. They have been modified to generate :term:`machine
code` for the Arduino_ processor (actually an Atmel atmega328p processor).

Everything beyond the ``avr-g++`` program name is a parameter being handed to
that program. The list is pretty long, but each line means something to the
compiler. Here is what I saw on my system:

..  code-block:: text


    avr-g++ 
        -c 
        -g 
        -Os 
        -Wall 
        -fno-exceptions 
        -ffunction-sections 
        -fdata-sections 
        -mmcu=atmega328p 
        -DF_CPU=16000000L 
        -MMD 
        -DUSB_VID=null 
        -DUSB_PID=null 
        -DARDUINO=105 

The next parameter tells the compiler where to look for addition components
that might be needed by the program being compiled. Typically, these will be
"include" lines in the program.

The compiler is being told to look in this directory for those :term:`include
files`:

..  code-block::

    -I/Applications/Arduino.app/Contents/Resources/Java/hardware/arduino/cores/arduino 
    -I/Applications/Arduino.app/Contents/Resources/Java/hardware/arduino/variants/standard 

The next line is important, it tells the compiler where the actual program
:term:`source code` file is located. 
Here is the file to be compiled:

..  code-block:: text

   /var/folders/9n/m1r7sf0568n34mz6t3qzhms00000gn/T/build8620850744663267204.tmp/Blink.cpp 

Notice this weird directory :term:`path`. The system uses a standard place to
collect temporary things created by a variety of programs. Periodically, we can
purge this directory area to free up space on the system, since these
directories are only needed during a compile step. They are left around to save
time when recompiling things just in case that would be helpful. These
directories should be re-created as necessary if needed in case they are
deleted.

Next, the compiler is being told what to place the :term:`object file` it will
produce as a result of this compile step.

..  code-block:: text

    -o /var/folders/9n/m1r7sf0568n34mz6t3qzhms00000gn/T/build8620850744663267204.tmp/Blink.cpp.o 
  
This is interesting because it is not the program we started with at all. The
"sketch" file we started with is named ``Blink.ino``, but we are compiling
``Blink.cpp``. 

This is a file created by the Arduino_ IDE out of the original file and some
standard boilerplate code the IDE merges together to build a real C++ program
:term:`source file`. 

Looking into this temporary directory, we see a bunch of files, but no
``Blink.cpp``. As it turns out, the compile step deleted the :term:`source code`` file, but
left behind the :term:`object file`. Unless the :term:`source file` changes, this :term:`object file`
is all we need to build the final :term:`executable file`.

WHat is also interesting is all of the other :term:`object files` we see in this directory:

..  code-block:: text

    ls *.o
    Blink.cpp.o		Tone.cpp.o		new.cpp.o
    CDC.cpp.o		USBCore.cpp.o		realloc.c.o
    HID.cpp.o		WInterrupts.c.o		wiring.c.o
    HardwareSerial.cpp.o	WMath.cpp.o		wiring_analog.c.o
    IPAddress.cpp.o		WString.cpp.o		wiring_digital.c.o
    Print.cpp.o		main.cpp.o		wiring_pulse.c.o
    Stream.cpp.o		malloc.c.o		wiring_shift.c.o

Wow!. ALl of these files are potentially combined together to make your final :term:`executable file`. This step will be managed by another run of ``avr-g++`` we will see later. SOmewhere in the Arduino_ IDE directory, the original :term:`source code` files for these components will be located. They have been copied into this temporary place as part of the compiling process. 

Searching for them, I located the original files here:

    * /Applications/Arduino.app/Resources/Java/hardware/arduino/cores/arduino

We can examine these files to see how to write conventional programs that run
on the Arduino_.


The next lines are messages from the IDE indicating that it is using many of these pre-compiled files::

..  code-block:: text

   Using previously compiled: /var/folders/9n/m1r7sf0568n34mz6t3qzhms00000gn/T/build8620850744663267204.tmp/malloc.c.o

   Using previously compiled: /var/folders/9n/m1r7sf0568n34mz6t3qzhms00000gn/T/build8620850744663267204.tmp/realloc.c.o
  
   Using previously compiled: /var/folders/9n/m1r7sf0568n34mz6t3qzhms00000gn/T/build8620850744663267204.tmp/WInterrupts.c.o
  
   Using previously compiled: /var/folders/9n/m1r7sf0568n34mz6t3qzhms00000gn/T/build8620850744663267204.tmp/wiring.c.o
  
   Using previously compiled: /var/folders/9n/m1r7sf0568n34mz6t3qzhms00000gn/T/build8620850744663267204.tmp/wiring_analog.c.o
  
   Using previously compiled: /var/folders/9n/m1r7sf0568n34mz6t3qzhms00000gn/T/build8620850744663267204.tmp/wiring_digital.c.o
  
   Using previously compiled: /var/folders/9n/m1r7sf0568n34mz6t3qzhms00000gn/T/build8620850744663267204.tmp/wiring_pulse.c.o
  
   Using previously compiled: /var/folders/9n/m1r7sf0568n34mz6t3qzhms00000gn/T/build8620850744663267204.tmp/wiring_shift.c.o
  
   Using previously compiled: /var/folders/9n/m1r7sf0568n34mz6t3qzhms00000gn/T/build8620850744663267204.tmp/CDC.cpp.o
  
   Using previously compiled: /var/folders/9n/m1r7sf0568n34mz6t3qzhms00000gn/T/build8620850744663267204.tmp/HardwareSerial.cpp.o
  
   Using previously compiled: /var/folders/9n/m1r7sf0568n34mz6t3qzhms00000gn/T/build8620850744663267204.tmp/HID.cpp.o
  
   Using previously compiled: /var/folders/9n/m1r7sf0568n34mz6t3qzhms00000gn/T/build8620850744663267204.tmp/IPAddress.cpp.o
  
   Using previously compiled: /var/folders/9n/m1r7sf0568n34mz6t3qzhms00000gn/T/build8620850744663267204.tmp/main.cpp.o
  
   Using previously compiled: /var/folders/9n/m1r7sf0568n34mz6t3qzhms00000gn/T/build8620850744663267204.tmp/new.cpp.o
  
   Using previously compiled: /var/folders/9n/m1r7sf0568n34mz6t3qzhms00000gn/T/build8620850744663267204.tmp/Print.cpp.o
  
   Using previously compiled: /var/folders/9n/m1r7sf0568n34mz6t3qzhms00000gn/T/build8620850744663267204.tmp/Stream.cpp.o
  
   Using previously compiled: /var/folders/9n/m1r7sf0568n34mz6t3qzhms00000gn/T/build8620850744663267204.tmp/Tone.cpp.o
  
   Using previously compiled: /var/folders/9n/m1r7sf0568n34mz6t3qzhms00000gn/T/build8620850744663267204.tmp/USBCore.cpp.o
  
   Using previously compiled: /var/folders/9n/m1r7sf0568n34mz6t3qzhms00000gn/T/build8620850744663267204.tmp/WMath.cpp.o
  
   Using previously compiled: /var/folders/9n/m1r7sf0568n34mz6t3qzhms00000gn/T/build8620850744663267204.tmp/WString.cpp.o

All of these lines refer to :term:`object files` previously compiled by the
IDE. They do not need to be recompiled unless something in the source code for
those components has changed on the system. Since these are all standard parts
of the Arduino_ system this is not likely to happen, so reusing these files is
speeding up the compile time.

Building a library
==================

In the next few lines, the :term:`IDE` is building a :term:`library` of :term:`object files, again to speed up the compiling process. The tool being used to do this is ``avr-ar``. Here are the commands (stripped of the leading :term:`path`:

..  code-block:: text

 avr-ar rcs /var/folders/9n/m1r7sf0568n34mz6t3qzhms00000gn/T/build8620850744663267204.tmp/core.a /var/folders/9n/m1r7sf0568n34mz6t3qzhms00000gn/T/build8620850744663267204.tmp/malloc.c.o 
avr-ar rcs /var/folders/9n/m1r7sf0568n34mz6t3qzhms00000gn/T/build8620850744663267204.tmp/core.a /var/folders/9n/m1r7sf0568n34mz6t3qzhms00000gn/T/build8620850744663267204.tmp/realloc.c.o 
avr-ar rcs /var/folders/9n/m1r7sf0568n34mz6t3qzhms00000gn/T/build8620850744663267204.tmp/core.a /var/folders/9n/m1r7sf0568n34mz6t3qzhms00000gn/T/build8620850744663267204.tmp/WInterrupts.c.o 
avr-ar rcs /var/folders/9n/m1r7sf0568n34mz6t3qzhms00000gn/T/build8620850744663267204.tmp/core.a /var/folders/9n/m1r7sf0568n34mz6t3qzhms00000gn/T/build8620850744663267204.tmp/wiring.c.o 
avr-ar rcs /var/folders/9n/m1r7sf0568n34mz6t3qzhms00000gn/T/build8620850744663267204.tmp/core.a /var/folders/9n/m1r7sf0568n34mz6t3qzhms00000gn/T/build8620850744663267204.tmp/wiring_analog.c.o 
avr-ar rcs /var/folders/9n/m1r7sf0568n34mz6t3qzhms00000gn/T/build8620850744663267204.tmp/core.a /var/folders/9n/m1r7sf0568n34mz6t3qzhms00000gn/T/build8620850744663267204.tmp/wiring_digital.c.o 
avr-ar rcs /var/folders/9n/m1r7sf0568n34mz6t3qzhms00000gn/T/build8620850744663267204.tmp/core.a /var/folders/9n/m1r7sf0568n34mz6t3qzhms00000gn/T/build8620850744663267204.tmp/wiring_pulse.c.o 
/Applications/Arduino.app/Contents/Resources/Java/hardware/tools/avr/bin/avr-ar rcs /var/folders/9n/m1r7sf0568n34mz6t3qzhms00000gn/T/build8620850744663267204.tmp/core.a /var/folders/9n/m1r7sf0568n34mz6t3qzhms00000gn/T/build8620850744663267204.tmp/wiring_shift.c.o 
avr-ar rcs /var/folders/9n/m1r7sf0568n34mz6t3qzhms00000gn/T/build8620850744663267204.tmp/core.a /var/folders/9n/m1r7sf0568n34mz6t3qzhms00000gn/T/build8620850744663267204.tmp/CDC.cpp.o 
avr-ar rcs /var/folders/9n/m1r7sf0568n34mz6t3qzhms00000gn/T/build8620850744663267204.tmp/core.a /var/folders/9n/m1r7sf0568n34mz6t3qzhms00000gn/T/build8620850744663267204.tmp/HardwareSerial.cpp.o 
avr-ar rcs /var/folders/9n/m1r7sf0568n34mz6t3qzhms00000gn/T/build8620850744663267204.tmp/core.a /var/folders/9n/m1r7sf0568n34mz6t3qzhms00000gn/T/build8620850744663267204.tmp/HID.cpp.o 
/Applications/Arduino.app/Contents/Resources/Java/hardware/tools/avr/bin/avr-ar rcs /var/folders/9n/m1r7sf0568n34mz6t3qzhms00000gn/T/build8620850744663267204.tmp/core.a /var/folders/9n/m1r7sf0568n34mz6t3qzhms00000gn/T/build8620850744663267204.tmp/IPAddress.cpp.o 
/Applications/Arduino.app/Contents/Resources/Java/hardware/tools/avr/bin/avr-ar rcs /var/folders/9n/m1r7sf0568n34mz6t3qzhms00000gn/T/build8620850744663267204.tmp/core.a /var/folders/9n/m1r7sf0568n34mz6t3qzhms00000gn/T/build8620850744663267204.tmp/main.cpp.o 
avr-ar rcs /var/folders/9n/m1r7sf0568n34mz6t3qzhms00000gn/T/build8620850744663267204.tmp/core.a /var/folders/9n/m1r7sf0568n34mz6t3qzhms00000gn/T/build8620850744663267204.tmp/new.cpp.o 
avr-ar rcs /var/folders/9n/m1r7sf0568n34mz6t3qzhms00000gn/T/build8620850744663267204.tmp/core.a /var/folders/9n/m1r7sf0568n34mz6t3qzhms00000gn/T/build8620850744663267204.tmp/Print.cpp.o 
avr-ar rcs /var/folders/9n/m1r7sf0568n34mz6t3qzhms00000gn/T/build8620850744663267204.tmp/core.a /var/folders/9n/m1r7sf0568n34mz6t3qzhms00000gn/T/build8620850744663267204.tmp/Stream.cpp.o 
avr-ar rcs /var/folders/9n/m1r7sf0568n34mz6t3qzhms00000gn/T/build8620850744663267204.tmp/core.a /var/folders/9n/m1r7sf0568n34mz6t3qzhms00000gn/T/build8620850744663267204.tmp/Tone.cpp.o 
avr-ar rcs /var/folders/9n/m1r7sf0568n34mz6t3qzhms00000gn/T/build8620850744663267204.tmp/core.a /var/folders/9n/m1r7sf0568n34mz6t3qzhms00000gn/T/build8620850744663267204.tmp/USBCore.cpp.o 
avr-ar rcs /var/folders/9n/m1r7sf0568n34mz6t3qzhms00000gn/T/build8620850744663267204.tmp/core.a /var/folders/9n/m1r7sf0568n34mz6t3qzhms00000gn/T/build8620850744663267204.tmp/WMath.cpp.o 
avr-ar rcs /var/folders/9n/m1r7sf0568n34mz6t3qzhms00000gn/T/build8620850744663267204.tmp/core.a /var/folders/9n/m1r7sf0568n34mz6t3qzhms00000gn/T/build8620850744663267204.tmp/WString.cpp.o 

Linking the object files
========================

Once all of the :term:`object files` are in place, we can link them together to build the actual :term:`executable file`. Here is the command issued by the :term:`IDE`:

..  code-block:: text

    avr-gcc 
        -Os 
        -Wl,--gc-sections 
        -mmcu=atmega328p 
        -o /var/folders/9n/m1r7sf0568n34mz6t3qzhms00000gn/T/build8620850744663267204.tmp/Blink.cpp.elf 
        /var/folders/9n/m1r7sf0568n34mz6t3qzhms00000gn/T/build8620850744663267204.tmp/Blink.cpp.o 
        /var/folders/9n/m1r7sf0568n34mz6t3qzhms00000gn/T/build8620850744663267204.tmp/core.a 
        -L/var/folders/9n/m1r7sf0568n34mz6t3qzhms00000gn/T/build8620850744663267204.tmp 
        -lm

This step builds a file named ``Blink.elf``. The real :term:`executable file` needed for loading into the Ardiono processor is created next:

..  code-block:: text

    avr-objcopy 
        -O ihex 
        -j .eeprom 
        --set-section-flags=.eeprom=alloc,load 
        --no-change-warnings 
        --change-section-lma .eeprom=0 
        /var/folders/9n/m1r7sf0568n34mz6t3qzhms00000gn/T/build8620850744663267204.tmp/Blink.cpp.elf 
        /var/folders/9n/m1r7sf0568n34mz6t3qzhms00000gn/T/build8620850744663267204.tmp/Blink.cpp.eep 

    avr-objcopy 
        -O ihex 
        -R .eeprom 
        /var/folders/9n/m1r7sf0568n34mz6t3qzhms00000gn/T/build8620850744663267204.tmp/Blink.cpp.elf 
        /var/folders/9n/m1r7sf0568n34mz6t3qzhms00000gn/T/build8620850744663267204.tmp/Blink.cpp.hex 

WHen the smoke clears, we see what happened in all this work. The final :term:`hex file` size is reported:

..  code-block:: text

    Binary sketch size: 1,084 bytes (of a 32,256 byte maximum)

Uploading the program to the Arduino board
******************************************

When we upload the program tot he board, we see this:

..  code-block;; text

    avrdude 
        -C/Applications/Arduino.app/Contents/Resources/Java/hardware/tools/avr/etc/avrdude.conf 
        -v -v -v -v 
        -patmega328p 
        -carduino 
        -P/dev/tty.usbmodem1411 
        -b115200 -
        D 
        -Uflash:w:/var/folders/9n/m1r7sf0568n34mz6t3qzhms00000gn/T/build8620850744663267204.tmp/Blink.cpp.hex:i 

The ``avrdude`` program reads the :term:`hex file` and sends it to the Arduino
board over the serial connection established between the Arduino_ and the host
computer we are using. 

..  note::

    We told ``avrdude`` to display a ton of imformation it generated as it
    worked. In looking over this output we see that the tool sends the program
    bytes to the Arduino, then reads then back to verify that they got loaded
    properly. Normally, we are not interested in seeing this information, so I
    will not include that output here. If you have problems with your board,
    looking this output over might help solve problems.

Here are some of the messages coming from ``avrdude``:

..  code-block:: text

    avrdude: Version 5.11, compiled on Sep  2 2011 at 18:52:52
         Copyright (c) 2000-2005 Brian Dean, http://www.bdmicro.com/
         Copyright (c) 2007-2009 Joerg Wunsch

         System wide configuration file is "/Applications/Arduino.app/Contents/Resources/Java/hardware/tools/avr/etc/avrdude.conf"
         User configuration file is "/Users/rblack/.avrduderc"
         User configuration file does not exist or is not a regular file, skipping

         Using Port                    : /dev/tty.usbmodem1411
         Using Programmer              : arduino
         Overriding Baud Rate          : 115200
    avrdude: Send: 0 [30]   [20] 
    avrdude: Send: 0 [30]   [20] 
    avrdude: Send: 0 [30]   [20] 
    avrdude: Recv: . [14] 
    avrdude: Recv: . [10] 
         AVR Part                      : ATMEGA328P
         Chip Erase delay              : 9000 us
         PAGEL                         : PD7
         BS2                           : PC2
         RESET disposition             : dedicated
         RETRY pulse                   : SCK
         serial program mode           : yes
         parallel program mode         : yes
         Timeout                       : 200
         StabDelay                     : 100
         CmdexeDelay                   : 25
         SyncLoops                     : 32
         ByteDelay                     : 0
         PollIndex                     : 3
         PollValue                     : 0x53

         ...

    avrdude: verifying ...
    avrdude: 1084 bytes of flash verified
    avrdude: Send: Q [51]   [20] 
    avrdude: Recv: . [14] 
    avrdude: Recv: . [10] 

    avrdude done.  Thank you.

AT last, we should see our new program running on the board, and we have a much better understanding of how that all happened!


     
