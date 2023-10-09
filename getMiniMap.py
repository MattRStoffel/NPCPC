from PathData import findAngleToTarget
from CharacterControl import movePlayerCharacter
from DataCapture import getRoi

HogwartsRoi =  (110, 1140, 209, 213)

if __name__ == "__main__":
    roi = HogwartsRoi
    # roi = getRoi()
    while(True):
        # get the minimap
        angleToTarget = findAngleToTarget(roi)        
        movePlayerCharacter(angleToTarget)