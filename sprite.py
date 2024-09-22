import pygame
pygame.init()

#set up the display area
WIDTH = 400
HEIGHT = 400
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Marching Soldier")

#define the player sprite
class Player(pygame.sprite.Sprite):
    #constructor
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"C:\Users\Admin\OneDrive\Documents\Game Dev 2\photos\Soldier.png")
        self.image = pygame.transform.scale(self.image,(70,100))
        self.rect = self.image.get_rect()

    def update(self,pressed_key):
        if pressed_key[pygame.K_DOWN]:
            self.rect.move_ip(0,5)


        #boundary wall
        if self.rect.bottom > HEIGHT :
            self.rect.bottom = HEIGHT

#class ended
sprites = pygame.sprite.Group()
def startgame():
    player = Player() #object
    sprites.add(player)
    
    while True:
        screen.fill("red")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
    
        sprites.draw(screen)

        #get the key
        pressed_key = pygame.key.get_pressed()
        player.update(pressed_key)

        pygame.display.update()

startgame()