#!/usr/bin/env python

import rospy
from geometry_msgs.msg import PoseWithCovarianceStamped

class PoseModifier:
    def __init__(self):
        # Initialize node and subscribers/publishers
        rospy.init_node('pose_modifier', anonymous=True)
        self.sub = rospy.Subscriber('initialPose', PoseWithCovarianceStamped, self.callback, queue_size=1)
        self.pub = rospy.Publisher('modifiedPose', PoseWithCovarianceStamped, queue_size=1)

    def callback(self, data):
        # Add 10 to the x value of the received pose
        modified_pose = PoseWithCovarianceStamped()
        modified_pose.header = data.header
        modified_pose.pose.pose.position.x = data.pose.pose.position.x + 10
        modified_pose.pose.pose.position.y = data.pose.pose.position.y
        modified_pose.pose.pose.position.z = data.pose.pose.position.z
        modified_pose.pose.pose.orientation = data.pose.pose.orientation

        # Publish the modified pose
        self.pub.publish(modified_pose)

if __name__ == '__main__':
    try:
        pose_modifier = PoseModifier()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass

