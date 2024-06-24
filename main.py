import serial
import time
import pyautogui  # This module is used to simulate keypresses

# Setup the serial port
# Adjust the port name based on your setup
ser = serial.Serial('COM4', 9600)

# Function to simulate "Alt + Tab"
def switch_application():
    print("Person detected. Switching application...")
    pyautogui.hotkey('alt', 'tab')

# Initial cooldown period
initial_cooldown = 5  # Cooldown period in seconds
print(f"Starting application. Initial cooldown for {initial_cooldown} seconds...")
time.sleep(initial_cooldown)
print("Cooldown period ended. Starting detection...")

# Main loop
while True:
    try:
        data = ser.readline().decode('utf-8').strip()
        print("Received:", data)

        if data.isdigit():
            distance = int(data)
            print(f"Detected distance: {distance} cm")

            if distance < 50:  # Adjust this threshold based on your sensor and setup
                switch_application()
                time.sleep(10)  # Adjust the interval time here
            else:
                print("No person detected within threshold distance.")

    except serial.SerialException as e:
        print(f"Serial error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
