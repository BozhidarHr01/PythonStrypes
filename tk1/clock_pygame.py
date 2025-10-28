import pygame
import math
import datetime

pygame.init()

screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()
running = True

angle = 0
start_pos = (300,300)

def draw_line(angle, lenght, color, thickness):
    angle = math.radians(angle - 90)
    x = start_pos[0] + lenght * math.cos(angle)
    y = start_pos[1] + lenght * math.sin(angle)
    pygame.draw.line(screen, color, start_pos, (x, y), thickness)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")
    
    lines_color="grey"
    
    for i in range(12):
        angle = i * 30 
        length = 20 if i % 3 == 0 else 10
        x_start = 300 + 230 * math.cos(math.radians(angle - 90))
        y_start = 300 + 230 * math.sin(math.radians(angle - 90))
        x_end = 300 + (215 - length) * math.cos(math.radians(angle - 90))
        y_end = 300 + (215 - length) * math.sin(math.radians(angle - 90))
        pygame.draw.line(screen, lines_color, (x_start, y_start), (x_end, y_end  ), 5)

    for i in range(60):
        if i % 5 != 0:
            angle = i * 6 
            x_start = 300 + 240 * math.cos(math.radians(angle - 90))
            y_start = 300 + 240 * math.sin(math.radians(angle - 90))
            x_end = 300 + 230 * math.cos(math.radians(angle - 90))
            y_end = 300 + 230 * math.sin(math.radians(angle - 90))
            pygame.draw.line(screen, lines_color, (x_start, y_start), (x_end, y_end), 2)

    now = datetime.datetime.now()

    hours = now.hour % 12 # divide by 12 since analog
    minutes = now.minute
    seconds = now.second

    #hour line
    angle = (hours + minutes / 60) * 30  # 360 / 12 = 30
    draw_line(angle, 150, "darkblue", 5)

    #minute line
    angle = (minutes + seconds / 60) * 6  # 360 / 60 = 6
    draw_line(angle, 175, "orange", 5)

    #second line 
    angle = seconds * 6
    draw_line(angle, 200, "red", 5)

    pygame.draw.circle(screen, "purple", (300,300), 250, 5)
    pygame.draw.circle(screen, "purple", (300,300), 7, 7)


    #digital clock
    font = pygame.font.SysFont(None, 48)
    time_str = now.strftime("%H:%M:%S")
    time_surf = font.render(time_str, True, "purple")
    time_rect = time_surf.get_rect(center=(300, 30))
    screen.blit(time_surf, time_rect)

    pygame.display.flip()

pygame.quit()