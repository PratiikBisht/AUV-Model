import rospy 
from std_msgs.msg import Float32MultiArray
from geometry_msgs.msg import Twist

def position_callback(msg):
    cx, cy= msg.data 
    cmd= Twist()

    # logic behond control to move toward object
    if cx<320 :
        cmd.linear.x=0.1
        cmd.linear.x=0.1
    elif cx>320:
        cmd.linear.x=0.1
        cmd.linear.z=-0.1
    else:
        cmd.linear.x=0.2
        cmd.linear.z=0.0

    cmd_pub.publish(cmd)

rospy.init_node('Vehicle_control_node')
poisition_sub= rospy.Subscriber('/object_position', Float32MultiArray, position_callback)
cmd_pub= rospy.Publisher('/cmd_vel', Twist, queue_size=10)
rospy.spin()