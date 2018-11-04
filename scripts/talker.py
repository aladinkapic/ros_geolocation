#!/usr/bin/env python

## Simple talker demo that published std_msgs/Strings messages
## to the 'chatter' topic

import rospy
from std_msgs.msg import String
import urllib
import urllib2


def talker():
    pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        hello_str = "hello world %s" % rospy.get_time()
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()
	url = 'http://192.168.0.11/mehatronika/index.php'
	values = {'lat' : 123, 'long' : 345}
	data = urllib.urlencode(values)
	req = urllib2.Request(url, data)
	response  = urllib2.urlopen(req)

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
