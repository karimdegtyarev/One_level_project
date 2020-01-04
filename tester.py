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


size = width, height = 1344, 690
screen = pygame.display.set_mode(size)
fps = 60
clock = pygame.time.Clock()
wall_im = load_image('wall.png')
thorn = load_image('шип.png', -1)
door = load_image('door.png')
wall_im1 = pygame.transform.scale(wall_im, (21, 21))
thorn1 = pygame.transform.scale(thorn, (21, 21))
door1 = pygame.transform.scale(door, (30, 150))
all_sprites = pygame.sprite.Group()


def terminate():
    pygame.quit()
    sys.exit()


def load_level(filename):
    filename = "data/" + filename
    # читаем уровень, убирая символы перевода строки
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]
    for i in level_map:
        print(len(i))

    # и подсчитываем максимальную длину
    max_width = max(map(len, level_map))

    # дополняем каждую строку пустыми клетками ('.')
    return list(map(lambda x: x.ljust(max_width, '.'), level_map))


def generate_level(levelmap):
    fon = pygame.transform.scale(
        load_image('fon2.jpg'),
        (width, height))
    screen.blit(fon, (0, 0))
    sprite1 = pygame.sprite.Sprite()
    sprite1.image = door1
    sprite1.rect = sprite1.image.get_rect()
    sprite1.rect.x = 1115
    sprite1.rect.y = 540
    all_sprites.add(sprite1)
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
                all_sprites.add(sprite)
            elif levelmap[i][j] == '*':
                sprite.image = thorn1
                sprite.rect = sprite.image.get_rect()
                sprite.rect.x = y
                sprite.rect.y = x
                all_sprites.add(sprite)


def start_screen():
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

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN:
                if event.key == 9:
                    generate_level(load_level('map'))
        pygame.display.flip()
        all_sprites.update()
        all_sprites.draw(screen)
        print(all_sprites)
        clock.tick(fps)


start_screen()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminate()
    pygame.display.flip()
    clock.tick(fps)
