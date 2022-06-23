import libhousy
#You can define helper functions here, make sure to but them *above* the main function
def main(robot: libhousy.robot):
    #Here is where your recurring code will go
    if robot.sense_hat.get_yaw() > -90:
        robot.lDrive.Set(-0.5)
        robot.rDrive.Set(0.5)
        # stuff and things
    elif robot.sense_hat.get_yaw() < -90: #overshot
        robot.rDrive.Set(-0.5)
        robot.lDrive.Set(0.5)

    else:   
        robot.rDrive.Set(0)
        robot.lDrive.Set(0)
    