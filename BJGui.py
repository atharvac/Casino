import pygame
import blackjack as bk
import time

# Window size
width: int = 1280
height: int = 720
white = (255, 255, 255)
black = (0, 0, 0)
brown = (80, 50, 25)

pygame.init()

gameDisplay = pygame.display.set_mode((width, height))
pygame.display.set_caption("Casino")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 40)
font2 = pygame.font.Font(None, 80)
font3 = pygame.font.Font(None, 60)
b1 = bk.Blackjack(2)
P_bust = False


class Button:
    def __init__(self, x1, y1, w, h, func, name, func_param=None, image=None):
        self.x1 = x1
        self.w = w
        self.y1 = y1
        self.h = h
        self.image = image
        self.func = func
        self.func_param = func_param
        self.button_name = name


def display_button(b):
    if b.image is None:
        pygame.draw.rect(gameDisplay, white, (b.x1, b.y1, b.w, b.h), 5)
        text1 = font.render(b.button_name, True, white)
        gameDisplay.blit(text1, (b.x1+43, b.y1+18))
    else:
        gameDisplay.blit(b.image, (b.x1, b.y1))
    # pygame.display.update((b.x1, b.y1, b.w, b.h))


def display_cards():
    global b1
    base_p_x = width * 0.3
    base_p_y = height * 0.6
    base_d_x = width * 0.3
    base_d_y = height * 0.1
    c = 0
    player1_cards = []
    player2_cards = []
    dealer_cards = []
    for x in b1.player_deck1:
        player1_cards.append(x.load_card())
    for x in b1.dealer_deck:
        dealer_cards.append(x.load_card())
    if b1.split:
        for x in b1.player_deck2:
            player2_cards.append(x.load_card())
        # HERE
    else:
        for _ in player1_cards:
            gameDisplay.blit(_, (base_p_x + c, base_p_y))
            c += 50
        c = 0
        for _ in dealer_cards:
            gameDisplay.blit(_, (base_d_x + c, base_d_y))
            c += 50

        p1_score = str(b1.playerTotal1)
        p2_score = str(b1.playerTotal1Alt)

        gameDisplay.blit(font.render(p1_score, True, white), (base_p_x - 50, base_p_y + 10))
        gameDisplay.blit(font.render(p2_score, True, white), (base_p_x - 50, base_p_y + 200))

        backside = pygame.image.load(f"newPNG/purple_back.png").convert()
        gameDisplay.blit(backside, (80, base_d_y))


def mask_dealer_card():
    base_d_x = width * 0.3
    base_d_y = height * 0.1
    backside = pygame.image.load(f"newPNG/purple_back.png").convert()
    gameDisplay.blit(backside, (base_d_x + 50, base_d_y))


def draw_all(b_lst):
    global b1
    pygame.draw.line(gameDisplay, white, (0, height/2), (width, height/2), 10)
    for x in b_lst:
        display_button(x)


def hit_ani(param):
    global P_bust
    result = b1.hit(param)
    if result == 1:
        P_bust = True
        after_stand()
    '''backside = (80, height*0.1)
    x = backside[0]
    y = backside[1]
    offset = (len(b1.player_deck1) - 1) * 50
    p_coord = (width*0.3 + offset, height*0.6)
    card = b1.player_deck1[-1].load_card()
    xnc = p_coord[0] - backside[0]
    ync = p_coord[1] - backside[1]
    l_ = max(xnc, ync)
    xinc = xnc/l_
    yinc = ync/l_
    for _ in range(int(l_)):
        x += xinc
        y += yinc
        gameDisplay.fill(brown)
        gameDisplay.blit(card, (x, y))
        draw_all([])
        pygame.display.update()
    '''


def after_stand():
    global b1
    global P_bust
    result = b1.stand()
    display_cards()
    if not b1.split:
        if result[0] == 1:
            txt = "Dealer wins!"
        else:
            txt = "Player wins!"
        tt = font2.render(txt, True, white)
        p_bust = "Player Bust!"
        surf = font2.render(p_bust, True, white)
        # pygame.draw.rect(gameDisplay, black, (width*0.2, height*0.4, 400, 100))
        gameDisplay.fill(brown)
        gameDisplay.blit(tt, (width*0.72, height*0.43))
        if P_bust:
            gameDisplay.blit(surf, (width * 0.65, height * 0.7))
        draw_all([])
        display_cards()
        d1_score = str(b1.dealerTotal)
        d2_score = str(b1.dealerAlternate)
        base_d_x = width * 0.3
        base_d_y = height * 0.1
        gameDisplay.blit(font.render(d1_score, True, white), (base_d_x - 50, base_d_y + 10))
        gameDisplay.blit(font.render(d2_score, True, white), (base_d_x - 50, base_d_y + 200))
    pygame.display.update()
    time.sleep(3)
    b1.reset_hand()
    P_bust = False
    print(b1.setup())  # Split Logic starts here


def all_buttons():
    global b1
    if not b1.split:
        b_lst = [Button(width*0.05, height*0.85, 170, 60, hit_ani, "HIT", 1),
                 Button(width*0.05, height*0.7, 170, 60, after_stand, "STAND"),
                 ]
    else:  # HERE
        b_lst = []
    return b_lst


def main():
    print(b1.setup())
    buttons_list = all_buttons()
    exit1 = False
    while not exit1:
        gameDisplay.fill(brown)
        draw_all(buttons_list)
        display_cards()
        mask_dealer_card()
        pygame.display.update()

        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit1 = True
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for x in buttons_list:
                    if (x.x1 < mouse[0] < x.x1+x.w) and (x.y1 < mouse[1] < x.y1+x.h):
                        if x.func_param is not None:
                            x.func(x.func_param)
                        else:
                            x.func()
        clock.tick(120)

    print(b1.player_deck1)
    print(b1.dealer_deck)


main()
