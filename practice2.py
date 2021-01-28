from mcpi.minecraft import Minecraft
qq=Minecraft.create()

while True:
    hits=qq.events      .pollProjectileHits()
    if len(hits)>0:
        a=hits[0]
        x,y,z=a.pos.x,a.pos.y,a.pos.z
        qq.player.setTilePos(x,y,z)
        qq.spawnEntity(x,y,z,99)