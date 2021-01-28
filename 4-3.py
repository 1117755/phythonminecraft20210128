
        
ans=randrange(0,16)
while True:
    hits=qq.events.pollBlockHits()
    if len(hits)>0:
        h=hits[0]
        block=qq.getBlockWithData(h.pos)
        data=block.data

        if data == ans:
            qq.postToChat("恭喜你找到了")
            qq.setBlock(h.pos,57)
            break
        
        elif data < ans:
            qq.postToChat("找啜了.找大意點的八>_<")
        
        elif data > ans:
            qq.postToChat("輟=呃,找小以點的")
        
        
        
    
        