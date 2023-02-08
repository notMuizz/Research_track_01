from __future__ import print_function

import time
from sr.robot import *

"""
Assignment 1 python script

Objective: Main code is after the definition of the functions. The code should make the robot:
	- 1) find and grab the silver marker (token)
	- 2) move the marker close to golden marker (token) and release it
	- 3) start again from 1

Theory: The method see() of the class Robot returns an object whose attribute info.marker_type may be MARKER_TOKEN_GOLD or MARKER_TOKEN_SILVER, depending of the type of marker (golden or silver). 
Modify the code of the exercise2 to make the robot:

1- retrieve the distance and the angle of the silver marker  which was previously not grabbed. If no silver marker is detected, the robot should rotate in order to find a marker.
2- drive the robot towards the marker and grab it
3- retrieve the distance and the angle of the closest golden marker which was previously not grabbed. If no golden marker is detected, the robot should rotate in order to find a marker.
4- find a golden marker, carry silver marker close to golden marker and release(use the method release() of the class Robot in order to release the marker)
5- start again from 1

Run:	When done, copy this python file in folder of simulator and run with:
	$ python run.py assignment.py

"""


a_th = 2.0
""" float: Threshold for the control of the linear distance"""

d_th = 0.4
""" float: Threshold for the control of the orientation"""

silver = True
""" boolean: variable for letting the robot know if it has to look for a silver or for a golden marker"""

hold = False
""" boolean: variable to check if robot is holding something or not """

R = Robot()
""" instance of the class Robot"""

silver_token_list = []
""" list: to store silver boxes that have been used"""

golden_token_list = []
""" list: to store golden boxes that have been used"""

def drive(speed, seconds):
    """
    Function for setting a linear velocity
    
    Args: speed (int): the speed of the wheels
	  seconds (int): the time interval
    """
    R.motors[0].m0.power = speed
    R.motors[0].m1.power = speed
    time.sleep(seconds)
    R.motors[0].m0.power = 0
    R.motors[0].m1.power = 0

def turn(speed, seconds):
    """
    Function for setting an angular velocity
    
    Args: speed (int): the speed of the wheels
	  seconds (int): the time interval
    """
    R.motors[0].m0.power = speed
    R.motors[0].m1.power = -speed
    time.sleep(seconds)
    R.motors[0].m0.power = 0
    R.motors[0].m1.power = 0

def find_silver_token():
    """
    Function to find the closest silver token which is not used before

    Returns:
	dist (float): distance of the closest silver token (-1 if no silver token is detected)
	rot_y (float): angle between the robot and the silver token (-1 if no silver token is detected)
	box_id (integer): token ID or marker Id which is going to be picked
    """
    dist=100
    for token in R.see():
        if token.dist < dist and token.info.marker_type is MARKER_TOKEN_SILVER and token.info.code not in silver_token_list:
            dist=token.dist
	    rot_y=token.rot_y
	    box_id = token.info.code
    if dist==100:
	return -1, -1, -1
    else:
   	return dist, rot_y, box_id

def find_golden_token():
    """
    Function to find the closest golden token which is not used before

    Returns:
	dist (float): distance of the closest golden token (-1 if no golden token is detected)
	rot_y (float): angle between the robot and the golden token (-1 if no golden token is detected)
	box_id (integer): token ID or marker Id where grabbed box is going to be released
    """
    dist=100
    for token in R.see():
        if token.dist < dist and token.info.marker_type is MARKER_TOKEN_GOLD and token.info.code not in golden_token_list :
            dist=token.dist
	    rot_y=token.rot_y
	    box_id = token.info.code
    if dist==100:
	return -1, -1, -1
    else:
   	return dist, rot_y, box_id

while 1:
    markers = R.see()
    print(len(markers))
    if silver == True: # if silver is True, than we look for a silver token, otherwise for a golden one
	dist, rot_y, box_id = find_silver_token()
    else:
	dist, rot_y, box_id = find_golden_token()
    if hold:
        dist = dist-0.5 # dropping box a little before so that it doesn't collide with other box
        
    print(silver_token_list)
    print(golden_token_list)
    if dist==-1 or box_id==-1: # if no token is detected, we make the robot turn 
	print("Not avaible any token!!")
	turn(+10, 1)
	drive(10,1)
    elif dist <d_th: # if we are close to the token, we try grab it or release it
        print("yeah Got  it!")
        if hold: # token is grabbed by robot, then release token
            drive(10,2)
            golden_token_list.append(box_id) # token ID is saved in array of boxes where silver box is released
            R.release()
            drive(-20, 2)
            silver = not silver # we modify the value of the variable silver, so that in the next step we will look for the other type of token
            hold = False # modify the hold to not holding token
        elif R.grab(): # if we grab the token, then  
            silver_token_list.append(box_id)
            print("Gotcha!")
	    hold = True # modify the not hold to holding token
	    silver = not silver # we modify the value of the variable silver, so that in the next step we will look for the other type of token
	else:
            print("token not in reach")    
    elif -a_th<= rot_y <= a_th: # if the robot is well aligned with the token, we go forward
	print("Ah, that'll do.")
        drive(10, 1)
    elif rot_y < -a_th: # if the robot is not well aligned with the token, we move it on the left or on the right
        print("go to the Left a bit...")
        turn(-2, 0.5)
    elif rot_y > a_th:
        print("go to the Right a bit...")
        turn(+2, 0.5)
	
