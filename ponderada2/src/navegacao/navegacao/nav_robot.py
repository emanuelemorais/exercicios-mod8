import rclpy
from nav2_simple_commander.robot_navigator import BasicNavigator
from geometry_msgs.msg import PoseStamped
from tf_transformations  import quaternion_from_euler

class ControlTurltebot():
    def __init__(self):
        rclpy.init()
        self.nav = BasicNavigator()
        self.q_x, self.q_y, self.q_z, self.q_w = quaternion_from_euler(0.0, 0.0, 0.0)
        self.initial_pose = self.create_initial_pose()
        self.nav.setInitialPose(self.initial_pose)
        self.nav.waitUntilNav2Active()

    def create_initial_pose(self):
        initial_pose = PoseStamped()
        initial_pose.header.frame_id = 'map'
        initial_pose.header.stamp = self.nav.get_clock().now().to_msg()
        initial_pose.pose.position.x = 0.0
        initial_pose.pose.position.y = 0.0
        initial_pose.pose.position.z = 0.0
        initial_pose.pose.orientation.x = self.q_x
        initial_pose.pose.orientation.y = self.q_y
        initial_pose.pose.orientation.z = self.q_z
        initial_pose.pose.orientation.w = self.q_w
        return initial_pose

    def create_pose_stamped(self, navigator, pos_x, pos_y, rot_z):
        self.q_x, self.q_y, self.q_z, self.q_w = quaternion_from_euler(0.0, 0.0, rot_z)
        pose = PoseStamped()
        pose.header.frame_id = 'map'
        pose.header.stamp = navigator.get_clock().now().to_msg()
        pose.pose.position.x = pos_x
        pose.pose.position.y = pos_y
        pose.pose.position.z = 0.0
        pose.pose.orientation.x = self.q_x
        pose.pose.orientation.y = self.q_y
        pose.pose.orientation.z = self.q_z
        pose.pose.orientation.w = self.q_w
        return pose        


    def coordenadas_destino(self):
        while True:
            destinox = input("Insira o lugar de destino em x: ")
            destinoy = input("Insira o lugar de destino em y: ")
            destinoz = input("Insira o lugar de destino em z: ")
            waypoints = [self.create_pose_stamped(self.nav, float(destinox), float(destinoy), float(destinoz))]
            self.nav.followWaypoints(waypoints)
            while not self.nav.isTaskComplete():
                print(self.nav.getFeedback())
                
def main(args=None):
    try:
        t = ControlTurltebot()
        t.coordenadas_destino()
    except Exception as e:
        print("Erro na inicialização do robô: ", e)

if __name__ == '__main__':
    main()