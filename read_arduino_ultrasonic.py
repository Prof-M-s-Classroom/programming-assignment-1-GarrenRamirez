import serial
import time
from stack import CircularStack

# Replace 'COM3' with the correct port for your system
arduino_port = 'COM3'
baud_rate = 9600

try:
    # Establish connection with Arduino
    arduino = serial.Serial(arduino_port, baud_rate, timeout=1)
    time.sleep(2)  # Allow time for connection to establish
    print("Connected to Arduino. Reading Ultrasonic Sensor data...")

    # Create Circular Stack to store sensor data
    sensor_readings = CircularStack()

    while True:
        if arduino.in_waiting > 0:
            distance = arduino.readline().decode('utf-8').strip()
            sensor_readings.push(distance)
            if distance:
                print(f"Distance: {distance} centimeters")
            print("\n")
            sensor_readings.print_stack()
        time.sleep(2)  # Read every 2 seconds

except KeyboardInterrupt:
    print("Exiting...")
    arduino.close()

except serial.SerialException:
    print("Error: Could not connect to Arduino. Check your port and connection.")
