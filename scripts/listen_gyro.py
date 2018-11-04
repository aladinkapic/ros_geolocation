#!/usr/bin/env python

## Simple talker demo that listens to std_msgs/Strings published
## to the 'chatter' topic

import rospy
from std_msgs.msg import String
from pynmea import nmea

gps = nmea.GPGGA()

def callback(data):
    #rospy.get_caller_id() + 
    recievedData = data.data
    gyro = recievedData.split()

    #if recievedData[0:6] == '$GPGGA':
    #	gps.parse(recievedData)
    #    latitude = "Latitude  : %s." % (float(gps.latitude) / 100)
    #	longitude = "Longitude : %s." % (float(gps.longitude) / 100)
    #	rospy.loginfo('%s', latitude)
    #	rospy.loginfo('%s', longitude)
    #else:
    rospy.loginfo('*--------------------------------------------*')
    alpha = "Alpha : %s." % float(gyro[1].replace(",", ""))
    beta = "Beta : %s." % float(gyro[3].replace(",", ""))
    gama = "Gama : %s." % float(gyro[5].replace(",", ""))
    rospy.loginfo(alpha)
    rospy.loginfo(beta)
    rospy.loginfo(gama)

    rospy.loginfo('*--------------------------------------------*')


def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The	
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber('gyro', String, callback)
    #rospy.Subscriber('chatter1', String, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
