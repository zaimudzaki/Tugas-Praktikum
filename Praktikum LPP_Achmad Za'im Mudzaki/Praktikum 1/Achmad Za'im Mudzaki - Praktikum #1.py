# Coin sprite 
# https://opengameart.org/content/rotating-coin-0
# Enemy sprite
# https://opengameart.org/content/bevouliin-free-ingame-items-spike-monsters
# Heart sprite
# https://opengameart.org/content/heart-1616
import pygame


def drawText(t, x, y):
    text = font.render(t, True, MUSTARD, DARK_GRAY )
    text_rectangle = text.get_rect()
    text_rectangle.topleft = (x,y)
    screen.blit(text, text_rectangle)

#constant variables
SCREEN_SIZE = (700,500)
DARK_GRAY = (50,50,50 )
MUSTARD =  (3,252,40)

# init
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption('Septian\'s Platform Game')
clock = pygame.time.Clock()
font = pygame.font.Font(pygame.font.get_default_font(), 24)

# games states = playing // win // lose
game_state = 'playing'

# player
player_image = pygame.image.load('robot_0.png')
player_x = 300

player_y = 0
player_speed = 0
player_acceleration = 0.15

player_width = 57
player_height = 51

player_direction = 'right'
# paltforms 
platforms = [
    # middle
    pygame.Rect(100,300,400,50),
    # left
    pygame.Rect(100,250,50,50),
    # right
    pygame.Rect(450,250,50,50),
]
# coins
coins_image = pygame.image.load('coin_0.png')
coins = [
    pygame.Rect(100,200,23,23),
    pygame.Rect(200,250,23,23),
    pygame.Rect(500,200,23,23)
]

score = 0

# enemies
enemies_image = pygame.image.load('enemies_0.png')
enemies = [
    pygame.Rect(150,271,50,29),
    pygame.Rect(400,271,50,29)
]

lives = 3
heart_image = pygame.image.load('heart.png')

running = True  
while running:
#game loop
    # -----
    # input
    # -----

    # check for quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
   

    if game_state == 'playing':

        new_player_x = player_x
        new_player_y = player_y 
        # player input
        keys = pygame.key.get_pressed()
        # left
        if keys[pygame.K_LEFT] :
            new_player_x -= 2
            player_direction = 'left'
        # right
        if keys[pygame.K_RIGHT] :
            new_player_x += 2 
            player_direction = 'right'
        # jump (if on the ground)
        if keys[pygame.K_UP] and player_on_ground:
            player_speed = -5

    # ------
    # UPDATE
    # ------

    if game_state == 'playing':
        # horizontal movement

        new_player_rect = pygame.Rect(new_player_x,player_y,player_width,player_height)
        x_collision = False

        #...check againsst every platform
        for p in platforms:
            if p.colliderect(new_player_rect) :
                x_collision = True
                break
    
        if x_collision == False :
            player_x = new_player_x 
    
        # vertical movement
        
        player_speed += player_acceleration
        new_player_y += player_speed
    
        new_player_rect = pygame.Rect(player_x,new_player_y,player_width,player_height)
        y_collision = False
        player_on_ground = False

        #...check againsst every platform
        for p in platforms:
            if p.colliderect(new_player_rect) :
                y_collision = True
                player_speed = 0
                # if the platform is below the player
                if p[1] > new_player_y:
                    #stick the player to the platform
                    player_y = p[1] - player_height
                    player_on_ground = True
                break
    

        if y_collision == False :
            player_y = new_player_y
        # update

        # see if any coins have been collected
        player_rect = pygame.Rect(player_x,player_y,player_width,player_height)
        for c in coins : 
            if c.colliderect(player_rect) :
                coins.remove(c)
                score += 1
                if score >= 3 :
                    game_state = 'win'
        # see if the player has hit an enemy
        for e in enemies : 
            if e.colliderect(player_rect) :
                lives -= 1
                # reset player possition
                player_x = 300
                player_y = 0
                player_speed = 0
                # change the game state
                # if no lives remaning
                if lives <= 0:
                    game_state = 'lose'
    
  
    # ----
    # DRAW 
    # ----
    # background
    screen.fill(DARK_GRAY)

    
      
    # platform
    for p in platforms:
        pygame.draw.rect(screen, (MUSTARD), p)
    
    # coins
    for c in coins :
        screen.blit(coins_image, (c.x, c.y))

    # enemies
    for e in enemies :
        screen.blit(enemies_image, (e.x, e.y))

    # player
    if player_direction == 'right':
        screen.blit(player_image, (player_x,player_y))
    elif player_direction == 'left':
        screen.blit(pygame.transform.flip(player_image, True, False), (player_x,player_y))
   
    # present screen
    pygame.display.flip()

    # player information display

    # score
    screen.blit(coins_image, (10,10))
    drawText(str(score), 50, 10)

    # lives
    for l in range(lives):
        screen.blit(heart_image, (200 + (l*50),0))
    if game_state == 'win':
        drawText('You win!', 50, 50)
        # draw win text
    if game_state == 'lose':
        # draw lose text
        drawText('You lose!', 50, 50)
    # present screen
    pygame.display.flip()
        
    clock.tick(60)

#Keluar
pygame.quit()