Connecting a Mac to Staff Wireless
##################################

As an employee of |ACC|, I often bring my MacBook Pro to school. ACC_ limits
wireless access for students so they cannot get into "trouble", and so I need
to access the staff wireless, which is less restrictive. This allows me to use
services I need to manage my teaching support systems.

Configuring the Mac
*******************

Step1: Join the right wireless network
======================================

Make sure the Wireless system is turned on (what machine could operate with it
turned off, these days?).

Select :menuselection:`Join Other Network`. In the panel that opens, enter
``StaffAnyConnect``. Make sure the `Remember this network` check box is
checked.  Security is set to `None`.

Step2: Configure the VPN service
================================

Open the `System Preferences` tool. Select `Network` in the panel. 

Click on the small "+" at the bottom left of the network connections list.

Under the :menuselection:`Interface` menu, select `VPN`. The type is `Cisco
IPSEC`. Once these are set, click on :menuselection:`Create` to set up the
connection. 

Click on the new network interface and enter the following information:

* Server Address: 10.29.2.2
* Account name: Your ACC EID number 
* Password, ACCEid password

Click on the :menuselection:`Show VPN status in the menu bar`. 

Click on the :menuselection`Authentication Settings` button:

Enter these:

* Shared Secret: imapuser
* Group Name: ACC WifiVPN

Finally, click on :menuselection:`OK`, then on :menuselection:`Apply`. You
should probably lock this panel so the settings will not get changed. 

Connecting to the VPN
*********************

Once all the settings are in place, click on the wireless network button in the
top menu. Find the `StaffAnyConnect` network, and click on
:menuselection:`Join`. Once the connection is made (watch the menu button to
see when that happens), click on the `VPN Connection icon which should be on
the top menu now. Enter your ACCEid and password and you should connect. 
