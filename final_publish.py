#!/usr/bin/env python3
# license removed for brevity
import rospy
from std_msgs.msg import Int64

def talker():
    rospy.init_node('node1', anonymous=True)
    pub = rospy.Publisher('std_id', Int64, queue_size=10)
    
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        hello_str = 6352500471
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass

