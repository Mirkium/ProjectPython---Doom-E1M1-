
    global player_x, player_y, player_angle
    dx, dy = 0, 0

    # Avancer / Reculer
    if keys[pygame.K_z]:
        dx += math.cos(player_angle) * PLAYER_SPEED
        dy += math.sin(player_angle) * PLAYER_SPEED
    if keys[pygame.K_s]:
        dx -= math.cos(player_angle) * PLAYER_SPEED
        dy -= math.sin(player_angle) * PLAYER_SPEED

    # Strafe gauche / droite
    if keys[pygame.K_q]:
        dx += math.cos(player_angle - math.pi/2) * PLAYER_SPEED
        dy += math.sin(player_angle - math.pi/2) * PLAYER_SPEED
    if keys[pygame.K_d]:
        dx += math.cos(player_angle + math.pi/2) * PLAYER_SPEED
        dy += math.sin(player_angle + math.pi/2) * PLAYER_SPEED

    # Collision simple avec les murs
    new_x = player_x + dx
    new_y = player_y + dy
    if map_data[int(player_y / TILE_SIZE)][int(new_x / TILE_SIZE)] == 0:
        player_x = new_x
    if map_data[int(new_y / TILE_SIZE)][int(player_x / TILE_SIZE)] == 0:
        player_y = new_y