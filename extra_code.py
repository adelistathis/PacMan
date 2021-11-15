# Create the player paddle object
    Pacman = Player(w, p_h, "images/pacman_c.png")
    all_sprites_list.add(Pacman)
    pacman_collide.add(Pacman)

    Blinky = Ghost(w, b_h, "images/blinky.png")
    monster_list.add(Blinky)
    all_sprites_list.add(Blinky)

    Pinky = Ghost(w, m_h, "images/pinky.png")
    monster_list.add(Pinky)
    all_sprites_list.add(Pinky)

    Inky = Ghost(i_w, m_h, "images/inky.png")
    monster_list.add(Inky)
    all_sprites_list.add(Inky)

    Clyde = Ghost(c_w, m_h, "images/Clyde.png")
    monster_list.add(Clyde)
    all_sprites_list.add(Clyde)

    bll = len(block_list)

    score = 0

    done = False

    i = 0

    while done == False:
        # EVENT PROCESSING
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    Pacman.change_speed(-30, 0)
                if event.key == pygame.K_RIGHT:
                    Pacman.change_speed(30, 0)
                if event.key == pygame.K_UP:
                    Pacman.change_speed(0, -30)
                if event.key == pygame.K_DOWN:
                    Pacman.change_speed(0, 30)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    Pacman.change_speed(30, 0)
                if event.key == pygame.K_RIGHT:
                    Pacman.change_speed(-30, 0)
                if event.key == pygame.K_UP:
                    Pacman.change_speed(0, 30)
                if event.key == pygame.K_DOWN:
                    Pacman.change_speed(0, -30)

        # GAME LOGIC
        Pacman.update(wall_list, gate)

        returned = Pinky.change_speed(Pinky_directions, False, p_turn, p_steps, pl)
        p_turn = returned[0]
        p_steps = returned[1]
        Pinky.change_speed(Pinky_directions, False, p_turn, p_steps, pl)
        Pinky.update(wall_list, False)

        returned = Blinky.change_speed(Blinky_directions, False, b_turn, b_steps, bl)
        b_turn = returned[0]
        b_steps = returned[1]
        Blinky.change_speed(Blinky_directions, False, b_turn, b_steps, bl)
        Blinky.update(wall_list, False)

        returned = Inky.change_speed(Inky_directions, False, i_turn, i_steps, il)
        i_turn = returned[0]
        i_steps = returned[1]
        Inky.change_speed(Inky_directions, False, i_turn, i_steps, il)
        Inky.update(wall_list, False)

        returned = Clyde.change_speed(Clyde_directions, "clyde", c_turn, c_steps, cl)
        c_turn = returned[0]
        c_steps = returned[1]
        Clyde.change_speed(Clyde_directions, "clyde", c_turn, c_steps, cl)
        Clyde.update(wall_list, False)

        # See if the Pacman block has collided with anything.
        blocks_hit_list = pygame.sprite.spritecollide(Pacman, block_list, True)

        # Check the list of collisions.
        if len(blocks_hit_list) > 0:
            score += len(blocks_hit_list)

        # DRAWINGS
        WIN.fill(BLACK)

        wall_list.draw(WIN)
        gate.draw(WIN)
        all_sprites_list.draw(WIN)
        monster_list.draw(WIN)

        text = font.render("Score: " + str(score) + "/" + str(bll), True, RED)
        WIN.blit(text, [10, 10])

        if score == bll:
            doNext("Congratulations, you won!", 145, all_sprites_list, block_list, monster_list, pacman_collide,
                   wall_list, gate)

        monsta_hit_list = pygame.sprite.spritecollide(Pacman, monster_list, False)

        if monsta_hit_list:
            doNext("Game Over", 235, all_sprites_list, block_list, monster_list, pacman_collide, wall_list, gate)

        pygame.display.flip()

        clock.tick(10)


def doNext(message, left, all_sprites_list, block_list, monster_list, pacman_collide, wall_list, gate):



  while True:
      # ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          sys.exit()
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()
          if event.key == pygame.K_RETURN:
            del all_sprites_list
            del block_list
            del monster_list
            del pacman_collide
            del wall_list
            del gate
            start_game()

      #Grey background
      w = pygame.Surface((400,200))  # the size of your rect
      w.set_alpha(10)                # alpha level
      w.fill((128,128,128))           # this fills the entire surface
      WIN.blit(w, (100,200))    # (0,0) are the top-left coordinates

      #Won or lost
      text1= font.render(message, True, WHITE)
      WIN.blit(text1, [left, 233])

      text2=font.render("To play again, press ENTER.", True, WHITE)
      WIN.blit(text2, [135, 303])
      text3=font.render("To quit, press ESCAPE.", True, WHITE)
      WIN.blit(text3, [165, 333])

      pygame.display.flip()

      clock.tick(10)


BLUE = pygame.Color(0, 0, 255)
GREEN = pygame.Color(0, 255, 0)
BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)
GREY = pygame.Color(128, 128, 128)
RED = pygame.Color(255, 0, 0)

FPS = 120

PACMAN1_ = pygame.image.load(os.path.join('images','pacman_c.png'))
PACMAN1 = pygame.transform.scale(PACMAN1_,(100,100))

PACMAN2_ = pygame.image.load(os.path.join('images','pacman_cr.png'))
PACMAN2 = pygame.transform.scale(PACMAN2_,(100,100))

PACMAN3_ = pygame.image.load(os.path.join('images','pacman_o.png'))
PACMAN3 = pygame.transform.scale(PACMAN3_,(100,100))

PACMAN4_ = pygame.image.load(os.path.join('images','pacman_or.png'))
PACMAN4 = pygame.transform.scale(PACMAN4_,(100,100))

Pinky_directions = [
[0,-30,4],
[15,0,9],
[0,15,11],
[-15,0,23],
[0,15,7],
[15,0,3],
[0,-15,3],
[15,0,19],
[0,15,3],
[15,0,3],
[0,15,3],
[15,0,3],
[0,-15,15],
[-15,0,7],
[0,15,3],
[-15,0,19],
[0,-15,11],
[15,0,9]
]

Blinky_directions = [
[0,-15,4],
[15,0,9],
[0,15,11],
[15,0,3],
[0,15,7],
[-15,0,11],
[0,15,3],
[15,0,15],
[0,-15,15],
[15,0,3],
[0,-15,11],
[-15,0,3],
[0,-15,11],
[-15,0,3],
[0,-15,3],
[-15,0,7],
[0,-15,3],
[15,0,15],
[0,15,15],
[-15,0,3],
[0,15,3],
[-15,0,3],
[0,-15,7],
[-15,0,3],
[0,15,7],
[-15,0,11],
[0,-15,7],
[15,0,5]
]

Inky_directions = [
[30,0,2],
[0,-15,4],
[15,0,10],
[0,15,7],
[15,0,3],
[0,-15,3],
[15,0,3],
[0,-15,15],
[-15,0,15],
[0,15,3],
[15,0,15],
[0,15,11],
[-15,0,3],
[0,-15,7],
[-15,0,11],
[0,15,3],
[-15,0,11],
[0,15,7],
[-15,0,3],
[0,-15,3],
[-15,0,3],
[0,-15,15],
[15,0,15],
[0,15,3],
[-15,0,15],
[0,15,11],
[15,0,3],
[0,-15,11],
[15,0,11],
[0,15,3],
[15,0,1],
]

Clyde_directions = [
[-30,0,2],
[0,-15,4],
[15,0,5],
[0,15,7],
[-15,0,11],
[0,-15,7],
[-15,0,3],
[0,15,7],
[-15,0,7],
[0,15,15],
[15,0,15],
[0,-15,3],
[-15,0,11],
[0,-15,7],
[15,0,3],
[0,-15,11],
[15,0,9],
]

pl = len(Pinky_directions)-1
bl = len(Blinky_directions)-1
il = len(Inky_directions)-1
cl = len(Clyde_directions)-1

WIDTH, HEIGHT = 1000, 1000
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PacMan")

# Create a surface we can draw on
background = pygame.Surface((500, 500))
background.fill(BLACK)

# default locations for Pacman and monstas
w = 303-16 # Width
p_h = (7*60)+19 # Pacman height
m_h = (4*60)+19 # Monster height
b_h = (3*60)+19 # Binky height
i_w = 303-16-32 # Inky width
c_w = 303+(32-16) # Clyde width

clock = pygame.time.Clock()

pygame.font.init()
font = pygame.font.Font("freesansbold.ttf", 24)


start_game()

pygame.quit()
sys.exit()