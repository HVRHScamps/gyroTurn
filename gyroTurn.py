import libhousy
#You can define helper functions here, make sure to but them *above* the main function
p=0.01
def main(robot: libhousy.robot):
    #Here is where your recurring code will go
    if robot.sense_hat.get_yaw() > -90:
        error=robot.sense_hat.get_yaw()+90
        speed= error *p
        robot.lDrive.Set(-speed)
        robot.rDrive.Set(speed)
        # stuff and things
    elif robot.sense_hat.get_yaw() < -90: #overshot
        error=-90-robot.sense_hat.get_yaw()
        speed= error *p
        robot.rDrive.Set(-speed)
        robot.lDrive.Set(speed)

    else:   
        robot.rDrive.Set(0)
        robot.lDrive.Set(0)
    