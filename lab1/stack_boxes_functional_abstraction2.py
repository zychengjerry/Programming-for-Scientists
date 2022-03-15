
import robot


robot.init(width=7, boxes = "flat")


# move right twice
def drive_right_twice():
    robot.drive_right()
    robot.drive_right()

# pick up the next box
# assumption: there are no boxes at the same level
# to the left and right     
def pick_up_box():    
    robot.drive_right()
    robot.lift_up()
    robot.gripper_to_open()
    robot.lift_down()
    robot.gripper_to_closed()
    robot.lift_up()

def grasp_next_box():
    robot.gripper_to_open()
    robot.lift_down()
    robot.gripper_to_closed()
    robot.lift_up()

pick_up_box()

drive_right_twice()

# grasp next box
grasp_next_box()

# move right twice
drive_right_twice()

# grasp next box
grasp_next_box()

# move right twice
drive_right_twice()

# finish
robot.gripper_to_open()
robot.lift_down()
robot.gripper_to_folded()
