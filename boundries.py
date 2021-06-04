from twoDOF import twoDOF
from matplotlib import pyplot
import numpy as np


end = 300
x = 0
badIdea = []
goodIdea = []
xcord = []
ycord = []
angles = []
def possible(x,y): 
    try:
        jontAngle, tipAngle = twoDOF(x,y, 50,68)
        # if(jontAngle < 0  or tipAngle < 0 or jontAngle > 180 or tipAngle > 180 ):
        #     return False, 'nigative'
        # else:
        angles.append(jontAngle)
        angles.append(tipAngle)
        return True, None
    except:
        return False, 'math'

for i in range(-1* end, end+1):
    print(round( (abs(i)/ (2*end)) * 100) ,'%')
    row = []
    for j in range(-1* end, end+1):
        isPossible, reason = possible(i, j)
        if(isPossible): 
            xcord.append(i)
            ycord.append(j)

print(max(angles) ) 
print(min(angles) ) 
print(angles)
pyplot.scatter(xcord, ycord)
pyplot.show()
