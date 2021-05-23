from pygame import *

window = display.set_mode((700, 500))
display.set_caption("Пинг-понг")

wh = 700
ww = 500

background = transform.scale( image.load('pole.jpg'),(wh,ww))

#mixer.init()
#mixer.music.load('jungles.ogg')
#mixer.music.play()
#kick = mixer.Sound("kick.ogg")

clock = time.Clock()
FPS = 60

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, width, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (width, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y ))

class Player1(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 40:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 345:
            self.rect.y += self.speed
        

class Player2(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 40:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 345:
            self.rect.y += self.speed






hero1 = Player1('hero1.png', 5, 190, 5, 40, 145)
hero2 = Player2('hero2.png', 620, 190, 5, 40, 140)
ball = GameSprite('ball.png', 325, 220, 3, 50, 50)

finish = False
game = True

x_speed = 3
y_speed = 3


while game:
    
    clock.tick(FPS)
    for e in event.get():
        if e.type == QUIT:
            game = False

    if not finish:
        window.blit(background,(0,0))
        # a = sprite.collide_rect(hero, enemy)
        # b = sprite.collide_rect(hero, tresh)
        ball.rect.x += x_speed
        ball.rect.y += y_speed
        if sprite.collide_rect(hero1, ball) or sprite.collide_rect(hero2, ball):
            x_speed *= -1
            y_speed *= 1
        if ball.rect.y > 410 or ball.rect.y < 15:
            y_speed *= -1

        hero1.update()
        hero2.update()
        hero1.reset()
        hero2.reset()
        ball.reset()
        ball.update()
    
       

        # if a == True:
        #     print('You died')
        #     background = transform.scale( image.load('background1.jpg'),(wh,ww))
        #     window.blit(background,(0,0))
        #     finish = True
        # if b == True:
        #     print('You win')
        #     background = transform.scale( image.load('background2.jpg'),(wh,ww))
        #     window.blit(background,(0,0))
        #     finish = True
        # if c == True or f == True or t == True or i == True or r == True or k == True or q == True :
        #     print('You died')
        #     background = transform.scale( image.load('background1.jpg'),(wh,ww))
        #     window.blit(background,(0,0))
        #     finish = True

       

    display.update()