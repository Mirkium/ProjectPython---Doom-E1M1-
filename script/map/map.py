import pygame
import math

# === Map ===
map_data = [
[1]*60,
[1]+[0]*10+[1]*6+[0]*20+[1]*21,
[1]+[0]*8+[1]*8+[0]*15+[1]*27,
[1]+[0]*8+[1,0,0,0,0,1,0,1,1,0,1,0,0,1,0,1,0,1,1,1,0,1,0,1,0,0,0,1]+[1]*10,
[1]+[0]*5+[1]*4+[0]*5+[3]+[0]*10+[3]+[0]*5+[1]*5+[0]*5+[1]*10,
[1]+[0]*5+[1]*5+[0]*6+[3]+[1]*10+[3]+[0]*6+[1]*10+[0]*5+[1]*5,
[1]+[0]*10+[3]+[0]*20+[3]+[0]*10+[1]*9,
[1]+[1,1,1,0,1,1,1,1,0,3,1,1,1,0,1,1,1,0,3,1,1,1,1,0,1,1,1,1,0,1,1,1,1,1,0,1]+[1]*17,
[1]+[0]*20+[3]+[0]*15+[3]+[0]*20+[1],
[1]+[0]*15+[3]+[1]*5+[3]+[0]*30+[1],
[1]+[0]*10+[3]+[0]*15+[3]+[0]*10+[1]*10+[0]*10+[1],
[1]+[0]*20+[1]*10+[0]*20+[1]*9,
[1]+[0]*15+[1]*15+[0]*15+[1]*14,
[1]+[0]*15+[1,0,0,0,0,1,0,0,0,0,1,0,1,0,0,1,0,0,1,1,0,0,0,1,0,1,0,0,0,1]+[1]*10,
[1]+[0]*10+[1]*10+[0]*10+[1]*10+[0]*10+[1]*9,
[1]+[0]*25+[3]+[0]*10+[3]+[0]*15+[1]*8,
[1]+[1,1,1,0,1,0,1,1,1,0,1,1,1,1,1,0,1,1,1,1,0,1,1,1,0,1,0,1,1,0,1,1,1,1,0,1]+[1]*18,
[1]+[0]*20+[3]+[0]*20+[3]+[0]*15+[1]*4,
[1]+[0]*25+[3]+[1]*10+[3]+[0]*20+[1]*4,
[1]+[0]*40+[1]*19,
[1]+[0]*25+[1]*10+[0]*10+[1]*14,
[1]+[0]*20+[1]*15+[0]*15+[1]*9,
[1]+[0]*15+[1]*20+[0]*15+[1]*9,
[1]+[0]*10+[1]*30+[0]*10+[1]*9,
[1]+[0]*20+[1]*20+[0]*15+[1]*4,
[1]+[0]*25+[1]*10+[0]*15+[1]*9,
[1]+[0]*20+[3]+[0]*10+[3]+[0]*20+[1]*9,
[1]+[0]*15+[3]+[0]*10+[3]+[0]*25+[1]*9,
[1]+[0]*40+[1]*19,
[1]+[0]*30+[3]+[0]*15+[3]+[0]*10+[1]*4,
[1]+[0]*40+[3]+[0]*15+[1]*4,
[1]+[0]*50+[1]*9,
[1]+[0]*45+[3]+[0]*10+[1]*4,
[1]+[0]*50+[1]*9,
[1]+[0]*55+[1]*4,
[1]+[0]*58+[1],
[1]*60
]


MAP_WIDTH = len(map_data[0])
MAP_HEIGHT = len(map_data)
TILE_SIZE = 64

# === Player ===
player_x = 2.5 * TILE_SIZE
player_y = 1.5 * TILE_SIZE
player_angle = 0
FOV = math.pi / 3
NUM_RAYS = 400  # plus de rayons pour plus de fluidité
MAX_DEPTH = 800
SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 920
PLAYER_SPEED = 5
ROT_SPEED = 0.07

# === Pygame setup ===
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

# === Colors ===
color_Wall = (100, 100, 100)
color_Floor = (50, 50, 50)
color_Ceil = (30, 30, 30)

# === Raycasting 2.5D ===
def cast_rays(surface):
    start_angle = player_angle - FOV / 2
    ray_width = surface.get_width() / NUM_RAYS

    for ray in range(NUM_RAYS):
        angle = start_angle + (ray / NUM_RAYS) * FOV
        for depth in range(1, MAX_DEPTH, 2):  # avancer de 2 pixels pour optimiser
            target_x = player_x + math.cos(angle) * depth
            target_y = player_y + math.sin(angle) * depth

            map_x = int(target_x / TILE_SIZE)
            map_y = int(target_y / TILE_SIZE)

            if 0 <= map_x < MAP_WIDTH and 0 <= map_y < MAP_HEIGHT:
                if map_data[map_y][map_x] == 1:
                    # corriger l’effet fish-eye
                    depth *= math.cos(player_angle - angle)
                    wall_height = 20000 / (depth + 0.0001)
                    color_value = max(0, min(255, 100 / (1 + depth * 0.01)))
                    pygame.draw.rect(surface, (color_value, color_value, color_value),
                                     (ray * ray_width,
                                      (surface.get_height() - wall_height) // 2,
                                        ray_width + 1,
                                        wall_height))
                    break
                
# === Movement Function ZQSD ===
def movement(keys):
    global player_x, player_y

    # Position future potentielle
    next_x = player_x
    next_y = player_y

    # Direction
    sin_a = math.sin(player_angle)
    cos_a = math.cos(player_angle)

    # Mouvement avant/arrière
    if keys[pygame.K_z]:
        next_x += cos_a * PLAYER_SPEED
        next_y += sin_a * PLAYER_SPEED
    if keys[pygame.K_s]:
        next_x -= cos_a * PLAYER_SPEED
        next_y -= sin_a * PLAYER_SPEED

    # Mouvement latéral
    if keys[pygame.K_q]:
        next_x += math.cos(player_angle - math.pi/2) * PLAYER_SPEED
        next_y += math.sin(player_angle - math.pi/2) * PLAYER_SPEED
    if keys[pygame.K_d]:
        next_x += math.cos(player_angle + math.pi/2) * PLAYER_SPEED
        next_y += math.sin(player_angle + math.pi/2) * PLAYER_SPEED

    # === Collision check ===
    # On calcule les tuiles où le joueur se déplacerait
    map_x = int(next_x / TILE_SIZE)
    map_y = int(next_y / TILE_SIZE)

    # Vérifie qu'on ne rentre pas dans un mur
    if 0 <= map_x < MAP_WIDTH and 0 <= map_y < MAP_HEIGHT:
        if map_data[map_y][map_x] == 0 or map_data[map_y][map_x] == 3:  # sol ou porte
            player_x = next_x
            player_y = next_y


# === Main loop ===
def game():
    pygame.mixer.music.load("./assets/sound/03. E1M1 - At Doom's Gate.mp3")
    pygame.mixer.music.set_volume(0.6)
    pygame.mixer.music.play(-1)

    global player_angle
    running = True

    # === Initialisation souris ===
    pygame.mouse.set_visible(False)
    pygame.event.set_grab(True)

    render_surface = pygame.Surface((SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        movement(keys)

        # === Rotation avec la souris ===
        mouse_dx, _ = pygame.mouse.get_rel()
        player_angle += mouse_dx * 0.0025  # Ajuste sensibilité ici

        # Dessin du décor
        render_surface.fill(color_Ceil)
        pygame.draw.rect(render_surface, color_Floor,
                            (0, render_surface.get_height()//2,
                            render_surface.get_width(), render_surface.get_height()//2))
        cast_rays(render_surface)

        scaled_surface = pygame.transform.scale(render_surface, (SCREEN_WIDTH, SCREEN_HEIGHT))
        screen.blit(scaled_surface, (0, 0))
        pygame.display.flip()
        clock.tick(60)


game()
pygame.quit()
