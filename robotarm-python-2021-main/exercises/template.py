import sys
sys.path.append('robotarm-python-2021-main')
from RobotArm import RobotArm

robotArm = RobotArm('exercise ')

# Jouw python instructies zet je vanaf hier:
robotArm.moveRight()
robotArm.grab()
robotArm.moveLeft()
robotArm.drop()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()