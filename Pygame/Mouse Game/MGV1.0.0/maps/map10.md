self.obstacle_list = [[[0,0,width,50],[0,0,0],0],
[[0,0,50,height],[0,0,0],0],
[[width-50,0,50,height],[0,0,0],0],
[[0,height-50,width,50],[0,0,0],0],
[[200,50,50,400],[0,0,0],0],
[[400,150,50,400],[0,0,0],0],
[[600,50,50,450],[0,0,0],0],
[[700,100,5,450],[0,0,0],0]]
for i in range (11):
    for x in range(5):
        if i%2 == 0:
            self.obstacle_list.append([[75+i*50,125+x*100,0,0],[0,0,0],[15,25,0.5,0]])
        else:
            self.obstacle_list.append([[75+i*50,75+x*100,0,0],[0,0,0],[15,25,0.5,0]])
for i in range(8):
    if i%2 == 0:
        self.obstacle_list.append([[750,100+i*50,10,50],[0,0,0],[100,110,-1,110]])
    else:
        self.obstacle_list.append([[640,100+i*50,10,50],[0,0,0],[100,110,1,0]])
self.spawn_point = [75,75]
self.win_point = [width-70,530,20]
self.difficulty = 7
self.hidden = 0
self.name = 'Checkers'