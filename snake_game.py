import pygame
import sys
import time
import random

def snake():
    global x,y,foodx,foody,game_over
    x=(x+tempx)%width
    y=(y+tempy)%height
    if (x,y) in body:
        game_over=True
        return
    body.append((x, y))
    if foodx==x and foody==y:
        while (foodx,foody) in body:
            foodx, foody = random.randrange(0, width) // 10 * 10, random.randrange(0, height) // 10 * 10
        pygame.mixer.music.play()
    else:
        del body[0]
    snake_ground.fill((0,0,0))
    score=font.render("Score : "+str(len(body)-1),True,(255,255,0))
    snake_ground.blit(score,[0,0])
    pygame.draw.rect(snake_ground,(0,0,255),(foodx,foody,10,10))
    for i,j in body:
        pygame.draw.rect(snake_ground,(0,255,0),(i,j,10,10))
    pygame.display.update()

pygame.init()
pygame.mixer.init()
pygame.mixer.music.set_volume(1)
pygame.mixer.music.load('C:\song.mp3')
width,height=800,600
snake_ground=pygame.display.set_mode((width,height))
pygame.display.set_caption("SNAKE GAME")
x,y=200,200
tempx,tempy=10,0
foodx,foody=random.randrange(0,width)//10*10,random.randrange(0,height)//10*10
clock=pygame.time.Clock()
body=[(x,y)]
game_over=False
font=pygame.font.SysFont("roboto",25)

while True:
    if game_over:
        score = font.render("Score : " + str(len(body)-1), True, (255, 255, 0))
        snake_ground.blit(score, [0, 0])
        snake_ground.fill((0,0,0))
        msg = font.render('Your Score is : ' + str(len(body) - 1), True, (255, 255, 255))
        snake_ground.blit(msg, [width // 3 + 40, height // 3 + 80])
        msg=font.render('GAME OVER!',True,(255,0,0))
        snake_ground.blit(msg,[width//3+50,height//3+110])
        pygame.display.update()
        time.sleep(2)
        pygame.quit()
        sys.exit()
    events=pygame.event.get()
    for event in events:
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                if tempx!=10:
                    tempx=-10
                tempy=0
            elif event.key==pygame.K_RIGHT:
                if tempx != -10:
                    tempx=10
                tempy=0
            elif event.key==pygame.K_UP:
                tempx=0
                if tempy != 10:
                    tempy=-10
            elif event.key == pygame.K_DOWN:
                tempx =0
                if tempy != -10:
                    tempy = 10
            elif event.key==pygame.K_0:
                game_over=True
            # else:
            #     continue

        snake()
    if not events:
        snake()
    clock.tick(15)
