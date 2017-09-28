from robot import Robot
from reward import Reward
import random

def check_reward(robot, rewards):
    ok = False

    for reward in rewards:
        if reward.x == robot.x and reward.y == robot.y:
            print('The robot has found the reward %s' % reward.name)
            ok = True

    return ok

robot = Robot(random.randint(0, 10), random.randint(0, 10))
reward1 = Reward(random.randint(0, 10), random.randint(0, 10), 'Reward 1')
reward2 = Reward(random.randint(0, 10), random.randint(0, 10), 'Reward 2')
reward3 = Reward(random.randint(0, 10), random.randint(0, 10), 'Reward 3')

rewards = [reward1, reward2, reward3]

print(robot)
print(reward1)
print(reward2)
print(reward3)

for i in range(10):
    action = input('Type up, down, left or right to perform an action: ')

    if action == 'up':
        robot.move_up()
    elif action == 'down':
        robot.move_down()
    elif action == 'left':
        robot.move_left()
    elif action == 'right':
        robot.move_right()
    else:
        print('Invalid action')
        continue

    check_reward(robot, rewards)
