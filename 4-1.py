from mcpi.minecraft import Minecraft
qq=Minecraft.create()
import random

x,y,z=qq.player.getTilePos()

for i in range(20):
    r=random.randrange(1,5)
    if r == 1:
        qq.setBlocks(x,y,z,x,y,z+4,41)
        z = z+4
    if r == 2:
        qq.setBlocks(x,y,z,x+4,y,z,41)
        z = z-4
    if r == 3:
        qq.setBlocks(x,y,z,x+4,y,z,41)
        x = x+4
    if r == 4:
        qq.setBlocks(x,y,z,x-4,y,z,41)
        x =x-4
            