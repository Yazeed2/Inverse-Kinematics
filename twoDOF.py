from math import sqrt, atan, acos, degrees

def twoDOF(x, y, d1, d2): 
    '''
    d1 is the demension from first joint to second joint d2 is after the second joint
    By taking x, y coordinates  and space between servos dimension we can calculate theta1 and theta2 
    '''
    r = sqrt(x**2 + y**2)
    phi1 = atan(y/x)
    phi2 = acos((d2**2 - d1**2 - r**2)/(-2 * d1 * r) )
    theta1 = degrees(phi1) - degrees(phi2)
    phi3 = acos((r**2 - d1**2 - d2**2)/ (-2 * d1* d2))
    theta2 =  degrees(phi3) - 90
    return theta1, theta2