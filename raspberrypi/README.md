# raspberrypi
Setup instructions, scripts and more useful with raspberrypi 3!

# RASPBERRY PI (Raspbian Stretch Setup)

> Basic instructions for setting up the Raspberry Pi with Raspbian.

## ApplePi-Baker (Mac OSX)

1. Pi-Crust: Select SD-Card or USB drive
   ...Select SD Card
2. Pi-Ingredients IMG Recipe
   ...Restore Backup

## Setup Wifi via command line

`$ sudo iwlist wlan0 scan | grep -i ESSID:`

copy name of desired wifi network (WIFINAME) without quotes

```
$ wpa_passphrase WIFINAME
$ reading passphrase from stdin
$ WIFIPASSWORD
```

```
network={
            ssid="WIFINAME"
            #psk="WIFIPASSWORD"
            psk=EXAMPLE3a871c5de00d6e4be3f74627a53f51ab980f0384670ef

        }
```
copy and paste output from above to bottom of file delete the non-encoded psk

`$ sudo vi /etc/wpa_supplicant/wpa_supplicant.conf`

## Turn on ssh

1. `$ sudo raspi-config`
2. Navigate to Interfacing Options.
3. Scroll down and select SSH > Yes.
