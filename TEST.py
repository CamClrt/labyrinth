def move(event):
    #move the hero's position
    if event.type == KEYDOWN:
        if event.key == K_LEFT:
            res = "Gauche"
        if event.key == K_RIGHT:
            res = "Droite"
        if event.key == K_UP:
            res = "Haut"
        if event.key == K_DOWN:
            res = "Bas"
    return res

#quit the window
dead = False
while(dead == False):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            dead = True