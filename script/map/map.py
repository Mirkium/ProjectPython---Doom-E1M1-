import pygame
import math

# === Map ===
map_data = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,1,1,1,0,0,1,0,1,1,1,0,1,1,1,0,0,1],
    [1,0,1,0,1,0,0,0,0,1,0,1,0,1,0,0,0,0,1],
    [1,0,1,0,0,0,3,0,0,1,0,0,0,1,0,3,0,0,1],
    [1,0,1,1,1,1,3,1,1,1,0,1,1,1,1,3,1,1,1],
    [1,0,0,0,0,0,3,0,0,0,0,0,0,0,0,3,0,0,1],
    [1,1,1,0,1,1,3,1,1,0,1,1,0,1,1,3,1,1,1],
    [1,0,0,0,1,0,3,0,1,0,0,0,0,1,0,3,0,0,1],
    [1,0,1,0,1,0,3,0,1,0,1,0,0,1,0,3,0,1,1],
    [1,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1],
    [1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
]

MAP_WIDTH = len(map_data[0])
MAP_HEIGHT = len(map_data)
TILE_SIZE = 64

# === Player ===
player_x = 2.5 * TILE_SIZE
player_y = 2.5 * TILE_SIZE
player_angle = 0
FOV = math.pi / 3
NUM_RAYS = 400  # plus de rayons pour plus de fluidité
MAX_DEPTH = 800
SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 920
PLAYER_SPEED = 2.5
ROT_SPEED = 0.03

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
    if keys[pygame.K_z]:
        player_x += math.cos(player_angle) * PLAYER_SPEED
        player_y += math.sin(player_angle) * PLAYER_SPEED
    if keys[pygame.K_s]:
        player_x -= math.cos(player_angle) * PLAYER_SPEED
        player_y -= math.sin(player_angle) * PLAYER_SPEED
    if keys[pygame.K_q]:
        player_x += math.cos(player_angle - math.pi/2) * PLAYER_SPEED
        player_y += math.sin(player_angle - math.pi/2) * PLAYER_SPEED
    if keys[pygame.K_d]:
        player_x += math.cos(player_angle + math.pi/2) * PLAYER_SPEED
        player_y += math.sin(player_angle + math.pi/2) * PLAYER_SPEED

# === Main loop ===
def game():
    pygame.mixer.music.load("./assets/sound/03. E1M1 - At Doom's Gate.mp3")
    pygame.mixer.music.set_volume(0.6)
    pygame.mixer.music.play(-1)
    
    global player_angle
    running = True
    # Créer surface plus petite pour plus de fluidité
    render_surface = pygame.Surface((SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        movement(keys)

        # Rotation
        if keys[pygame.K_LEFT]:
            player_angle -= ROT_SPEED
        if keys[pygame.K_RIGHT]:
            player_angle += ROT_SPEED

        # Dessin
        render_surface.fill(color_Ceil)  # plafond
        pygame.draw.rect(render_surface, color_Floor,
                            (0, render_surface.get_height()//2,
                            render_surface.get_width(), render_surface.get_height()//2))
        cast_rays(render_surface)

        # Étirement de la surface pour l'écran principal
        scaled_surface = pygame.transform.scale(render_surface, (SCREEN_WIDTH, SCREEN_HEIGHT))
        screen.blit(scaled_surface, (0, 0))

        pygame.display.flip()
        clock.tick(60)

game()
pygame.quit()
