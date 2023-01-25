#   #   #Imports
import pygame
from sys import exit
from random import randint

#   #   #Initialising
pygame.init()
WINDOW = pygame.display.set_mode((800,400))
CLOCK = pygame.time.Clock()
pygame.display.set_caption("Jump Jump game")
gravity = .0

#   #   #Variables
game_active = False
obstacle_list = []
score = 0
FONT =  pygame.font.Font("C:\\Users\\singl\\Desktop\\Coding\\Pygame\\UltimatePygameIntro-main\\font\\Pixeltype.ttf", 50)

#   #   #Functions
# def score(x):
#     if obstacle_list:
#         for i in obstacle_list:
#             if i.x == 50:
#                 score = score + 1

#             score_surf = FONT.render(f'Score: {score}',False, (204, 119, 33))
#             score_rect = score_surf.get_rect(center = (400,50))
#             WINDOW.blit(score_surf, score_rect)

#             return x
#     else:



def obstacles(obstacle_list):
    global score
    if obstacle_list:
        for i in obstacle_list:
            i.x -= 4

            if i.top == 175:
                WINDOW.blit(Obstacle1_1, i)
                if i.left == 102:
                    score += 1
            if i.bottom == 45:
                WINDOW.blit(Obstacle1_2, i)
            if i.bottom == 85:
                WINDOW.blit(Obstacle3, i)
                if i.left == 102:
                    score += 1
            if i.top == 215:
                WINDOW.blit(Obstacle3, i)
            if i.bottom == 170:
                WINDOW.blit(Obstacle4, i)
                if i.left == 102:
                    score += 1
            if i.top == 130:
                WINDOW.blit(Obstacle4, i)
                if i.left == 102:
                    score += 1


        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]
        return obstacle_list
    else:
        return []

def collisions(player, obstacle_list):
    if obstacle_list:
        for i in obstacle_list:
            if player.colliderect(i):
                return False

    return True




#   #   #Loading Images + Making Rects
ground = pygame.image.load("C:\\Users\\singl\\Desktop\\Coding\\Pygame\\Actual Games\\Flappy Clone\\ground1.png").convert()
sky = pygame.image.load('C:\\Users\\singl\\Desktop\\Coding\\Pygame\\Actual Games\\Flappy Clone\\CitySkyline.png').convert()

Space_strt_surface = FONT.render("Press 'X' to Start", False , (204, 119, 33))
Space_strt_rect = Space_strt_surface.get_rect(center = (400, 50))
ScoreDisplay = FONT.render(str(score), False , (204, 119, 33))
ScoreDisplay_rect = ScoreDisplay.get_rect(center = (400, 50))
#Player
player = pygame.image.load("C:\\Users\\singl\\Desktop\\Coding\\Pygame\\Actual Games\\Flappy Clone\\jumpjumptank.png").convert_alpha()
player_rect = player.get_rect(midbottom = (50,100))

#Rectangles
Obstacle1_1 = pygame.image.load("C:\\Users\\singl\\Desktop\\Coding\\Pygame\\Actual Games\\Flappy Clone\\Obstacle1.png").convert_alpha()
Obstacle1_2 = pygame.image.load("C:\\Users\\singl\\Desktop\\Coding\\Pygame\\Actual Games\\Flappy Clone\\Obstacle2.png").convert_alpha()
Obstacle3 = pygame.image.load("C:\\Users\\singl\\Desktop\\Coding\\Pygame\\Actual Games\\Flappy Clone\\Obstacle3.png").convert_alpha()
Obstacle4 = pygame.image.load("C:\\Users\\singl\\Desktop\\Coding\\Pygame\\Actual Games\\Flappy Clone\\Obstacle4.png").convert_alpha()

#   #   #Events
Spawn_timer = pygame.USEREVENT + 1
pygame.time.set_timer(Spawn_timer,1400)

#   #   #Event Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           pygame.quit()
           exit()

        if game_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.y > 0:
                    gravity = -10
            if event.type == Spawn_timer and game_active:
                rand = randint(0,3)
                if rand == 0:
                    obstacle_list.append(Obstacle1_1.get_rect(midbottom = (850,300)))
                    obstacle_list.append(Obstacle1_2.get_rect(midtop = (850,0)))
                elif rand == 1:
                    obstacle_list.append(Obstacle3.get_rect(midtop = (850,0)))
                    obstacle_list.append(Obstacle3.get_rect(midbottom = (850,300)))
                elif rand == 2:
                    obstacle_list.append(Obstacle4.get_rect(midtop = (850,0)))
                elif rand == 3:
                    obstacle_list.append(Obstacle4.get_rect(midbottom = (850,300)))
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_x:
                game_active = True
                start_time = int((pygame.time.get_ticks() /1000))


#Border Control
    if player_rect.bottom <= -30:
            player_rect.top = -30
    if player_rect.bottom >= 300:
        game_active = False
        player_rect.bottom = 300


    if game_active:
        #Background
        WINDOW.blit(ground, (0, 300))
        WINDOW.blit(sky,(0,0))

        #Gravity
        gravity += .7
        player_rect.y += gravity

        #Player
        if player_rect.bottom >= 300:
            player_rect.bottom = 300
        WINDOW.blit(player, player_rect)

        #Obstacles
        obstacle_list = obstacles(obstacle_list)

        #Score
        ScoreDisplay = FONT.render(str(score), False , (204, 119, 33))
        WINDOW.blit(ScoreDisplay, ScoreDisplay_rect)



        #Collisions
        #game_active = collisions(player_rect, obstacle_list)


    else:
        gravity = 0
        player_rect.midbottom = (50, 100)
        WINDOW.blit(ground, (0, 300))
        WINDOW.blit(sky,(0,0))
        WINDOW.blit(Space_strt_surface, Space_strt_rect)
        WINDOW.blit(player, player_rect)
        obstacle_list.clear()
        score = 0

    pygame.display.update()
    CLOCK.tick(60)
