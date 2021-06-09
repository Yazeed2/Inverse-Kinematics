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
base = board.get_pin('d:'+ basePin+':s') 
joint = board.get_pin('d:'+ jointPin+':s') 
tip = board.get_pin('d:'+ tipPin+':s') 


base.write(float(90))

end = 106
start = 68
x = 50
badIdea = []
goodIdea = []
loop = True
moveIt = False
while loop: 
    for i in range(start, end+1):
        print(i)
        jontAngle, tipAngle = twoDOF(x,i, 50,68)
        joint.write(jontAngle)
        tip.write(tipAngle)
        print(jontAngle, tipAngle) 
        sleep(0.02)
    for i in range(end,start-1, -1):
            print(i)
            jontAngle, tipAngle = twoDOF(x,i, 50,68)
            joint.write(jontAngle)
            tip.write(tipAngle)
            print(jontAngle, tipAngle)
            sleep(0.02)      
for i in range(start, end+1):
        print(i)
        try:
            jontAngle, tipAngle = twoDOF(x,i, 50,68)
            if moveIt: 
                joint.write(jontAngle)
                tip.write(tipAngle)
                sleep(0.02)
            print(jontAngle, tipAngle) 
            
            if(jontAngle < 0  or tipAngle < 0):
                badIdea.append(i)
            else:
                goodIdea.append(i)
        except:
            badIdea.append(i)
print ('good idea', goodIdea)
print('range ', min(goodIdea), 'to', max(goodIdea))
