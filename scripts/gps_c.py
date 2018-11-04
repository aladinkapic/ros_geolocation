#!/usr/bin/env python

import roslib
roslib.load_manifest('meh')
import rospy
from std_msgs.msg import String
import serial
from pynmea import nmea
import sys
import urllib
import urllib2

# Give ourselves the ability to run a dynamic reconfigure server.
from dynamic_reconfigure.server import Server as DynamicReconfigureServer

ser = serial.Serial()
ser.port = "/dev/ttyACM0"
ser.baudrate = 9600
ser.timeout = 1
ser.open()
gps = nmea.GPGGA()

def talker():
	pub = rospy.Publisher('gps', String, queue_size=10)
	rospy.init_node('talker', anonymous=True)
	rate = rospy.Rate(5) # 10hz
	while not rospy.is_shutdown():
        	data = ser.readline()
        	if data[0:6] == '$GPGGA':
			##method for parsing the sentence
			gps.parse(data)
            		latitude = gps.latitude
            		latitude_direction = gps.lat_direction
	
            		longitude = gps.longitude
            		longitude_direction = gps.lon_direction


            		antena_altitude = gps.antenna_altitude

            		##sent to reciever

            		#Latitude
            		lat = "Latitude : %s."  % latitude;
  		        rospy.loginfo(str(lat))
   		        pub.publish(str(lat))

            		#Longitude
            		lon = "Longitude : %s." %longitude;
            		rospy.loginfo(str(lon))
            		pub.publish(str(lon))

            		#Longitude
            		#lon = "Longitude : %s." %longitude;
            		rospy.loginfo(data)
            		pub.publish(data)
			
			#make a http

			#deg = int(longitude / 100);
			#mm = longitude % 100;
			#longitude = deg + (mm / 60); 
			url = 'https://mehatronics-livetolearn.c9users.io/index.php'
			values = {'lat' : latitude, 'long' : longitude}
			data = urllib.urlencode(values)
			req = urllib2.Request(url, data)
			response  = urllib2.urlopen(req)
				
	
        #hello_str = "hello world %s, it is your dady" % rospy.get_time()
        #rospy.loginfo(hello_str)
        #pub.publish(hello_str)
        	rate.sleep()

if __name__ == '__main__':
	try:
	        talker()
	except rospy.ROSInterruptException:
        	pass
