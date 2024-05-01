import sys, pygame

pygame.init()

size = width, height = 840, 440
dx = 1
dy = 1
x= 163
y = 120
dzx = 1
dzy = 1
zx=30
zy=20
black = (0,0,0)
white = (255,255,255)
blue = (25,200,66)

screen = pygame.display.set_mode(size)

while 1:

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    x += dx
    y += dy

    zx += dzx
    zy += dzy*3

    if x < 0 or x > width:   
        dx = -dx

    if y < 0 or y > height:
        dy = -dy

    if zx < 0 or zx > width:   
        dzx = -dzx

    if zy < 0 or zy > height:
        dzy = -dzy

    screen.fill(black)

    pygame.draw.circle(screen, white, (x,y), 8)
    pygame.draw.circle(screen, blue, (zx,zy), 8)

    pygame.display.flip()