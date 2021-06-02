from time import sleep

def smooth(startPos, endPos, delay, func): 
    '''
    startPos, endPos, delay in seconds, servo function 
    '''

    step = 1
    if startPos > endPos: 
        step = -1
    for i in range(startPos, endPos + step, step):
        func(i) 
        sleep(delay / abs(endPos - startPos))