lircapi
=======

Extremely basic Python API for using lirc. I wrote this specifically for raspberry pi (raspbian) to blast (IRSend) using my MCE eHome Infrared Transceiver.

Takes the format http://[address]:[port]/[remote]/[button]
For example:
http://192.168.1.49:8085/onkyo/KEY_POWER

Install
=======

cd ~

sudo apt-get install python-cherrypy3 python-bottle python-configobj git

git clone git://github.com/p3tecracknell/lircapi.git

cd lircapi

sudo python lircapi.py


Setting up LIRC
===============

Instructions borrowed from http://alexba.in/blog/2013/01/06/setting-up-lirc-on-the-raspberrypi/

Install lirc:
$ sudo apt-get install lirc

Change your /etc/lirc/hardware.conf:
DRIVER="default"
DEVICE="/dev/lirc0"
MODULES="lirc_rpi"

Restart lircd

$ sudo /etc/init.d/lirc restart

Test the IR receiver

$ sudo /etc/init.d/lirc stop

$ mode2 -d /dev/lirc0

Point a remote at the receiver and verify space/pulse

Run the following to see what commands can be used:

$ irrecord --list-namespace

Create a remote configuration file by stopping lirc to free up /dev/lirc0

$ sudo /etc/init.d/lirc stop

Create a new remote control configuration file (using /dev/lirc0) and save the output to ~/lircd.conf

$ irrecord -d /dev/lirc0 ~/lircd.conf

Make a backup of the original lircd.conf file

$ sudo mv /etc/lirc/lircd.conf /etc/lirc/lircd_original.conf

Copy over your new configuration file

$ sudo cp ~/lircd.conf /etc/lirc/lircd.conf

Start up lirc again

$ sudo /etc/init.d/lirc start

Verify the irsend usingthe remote you set up earlier.
List all of the commands that LIRC knows for 'yamaha'

$ irsend LIST yamaha ""

Send the KEY_POWER command once

$ irsend SEND_ONCE yamaha KEY_POWER

Send the KEY_VOLUMEDOWN command once

$ irsend SEND_ONCE yamaha KEY_VOLUMEDOWN

