# Alt-TAB Proximity Switcher

## Overview

This project uses an Arduino with an ultrasonic sensor to detect proximity and switches applications on your laptop by simulating an "Alt + Tab" keypress. The project logs the detection events and the corresponding distances to a CSV file.

## Features

- Detects the presence of a person using an ultrasonic sensor.
- Simulates "Alt + Tab" keypress to switch applications on detection.
- Logs detection events with timestamps and distances to a CSV file.
- Initial cooldown period to avoid immediate switching on startup.

## Components

- Arduino board
- Ultrasonic sensor (HC-SR04)
- Laptop/PC with Python installed
- USB cable to connect Arduino to laptop/PC

## Arduino Setup

### Wiring

- VCC of HC-SR04 to 5V on Arduino
- GND of HC-SR04 to GND on Arduino
- Trig pin of HC-SR04 to digital pin 9 on Arduino
- Echo pin of HC-SR04 to digital pin 10 on Arduino

### Arduino Code

Upload the Arduino code from the `arduino_code.ino` file to your Arduino board.

## Python Setup

### Requirements

- Python 3.x
- `pyserial` library for serial communication
- `pyautogui` library for simulating keypresses

Install the required libraries using pip:

```bash
pip install pyserial pyautogui
```

## Usage

1. Connect the Arduino to your laptop/PC using a USB cable.
2. Upload the Arduino code to the Arduino board.
3. Run the Python script using the command:

```bash
python proximity_switcher.py
```

