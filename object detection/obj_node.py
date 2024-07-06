#!/usr/bin/env python
import rospy 
from sensor_msgs.msg import image
from std_msgs.msg import Float32MultiArray
from cv_bridge import CvBridge
import cv2


# detect th eimage and call's function callback
def image_callback(msg):
    bridge= CvBridge()
    cv_image= bridge.imgmsg_to_cvcv2(msg,"bgr8")


#logic of detection
#hsv image from bgr 
hsv_image= cv2.cvtColor(cv_image, cv2.COLOR_BGR2HSV)
lower_bound=(300,100,100)
higher_bound=(90,255,255)

mask= cv2.inRange(hsv_image, lower_bound, higher_bound)
moments= cv2.moments(mask)

#cehecking the mask value 
if moments["m00"]!=0:
    cx= int(moments["m10"]/moments["m00"])
    cy= int(moments["m01"]/moments["m00"])
    rospy.loginfo(f"Object position:({cx,cy})")
    #incorporating the data of cx and cy
    position_pub.publish(Float32MultiArray(data=[cx,cy]))

rospy.init_node("Object detection node ")
image_sub= rospy.Subscriber('/camera/image_raw, Image, image_callback')
position_pub= rospy.Publisher('/object_position', Float32MultiArray, queue_size=10)
rospy.spin()