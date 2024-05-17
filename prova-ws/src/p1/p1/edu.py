# Criar uma cli que recebe comandos e executa nessa tal de deque    
import rclpy
from rclpy.node import Node
from InquirerPy import inquirer
from InquirerPy.utils import patched_print as print
from InquirerPy.validator import EmptyInputValidator
from collections import deque
from rclpy.node import Node
import time
from geometry_msgs.msg import Twist, Vector3

class TurtleBot(Node):
    def __init__(self):
        super().__init__('turtlebot')
        self.publisher_ = self.create_publisher(Twist, 'cmd_vel', 10)

    def move(self, linear: Vector3, angular: Vector3, duration: float):
        msg = Twist()
        msg.linear = linear
        msg.angular = angular
        self.publisher_.publish(msg)
        time.sleep(duration)
        self.stop()

    def stop(self):
        stop_msg = Twist()
        self.publisher_.publish(stop_msg)

    def forward(self, speed: float, duration: float):
        self.move(Vector3(x=speed, y=0.0, z=0.0), Vector3(), duration=2000)



def deque_line():
    dq = deque()
    dq.append('1.0')
    dq.append('0')
    dq.append('1.0')
    dq.append('2.2')




def main(args=None):

    rclpy.init(args=args)


    
    robot = TurtleBot()

    first_run = deque_line()

    # robot.forward(2.3, 3.0)
    print(first_run)

if __name__ == "__main__":
    main()
