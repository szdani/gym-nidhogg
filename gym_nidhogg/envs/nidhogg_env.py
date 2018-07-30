import pygame
pygame.init()

GROUND = 250

BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
BACKGROUND_ORANGE = (255, 190, 100)
BACKGROUND_GRAY = (122, 117, 116)
BACKGROUND_GREEN = ( 0, 255, 0)
RED = ( 255, 0, 0)

FIGHTER_HEIGHT = GROUND
FIGHTER_WIDTH = 30
FIGHTER_START_Y = GROUND - 60




class Fighter(pygame.sprite.Sprite):
    #This class represents a car. It derives from the "Sprite" class in Pygame.
    # Force (v) up and mass m.
    v = 1 
    m = 2
    isjump = 0

    def __init__(self, color, width=FIGHTER_WIDTH, height=FIGHTER_HEIGHT):
        # Call the parent class (Sprite) constructor
        super().__init__()
        
        # Pass in the color of the car, and its x and y position, width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)
 
        # Draw the car (a rectangle!)
        pygame.draw.rect(self.image, color, [0, FIGHTER_START_Y, width, height])
        
        # Instead we could load a proper pciture of a car...
        # self.image = pygame.image.load("car.png").convert_alpha()
 
        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()
        
    def update(self):
        if self.isjump:
            # Calculate force (F). F = 0.5 * mass * velocity^2.
            if self.v != 0:
                F = ( 0.5 * self.m * (self.v*self.v) )
            else:
                F = -( 0.5 * self.m * (self.v*self.v) )
 
            # Change position
            self.rect.y = self.rect.y - F
 
            # Change velocity
            self.v = self.v - 1
 
            # If ground is reached, reset variables.
            if self.rect.y == GROUND:
                self.rect.y = GROUND
                self.isjump = 0
                self.v = 1 
            print('Jump', self.rect)


    def moveRight(self, pixels):
        self.rect.x += pixels
 
    def moveLeft(self, pixels):
        self.rect.x -= pixels

    def jump(self):
        self.isjump = 1

all_sprites_list = pygame.sprite.Group()
 
playerCar = Fighter(( 255, 0, 0))
all_sprites_list.add(playerCar)





size = (1000, 300)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My First Game")

carryOn = True
clock = pygame.time.Clock()

while carryOn:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
                carryOn = False # Flag that we are done so we exit this loop
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_x: #Pressing the x Key will quit the game
                    carryOn=False
 
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            playerCar.moveLeft(5)
        if keys[pygame.K_RIGHT]:
            playerCar.moveRight(5)
        if keys[pygame.K_UP]:
            playerCar.jump()
        
        screen.fill(BACKGROUND_ORANGE)
        pygame.draw.rect(screen, BACKGROUND_GRAY, [0, 250, 1000, 50],0)
        pygame.draw.rect(screen, BACKGROUND_GRAY, [400, 100, 200, 25],0)
        # --- Game logic should go here
        all_sprites_list.update()

        #Now let's draw all the sprites in one go. (For now we only have 1 sprite!)
        all_sprites_list.draw(screen)

        pygame.display.flip()
        clock.tick(60)
        
#Once we have exited the main program loop we can stop the game engine:
pygame.quit()
