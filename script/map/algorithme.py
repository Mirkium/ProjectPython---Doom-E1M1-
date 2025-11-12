def cast_rays():
    start_angle = player_angle - FOV/2
    for ray in range(NUM_RAYS):
        angle = start_angle + (ray / NUM_RAYS) * FOV
        for depth in range(1, MAX_DEPTH):
            target_x = player_x + math.cos(angle) * depth
            target_y = player_y + math.sin(angle) * depth

            map_x = int(target_x / TILE_SIZE)
            map_y = int(target_y / TILE_SIZE)

            if 0 <= map_x < MAP_WIDTH and 0 <= map_y < MAP_HEIGHT:
                if map_data[map_y][map_x] == 1:
                    # Calculer hauteur du mur en fonction de la distance
                    depth *= math.cos(player_angle - angle)  # corriger l’effet fish-eye
                    wall_height = 20000 / (depth + 0.0001)
                    color = 100 / (1 + depth * 0.01)
                    pygame.draw.rect(screen, (color, color, color),
                                     (ray * (SCREEN_WIDTH/NUM_RAYS),
                                        (SCREEN_HEIGHT - wall_height)//2,
                                        SCREEN_WIDTH/NUM_RAYS + 1,
                                        wall_height))
                    break
