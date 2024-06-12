import pygame

pygame.font.init()
Window = pygame.display.set_mode((700, 700))
pygame.display.set_caption("SUDOKU GAME")
x, z = 0, 0
diff = 700 // 9  
value = 0
defaultgrid = [
    [0, 0, 2, 0, 5, 3, 0, 9, 0],
    [0, 7, 0, 0, 0, 0, 8, 1, 0],
    [0, 4, 0, 6, 0, 0, 0, 7, 5],
    [5, 0, 0, 0, 0, 0, 9, 0, 2],
    [0, 3, 7, 0, 6, 0, 0, 0, 0],
    [0, 0, 6, 1, 0, 8, 0, 0, 0],
    [0, 0, 8, 9, 0, 0, 4, 3, 0],
    [0, 0, 0, 4, 0, 0, 7, 0, 0],
    [1, 6, 0, 2, 0, 0, 0, 0, 0],
]

original_grid = [row[:] for row in defaultgrid]

font = pygame.font.SysFont("comicsans", 40)
font1 = pygame.font.SysFont("comicsans", 20)

def cord(pos):
    global x, z
    x = int(pos[0] // diff)
    z = int(pos[1] // diff)

def highlightbox():
    for k in range(2):
        pygame.draw.line(Window, (0, 0, 0), (x * diff - 3, (z + k) * diff), (x * diff + diff + 3, (z + k) * diff), 7)
        pygame.draw.line(Window, (0, 0, 0), ((x + k) * diff, z * diff), ((x + k) * diff, z * diff + diff), 7)

def drawlines():
    for i in range(9):
        for j in range(9):
            if defaultgrid[i][j] != 0:
                pygame.draw.rect(Window, (255, 255, 0), (j * diff, i * diff, diff + 1, diff + 1))
                text1 = font.render(str(defaultgrid[i][j]), 1, (0, 0, 0))
                Window.blit(text1, (j * diff + 15, i * diff + 15))
    for l in range(10):
        thick = 7 if l % 3 == 0 else 1
        pygame.draw.line(Window, (0, 0, 0), (0, l * diff), (700, l * diff), thick)
        pygame.draw.line(Window, (0, 0, 0), (l * diff, 0), (l * diff, 700), thick)

def fillvalue(value):
    text1 = font.render(str(value), 1, (0, 0, 0))
    Window.blit(text1, (x * diff + 15, z * diff + 15))

def raiseerror():
    text1 = font.render("Wrong!", 1, (0, 0, 0))  
    Window.blit(text1, (300, 300)) 
    pygame.display.update() 
    pygame.time.delay(1300)  

    Window.fill((255, 182, 193))  
    drawlines() 
    if flag1 == 1:  
        highlightbox()
    pygame.display.update()

def validvalue(m, k, l, value):
    for it in range(9):
        if m[k][it] == value or m[it][l] == value:
            return False
    it = k // 3
    jt = l // 3
    for i in range(it * 3, it * 3 + 3):
        for j in range(jt * 3, jt * 3 + 3):
            if m[i][j] == value:
                return False
    return True

def solvegame(defaultgrid, i, j):
    while defaultgrid[i][j] != 0:
        if i < 8:
            i += 1
        elif i == 8 and j < 8:
            i = 0
            j += 1
        elif i == 8 and j == 8:
            return True
    pygame.event.pump()
    for it in range(1, 10):
        if validvalue(defaultgrid, i, j, it):
            defaultgrid[i][j] = it
            global x, z
            x, z = j, i
            Window.fill((255, 255, 255))
            drawlines()
            highlightbox()
            pygame.display.update()
            pygame.time.delay(20)
            if solvegame(defaultgrid, i, j):
                return True
            defaultgrid[i][j] = 0
            Window.fill((255, 255, 255))
            drawlines()
            highlightbox()
            pygame.display.update()
            pygame.time.delay(50)
    return False

def gameresult():
    text1 = font.render("Game finished", 1, (0, 0, 0))
    Window.blit(text1, (20, 700 - 30))
    
flag = True
flag1 = 0
flag2 = 0
rs = 0
error = 0

while flag:
    Window.fill((255, 182, 193))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            flag1 = 1
            pos = pygame.mouse.get_pos()
            cord(pos)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x = max(0, x - 1)
                flag1 = 1
            if event.key == pygame.K_RIGHT:
                x = min(8, x + 1)
                flag1 = 1
            if event.key == pygame.K_UP:
                z = max(0, z - 1)
                flag1 = 1
            if event.key == pygame.K_DOWN:
                z = min(8, z + 1)
                flag1 = 1
            if event.key in [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9]:
                if original_grid[z][x] == 0:
                    value = int(event.unicode)
            if event.key == pygame.K_RETURN:
                flag2 = 1
            if event.key == pygame.K_r:
                rs = 0
                error = 0
                flag2 = 0
                defaultgrid = [row[:] for row in original_grid]
            if event.key == pygame.K_d:
                rs = 0
                error = 0
                flag2 = 0
                defaultgrid = [
                    [0, 0, 2, 0, 5, 3, 0, 9, 0],
                    [0, 7, 0, 0, 0, 0, 8, 1, 0],
                    [0, 4, 0, 6, 0, 0, 0, 7, 5],
                    [5, 0, 0, 0, 0, 0, 9, 0, 2],
                    [0, 3, 7, 0, 6, 0, 0, 0, 0],
                    [0, 0, 6, 1, 0, 8, 0, 0, 0],
                    [0, 0, 8, 9, 0, 0, 4, 3, 0],
                    [0, 0, 0, 4, 0, 0, 7, 0, 0],
                    [1, 6, 0, 2, 0, 0, 0, 0, 0],
                ]
                original_grid = [row[:] for row in defaultgrid]
    if flag2 == 1:
        if not solvegame(defaultgrid, 0, 0):
            error = 1
        else:
            rs = 1
        flag2 = 0
    if value != 0:
        if validvalue(defaultgrid, int(z), int(x), value):
            defaultgrid[int(z)][int(x)] = value
            flag1 = 0
        else:
            raiseerror()
        value = 0
    if error == 1:
        raiseerror()
    if rs == 1:
        gameresult()
    drawlines()
    if flag1 == 1:
        highlightbox()
    pygame.display.update()

pygame.quit()