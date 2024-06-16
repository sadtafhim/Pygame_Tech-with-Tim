import pygame #importing pygame
pygame.init() #initiating pygame

win = pygame.display.set_mode((500,500)) #make a window in pygame
pygame.display.set_caption("first game") #name of the window

#initializing parameters
x = 50
y = 50
width = 40
height = 60
vel = 5

#loop
run =True #run variable
while run:
    pygame.time.delay(100) #game clock initialization

    #checking for event
    for event in pygame.event.get(): #this gets all the event that happens(like mouseclick, mousemove etc):
         if event.type==pygame.QUIT: #if we press the exit button in our window
             run =False #change the run variable and breaks the while loop
    # moving the rectangle
    keys = pygame.key.get_pressed() #list of keys being pressed
    if keys[pygame.K_LEFT]:# if left arrow key is pressed
        x-= vel #changing the x coordinate by the velocity
    if keys[pygame.K_RIGHT]: # if right arrow key is pressed
        x += vel  # changing the x coordinate by the velocity
    if keys[pygame.K_UP]: # if Up arrow key is pressed
        y -= vel # changing the y coordinate by the velocity
    if keys[pygame.K_DOWN]: # if Down arrow key is pressed
        y += vel  # changing the y coordinate by the velocity
    win.fill((0,0,0)) #filling the rest of the window with background color so the character stays in shape
    # drawing character(rectangle)
    pygame.draw.rect(win,(255,0,0),(x,y,width,height)) #first one is where it will be layed over, next is the color selection, third is the the position(x,y) and size(height,width) of the character)
    pygame.display.update()#refresh the display, without it the characters wont show up


pygame.quit() #quits the pygame window