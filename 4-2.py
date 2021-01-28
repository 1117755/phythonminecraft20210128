from mcpi.minecraft import Minecraft
qq=Minecraft.create()
import random

x,y,z=qq.player.getTilePos()

for i in range(20):
    r=random.randrange(1,7)
    if r == 1:
        qq.setBlocks(x,y,z,x,y,z+4,41)
        z = z+4
    if r == 2:
        qq.setBlocks(x,y,z,x,y,z-4,41)
        z = z-4
    if r == 3:
        qq.setBlocks(x,y,z,x+4,y,z,41)
        x = x+4
    if r == 4:
        qq.setBlocks(x,y,z,x-4,y,z,41)
        x =x-4
    if r == 5:
        qq.setBlocks(x,y,z,x,y+4,z,57)
        y=y+4
    if r == 6:
        qq.setBlocks(x,y,z,x,y-4,z,88)
        y=y-4