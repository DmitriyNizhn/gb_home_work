from time import perf_counter

import pygame


class TrafficLight:

    def __init__(self):
        self.__red = 'red'
        self.__yellow = 'yellow'
        self.__green = 'green'

    def running(self, sec_r=7, sec_y=2, sec_g=7, cycle=1000):

        pygame.init()

        running = True
        while running:
            for i in range(sec_r, 0, -1):
                self.light(self.__red, i)
                quit_prog()
                sec(1)
            mark = 1
            while cycle != 0:
                self.light(self.__yellow)
                quit_prog()
                sec(sec_y)
                if mark:
                    for i in range(sec_g, 0, -1):
                        self.light(self.__green, i)
                        quit_prog()
                        sec(1)
                    mark = 0
                else:
                    for i in range(sec_r, 0, -1):
                        self.light(self.__red, i)
                        quit_prog()
                        sec(1)
                    mark = 1
                cycle -= 1
        pygame.quit()

    def light(self, color, i=None):
        screen = pygame.display.set_mode([500, 500])
        screen.fill((255, 255, 255))
        pygame.draw.line(screen, 'black', (250, 0), (250, 500), 150)
        pygame.draw.circle(screen, 'grey', (250, 100), 75)
        pygame.draw.circle(screen, 'grey', (250, 250), 75)
        pygame.draw.circle(screen, 'grey', (250, 400), 75)
        if color == self.__red:
            pygame.draw.circle(screen, self.__red, (250, 100), 75)
        if color == self.__yellow:
            pygame.draw.circle(screen, self.__yellow, (250, 250), 75)
        if color == self.__green:
            pygame.draw.circle(screen, self.__green, (250, 400), 75)
        if i:
            font = pygame.font.Font(None, 120)
            text = font.render(str(i), True, color)
            screen.blit(text, [230, 210])
        pygame.display.flip()


def quit_prog():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()


def sec(i):
    start_time = perf_counter()
    while perf_counter() - start_time != i:
        continue


t_l = TrafficLight()
t_l.running()
