from main import base, tip, joint
from time import sleep

base.write(0)
joint.write(0)
tip.write(0)
sleep(1)

base.write(180)
joint.write(180)
tip.write(180)