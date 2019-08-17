import smbus
import time

bus = smbus.SMBus(1)

address= 0x74

CLOSE_POS=180
OPEN_POS=90
MOTORS=(1,2,3,4,5,6,7)
motor_add={1:(1,2),2:(3,4),3:(5,6),4:(7,8),5:(9,10),6:(11,12),7:(13,14)}

def writeRegister (register,value):
    bus.write_byte_data(address, register, value)

def ack():
   writeRegister(37,0)

def open_all(motors):
    for m in motors:
        writeRegister(motor_add[m][0],OPEN_POS)
        writeRegister(motor_add[m][1],128)
    ack()

def close_all(motors):
    for m in motors:
        writeRegister(motor_add[m][0],CLOSE_POS)
        writeRegister(motor_add[m][1],128)
    ack()

def open_motor(motors,to_open):
    for m in motors:
        if m==to_open:
            writeRegister(motor_add[m][0],OPEN_POS)
        else:
            writeRegister(motor_add[m][0],CLOSE_POS)
        writeRegister(motor_add[m][1],128)
    ack()


while True:
    open_motor(MOTORS,1)
    time.sleep(1)
    open_motor(MOTORS,2)
    time.sleep(1)