import pygame
import pygame_gui
import time

pygame.init()

white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
gray = (60, 60, 60)
blue = (0, 0, 255)
green = (0, 255, 0)
yellow = (255,255,0)
purple = (138,43,226)
orange = (255,165,0)
pink = (255,105,180)
dis_width = 800
dis_height = 800
dis = pygame.display.set_mode((dis_width, dis_height), pygame.RESIZABLE)
pygame.display.set_caption("Blair Tac Toe by Mike Wolski")
clock = pygame.time.Clock()

manager = pygame_gui.UIManager((dis_width, dis_height))

xc = red
cc = blue

def startscreen(xc, cc):
    dis_width = dis.get_width()
    dis_height = dis.get_height()
    manager.clear_and_reset()
    manager.set_window_resolution((dis_width, dis_height))
    so = (dis_width + dis_height)/80
    title_font = pygame.font.SysFont("bahnschrift", int(so*4))
    font_style = pygame.font.SysFont("bahnschrift", int(so*2))
    dis.fill(gray)
    rad = dis_width
    if dis_width > dis_height:
        rad = dis_height

    def message(msg,color, x, y):
        mesg = font_style.render(msg, True, color)
        dis.blit(mesg, [(dis_width-mesg.get_rect().width)/2, y])
    
    def title(msg,color, y):
        mesg = title_font.render(msg, True, color)
        dis.blit(mesg, [(dis_width-mesg.get_rect().width)/2, y])

    def circle(color):
        pygame.draw.circle(dis, color, [dis_width*3/4, dis_height*1/3], rad/9, int(so))
        pygame.display.update()

    def ex(color):
        pygame.draw.line(dis, color, [dis_width*1/6, dis_height*1/4], [dis_width*1/3, dis_height*7/16], int(so))
        pygame.draw.line(dis, color, [dis_width*1/6, dis_height*7/16], [dis_width*1/3, dis_height*1/4], int(so))
        pygame.display.update()

    start_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((dis_width*1/2-so*5, dis_height*1/3), (so*10, so*2)), text="Start", manager=manager)

    ex(xc)
    red_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((dis_width*1/4-so*5, dis_height*1/2), (so*10, so*2)), text="Red", manager=manager)
    green_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((dis_width*1/4-so*5, dis_height*1/2+so*2), (so*10, so*2)), text="Green", manager=manager)
    blue_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((dis_width*1/4-so*5, dis_height*1/2+so*4), (so*10, so*2)), text="Blue", manager=manager)
    yellow_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((dis_width*1/4-so*5, dis_height*1/2+so*6), (so*10, so*2)), text="Yellow", manager=manager)
    purple_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((dis_width*1/4-so*5, dis_height*1/2+so*8), (so*10, so*2)), text="Purple", manager=manager)
    orange_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((dis_width*1/4-so*5, dis_height*1/2+so*10), (so*10, so*2)), text="Orange", manager=manager)
    pink_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((dis_width*1/4-so*5, dis_height*1/2+so*12), (so*10, so*2)), text="Pink", manager=manager)

    circle(cc)
    red_buttono = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((dis_width*3/4-so*5, dis_height*1/2), (so*10, so*2)), text="Red", manager=manager)
    green_buttono = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((dis_width*3/4-so*5, dis_height*1/2+so*2), (so*10, so*2)), text="Green", manager=manager)
    blue_buttono = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((dis_width*3/4-so*5, dis_height*1/2+so*4), (so*10, so*2)), text="Blue", manager=manager)
    yellow_buttono = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((dis_width*3/4-so*5, dis_height*1/2+so*6), (so*10, so*2)), text="Yellow", manager=manager)
    purple_buttono = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((dis_width*3/4-so*5, dis_height*1/2+so*8), (so*10, so*2)), text="Purple", manager=manager)
    orange_buttono = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((dis_width*3/4-so*5, dis_height*1/2+so*10), (so*10, so*2)), text="Orange", manager=manager)
    pink_buttono = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((dis_width*3/4-so*5, dis_height*1/2+so*12), (so*10, so*2)), text="Pink", manager=manager)
    
    while True:
        time_delta = clock.tick(60)/1000.0
        title("BLAIR-TAC-TOE", white, 0)
        manager.draw_ui(dis)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.VIDEORESIZE:
                dis_height = dis.get_height()
                dis_width = dis.get_width()
                rad = dis_width
                if dis_width > dis_height:
                    rad = dis_height
                so = (dis_width + dis_height)/80
                title_font = pygame.font.SysFont("bahnschrift", int(so*4))
                font_style = pygame.font.SysFont("bahnschrift", int(so*2))
                dis.fill(gray)
                manager.clear_and_reset()
                manager.set_window_resolution((dis_width, dis_height))
                title("TicTacToe", white, 0)
                start_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((dis_width*1/2-so*5, dis_height*1/3), (so*10, so*2)), text="Start", manager=manager)
                so = (dis_width + dis_height)/80
                ex(xc)
                red_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((dis_width*1/4-so*5, dis_height*1/2), (so*10, so*2)), text="Red", manager=manager)
                green_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((dis_width*1/4-so*5, dis_height*1/2+so*2), (so*10, so*2)), text="Green", manager=manager)
                blue_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((dis_width*1/4-so*5, dis_height*1/2+so*4), (so*10, so*2)), text="Blue", manager=manager)
                yellow_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((dis_width*1/4-so*5, dis_height*1/2+so*6), (so*10, so*2)), text="Yellow", manager=manager)
                purple_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((dis_width*1/4-so*5, dis_height*1/2+so*8), (so*10, so*2)), text="Purple", manager=manager)
                orange_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((dis_width*1/4-so*5, dis_height*1/2+so*10), (so*10, so*2)), text="Orange", manager=manager)
                pink_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((dis_width*1/4-so*5, dis_height*1/2+so*12), (so*10, so*2)), text="Pink", manager=manager)

                circle(cc)
                red_buttono = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((dis_width*3/4-so*5, dis_height*1/2), (so*10, so*2)), text="Red", manager=manager)
                green_buttono = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((dis_width*3/4-so*5, dis_height*1/2+so*2), (so*10, so*2)), text="Green", manager=manager)
                blue_buttono = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((dis_width*3/4-so*5, dis_height*1/2+so*4), (so*10, so*2)), text="Blue", manager=manager)
                yellow_buttono = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((dis_width*3/4-so*5, dis_height*1/2+so*6), (so*10, so*2)), text="Yellow", manager=manager)
                purple_buttono = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((dis_width*3/4-so*5, dis_height*1/2+so*8), (so*10, so*2)), text="Purple", manager=manager)
                orange_buttono = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((dis_width*3/4-so*5, dis_height*1/2+so*10), (so*10, so*2)), text="Orange", manager=manager)
                pink_buttono = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((dis_width*3/4-so*5, dis_height*1/2+so*12), (so*10, so*2)), text="Pink", manager=manager)

                pygame.display.update()
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == start_button:
                    gameloop(cc, xc)
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == red_button:
                    xc = red
                    ex(red)
                    pygame.display.update()
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == green_button:
                    xc = green
                    ex(green)
                    pygame.display.update()
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == blue_button:
                    xc = blue
                    ex(blue)
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == yellow_button:
                    xc = yellow
                    ex(yellow)
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == purple_button:
                    xc = purple
                    ex(purple)
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == orange_button:
                    xc = orange
                    ex(orange)
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == pink_button:
                    xc = pink
                    ex(pink)
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == red_buttono:
                    cc = red
                    circle(red)
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == green_buttono:
                    cc = green
                    circle(green)
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == blue_buttono:
                    cc = blue
                    circle(blue)
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == yellow_buttono:
                    cc = yellow
                    circle(yellow)
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == purple_buttono:
                    cc = purple
                    circle(purple)
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == orange_buttono:
                    cc = orange
                    circle(orange)
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == pink_buttono:
                    cc = pink
                    circle(pink)
            manager.process_events(event)
        manager.update(time_delta)
def gameloop(cc, xc):
    dis_width = dis.get_width()
    dis_height = dis.get_height()
    so = (dis_width + dis_height)/240
    dis.fill(gray)
    font_style = pygame.font.SysFont("bahnschrift", int(so*8))
    game_over = False
    xcolor = xc
    ocolor = cc
    rad = dis_width
    if dis_width > dis_height:
        rad = dis_height

    def board():
        pygame.draw.rect(dis, black, [(dis_width*1/8)-(so/2), 0, so, dis_height])
        pygame.draw.rect(dis, black, [(dis_width*2/8)-(so/2), 0, so, dis_height])
        pygame.draw.rect(dis, black, [(dis_width*3/8)-(so/2), 0, so, dis_height])
        pygame.draw.rect(dis, black, [(dis_width*4/8)-(so/2), 0, so, dis_height])
        pygame.draw.rect(dis, black, [(dis_width*5/8)-(so/2), 0, so, dis_height])
        pygame.draw.rect(dis, black, [(dis_width*6/8)-(so/2), 0, so, dis_height])
        pygame.draw.rect(dis, black, [(dis_width*7/8)-(so/2), 0, so, dis_height])
        pygame.draw.rect(dis, black, [0, (dis_height*1/8)-(so/2), dis_width, so])
        pygame.draw.rect(dis, black, [0, (dis_height*2/8)-(so/2), dis_width, so])
        pygame.draw.rect(dis, black, [0, (dis_height*3/8)-(so/2), dis_width, so])
        pygame.draw.rect(dis, black, [0, (dis_height*4/8)-(so/2), dis_width, so])
        pygame.draw.rect(dis, black, [0, (dis_height*5/8)-(so/2), dis_width, so])
        pygame.draw.rect(dis, black, [0, (dis_height*6/8)-(so/2), dis_width, so])
        pygame.draw.rect(dis, black, [0, (dis_height*7/8)-(so/2), dis_width, so])
        pygame.display.update()

    def circle(x, y):
        pygame.draw.circle(dis, ocolor, [dis_width*x, dis_height*y], rad/18, int(so))
        pygame.display.update()

    def ex(x, y, a, b):
        pygame.draw.line(dis, xcolor, [dis_width*x, dis_height*a], [dis_width*y, dis_height*b], int(so))
        pygame.draw.line(dis, xcolor, [dis_width*x, dis_height*b], [dis_width*y, dis_height*a], int(so))
        board()
        pygame.display.update()

    def blank(x, y):
        pygame.draw.rect(dis, gray, [dis_width*x, dis_height*y, dis_width*1/8, dis_height*1/8])
        board()
        pygame.display.update()

    class area():
        def __init__(self, x, y, taken):
            self.rect = pygame.Rect(dis_width*x, dis_height*y, dis_width*1/8, dis_height*1/8)
            self.taken = taken
            self.x = x
            self.y = y

    a1 = area(0,0,0)
    a2 = area(1/8,0,0)
    a3 = area(2/8,0,0)
    a4 = area(3/8,0,0)
    a5 = area(4/8,0,0)
    a6 = area(5/8,0,0)
    a7 = area(6/8,0,0)
    a8 = area(7/8,0,0)
    b1 = area(0,1/8,0)
    b2 = area(1/8,1/8,0)
    b3 = area(2/8,1/8,0)
    b4 = area(3/8,1/8,0)
    b5 = area(4/8,1/8,0)
    b6 = area(5/8,1/8,0)
    b7 = area(6/8,1/8,0)
    b8 = area(7/8,1/8,0)
    c1 = area(0,2/8,0)
    c2 = area(1/8,2/8,0)
    c3 = area(2/8,2/8,0)
    c4 = area(3/8,2/8,0)
    c5 = area(4/8,2/8,0)
    c6 = area(5/8,2/8,0)
    c7 = area(6/8,2/8,0)
    c8 = area(7/8,2/8,0)
    d1 = area(0,3/8,0)
    d2 = area(1/8,3/8,0)
    d3 = area(2/8,3/8,0)
    d4 = area(3/8,3/8,0)
    d5 = area(4/8,3/8,0)
    d6 = area(5/8,3/8,0)
    d7 = area(6/8,3/8,0)
    d8 = area(7/8,3/8,0)
    e1 = area(0,4/8,0)
    e2 = area(1/8,4/8,0)
    e3 = area(2/8,4/8,0)
    e4 = area(3/8,4/8,0)
    e5 = area(4/8,4/8,0)
    e6 = area(5/8,4/8,0)
    e7 = area(6/8,4/8,0)
    e8 = area(7/8,4/8,0)
    f1 = area(0,5/8,0)
    f2 = area(1/8,5/8,0)
    f3 = area(2/8,5/8,0)
    f4 = area(3/8,5/8,0)
    f5 = area(4/8,5/8,0)
    f6 = area(5/8,5/8,0)
    f7 = area(6/8,5/8,0)
    f8 = area(7/8,5/8,0)
    g1 = area(0,6/8,0)
    g2 = area(1/8,6/8,0)
    g3 = area(2/8,6/8,0)
    g4 = area(3/8,6/8,0)
    g5 = area(4/8,6/8,0)
    g6 = area(5/8,6/8,0)
    g7 = area(6/8,6/8,0)
    g8 = area(7/8,6/8,0)
    h1 = area(0,7/8,0)
    h2 = area(1/8,7/8,0)
    h3 = area(2/8,7/8,0)
    h4 = area(3/8,7/8,0)
    h5 = area(4/8,7/8,0)
    h6 = area(5/8,7/8,0)
    h7 = area(6/8,7/8,0)
    h8 = area(7/8,7/8,0)

    def message(msg,color):
        mesg = font_style.render(msg, True, color)
        dis.blit(mesg, [(dis_width-mesg.get_rect().width)/2, (dis_height-mesg.get_rect().height)/2])

    def end(msg):
        message(msg, green)
        pygame.display.update()

    def move(a):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if a.rect.collidepoint(event.pos):
                    if a.taken == 0:
                        a.taken += 1
                        blank(a.x, a.y)
                        ex(a.x, a.x+1/8, a.y, a.y+1/8)
                        pygame.display.update()
                    elif a.taken == 1:
                        a.taken -= 1
                        blank(a.x, a.y)
                        circle(a.x+1/16, a.y+1/16)
                        pygame.display.update()
    board()

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type==pygame.VIDEORESIZE:
                dis_height = dis.get_height()
                dis_width = dis.get_width()
                dis.fill(gray)
                a1 = area(0,0,0)
                a2 = area(1/8,0,0)
                a3 = area(2/8,0,0)
                a4 = area(3/8,0,0)
                a5 = area(4/8,0,0)
                a6 = area(5/8,0,0)
                a7 = area(6/8,0,0)
                a8 = area(7/8,0,0)
                b1 = area(0,1/8,0)
                b2 = area(1/8,1/8,0)
                b3 = area(2/8,1/8,0)
                b4 = area(3/8,1/8,0)
                b5 = area(4/8,1/8,0)
                b6 = area(5/8,1/8,0)
                b7 = area(6/8,1/8,0)
                b8 = area(7/8,1/8,0)
                c1 = area(0,2/8,0)
                c2 = area(1/8,2/8,0)
                c3 = area(2/8,2/8,0)
                c4 = area(3/8,2/8,0)
                c5 = area(4/8,2/8,0)
                c6 = area(5/8,2/8,0)
                c7 = area(6/8,2/8,0)
                c8 = area(7/8,2/8,0)
                d1 = area(0,3/8,0)
                d2 = area(1/8,3/8,0)
                d3 = area(2/8,3/8,0)
                d4 = area(3/8,3/8,0)
                d5 = area(4/8,3/8,0)
                d6 = area(5/8,3/8,0)
                d7 = area(6/8,3/8,0)
                d8 = area(7/8,3/8,0)
                e1 = area(0,4/8,0)
                e2 = area(1/8,4/8,0)
                e3 = area(2/8,4/8,0)
                e4 = area(3/8,4/8,0)
                e5 = area(4/8,4/8,0)
                e6 = area(5/8,4/8,0)
                e7 = area(6/8,4/8,0)
                e8 = area(7/8,4/8,0)
                f1 = area(0,5/8,0)
                f2 = area(1/8,5/8,0)
                f3 = area(2/8,5/8,0)
                f4 = area(3/8,5/8,0)
                f5 = area(4/8,5/8,0)
                f6 = area(5/8,5/8,0)
                f7 = area(6/8,5/8,0)
                f8 = area(7/8,5/8,0)
                g1 = area(0,6/8,0)
                g2 = area(1/8,6/8,0)
                g3 = area(2/8,6/8,0)
                g4 = area(3/8,6/8,0)
                g5 = area(4/8,6/8,0)
                g6 = area(5/8,6/8,0)
                g7 = area(6/8,6/8,0)
                g8 = area(7/8,6/8,0)
                h1 = area(0,7/8,0)
                h2 = area(1/8,7/8,0)
                h3 = area(2/8,7/8,0)
                h4 = area(3/8,7/8,0)
                h5 = area(4/8,7/8,0)
                h6 = area(5/8,7/8,0)
                h7 = area(6/8,7/8,0)
                h8 = area(7/8,7/8,0)
                so = (dis_width + dis_height)/240
                font_style = pygame.font.SysFont("bahnschrift", int(so*8))
                rad = dis_width
                if dis_width > dis_height:
                    rad = dis_height
                board()
                pygame.display.update()
            move(a1)
            move(a2)
            move(a3)
            move(a4)
            move(a5)
            move(a6)
            move(a7)
            move(a8)
            move(b1)
            move(b2)
            move(b3)
            move(b4)
            move(b5)
            move(b6)
            move(b7)
            move(b8)
            move(c1)
            move(c2)
            move(c3)
            move(c4)
            move(c5)
            move(c6)
            move(c7)
            move(c8)
            move(d1)
            move(d2)
            move(d3)
            move(d4)
            move(d5)
            move(d6)
            move(d7)
            move(d8)
            move(e1)
            move(e2)
            move(e3)
            move(e4)
            move(e5)
            move(e6)
            move(e7)
            move(e8)
            move(f1)
            move(f2)
            move(f3)
            move(f4)
            move(f5)
            move(f6)
            move(f7)
            move(f8)
            move(g1)
            move(g2)
            move(g3)
            move(g4)
            move(g5)
            move(g6)
            move(g7)
            move(g8)
            move(h1)
            move(h2)
            move(h3)
            move(h4)
            move(h5)
            move(h6)
            move(h7)
            move(h8)

        clock.tick(60)
    pygame.quit()
    quit()

startscreen(xc, cc)