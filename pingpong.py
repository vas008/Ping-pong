from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, size_x, size_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
        
class Player(GameSprite):
    def update1(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 140:
            self.rect.y += self.speed
    def update2(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 140:
            self.rect.y += self.speed

class Ball(GameSprite):
    def update(self):
        pass

win_width = 800
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Пинг-понг")
window.fill((200, 150, 230))

player1 = Player('racket.png', 50, 180, 5, 40, 140)
player2 = Player('racket.png', 710, 180, 5, 40, 140)
ball = Ball('tenis_ball.png', 375, 225, 5, 50, 50)

game = True
finish = False
clock = time.Clock()
FPS = 60

while game:
    for e in event.get():
        if e.type == QUIT:
           game = False

    if finish == False:
        window.fill((200, 150, 230))

        player1.update1()
        player2.update2()
        
        player1.reset()
        player2.reset()
        ball.reset()

    display.update()
    clock.tick(FPS)
