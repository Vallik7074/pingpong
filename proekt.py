import pygame 
okno = pygame.display.set_mode((1000, 800))

clock = pygame.time.Clock()
class Player():
    def __init__ (self, x, y, speed):
        self.hitbox = pygame.Rect(x, y, 50, 200)
        self.speed = speed

    def move(self):
        key_list = pygame.key.get_pressed()
        if key_list[pygame.K_w]:
            self.hitbox.y -= self.speed
        if key_list[pygame.K_s]:
            self.hitbox.y += self.speed
        if self.hitbox.bottom > 750:
            self.hitbox.bottom = 750
        if self.hitbox.top < 50:
            self.hitbox.top = 50

player1 = Player(50, 200, 4)
while True:
    okno.fill((0, 0, 0))
    event_list = pygame.event.get()
    for e in event_list:
        if e.type == pygame.QUIT:
            exit()
    player1.move()
    pygame.draw.rect(okno, (255, 0, 0), player1.hitbox)
    pygame.display.update()
    clock.tick(100)