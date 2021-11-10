<p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="artwork/CPT.png" alt="Project logo"></a>
</p>

<h3 align="center">Cryptocurrency Price Ticker</h3>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()

</div>

---

<p align="center"> Cryptocurrency Price Ticker
    <br> 
</p>

## 📝 Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Circuit](#circuit)
<!-- - [Server Details](#server)
- [MQTT Topic Details](#mqtt)
- [API Details](#api) -->
- [Usage](#usage)
- [List Of Components](#list)
- [Built Using](#built_using)
- [Authors](#authors)

## 🧐 About <a name = "about"></a>

This repo contains

- Backend
- Firmware
- Detailed instructions

for Cryptocurrency Price Ticker.

## Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your system.

### Prerequisites

Things you need to install the FW.

```
- Arduino IDE
```

### Installing <a name = "installing"></a>

A step by step series that tell you how to get the Firmware and Backend running

#### ESP32 Configuration

You should have Arduino IDE Installed

1.  Add ESP32 Board to your Arduino IDE
1.  In your Arduino IDE, go to File> Preferences
    Installing ESP32 Add-on in Arduino IDE Windows, Mac OS X, Linux open preferences
1.  Enter `https://dl.espressif.com/dl/package_esp32_index.json`
    into the “Additional Board Manager URLs” field then, click the “OK” button:
    Note: if you already have the ESP32 boards URL, you can separate the URLs with a comma(each board will go to neaw line) as follows:
    `https://dl.espressif.com/dl/package_esp32_index.json,\n http://arduino.esp8266.com/stable/package_esp8266com_index.json`

1.  Open the Boards Manager. Go to Tools > Board > Boards Manager…
1.  Search for ESP32 and press install button for the ESP32 by Espressif Systems“:
1.  That’s it. It should be installed after a few seconds.
1.  In your Arduino sketchbook directory, create tools directory if it doesn't exist yet.
1.  Unpack the tool into tools directory(present in libs/ESP32FS-1.0.zip) (the path will look like <home_dir>/Arduino/tools/ESP32FS/tool/esp32fs.jar).
1.  Close and re-open the Arduino IDE.

1.  Now copy the contents of the libs folder to the libraries directory of your Arduino
    1. If you are using windows, the libraries directory will be Documents/Arduino/libraries

##### ESP32 Node FW Uploading

1.  Select ESP32 Dev Module from Tools->Board->ESP32
2.  Select the correct port from Tools->Port
3.  Then open Firmware.ino file,
4.  Select Tools > ESP32 Sketch Data Upload menu item. This should start uploading the files into ESP32 flash file system.
5.  Now Upload the Code to your ESP32 Dev Module.
6.  Your ESP32 is now ready to be used.

## Circuit <a name = "circuit"></a>

### ESP32 Dev Module Pinout

Follow the pinout diagram given below to connect different components to your ESP32 Dev Module board.

![Pinout](Circuit/esp32pinout.jpg)

### Complete Circuit Diagram

Here's the complete circuit diagram of the system.

![CircuitDiagram](Circuit/Circuit_bb.png)

### Other Components

```http
Other components pin connection details
```

#### MAX7219 Dot Matrix Display

```MAX7219 Dot Matrix Display Connected with ESP32```

| MAX7219 Pins | ESP32 | 
| :--- | :--- | 
| `3.3V` | `3.3V` |
| `CLK` | `D18` | 
| `DIN` | `D23` | 
| `CS` | `D15` | 
| `GND` | `GND` |

#### Display On/Off Button

```Display On/Off Button Connected with ESP32```

| MAX7219 Pins | ESP32 | 
| :--- | :--- | 
| `PIN1` | `D32` |
| `PIN2` | `GND` | 


## Usage <a name = "usage"></a>

1.  Upload the code to your ESP32.
2.  Power on your ESP32, it will present you with an AP named `CPT-abc` (while `CPT` can be changed in the portal and `abc` is a unique id for each esp32) 
3.  Default captive portal password `123456789AP` which can be changed in captive portal. 
4.  Connect to the ESP32 access point and open the web-browser and navigate to the link `http://esp32.local/_ac`. This link will work on most of the operating systems but if your operating system is not allowing to open it, you may want to check the captive portal IP Address from the serial monitor and can use that IP address inplace of the above mentioned URL. 
5.  The default access IP Address is `http://192.168.4.1/_ac` 
6.  You will be presented with a main dashboard as shown below(based on your device)
![SCR1](artwork/scr1.png)

7.  Once connected to a WiFi network, you can again access the captive portal using same URL or the IP Address from the Serial monitor.
8. The data is published to the MQTT Topic `CPT/{hostname}` while the hostname is the one which you can define in Settings page of the captive portal.
9. You can open settings page with following default credentials
   1.  User: **AP Name (CPT)**
   2.  Password: **admin**

## List of Components <a name = "list"></a>

Following components are used to make this project

1.  ESP32 Dev Module
    ○ https://www.amazon.com/ESP32-WROOM-32-Development-ESP-32S-Bluetooth-Arduino/dp/B084KWNMM4/ref=sr_1_3?dchild=1&keywords=esp32+devkit&qid=1635342032&sr=8-3
2.  LED Matrix 4x (8x8 Matrix)
    ○ https://www.amazon.com/HiLetgo-MAX7219-Arduino-Microcontroller-Display/dp/B07FFV537V/ref=sr_1_12?dchild=1&keywords=led+matrix&qid=1635341741&sr=8-12
3.  On/OFF Switch
    ○ https://www.amazon.com/URWOOW-Latching-Button-Household-Appliances/dp/B08F7ZR4VW/ref=sr_1_10_sspa?dchild=1&keywords=on+off+button&qid=1610176872&sr=8-10-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzRElYRElPQU1IQkFXJmVuY3J5cHRlZElkPUEwOTk2NzUwMVlWTkJPQ1ozWDdSVyZlbmNyeXB0ZWRBZElkPUEwNTg4Nzg1MUhTWTNNSEcyRlZLViZ3aWRnZXROYW1lPXNwX210ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU=

## ⛏️ Built Using <a name = "built_using"></a>


- [Arduino](https://www.arduino.cc/) - Embedded Framework and IDE - For Sensor Node Design


## ✍️ Authors <a name = "authors"></a>

- [@Nauman3S](https://github.com/Nauman3S) - Development and Deployment
