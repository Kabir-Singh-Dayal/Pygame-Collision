import pygame
import random
pygame.init()
Width = 500
Height = 400
MovSpeed = 5
fontsize = 72
background = pygame.transform.scale(pygame.image.load("bg_img.jpg"), (Width, Height))
font = pygame.font.SysFont("Times New Roman", fontsize)

class sprite(pygame.sprite.Sprite):
    def __init__(self, colour, width, height):
        super().__init__()
        self.width = width
        self.height = height
        self.image = pygame.Surface([width, height])
        self.set_colour(colour)
        self.rect = self.image.get_rect()

    def set_colour(self, colour):
        self.image.fill(pygame.Color("Black"))
        pygame.draw.rect(self.image, colour, pygame.Rect(0, 0, self.width, self.height))

    def move(self, xch, ych):
        self.rect.x = max(min(self.rect.x + xch, Width - self.rect.width), 0)
        self.rect.y = max(min(self.rect.y + ych, Height - self.rect.height), 0)

screen = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Pygame Collision")
all_sprites = pygame.sprite.Group()
s1 = sprite(pygame.Color("Green"), 30, 50)
s1.rect.x, s1.rect.y = random.randint(0, Width - s1.rect.width), random.randint(0, Height - s1.rect.height)
all_sprites.add(s1)
s2 = sprite(pygame.Color("Blue"), 25, 45)
s2.rect.x, s2.rect.y = random.randint(0, Width - s2.rect.width), random.randint(0, Height - s2.rect.height)
all_sprites.add(s2)
running = True
won = False
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if not won:
        keys = pygame.key.get_pressed()
        xch = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * MovSpeed
        ych = (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * MovSpeed
        s1.move(xch, ych)
        if s1.rect.colliderect(s2.rect):
            s1.set_colour(pygame.Color("Red"))
            s2.set_colour(pygame.Color("Yellow"))
            won = True
    screen.blit(background, (0, 0))
    all_sprites.draw(screen)
    if won:
        win = font.render("You Win!", True, pygame.Color("Black"))
        screen.blit(win, ((Width - win.get_width()) // 2, (Height - win.get_height()) // 2))
    pygame.display.flip()
    clock.tick(90)
pygame.quit()
