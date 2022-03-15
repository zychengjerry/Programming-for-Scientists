# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 16:32:37 2022

@author: ZeyuanCheng
"""
# Lab3 test2

import robot

robot.init(width = 7, boxes = "flat")

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

def make_tower(n):
    pick_up_box()
    drive_right_twice()
    
    for i in range(n - 2):
        if i < n - 2: 
            # grasp next box
            grasp_next_box()
            # move right twice
            drive_right_twice()
            
    # finish
    robot.gripper_to_open()
    robot.lift_down()
    robot.gripper_to_folded()


make_tower(4)