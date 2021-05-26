from main import board, tip, joint
from math import sqrt, atan, acos, degrees

def calcAngles(x, y, d): 
    '''
    By taking x, y cordinates  and space between servos dimention we can calculate theta1 and theta2 

    '''
    r = sqrt(x**2 + y**2)
    phi2 = atan(y/x)
    phi1 = acos((r**2)/(2 * d * r) )
    theta1 = degrees(phi2) - degrees(phi1)
    phi3 = acos((r**2 - 2* d**2)/ (-d * d**2))
    theta2 =  270 - degrees(phi3)
    return {"theta1": theta1, "theta2": theta2}