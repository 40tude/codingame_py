import sys
import math
from enum import IntEnum

class Cap(IntEnum):                                                 #IntEnum, not an enum
    E   = 0
    NE  = 1
    N   = 2
    NW  = 3
    W   = 4
    SW  = 5
    S   = 6
    SE  = 7

Directions = ["E", "NE", "N", "NW", "W", "SW", "S", "SE"]

LightX, LightY, ThorX, ThorY = [int(i) for i in input().split()]

while True:
    if (LightX != ThorX):                                           # if not at same abscisse there is an angle
        angle = (-(LightY - ThorY)) / (LightX - ThorX)              # -(LightY - ThorY) because y axis is top down
        #print("angle ", angle, file=sys.stderr)
        angle = math.atan(angle)
    
        if (LightX < ThorX): 
            angle = math.pi + angle
    
        ThorCap = int(angle / (math.pi / 4.0))                      # convert from angle to 0...7
        ThorCap = (ThorCap + 8) % 8                                 # handle cases with negative angles
    
    elif(LightY > ThorY):                                           # manage division by 0 in the previous case when LightX = ThorX
        ThorCap = Cap.S
    else:
        ThorCap = Cap.N

    if(ThorCap==Cap.E):                                             # Update ThorX, ThorY
        ThorX +=1
    elif (ThorCap==Cap.NE):                                                     
        ThorX +=1
        ThorY -=1 
    elif (ThorCap==Cap.N):                                                      
        ThorY -= 1
    elif (ThorCap==Cap.NW):                                                     
        ThorX -=1
        ThorY -=1 
    elif (ThorCap==Cap.W):                                                      
        ThorX -=1
    elif (ThorCap==Cap.SW):                                                     
        ThorX -=1
        ThorY +=1 
    elif (ThorCap==Cap.S):                                                      
        ThorY +=1
    elif (ThorCap==Cap.SE):                                                     
        ThorX +=1
        ThorY +=1

    print(Directions[ThorCap])