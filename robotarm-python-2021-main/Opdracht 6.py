from RobotArm import RobotArm

def robotMoveRight(forMany):
    for i in range(forMany):robotArm.moveRight()

def robotMoveLeft(forMany2):
    for i in range(forMany2):robotArm.moveLeft()

robotArm = RobotArm('exercise 6')
robotMoveRight(7)
robotArm.grab()
robotArm.moveRight()
robotArm.drop()
robotArm.moveLeft()
for i in range(7):
    if i == 0:
        robotArm.moveLeft()
    else:
        robotMoveLeft(2)
    robotArm.grab()
    robotArm.moveRight()
    robotArm.drop()
# Jouw python instructies zet je vanaf hier:


# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()