#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int64

def callback(sub_data):
    input_data = sub_data.data
    print(input_data)
    
def listener():

    
    rospy.init_node('node2', anonymous=True)

    rospy.Subscriber("std_id", Int64, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
