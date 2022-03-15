
import robot

robot.init(boxes = [["black"], [], ["red"], [], ["red"]])
#robot.init(boxes = [["red"], [], ["black"], [], ["red"]])
#robot.init(boxes = [["red"], [], ["red"], [], ["black"]])

def drive_left_twice():
    robot.drive_left()
    robot.drive_left()

def drive_right_twice():
    robot.drive_right()
    robot.drive_right()

def pickup_box():
    '''pick up box in front of gripper from shelf;
    assumes lift is down and gripper is folded'''
    robot.lift_up()
    robot.gripper_to_open()
    robot.lift_down()
    robot.gripper_to_closed()
    robot.lift_up()

def stack_box():
    '''stack box in gripper on top of another box,
    returning gripper to folded position and lift to down'''
    robot.gripper_to_folded()
    robot.lift_down()

def stack_red_boxes():
    '''this function stacks the 2 red boxes together'''
    if robot.sense_color() == 'red':
        # 1st box is red
        drive_right_twice()
        if robot.sense_color() == 'red':
            # red, red, black
            robot.drive_left()
            pickup_box()
            drive_right_twice()
            stack_box()
        else:
            # red, black, red
            robot.drive_left()
            pickup_box()
            drive_right_twice()
            drive_right_twice()
            stack_box()
    else:
        # black, red, red
        drive_right_twice()
        robot.drive_right()
        pickup_box()
        drive_right_twice()
        stack_box()
        