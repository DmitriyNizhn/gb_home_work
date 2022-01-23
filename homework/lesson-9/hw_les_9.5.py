class Stationery():
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print("\033[34m{}".format(f'{self.title} запуск отрисовки'))
        print("\033[0m{}".format(''))


class Pencil(Stationery):
    def draw(self):
        print("\033[33m{}".format(f'{self.title} запуск отрисовки'))
        print("\033[0m{}".format(''))


class Handle(Stationery):
    def draw(self):
        print("\033[1m{}".format(f'{self.title} запуск отрисовки'))
        print("\033[0m{}".format(''))


pen = Pen('Ручка')
pen.draw()
pencil = Pencil('Карандаш')
pencil.draw()
handle = Handle('Маркер')
handle.draw()
