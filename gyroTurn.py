# inclue code to help us talk to the robot
import libhousy

def main(robot: libhousy.robot):
    # Here is where your recurring code will go
    if robot.sense_hat.get_yaw() > -90:
        robot.lDrive.Set(-0.4)
        robot.rDrive.Set(0.4)
    else:
        robot.lDrive.Set(0)
        robot.rDrive.Set(0)
        return libhousy.DONE
    # After everything is done, we tell the main program to stop us