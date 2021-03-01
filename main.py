import pygame
import random
from time import time


class Board:
    def __init__(self, width, height, mines):
        # инициализация перемен описывающие доску
        self.width = width
        self.height = height
        self.board = []
        self.time = 999
        self.playing = False
        self.won = False
        self.opened = self.width * self.height - mines
        # по умолчанию заполняем доску значениями (0,0) 0-ячейка закрыта, 1-ячейка открыта 2- на ячейке стоит флажок
        # второе число описывает количество бомб вокруг этой ячейки если > 9 то на этой ячейке бомба
        for i in range(width):
            a = []
            for j in range(height):
                a.append([0, 0])
            self.board.append(a)
        self.started = False
        self.left = 10
        self.top = 10
        self.cell_size = 30
        self.mines = mines

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        for y in range(self.height):
            for x in range(self.width):
                if self.board[x][y][0] == 0:
                    # рисуем ячейки в закрытом состояний
                    pygame.draw.rect(screen, pygame.Color(255, 255, 255), (
                        x * self.cell_size + self.left, y * self.cell_size + self.top, self.cell_size,
                        self.cell_size), 0)
                    pygame.draw.polygon(screen, pygame.Color(105, 105, 105), [
                        (x * self.cell_size + self.left, y * self.cell_size + self.top + self.cell_size),
                        (x * self.cell_size + self.left + self.cell_size,
                         y * self.cell_size + self.top + self.cell_size),
                        (x * self.cell_size + self.left + self.cell_size, y * self.cell_size + self.top)], 0)
                    pygame.draw.rect(screen, pygame.Color(169, 169, 169), (
                        x * self.cell_size + self.left + 3, y * self.cell_size + self.top + 3, self.cell_size - 6,
                        self.cell_size - 6), 0)
                if self.board[x][y][0] == 2:
                    # рисуем ячейку на которою поставили флажок
                    pygame.draw.rect(screen, pygame.Color(255, 255, 255), (
                        x * self.cell_size + self.left, y * self.cell_size + self.top, self.cell_size,
                        self.cell_size), 0)
                    pygame.draw.polygon(screen, pygame.Color(105, 105, 105), [
                        (x * self.cell_size + self.left, y * self.cell_size + self.top + self.cell_size),
                        (x * self.cell_size + self.left + self.cell_size,
                         y * self.cell_size + self.top + self.cell_size),
                        (x * self.cell_size + self.left + self.cell_size, y * self.cell_size + self.top)], 0)
                    pygame.draw.rect(screen, pygame.Color(169, 169, 169), (
                        x * self.cell_size + self.left + 3, y * self.cell_size + self.top + 3, self.cell_size - 6,
                        self.cell_size - 6), 0)
                    pygame.draw.rect(screen, pygame.Color(0, 0, 0),
                                     (x * self.cell_size + self.left + 14, y * self.cell_size + self.top + 13, 2, 8), 0)
                    pygame.draw.polygon(screen, pygame.Color(255, 0, 0),
                                        [(x * self.cell_size + self.left + 7, y * self.cell_size + self.top + 9),
                                         (x * self.cell_size + self.left + 15, y * self.cell_size + self.top + 4),
                                         (x * self.cell_size + self.left + 15, y * self.cell_size + self.top + 14)], 0)
                    pygame.draw.rect(screen, pygame.Color(0, 0, 0),
                                     (x * self.cell_size + self.left + 10, y * self.cell_size + self.top + 21, 10, 2),
                                     0)
                    pygame.draw.rect(screen, pygame.Color(0, 0, 0),
                                     (x * self.cell_size + self.left + 7, y * self.cell_size + self.top + 23, 16, 2), 0)
                if self.board[x][y][0] == 1 and self.board[x][y][1] < 9:
                    # рисуем открытую ячейку и под которой нет бомбы
                    pygame.draw.rect(screen, pygame.Color(169, 169, 169), (
                        x * self.cell_size + self.left, y * self.cell_size + self.top, self.cell_size, self.cell_size),
                                     0)
                    pygame.draw.rect(screen, pygame.Color(105, 105, 105), (
                        x * self.cell_size + self.left, y * self.cell_size + self.top, self.cell_size, self.cell_size),
                                     1)
                    # пишем внутри ячейки сколько бомб вокруг неё имеется
                    font = pygame.font.SysFont('monospace', 30, bold=True)
                    if self.board[x][y][1] == 1:
                        text = font.render('1', 1, (0, 0, 255))
                        screen.blit(text, (x * self.cell_size + self.left + 8, y * self.cell_size + self.top + 2))
                    elif self.board[x][y][1] == 2:
                        text = font.render('2', 1, (0, 255, 0))
                        screen.blit(text, (x * self.cell_size + self.left + 8, y * self.cell_size + self.top + 2))
                    elif self.board[x][y][1] == 3:
                        text = font.render('3', 1, (255, 0, 0))
                        screen.blit(text, (x * self.cell_size + self.left + 8, y * self.cell_size + self.top + 2))
                    elif self.board[x][y][1] == 4:
                        text = font.render('4', 1, (0, 0, 139))
                        screen.blit(text, (x * self.cell_size + self.left + 8, y * self.cell_size + self.top + 2))
                    elif self.board[x][y][1] == 5:
                        text = font.render('5', 1, (139, 0, 0))
                        screen.blit(text, (x * self.cell_size + self.left + 8, y * self.cell_size + self.top + 2))
                    elif self.board[x][y][1] == 6:
                        text = font.render('6', 1, (0, 128, 128))
                        screen.blit(text, (x * self.cell_size + self.left + 8, y * self.cell_size + self.top + 2))
                    elif self.board[x][y][1] == 7:
                        text = font.render('7', 1, (0, 0, 0))
                        screen.blit(text, (x * self.cell_size + self.left + 8, y * self.cell_size + self.top + 2))
                    elif self.board[x][y][1] == 8:
                        text = font.render('8', 1, (55, 55, 55))
                        screen.blit(text, (x * self.cell_size + self.left + 8, y * self.cell_size + self.top + 2))
                if self.board[x][y][0] == 1 and self.board[x][y][1] >= 9:
                    # рисуем ячейку которая открыта и под ней бомба, то есть пользователь надорвался
                    pygame.draw.rect(screen, pygame.Color(169, 169, 169), (
                        x * self.cell_size + self.left, y * self.cell_size + self.top, self.cell_size, self.cell_size),
                                     0)
                    pygame.draw.rect(screen, pygame.Color(105, 105, 105), (
                        x * self.cell_size + self.left, y * self.cell_size + self.top, self.cell_size, self.cell_size),
                                     1)
                    # рисование самой бомбочки
                    pygame.draw.circle(screen, pygame.Color(0, 0, 0),
                                       (x * self.cell_size + self.left + 15, y * self.cell_size + self.top + 15), 7)
                    pygame.draw.rect(screen, pygame.Color(0, 0, 0),
                                     (x * self.cell_size + self.left + 4, y * self.cell_size + self.top + 14, 22, 2), 0)
                    pygame.draw.rect(screen, pygame.Color(0, 0, 0),
                                     (x * self.cell_size + self.left + 14, y * self.cell_size + self.top + 4, 2, 22), 0)
                    pygame.draw.line(screen, pygame.Color(0, 0, 0),
                                     (x * self.cell_size + self.left + 6, y * self.cell_size + self.top + 6),
                                     (x * self.cell_size + self.left + 22, y * self.cell_size + self.top + 22), 2)
                    pygame.draw.line(screen, pygame.Color(0, 0, 0),
                                     (x * self.cell_size + self.left + 6, y * self.cell_size + self.top + 22),
                                     (x * self.cell_size + self.left + 22, y * self.cell_size + self.top + 6), 2)
                    pygame.draw.rect(screen, pygame.Color(255, 255, 255),
                                     (x * self.cell_size + self.left + 11, y * self.cell_size + self.top + 11, 3, 3), 0)

    def get_cell(self, mouse_pos):
        # возвращает координаты нажатой ячейки, если вне доски то None
        x, y = mouse_pos
        x -= self.left
        y -= self.top
        if x // self.cell_size < self.width and y // self.cell_size < self.height \
                and y // self.cell_size >= 0 and x // self.cell_size >= 0:
            return x // self.cell_size, y // self.cell_size

    def get_click(self, mouse_pos, button):
        cell = self.get_cell(mouse_pos)
        if button == 1:  # если была нажата левая кнопка мыши
            self.on_click(cell)
        elif button == 3:  # если была нажата правая кнопка мыши
            self.on_right_click(cell)

    def on_click(self, cell):
        if cell != None:
            x, y = cell
            if self.board[x][y][0] == 0:  # если текущая нажатая ячейка закрыта
                if not self.started:  # если это первая ячейка которая нажата за игру
                    self.placemines(cell)  # рандомно генерирует куда положить бомбы
                    self.started = True
                    self.inittime = time()  # фиксируем время когда первая ячейка была нажата, то есть
                    # когда игра началась
                    self.playing = True

                self.board[x][y][0] = 1  # открываем ячейку
                self.opened -= 1  # количество оставшихся не открытых ячеек
                if self.board[x][y][1] >= 9:  # если под нажатой ячейкой бомба
                    # абсолютно все ячейки на доске открываются и игра заканчивается
                    for i in range(self.width):
                        for j in range(self.height):
                            self.board[i][j][0] = 1
                    self.time = int(time() - self.inittime)  # фиксация времени когда игра закончилась
                    self.playing = False
                if self.board[x][y][1] == 0:  # если вокруг открытой ячейки 0 бомб автоматически открываются все
                    # соседние ячейки
                    self.open_neighbors((x, y))
            if self.mines == 0 and self.opened == 0 and not self.won:
                self.time = int(time() - self.inittime)
                self.playing = False
                self.won = True

    def open_neighbors(self, cell):  # открывает ячейки вокруг безопасных ячеек по рекурсий
        x, y = cell
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == j and i == 0:
                    continue
                if x + i >= 0 and x + i < self.width and y + j >= 0 and y + j < self.height:
                    if self.board[x + i][y + j][0] == 0:
                        self.board[x + i][j + y][0] = 1
                        self.opened -= 1
                        if self.board[x + i][j + y][1] == 0:
                            self.open_neighbors((x + i, y + j))

    def on_right_click(self, cell):
        if cell != None:
            x, y = cell
            if self.board[x][y][0] == 2:  # если право-нажатая ячейка уже с флагом, то флаг наоборот, убирается
                self.board[x][y][0] = 0
                self.mines += 1
            elif self.board[x][y][0] == 0:  # а если он закрыт, то на него ставится флаг
                self.board[x][y][0] = 2
                self.mines -= 1
            if self.mines == 0 and self.opened == 0 and not self.won:  # проверяем если игра была успешно закончена
                self.time = int(time() - self.inittime)  # фиксируем время при выигрыше
                self.playing = False
                self.won = True

    def placemines(self, cell):  # рандомно генерирует бомбы
        x, y = cell
        a = list(range(0, self.height * self.width))  # список от 0 до width*height(всё количество ячеек)
        a.remove(y * self.width + x)  # первая нажатая ячейка не может быть бомбой, поэтому убираем из списка
        mines = random.sample(a, k=self.mines)  # создание неповторимых рандомных чисел
        for i in mines:
            curcell = i % self.width, i // self.width
            cx, cy = curcell
            self.board[cx][cy] = [0, 9]  # изменяем список с указанием что эта ячейка бомба
            # увеличиваем число соседних бомб для каждой ячейку вокруг бомбы на +1
            for j in range(-1, 2):
                for k in range(-1, 2):
                    if j == k and j == 0:
                        continue
                    if cx + j < self.width and cx + j > -1 and cy + k < self.height and cy + k > -1:
                        self.board[cx + j][cy + k][1] += 1


# класс симулирующий кнопку
class button():
    def __init__(self, color, x, y, width, height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.chosen = False

    def draw(self, win, outline=None):
        # метод для демонстраций кнопки на экране
        if outline:
            pygame.draw.rect(win, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 2)

        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 2)
        if self.chosen:  # если эта кнопка с уровнем сложности выбрана то рядом рисуется круг
            pygame.draw.circle(win, (255, 255, 255), (self.x + self.width - 17, self.y + self.height - 15), 10, 0)
            pygame.draw.circle
        if self.text != '':
            font = pygame.font.SysFont('monospace', 20)
            text = font.render(self.text, 1, (255, 255, 255))
            win.blit(text,
                     (self.x + 2,
                      self.y + 2))

    def isOver(self, pos):
        # возвращает значение если кнопка была нажата
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True

        return False


def main():
    pygame.init()
    size = 350, 400
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Инициализация игры')
    myfont = pygame.font.SysFont("monospace", 20)
    opt = "easy"
    board = Board(0, 0, 10)
    board.set_view(200, 200, 30)
    running = True
    # создание кнопок для интерфэйса
    easy = button((255, 255, 255), 10, 50, 320, 30, "Easy 9x9 / 10 mines")
    easy.chosen = True
    normal = button((255, 255, 255), 10, 85, 320, 30, "Normal 16x16 / 40 mines")
    hard = button((255, 255, 255), 10, 120, 320, 30, "Hard 16x30 / 99 mines")
    play = button((255, 255, 255), 140, 155, 60, 30, "PLAY")
    while running:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # если была нажата левая кнопка мыши
                board.get_click(event.pos, 1)
                board.render(screen)
                # какая сложнасть выбрана
                if easy.isOver(event.pos):
                    easy.chosen = True
                    normal.chosen = False
                    hard.chosen = False
                    opt = 'easy'
                elif normal.isOver(event.pos):
                    normal.chosen = True
                    easy.chosen = False
                    hard.chosen = False
                    opt = 'normal'

                elif hard.isOver(event.pos):
                    hard.chosen = True
                    easy.chosen = False
                    normal.chosen = False
                    opt = 'hard'
                elif play.isOver(event.pos):  # если нажата кнопка play
                    if opt == 'easy':
                        # инициализация игры
                        screen = pygame.display.set_mode((350, 500))
                        board = Board(9, 9, 10)
                        board.set_view(40, 200, 30)


                    elif opt == 'normal':
                        board = Board(16, 16, 40)
                        screen = pygame.display.set_mode((550, 700))
                        board.set_view(40, 200, 30)

                    elif opt == 'hard':
                        board = Board(30, 16, 99)
                        screen = pygame.display.set_mode((1000, 700))
                        board.set_view(40, 200, 30)

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:  # если была нажата правая кнопка мыши
                board.get_click(event.pos, 3)
                board.render(screen)

        pygame.draw.rect(screen, (255, 255, 255), (70, 155, 70, 30), 2)
        font = pygame.font.SysFont('monospace', 20)
        # поле где выводится число оставшихся мин
        if board.mines<0:
            mn=0
        else:
            mn=board.mines
        textmine = font.render(str(mn), 1, (255, 255, 255))
        screen.blit(textmine, (72, 157))
        pygame.draw.rect(screen, (255, 255, 255), (200, 155, 70, 30), 2)

        # расчет времени в зависимости от состояния игры
        if board.started and board.playing:
            texttime = font.render(str(int(time() - board.inittime)), 1, (255, 255, 255))
        elif board.started and not board.playing:
            texttime = font.render(str(board.time), 1, (255, 255, 255))
        else:
            texttime = font.render(str(board.time), 1, (255, 255, 255))
        screen.blit(texttime, (202, 157))  # вывод прошедшего времени в секундах
        board.render(screen)
        if board.won:  # если пользователь выиграл
            width, height = screen.get_size()
            # рисуется золотой прямоугольник с надписью YOU WON
            pygame.draw.rect(screen, pygame.Color(255, 215, 0),
                             (width // 2 - 120, 170 + (height - 170) // 2 - 45, 240, 90))
            fontwin = pygame.font.SysFont('monospace', 45, bold=True)
            textwin = fontwin.render("YOU WON", 1, (pygame.Color(255, 255, 255)))
            screen.blit(textwin, (width // 2 - 110, 170 + (height - 170) // 2 - 25))
        # вывод на экрна всех кнопок интерфэйса
        textdif = myfont.render("Difficulty", 1, (255, 255, 255))
        screen.blit(textdif, (10, 10))
        easy.draw(screen)
        normal.draw(screen)
        hard.draw(screen)
        play.draw(screen)
        pygame.display.update()
    pygame.quit()


if __name__ == '__main__':
    main()
