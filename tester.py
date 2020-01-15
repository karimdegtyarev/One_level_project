import pygame
import sys
import os


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname).convert()
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = stikmen
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 273

    def update(self):
        global height
        global flag1
        global karta
        if flag1 != 0:
            if len(pygame.sprite.spritecollide(self, walls, False)) >= 0:
                if len(pygame.sprite.spritecollide(self, thorns, False)) == 0:
                    if flag1 == 'a':
                        self.rect.x -= v / fps
                    elif flag1 == 'd':
                        self.rect.x += v / fps
                    elif flag1 == 'w':
                        for i in range(70):
                            if len(pygame.sprite.spritecollide(self, thorns, False)) == 0:
                                if len(pygame.sprite.spritecollide(self, walls,
                                                                   False)) >= 0 and \
                                        karta[self.rect.y // 21][self.rect.x // 21] != '.':
                                    print(karta[self.rect.y // 21][self.rect.x // 21])
                                    for event in pygame.event.get():
                                        if event.type == pygame.KEYDOWN:
                                            if event.key == pygame.K_LEFT:
                                                flag1 = 'a'
                                            elif event.key == pygame.K_RIGHT:
                                                flag1 = 'd'
                                        elif event.type == pygame.KEYUP:
                                            flag1 = 0
                                    if flag1 != 0:
                                        if flag1 == 'a':
                                            if karta[self.rect.y // 21][self.rect.x // 21] != '.':
                                                self.rect.x -= v / fps
                                        elif flag1 == 'd':
                                            if karta[self.rect.y // 21][
                                                self.rect.x // 21 + 1] != '.':
                                                self.rect.x += v / fps
                                    self.rect.y -= 3
                                    clock.tick(fps * 0.9)
                                    screen.fill((0, 0, 0))
                                    screen.blit(fon1, (0, 0))
                                    walls.draw(screen)
                                    thorns.draw(screen)
                                    player.update()
                                    player.draw(screen)
                                    pygame.display.flip()
                                else:
                                    self.rect.y += 3
                                    break
                            else:
                                generate_level(load_level('map'))
                                self.rect.x = 100
                                self.rect.y = 273
                                player.add(self)
                                player.update()
                                player.draw(screen)
                                flag1 = 0
                                break
                        while self.rect.y <= height - 65 and len(
                                pygame.sprite.spritecollide(self, walls, False)) == 0:
                            if len(pygame.sprite.spritecollide(self, thorns, False)) == 0:
                                for event in pygame.event.get():
                                    if event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_LEFT:
                                            flag1 = 'a'
                                        elif event.key == pygame.K_RIGHT:
                                            flag1 = 'd'
                                    elif event.type == pygame.KEYUP:
                                        flag1 = 0
                                if flag1 != 0:
                                    if flag1 == 'a':
                                        if karta[self.rect.y // 21][self.rect.x // 21] != '.':
                                            self.rect.x -= v / fps
                                    elif flag1 == 'd':
                                        if karta[self.rect.y // 21][self.rect.x // 21 + 1] != '.':
                                            self.rect.x += v / fps
                                self.rect.y += 3
                                clock.tick(fps * 0.9)
                                screen.fill((0, 0, 0))
                                screen.blit(fon1, (0, 0))
                                walls.draw(screen)
                                thorns.draw(screen)
                                player.update()
                                player.draw(screen)
                                pygame.display.flip()
                            else:
                                print('ok')
                                generate_level(load_level('map'))
                                self.rect.x = 100
                                self.rect.y = 273
                                player.add(self)
                                player.update()
                                player.draw(screen)
                                break
                else:
                    generate_level(load_level('map'))
                    self.rect.x = 100
                    self.rect.y = 273
                    player.add(self)
                    player.update()
                    player.draw(screen)

    def gravity(self):
        global flag1
        global flag2
        while self.rect.y <= height - 65 and len(
                pygame.sprite.spritecollide(self, walls, False)) == 0:
            if flag2 == 1:
                break
            if len(pygame.sprite.spritecollide(self, thorns, False)) == 0:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT:
                            flag1 = 'a'
                        elif event.key == pygame.K_RIGHT:
                            flag1 = 'd'
                    elif event.type == pygame.KEYUP:
                        flag1 = 0
                if flag1 != 0:
                    if flag1 == 'a':
                        if karta[self.rect.y // 21][self.rect.x // 21] != '.':
                            self.rect.x -= v / fps
                    elif flag1 == 'd':
                        if karta[self.rect.y // 21][self.rect.x // 21 + 1] != '.':
                            self.rect.x += v / fps
                self.rect.y += 3
                clock.tick(fps * 0.9)
                screen.fill((0, 0, 0))
                screen.blit(fon1, (0, 0))
                walls.draw(screen)
                thorns.draw(screen)
                player.update()
                player.draw(screen)
                pygame.display.flip()
            else:
                generate_level(load_level('map'))
                self.rect.x = 100
                self.rect.y = 273
                player.add(self)
                player.update()
                player.draw(screen)
                #                flag2 = 1
                break


flag2 = 0
size = width, height = 1264, 690
screen = pygame.display.set_mode(size)
pygame.display.set_caption("One Level")
v = 150
fps = 100
clock = pygame.time.Clock()
wall_im = load_image('wall.png')
thorn = load_image('шип.png', -1)
stikmen = load_image('стикмен-стоит.png', -1)
door = load_image('door.png')
key = load_image('ключ.png', -1)
wall_im1 = pygame.transform.scale(wall_im, (21, 21))
thorn1 = pygame.transform.scale(thorn, (21, 21))
door1 = pygame.transform.scale(door, (30, 150))
walls = pygame.sprite.Group()
player = pygame.sprite.Group()
thorns = pygame.sprite.Group()
player1 = Player()
player.add(player1)
flag1 = 0


def terminate():
    pygame.quit()
    sys.exit()


def load_level(filename):
    filename = "data/" + filename
    # читаем уровень, убирая символы перевода строки
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]
    # и подсчитываем максимальную длину
    max_width = max(map(len, level_map))

    # дополняем каждую строку пустыми клетками ('.')
    return list(map(lambda x: x.ljust(max_width, '.'), level_map))


karta = load_level('map')


def generate_level(levelmap):
    global fon1
    fon1 = pygame.transform.scale(
        load_image('fon2.jpg'),
        (width, height))
    screen.blit(fon1, (0, 0))
    sprite1 = pygame.sprite.Sprite()
    sprite1.image = door1
    sprite1.rect = sprite1.image.get_rect()
    sprite1.rect.x = 1035
    sprite1.rect.y = 540
    walls.add(sprite1)
    pygame.init()
    x = -21
    y = -21
    for i in range(len(levelmap)):
        x += 21
        y = -21
        for j in range(len(levelmap[i])):
            y += 21
            sprite = pygame.sprite.Sprite()
            if levelmap[i][j] == '.':
                sprite.image = wall_im1
                sprite.rect = sprite.image.get_rect()
                sprite.rect.x = y
                sprite.rect.y = x
                walls.add(sprite)
            elif levelmap[i][j] == '*':
                sprite.image = thorn1
                sprite.rect = sprite.image.get_rect()
                sprite.rect.x = y
                sprite.rect.y = x
                thorns.add(sprite)


# def stikmen_movement(direction):


def start_screen():
    global flag1
    global karta
    intro_text = ["Press 'tab' to start"]

    fon = pygame.transform.scale(
        load_image('one.jpg'),
        (width, height))
    screen.blit(fon, (0, 0))
    pygame.init()
    font = pygame.font.Font(None, 50)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1,
                                      pygame.Color('grey'))
        intro_rect = string_rendered.get_rect()
        text_coord += 570
        intro_rect.top = text_coord
        intro_rect.x = 500
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)
    flag = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN:
                if event.key == 9 and flag == 0:
                    generate_level(load_level('map'))
                    flag = 1
                if event.key == pygame.K_LEFT:
                    flag1 = 'a'
                elif event.key == pygame.K_RIGHT:
                    flag1 = 'd'
                elif event.key == 32:
                    if flag == 1:
                        flag1 = 'w'
                        player.update()
            elif event.type == pygame.KEYUP:
                flag1 = 0
        if flag1 == 'a':
            if karta[player1.rect.y // 21][player1.rect.x // 21] != '.':
                player.update()
        elif flag1 == 'd':
            if karta[player1.rect.y // 21][player1.rect.x // 21 + 1] != '.':
                player.update()
            else:
                print('ok')
                if len(pygame.sprite.spritecollide(player1, walls, False)) <= 1:
                    player.update()
        pygame.display.flip()
        walls.draw(screen)
        thorns.draw(screen)
        if flag == 1:
            screen.fill((0, 0, 0))
            screen.blit(fon1, (0, 0))
            walls.draw(screen)
            thorns.draw(screen)
            # player.add(player1)
            # player.update()
            player.draw(screen)
            if len(pygame.sprite.spritecollide(player1, walls, False)) == 0:
                player1.gravity()
        clock.tick(fps)


start_screen()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminate()
    pygame.display.flip()
    clock.tick(fps)
