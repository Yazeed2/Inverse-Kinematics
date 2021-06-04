from twoDOF import twoDOF
import matplotlib.pyplot; print(matplotlib.backends.backend)
end = 300
x = 0
badIdea = []
goodIdea = []
xcord = []
ycord = []
def possible(x,y): 
    try:
        jontAngle, tipAngle = twoDOF(x,y, 50,68)
        if(jontAngle < 0  or tipAngle < 0):
            return False, 'nigative'
        else:
            return True, None
    except:
        return False, 'math'

for i in range(0, end+1):
    # print((i/end) * 100 ,'%')
    row = []
    for j in range(-1* end, end+1):
        isPossible, reason = possible(i, j)
        if(isPossible): 
            xcord.append(i)
            ycord.append(j)

print('done')
matplotlib.pyplot.scatter(xcord, ycord)