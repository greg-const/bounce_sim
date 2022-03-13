import pygame as pg
import pygame.gfxdraw as gfx
from vec2d import vec2d as vec
from random import randint


class Game:
    def __init__(self):
        self.disp_h = 1000
        self.disp_w = 1300
        self.fps = 60
        self.surface = pg.display.set_mode((self.disp_w, self.disp_h))
        self.clock = pg.time.Clock()
        self.windowname = pg.display.set_caption("Peaceful, happy window")
        self.initialv = vec(-3, -16)
        self.r = 20
        self.path = 1
        self.dots = []
        self.loop()

    def loop(self):
        pos = vec(self.disp_w * 8/9, self.disp_h/2)
        v = self.initialv
        a = vec(0, .5)
        while True:
            self.clock.tick(self.fps)
            self.events()
            self.surface.fill((0, 0, 0))

            pos = pos.add(v)

            if pos.y + v.y + self.r > self.disp_h or pos.y + v.y - self.r <= 0:
                v.y *= -1
                print(v.y)
            else:
                v.y += a.y
            if pos.x + v.x + self.r >= self.disp_w or pos.x + v.x - self.r <= 0:
                v.x *= -1
            else:
                v.x += a.x

            if abs(pos.y + self.r - self.disp_h) < 10:
                v.x *= 1

            self.displayball(pos.x, pos.y)

            pg.display.update()

    def bounce(self, pos):
        return

    def displayball(self, x, y):
        pg.gfxdraw.aacircle(self.surface, int(x), int(y), self.r, (255, 255, 100))
        pg.gfxdraw.filled_circle(self.surface, int(x), int(y), self.r, (255, 255, 100))
        if self.path:
            self.dots.append((x, y))
            for dot in self.dots:
                pg.gfxdraw.aacircle(self.surface, int(dot[0]), int(dot[1]), 2, (255, 255, 255))

    @staticmethod
    def events():
        for event in pg.event.get():
            if event.type == pg.QUIT:
                quit()
            if event.type == pg.KEYDOWN:
                pass


game = Game()
