import pygame
pygame.init()
screen = pygame.display.set_mode((640,640))
run = True
color= (222,10,150)
screen.fill(color)
for i in range (0,64):
    x = 10*i
    for n in range (0,64):
        y = 10*n
        color=(n+i+20,3.5*n,3.5*i)
        pygame.draw.rect(screen, color, (x,y,10,10), 0)
pygame.display.update()
pygame.display.flip()
while run:
    for event in pygame.event.get():
        #print (event)
        if event.type == pygame.QUIT:
            pygame.display.flip()
            run = False
            #print("quit!")
            break
pygame.display.quit()
pygame.quit()
