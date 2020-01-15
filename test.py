import pygame
import sys
import os


def terminate():
    pygame.quit()
    sys.exit()


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


def load_level(filename):
    filename = "data/" + filename
    # читаем уровень, убирая символы перевода строки
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]
    # и подсчитываем максимальную длину
    max_width = max(map(len, level_map))

    # дополняем каждую строку пустыми клетками ('.')
    return list(map(lambda x: x.ljust(max_width, '.'), level_map))


def generate_level(levelmap):
    first_player, x, y = None, None, None
    fon = pygame.transform.scale(
        load_image('fon2.jpg'),
        (width, height))
    screen.blit(fon, (0, 0))
    for y in range(len(levelmap)):
        for x in range(len(levelmap[y])):
            if levelmap[y][x] == '.':
                Tile('wall', x, y)
            elif levelmap[y][x] == '*':
                Tile('thorn', x, y)
    Tile('door', 49, 26)
    first_player = Player(5, 13)
    key = Key(52, 6)
    return first_player, x, y


class Key(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(key_group, all_sprites)
        self.image = key_image
        self.type = "key"
        self.rect = self.image.get_rect().move(
            tile_width * pos_x + 15, tile_height * pos_y + 5)


class Door:
    pass


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(tiles_group, all_sprites)
        self.image = tile_images[tile_type]
        self.type = tile_type
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(player_group, all_sprites)
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.image = player_image
        self.type = "player"
        self.rect = self.image.get_rect().move(
            tile_width * pos_x + 15, tile_height * pos_y + 5)

    def update(self):
        if move_1 == "Up":
            # player.image = walkUp
            player.move(0, -step)
        if move_1 == "Right":
            # player.image = walkRight
            player.move(+step, 0)
        if move_1 == "Left":
            # player.image = walkLeft
            player.move(-step, 0)

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy
        test = pygame.sprite.spritecollide(self, tiles_group, False)
        #        if len(test) == 0:
        #            self.gravity()
        for obj in test:
            if obj.type == "wall" or obj.type == "door":
                self.rect.x -= dx
                self.rect.y -= dy
                break

        test = pygame.sprite.spritecollide(self, tiles_group, False)
        for obj in test:
            if obj.type == "thorn":
                self.rect.x = tile_width * self.pos_x + 15
                self.rect.y = tile_height * self.pos_y + 5
                break


#    def gravity(self):
#        self.rect.y += step


def start_screen():
    global tiles_group
    global all_sprites
    global player_group
    global key_group
    global freeze
    global stop
    global player
    global move_1
    global move_2
    all_sprites = pygame.sprite.Group()
    tiles_group = pygame.sprite.Group()
    player_group = pygame.sprite.Group()
    key_group = pygame.sprite.Group()
    fon = pygame.transform.scale(
        load_image('one.jpg'),
        (width, height))
    fon1 = pygame.transform.scale(
        load_image('fon2.jpg'),
        (width, height))
    move_1 = "Stop"
    move_2 = "Stop"
    freeze = 0
    player, level_x, level_y = generate_level(load_level('map'))
    running = True
    while running:
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN and event.key == 9:
                    stop = 0
                if event.type == pygame.KEYDOWN and event.key == 32:
                    freeze = (freeze + 1) % 2
                if freeze == 0 and stop == 0:
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                        move_1 = "Left"
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                        move_1 = "Right"
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                        move_1 = "Up"

                    if event.type == pygame.KEYUP and event.key == pygame.K_LEFT and move_1 == "Left":
                        move_1 = "Stop"
                    if event.type == pygame.KEYUP and event.key == pygame.K_RIGHT and move_1 == "Right":
                        move_1 = "Stop"
                    if event.type == pygame.KEYUP and event.key == pygame.K_UP and move_1 == "Up":
                        move_1 = "Stop"

                    if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
                        move_1 = "Left"
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
                        move_1 = "Right"
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
                        move_1 = "Up"

                    if event.type == pygame.KEYUP and event.key == pygame.K_a and move_2 == "Left":
                        move_1 = "Stop"
                    if event.type == pygame.KEYUP and event.key == pygame.K_d and move_2 == "Right":
                        move_1 = "Stop"
                    if event.type == pygame.KEYUP and event.key == pygame.K_w and move_2 == "Up":
                        move_1 = "Stop"
            if stop == 1:
                screen.blit(fon, (0, 0))
                pygame.display.flip()
            if freeze == 0 and stop == 0:
                player.update()
                screen.fill((0, 0, 0))
                screen.blit(fon1, (0, 0))
                tiles_group.draw(screen)
                key_group.draw(screen)
                player_group.draw(screen)
                pygame.display.flip()


size = width, height = 1260, 690
screen = pygame.display.set_mode(size)
pygame.display.set_caption("One Level")
clock = pygame.time.Clock()
step = 3
stop = 1
v = 200
fps = 100
wall_image = load_image('wall.png')
thorn_image = load_image('шип.png', -1)
player_image = pygame.transform.scale(load_image("стикмен-стоит.png", -1), (28, 57))
key_image = pygame.transform.scale(load_image('ключ1.png', -1), (40, 44))
tile_images = {"wall": load_image("wall.png"),
               "thorn": load_image("шип.png", -1),
               "door": pygame.transform.scale(load_image("door.png"), (30, 150))}
tile_width = tile_height = 21
if __name__ == "__main__":
    start_screen()
