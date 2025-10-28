#create analog clock with pygame that shows current time
import pygame
import math
import datetime
#draw a line x1,y1,x2,y2
#how to rotate the line
#draw a circle x,y,radius
pygame.init()
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()
running = True
FPS = 60
angle = 0
start_pos = (300,300)
line_len = 200
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    lines_color="grey"
    pygame.draw.line(screen, lines_color, (300,50), (300,100), 5) #up
    pygame.draw.line(screen, lines_color, (300, 500), (300, 545), 5) #down
    pygame.draw.line(screen, lines_color, (50, 300), (100, 300), 5) #left
    pygame.draw.line(screen, lines_color, (500, 300), (545, 300), 5) #right
    pygame.draw.line(screen, lines_color, (150,150), (125,125), 5) #upleft
    pygame.draw.line(screen, lines_color, (450,150), (475,125), 5) #upright
    pygame.draw.line(screen, lines_color, (150,450), (125,475), 5) #downleft
    pygame.draw.line(screen, lines_color, (450,450), (475,475), 5) #downright

    pygame.draw.circle(screen, "purple", (300,300), 250, 5)
    pygame.draw.circle(screen, "red", (300,300), 5, 3)

    timenow_seconds = datetime.datetime.now().time().second * 6

    angle = timenow_seconds
    x = start_pos[0] + math.cos(math.radians(angle)) * line_len
    y = start_pos[1] + math.sin(math.radians(angle)) * line_len
    pygame.draw.line(screen, "blue", start_pos, (x, y), 3)

    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()