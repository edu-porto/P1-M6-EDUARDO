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

    def forward(self, vx: float, vy:float, vtheta:float, tempo_em_ms: int):
        self.move(Vector3(x=vx, y=vy, z=vtheta), Vector3(), duration=tempo_em_ms)



def deque_line():
    dq = deque()
    dq.append('1.0')
    dq.append('0')
    dq.append('1.0')
    dq.append('2000')

def deque_line2():
    dq = deque()
    dq.append('1.4')
    dq.append('2.7')
    dq.append('0.0')
    dq.append('3500')




def main(args=None):

    rclpy.init(args=args)


    
    robot = TurtleBot()

    first_run = deque_line()
    rclpy.spin(robot)


    robot.forward(0.0,2.3,0.0,2000)

    rclpy.shutdown()



if __name__ == "__main__":
    main()
