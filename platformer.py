import pygame
import random
pygame.init()

screenw = 1000
screenh = 500
win = pygame.display.set_mode((screenw, screenh))
pygame.display.set_caption("Rip-off tRex gOOGle gaMe")
gameIcon = pygame.image.load('PTSD.png')
pygame.display.set_icon(gameIcon)

rangemin = 30
rangemax = 70

speed = 10
between = 0
score = 0

#skins
skin = 5
one = pygame.image.load('SKIN_1.png')
two = pygame.image.load('SKIN_2.png')
three = pygame.image.load('SKIN_3.png')
four = pygame.image.load('SKIN_4.png')
five = pygame.image.load('SKIN_5.png')
wight = pygame.image.load('WHITE.png')

clock = pygame.time.Clock()

#colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 163, 48)
blue = (0, 0, 255)
grey = (100, 100, 100)
a = 50
color = (random.randint(50,200), random.randint(50,200), random.randint(50,200), a)

class smolboi():
    def __init__ (self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.jump = False
        self.jumpcount = 10
    def draw (self, win):
        win.blit(skins, [self.x, self.y])
        #pygame.draw.rect (win, black, (self.x, self.y, self.width, self.height))
        

class blo():
    def __init__(self, x, y, width, height):
        self.x = screenw + 100
        self.y = 400
        self.width = random.randint(25,75)
        self.height = random.randint(50,100)
        self.counted = False
        #self.r = random.randint(1,254)
        #self.g = random.randint(1,254)
        #self.b = random.randint(1,254)
        #self.color = (self.r, self.g, self.b)
    def draw (self, win):
        pygame.draw.rect (win, white, (self.x, self.y, self.width, self.height))

class ammo():
    def __init__(self,x,y,radius,color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.vel = 8
        
    def draw(self,win):
       pygame.draw.circle(win, self.color, (self.x,self.y), self.radius)

#text
s_smallText = pygame.font.Font('freesansbold.ttf',20)
smallText = pygame.font.Font('freesansbold.ttf',30)
mediumText = pygame.font.Font('freesansbold.ttf',50)
largeText = pygame.font.Font('freesansbold.ttf',70)

def text_objects(text, color, size):
    if size == "s_small":
        textSurface = s_smallText.render(text, True, color)
    elif size == "small":
        textSurface = smallText.render(text, True, color)
    elif size == "medium":
        textSurface = mediumText.render(text, True, color)
    elif size == "large":
        textSurface = largeText.render(text, True, color)
    return textSurface, textSurface.get_rect()

def message_display(text, color, x=0, y=0, size="small"):
    TextSurf, TextRect = text_objects(text, color, size)
    #TextRect.x = 20
    #TextRect.y = 20
    TextRect.center = (screenw/2)+x, (screenh/2)+y
    win.blit(TextSurf, TextRect)

def message_bisplay(text, color, size="small"):
    TextSurf, TextRect = text_objects(text, color, size)
    TextRect.x = 20
    TextRect.y = 20
    win.blit(TextSurf, TextRect)

def drawUpdate ():
    win.fill (color)
    boi.draw(win)
    for block in blocks:
        block.draw(win)
    for bullet in bullets:
        bullet.draw(win)
    #output = "score: " + str(score)
    message_bisplay("score: " + str(score), white, size="small")
    pygame.draw.rect (win, white, (0, screenh - 50, screenw, 50))
    pygame.display.update()

#intro
beg=True
run=False

while beg:
    clock.tick(5)
    win.fill(grey)
    win.blit(one, (75+0*(screenw-200)/(skin-1), screenh-200))
    win.blit(two, (75+1*(screenw-200)/(skin-1), screenh-200))
    win.blit(three, (75+2*(screenw-200)/(skin-1), screenh-200))
    win.blit(four, (75+3*(screenw-200)/(skin-1), screenh-200))
    win.blit(five, (75+4*(screenw-200)/(skin-1), screenh-200))
    #intro = "Rip-off tRex gOOGle gaMe"
    message_display("Rip-off tRex gOOGle gaMe", white, 0, -175, size="medium")
    message_display("Press the corresponding number to choose the skin:", white, 0, -90, size="small")
    message_display("Skin 1", white, 75+0*(screenw-200)/(skin-1) - screenw/2 + 25, 0, size="s_small")
    message_display("Skin 2", white, 75+1*(screenw-200)/(skin-1) - screenw/2 + 25, 0, size="s_small")
    message_display("Skin 3", white, 75+2*(screenw-200)/(skin-1) - screenw/2 + 25, 0, size="s_small")
    message_display("Skin 4", white, 75+3*(screenw-200)/(skin-1) - screenw/2 + 25, 0, size="s_small")
    message_display("Skin 5", white, 75+4*(screenw-200)/(skin-1) - screenw/2 + 25, 0, size="s_small")
    message_display("Press 0 if you want the OG white square.", white, 0, 175, size="s_small")
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            beg = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                skins = one
                beg = False
                run = True
            elif event.key == pygame.K_2:
                skins = two
                beg = False
                run = True
            elif event.key == pygame.K_3:
                skins = three
                beg = False
                run = True
            elif event.key == pygame.K_4:
                skins = four
                beg = False
                run = True
            elif event.key == pygame.K_5:
                skins = five
                beg = False
                run = True
            elif event.key == pygame.K_0:
                skins = wight
                beg = False
                run = True

#main
boi=smolboi(200,400,50,50)
bullets=[]
blocks=[]

while run:
    clock.tick(40)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            bullets.append(ammo(round(boi.x+boi.width//2), round(boi.y+boi.height//2), 12, black))

    if between == 0:
        blocks.append(blo(screenw+100, 400,random.randint(50,100),random.randint(75,125)))
        between = random.randint(rangemin, rangemax)
    between -= 1

    for bullet in bullets:
        if bullet.x < screenw and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    for block in blocks:
        if block.x > 0 - block.width:
            block.x -= speed
            #eventually change to /20 * score / 2 except for 0
        if block.y + block.height > 450:
            block.y = 450 - block.height
        elif block.x + block.width < 0:
            blocks.pop(blocks.index(block))
        if block.x < boi.x and block.counted==False:
            score += 1
            color = (random.randint(50,200), random.randint(50,200), random.randint(50,200), a)
            block.counted = True
            speed += .25
            if score%5==0:
                if rangemin>20:
                    rangemin -= 1
                if rangemax>40:
                    rangemax -= 1
            
        #collision
        x_crossover = boi.x > block.x and boi.x <= block.x + block.width
        XnW_crossover = boi.x + boi.width > block.x and boi.x + boi.width <= block.x + block.width
        y_crossover = boi.y > block.y and boi.y <= block.y + block.height
        YnH_crossover = boi.y + boi.height > block.y and boi.y + boi.height <= block.y + block.height
    
        if x_crossover or XnW_crossover:
            if y_crossover:
                run = False
            elif YnH_crossover:
                run = False

    keys = pygame.key.get_pressed()
    if not (boi.jump):
        if keys[pygame.K_SPACE]:
            boi.jump = True
    else:
        if boi.jumpcount >= -10:
            neg = 1
            if boi.jumpcount < 0:
                neg = -1
            boi.y -= neg*(boi.jumpcount**2)/2
            boi.jumpcount -= 1
        else:
            boi.jump = False
            boi.jumpcount = 10
    
    drawUpdate()
    
pygame.quit()
quit()




