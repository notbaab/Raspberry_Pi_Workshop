self.obstacle_list = [[[100,285,30,30],[0,0,0],[100,570,3,0]]]
the_type = 1
l = 0
for i in range(100):
    if i%10 == 0: 
        the_type = -the_type
        l += 10
    if the_type == 1:
        self.obstacle_list.append([[100+i*6,0,6,225-(i-l)*6],[0,0,0],0])
        self.obstacle_list.append([[100+i*6,315-(i-l)*6,6,300+(i-l)*6],[0,0,0],0])
    else:
        self.obstacle_list.append([[100+i*6,0,6,285+(i-l)*6],[0,0,0],0])
        self.obstacle_list.append([[100+i*6,375+(i-l)*6,6,250-(i-l)*6],[0,0,0],0])
self.spawn_point = [75,300]
self.win_point = [width-70,300,20]
self.difficulty = 2
self.hidden = 0
self.name = 'Zig-Zag'