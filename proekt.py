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
        if self.hitbox.bottom > 775:
            self.hitbox.bottom = 775
        if self.hitbox.top < 25:
            self.hitbox.top = 25

class Ball():
    def __init__ (self, x, y, speed):
        self.hitbox = pygame.Rect(x, y, 40, 40)
        self.speed = speed
        self.speed_x = speed
        self.speed_y = speed
    def move(self):
        self.hitbox.x += self.speed_x
        self.hitbox.y += self.speed_y
        if self.hitbox.top < 0:
            self.speed_y = self.speed
        if self.hitbox.top > 800:
            self.speed_y = - self.speed
        if self.hitbox.left < 0:
            self.speed_x = self.speed
        if self.hitbox.right > 1000:
            self.speed_x = - self.speed


player1 = Player(50, 200, 4)
ball = Ball(500, 400, 5)

while True:
    okno.fill((0, 0, 0))
    event_list = pygame.event.get()
    for e in event_list:
        if e.type == pygame.QUIT:
            exit()
    player1.move()
    ball.move()
    pygame.draw.rect(okno, (255, 0, 0), player1.hitbox)
    pygame.draw.rect(okno, (255, 0, 0), ball.hitbox)
    pygame.display.update()
    clock.tick(100)