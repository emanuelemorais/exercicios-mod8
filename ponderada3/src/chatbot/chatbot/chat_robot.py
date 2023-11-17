import rclpy
from nav2_simple_commander.robot_navigator import BasicNavigator
from geometry_msgs.msg import PoseStamped
import tf_transformations
from tf_transformations  import quaternion_from_euler
import re

class ControlTurltebot():
    def __init__(self):
        rclpy.init()
        self.nav = BasicNavigator()
        self.q_x, self.q_y, self.q_z, self.q_w = quaternion_from_euler(0.0, 0.0, 0.0)
        self.initial_pose = self.create_initial_pose()
        self.nav.setInitialPose(self.initial_pose)
        self.nav.waitUntilNav2Active()
        self.regex = r'.*?(ponto|prateleira|estante|local|peça|lugar|posi[çc][aã]o|[áa]rea|arm[áa]rio)?\s?([sS]ecretaria|[lL]aborat[óo]rio|[bB]iblioteca)'


        self.intencoes = {
            "secretaria": self.create_pose_stamped(self.nav, 1.6, -1.4, 0.0),
            "laboratorio": self.create_pose_stamped(self.nav, 1.6, 2.30, 0.0),
            "biblioteca": self.create_pose_stamped(self.nav, 3.8, 0.5, 0.0)
        }

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

    def coordenadas_destino(self, local):
        if local in self.intencoes:
            return self.intencoes[local]

    def create_waypoints(self):
        while True:
            local = input("Para onde deseja ir? (Digite 'sair' para encerrar) ")
            match = re.search(self.regex, local, re.IGNORECASE | re.UNICODE)
            if local == 'sair':
                self.nav.followWaypoints([self.create_pose_stamped(self.nav, 0.0, 0.0, 0.0)])
                print("Vontando para a posição inicial...")
                rclpy.shutdown()
                print("Até a próxima!")
                break
            if match:
                numero_encontrado = match.group(2)  
                self.nav.followWaypoints([self.coordenadas_destino(numero_encontrado)])
                while not self.nav.isTaskComplete():
                    print("Indo...")

            else:
                print("Local indicado não mapeado.")

def main():
    try:
        t = ControlTurltebot()
        t.create_waypoints()
    except Exception as e:
        print("Erro na inicialização do robô: ", e)

if __name__ == '__main__':
    main()