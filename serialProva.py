'''
	Prova de mínims:
		1. Crea un serial
		2. Envia una trama
		3. Rep la resposta
'''
import serial

#obre serial
ser=serial.Serial()
ser.port="/dev/ttyUSB0"
ser.baudrate=9600
ser.bytesize=8
ser.parity=serial.PARITY_EVEN
ser.stopbits=1
ser.xonxoff=False
ser.rtscts=False
ser.dsrdtr=False
ser.timeout=1
ser.open()

#munta trama test
trama='\x10\x49\x01\x00\x4a\x16'
print("Enviant: "+str(trama))

#envia
ser.write(bytearray(trama))
ser.flush()

#resposta
resposta=ser.readlines()

#print resposta
print("Resposta:")
print(type(resposta))
print(resposta)
