self.obstacle_list = []
for i in range(3,15):
    self.obstacle_list.append([[700,300,20],[0,0,0],[[400,300],300,1,0+i*5]])
    self.obstacle_list.append([[700,300,20],[0,0,0],[[400,300],300,1,90+i*5]])
    self.obstacle_list.append([[700,300,20],[0,0,0],[[400,300],300,1,180+i*5]])
    self.obstacle_list.append([[700,300,20],[0,0,0],[[400,300],300,1,270+i*5]])
for i in range(0,20):
    self.obstacle_list.append([[700,300,20],[0,0,0],[[400,300],300-i*30,1,45]])
    self.obstacle_list.append([[700,300,20],[0,0,0],[[400,300],300-i*30,1,135]])
#self.obstacle_list.append([[400,300,0],[0,0,0],[200,300,1,0]])
self.spawn_point = [60,height/2]
self.win_point = [width-60,height/2,20]
self.difficulty = 3
self.hidden = 0
self.name = 'Wheel-go-round'