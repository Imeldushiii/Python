import serial
import sys
port = 'COM9'
baundrate = 9600
arduino = serial.Serial(port, baundrate, timeout=.1)

while True:
	data = arduino.readline()[:-2]
	if data:

		print(f'[Message: {data.decode()} size: {sys.getsizeof(data)} Long: {len(data)} Type: {type(data)}')
