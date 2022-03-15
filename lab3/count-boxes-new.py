
import robot

#robot.init(height = 5, boxes = [["blue", "green", "yellow", "red"]])
#robot.init(height = 6, boxes = [["black", "yellow", "red", "white", "blue"]])
robot.init(height = 7, boxes = "random")

def count_boxes():
    '''Return number of boxes in the stack in front of robot'''
    if robot.sense_color() == '':
        return 0
    else:
        robot.lift_up()
        num = count_boxes()
        robot.lift_down()
        return 1+num
    
    