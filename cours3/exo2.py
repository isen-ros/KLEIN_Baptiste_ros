#!/usr/bin/env python
import rospy
from nav_msgs.msg import OccupancyGrid

def callback(data):
	x=-10
	y=-10
	for x in range (-10,10):
		for y in range (-10,10):
			a,b=erdro(x,y,data.info.origin.position,data.info.resolution)
			rospy.loginfo("Received "+str(ijtoi(a,b,data.info.width)))


def itoij (i,width):
 return (i/width, i % width)

def ijtoi(i,j,width):
 return(i*width+j)

def ordre(i,j,origin, resolution):
 return((i+origin.x)*resolution,(j+origin.y)*resolution)

def erdro(x,y,origin,resolution):
 return((x//resolution)-origin.x,(y//resolution)-origin.y)


def sub():
	rospy.init_node('mapMetadataNode', anonymous=False)
	sub = rospy.Subscriber('map', OccupancyGrid, callback)	
	rate = rospy.Rate(10) 
	while not rospy.is_shutdown():
		rate.sleep()
	



if __name__ == '__main__':
    try:
      sub()
    except rospy.ROSInterruptException:
        pass


  
