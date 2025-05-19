import numpy as np
import time

link1_length = 10
link2_length = 10

theta1 = 0
theta2 = 0
theta3 = 0

end_effector_pose = np.array([10, 10, 10])

def inverse_kinematics(end_effector_pose):
    theta1 = np.arctan2(end_effector_pose[1], end_effector_pose[0])
    theta2 = np.arccos((end_effector_pose[0]**2 + end_effector_pose[1]**2 - link1_length**2 - link2_length**2) / (2 * link1_length * link2_length))
    theta3 = np.arctan2(end_effector_pose[2], np.sqrt(end_effector_pose[0]**2 + end_effector_pose[1]**2))
    return theta1, theta2, theta3

def move_arm(theta1, theta2, theta3):
    print(f"Moving arm to theta1={theta1}, theta2={theta2}, theta3={theta3}")

def main():
    global theta1, theta2, theta3, end_effector_pose
    theta1, theta2, theta3 = inverse_kinematics(end_effector_pose)
    move_arm(theta1, theta2, theta3)
    end_effector_pose = np.array([15, 15, 15])
    theta1, theta2, theta3 = inverse_kinematics(end_effector_pose)
    move_arm(theta1, theta2, theta3)

if __name__ == "__main__":
    main()
