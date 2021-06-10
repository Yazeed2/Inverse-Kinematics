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
while False: 
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

class StepMotor: 
    stepPattern = [[1,1,0,0], [0,1,1,0], [0,0,1,1], [1,0,0,1]]
    speed = 1 # steps / second 
    gearRatio = 1 
    def __init__(self, digitalPins, board):
        '''
            digitalPins = [1 ,2 ,3 ,4] arr[int]
            board = pyfirmata [board]
        '''
        self.digitalPins  = digitalPins
        self.board = board
    
    def move(self, steps):
        for step in range(steps): 
            for i in self.stepPattern:
                for j in range(len(i)): 
                    self.board.digital[self.digitalPins[j]].write(i[j])
                sleep(self.speed)