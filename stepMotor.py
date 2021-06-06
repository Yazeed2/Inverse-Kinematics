import pyfirmata
from time import sleep


board = pyfirmata.Arduino('/dev/ttyACM0')

# start an iterator thread so
# serial buffer doesn't overflow
iter8 = pyfirmata.util.Iterator(board)
iter8.start()
step1 = 8
step2 = 9
step3 = 10
step4 = 11

i = 0 
delay = 0.01
while True: 
    print(i) 
    sleep(delay)        
    board.digital[step1].write(1)
    board.digital[step2].write(1)
    board.digital[step3].write(0)
    board.digital[step4].write(0)
    sleep(delay)        
    board.digital[step1].write(0)
    board.digital[step2].write(1)
    board.digital[step3].write(1)
    board.digital[step4].write(0)
    sleep(delay)        
    board.digital[step1].write(0)
    board.digital[step2].write(0)
    board.digital[step3].write(1)
    board.digital[step4].write(1)
    sleep(delay)        
    board.digital[step1].write(1)
    board.digital[step2].write(0)
    board.digital[step3].write(0)
    board.digital[step4].write(1)
    sleep(delay)        
print('done')