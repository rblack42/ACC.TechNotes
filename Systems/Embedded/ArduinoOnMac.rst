Arduino on the Mac
##################

..  include::   /references.inc

Getting the Arduino_ working on the Mac is pretty simple. First, download the
Mac IDE file from this link:

    * http://arduino.googlecode.com/files/arduino-1.0.5-macosx.zip

Open this zip file and move the single file to the ``/Applications// folder.

Installing the Java tools
*************************

If your system does not currently have Java installed, the first time you
launch the Arduino_ IDE, it will offer to install them. Let this happen and the
IDE should start.

Testing the setup
*****************

Once the tools are in place, load the example blink program using
:menuselection:`File --> Examples --> 01.Basics --> Blink. You should see this
code in the program window:

..  code-block:: c

    /*
      Blink
      Turns on an LED on for one second, then off for one second, repeatedly.
 
      This example code is in the public domain.
    */
 
    // Pin 13 has an LED connected on most Arduino boards.
    // give it a name:
    int led = 13;

    // the setup routine runs once when you press reset:
    void setup() {                
      // initialize the digital pin as an output.
      pinMode(led, OUTPUT);     
    }

    // the loop routine runs over and over again forever:
    void loop() {
      digitalWrite(led, HIGH);   // turn the LED on (HIGH is the voltage level)
      delay(100);               // wait for a second
      digitalWrite(led, LOW);    // turn the LED off by making the voltage LOW
      delay(100);               // wait for a second
    }

This is an Arduino_ "Sketch", not a full C/C++ program. The IDE links in the
remaining program components to build a real application. We will see how that
happens in a bit.

Running the example
*******************

Configure the IDE for the particular board you have attached. This is done in
two steps:

Set the board
=============

Click on :menuselection:`Tools --> Board`` and click on the board you have Mine
is an Arduino_ UNO, one of the most popular boards available today.

Set the Serial Port
===================

Click on :menuselection:`Tools --> Serial Port``. On my Mac, I was presented
with a bunch of possible choices. I selected ``/dev.tty.usbmodem1411`` based on
a bit of Googling that suggested this was the right port. (It worked!). 

..  note::

    Many messages on the Internet suggested that if you do not see a device
    with a similar name, you might have to update your FTDI drivers. These let
    your USB device act as a serial communication channel. My system work fine
    without needing an update.

Once the board IDE is properly configured, we can run the program.

Running the Example code
************************

Click on the check icon (verify) to compile your code and make sure there are
no errors. Following that, click on the right-arrow icon (upload) to send the
program code to the board. You should see signs that code has been sent to the
board as that takes place. The result of loading the program should be visible
as a yellow LED blinks at a rate of one-second on, one-second off. 

..  note::

    Unfortunately, the new boards have this code installed by default, so we
    really do not know if it is our code running or the default code. Edit the
    program showing in the code window and change the `1000` to `100` in the
    call to ``delay``. Rerun this code and the yellow LED should be blinking
    on and off at ten times the original rate. If this happens, you have a
    working Arduino_ IDE environment!


