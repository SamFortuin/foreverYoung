from RobotArm import RobotArm

robotArm = RobotArm('exercise 4')

def robotMoveRight(forMany):
    for i in range(forMany):robotArm.moveRight()

def robotMoveLeft(forMany2):
    for i in range(forMany2):robotArm.moveLeft()

# Jouw python instructies zet je vanaf hier:
robotArm.grab()
robotMoveRight(2)
robotArm.drop()
robotMoveLeft(2)
robotArm.grab()
robotMoveRight(2)
robotArm.drop()
robotMoveLeft(2)
robotArm.grab()
robotArm.moveRight()
robotArm.drop()
for i in range(2):
    robotArm.moveRight()
    robotArm.grab()
    robotArm.moveLeft()
    robotArm.drop()


# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()