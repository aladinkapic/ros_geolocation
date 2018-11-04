#!/usr/bin/env python

# Import required Python code
import roslib
roslib.load_manifest('meh')
import rospy
import sys

# Give ourselves the ability to run a dynamic reconfigure server.
from dynamic_reconfigure.server import Server as DynamicReconfigureServer

# Import custom message data and dynamic reconfigure variables.
from meh.msg import meh_data
from meh.cfg import meh_paramsConfig as ConfigType

# Node example class.
class NodeExample():
    # Must have __init__(self) function for a class, similar to a C++ class constructor.
    def __init__(self):
        # Get the ~private namespace parameters from command line or launch file.
        init_message = rospy.get_param('~message', 'hello')
        rate = float(rospy.get_param('~rate', '1.0'))
        topic = rospy.get_param('~topic', 'chatter')
        rospy.loginfo('rate = %d', rate)
        rospy.loginfo('topic = %s', topic)
        # Create a dynamic reconfigure server.
        self.server = DynamicReconfigureServer(ConfigType, self.reconfigure)
        # Create a publisher for our custom message.
        pub = rospy.Publisher(topic, node_example_data)
        # Set the message to publish as our custom message.
        msg = node_example_data()
        # Initialize message variables.
        msg.a = 1
        msg.b = 2
        msg.message = init_message
        # Main while loop.
        while not rospy.is_shutdown():
            # Fill in custom message variables with values from dynamic reconfigure server.
            msg.message = self.message
            msg.a = self.a
            msg.b = self.b
            # Publish our custom message.
            pub.publish(msg)
            # Sleep for a while before publishing new messages. Division is so rate != period.
            rospy.sleep()

    # Create a callback function for the dynamic reconfigure server.
    def reconfigure(self, config, level):
    # Fill in local variables with values received from dynamic reconfigure clients (typically the GUI).
        self.message = config["message"]
        self.a = config["a"]
        self.b = config["b"]
   # Return the new variables.
        return config
# Main function.
if __name__ == '__main__':
    # Initialize the node and name it.
    rospy.init_node('pytalker')
    # Go to class functions that do all the heavy lifting. Do error checking.
    try:
        ne = NodeExample()
    except rospy.ROSInterruptException: pass
