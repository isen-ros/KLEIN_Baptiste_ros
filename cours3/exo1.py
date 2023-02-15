#!/usr/bin/env python
import rospy
from nav_msgs.msg import MapMetaData

def callback(data):
	rospy.loginfo("Received " +str( ordre(2,3, data.origin.position, data.resolution)))


def itoij (i,width):
 return (i/width, i % width)

def ordre(i,j,origin, resolution):
 return((i+origin.x)*resolution,(j+origin.y)*resolution)



def sub():
	rospy.init_node('mapMetadataNode', anonymous=False)
	sub = rospy.Subscriber('map_metadata', MapMetaData, callback)	
	rate = rospy.Rate(10) 
	while not rospy.is_shutdown():
		rate.sleep()
	


if __name__ == '__main__':
    try:
      sub()
    except rospy.ROSInterruptException:
        pass
