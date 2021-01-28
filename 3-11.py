from mcpi.minecraft import Minecraft
qq=Minecraft.create()

x,y,z=qq.player.getTilePos()

number=1

for i in range(8):
    for j in range(number):
        qq.spawnEntity(x,y,z,60)
    number=number*2
    WWSqq.postToChat('這次生成了'+str(number))

