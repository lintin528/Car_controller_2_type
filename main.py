import sys
import rclpy
import os
from Supervised.supervised_collect_data import supervised_collect_data_node
from Supervised.supervised_inference import supervised_inference_node
from RL.RLModel_training_node import RLModel_Node
from RL.RLModel_inference import RLModel_inference_Node


def spin_pros(node):
    exe = rclpy.executors.SingleThreadedExecutor()
    exe.add_node(node)
    exe.spin()
    rclpy.shutdown()
    sys.exit(0)

def print_usage():
    print("modes:")
    print(" 1 -- supervised learning data colletion.")
    print(" 2 -- supervised learning inference.")
    print(" 3 -- reinforced learning training.")
    print(" 4 -- reinforced learning inference.")
    print(" 5 -- rule-based control.")
    

def change_working_directory(mode):
    if mode in ["1", "2"]:
        new_directory = "./Supervised"
        os.chdir(new_directory)
    elif mode in ["3", "4"]:
        new_directory = "./RL"
        os.chdir(new_directory)

def main(mode):
    rclpy.init()
    change_working_directory(mode)
    if mode == "1":
        node = supervised_collect_data_node() 
    elif mode == "2":
        node = supervised_inference_node()
    elif mode == "3":
        node = RLModel_Node()
    elif mode == "4":
        node = RLModel_inference_Node()
    else:
        print("please type the mode nums listed upside.")
    spin_pros(node)  

if __name__ == '__main__':
    print_usage()
    mode = input("Enter mode: ")
    main(mode)