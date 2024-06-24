import serial
import time
import pyautogui  # This module is used to simulate keypresses

# Setup the serial port
ser = serial.Serial('COM4', 9600)

# Function to simulate "Alt + Tab"
def switch_application():
    print("Person detected. Switching application...")
    pyautogui.hotkey('alt', 'tab')

# Main loop
while True:
    try:
        data = ser.readline().decode('utf-8').strip()
        print("Received:", data)

        if data.isdigit():
            distance = int(data)
            if distance < 50:  # Adjust this threshold based on your sensor and setup
                switch_application()
                time.sleep(60)  # Wait for one minute before detecting again

    except serial.SerialException as e:
        print(f"Serial error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
