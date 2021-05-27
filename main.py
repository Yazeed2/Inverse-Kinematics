import pyfirmata
from twoDOF import twoDOF
from time import sleep
board = pyfirmata.Arduino('/dev/ttyACM0')

# start an iterator thread so
# serial buffer doesn't overflow
iter8 = pyfirmata.util.Iterator(board)
iter8.start()

# set up pin D9 as Servo Output
basePin = '7'
jointPin = '6'
tipPin = '5'
base = board.get_pin('d:'+ basePin+':s') # pin PWM no 2 
joint = board.get_pin('d:'+ jointPin+':s') # pin PWM no 2 
tip = board.get_pin('d:'+ tipPin+':s') # pin PWM no 2 

# while True:
#     value = input('Position (0-255):')
#     if value == 'exit': 
#        break  
#     else:
#         base.write(float(value))
#         joint.write(float(value))
#         tip.write(float(value))
#         sleep(1)
#         jontAngle, tipAngle = twoDOF(50,68,50,68)
#         joint.write(jontAngle)
#         tip.write(tipAngle)
#         print(jontAngle, tipAngle)
base.write(float(90))

while True: 
    for i in range(68, 107):
        print(i)
        jontAngle, tipAngle = twoDOF(50,i, 50,68)
        joint.write(jontAngle)
        tip.write(tipAngle)
        print(jontAngle, tipAngle) 
        sleep(0.02)
    for i in range(106,69, -1):
            print(i)
            jontAngle, tipAngle = twoDOF(50,i, 50,68)
            joint.write(jontAngle)
            tip.write(tipAngle)
            print(jontAngle, tipAngle)
            sleep(0.02)      
for i in range(68, 106):
        print(i)
        jontAngle, tipAngle = twoDOF(50,i, 50,68)
        joint.write(jontAngle)
        tip.write(tipAngle)
        print(jontAngle, tipAngle) 
        sleep(0.02)
print ('good bye')
