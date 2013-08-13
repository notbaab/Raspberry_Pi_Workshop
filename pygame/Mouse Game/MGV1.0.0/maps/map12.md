self.obstacle_list = [[[400,300,100],[0,0,0],1]]
for i in range(30):
    self.obstacle_list.append([[700,300,20],[0,0,0],[[400,300],300,1,0+i*5]])
    self.obstacle_list.append([[700,300,20],[0,0,0],[[400,300],225,1,0+i*5]])
    self.obstacle_list.append([[700,300,20],[0,0,0],[[400,300],300,1,180+i*5]])
    self.obstacle_list.append([[700,300,20],[0,0,0],[[400,300],225,1,180+i*5]])
    self.obstacle_list.append([[700,300,20],[0,0,0],[[400,300],150,1,0+i*5]])
    self.obstacle_list.append([[700,300,20],[0,0,0],[[400,300],150,1,180+i*5]])
for i in range(10):
    self.obstacle_list.append([[700,300,20],[0,0,0],[[400,300],150+i*15,1,0]])
    self.obstacle_list.append([[700,300,20],[0,0,0],[[400,300],150+i*15,1,145]])
    self.obstacle_list.append([[700,300,20],[0,0,0],[[400,300],150+i*15,1,180]])
    self.obstacle_list.append([[700,300,20],[0,0,0],[[400,300],150+i*15,1,325]])
self.spawn_point = [60,300]
self.win_point = [width-60,300,20]
self.difficulty = 6
self.hidden = 0
self.name = 'Chunker'