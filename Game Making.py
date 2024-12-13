import pygame
pygame.init()
#screen
screenWidth=800
screenHeight=600
screen=pygame.display.set_mode((screenWidth,screenHeight))
#variables
player=pygame.Rect((300,250,50,50))
obstacle=pygame.Rect((0,0,800,20))
obstacle2=pygame.Rect((800,800,20,800))
obstacle3=pygame.Rect((800,800,-800,20))
obstacle4=pygame.Rect((0,0,20,-800))
square=pygame.Rect((400,400,30,30))

work=True
while work:
#updates the software

 screen.fill((0,0,0))

#obstacles and players

 a=pygame.draw.rect(screen,(125,133,56),player)
 b=pygame.draw.rect(screen,(255,0,0),obstacle)
 c=pygame.draw.rect(screen,(255,0,0),obstacle2)
 d=pygame.draw.rect(screen,(255,0,0),obstacle3)
 e=pygame.draw.rect(screen,(255,0,0),obstacle4)
 f=pygame.draw.rect(screen,(0,0,255),square)


#movements
 key = pygame.key.get_pressed()
 if key[pygame.K_a]==True:
  player.move_ip(-1,0)

 elif key[pygame.K_d]==True:
  player.move_ip(1,0)

 elif key[pygame.K_s]==True:
  player.move_ip(0,1)

 elif key[pygame.K_w]==True:
  player.move_ip(0,-1)
#quites the game
 for event in pygame.event.get():
  if event.type==pygame.QUIT:
   work=False
#updates after every loop
 pygame.display.update()
pygame.quit()
