""" Encoding: UTF-8 """

from math import sqrt
import pygame
from lang_translation import langues
import sys
import time

pygame.init()

pygame.display.set_caption("Jeu De Hex")

logo = pygame.image.load("Icon/Hex_icon.png")
pygame.display.set_icon(logo)

music = pygame.mixer.Sound("Music/Music.ogg")
music.play(256)

mainClock = pygame.time.Clock()


global_font = "Roboto"
LANG = "en"

#-----Dimensions
#---------------Screen Size
SIZE_X = 1080
SIZE_Y = 720
#----------------BOX
BOX_Y = 600
BOX_X = BOX_Y* sqrt(3)
BOTTOM_BOX=SIZE_Y-25
TOP_BOX = BOTTOM_BOX - BOX_Y
LEFT_BOX = (SIZE_X-BOX_X)/2
RIGHT_BOX = (SIZE_X-BOX_X)/2 + BOX_X
MIDY_BOX = (TOP_BOX + BOTTOM_BOX)/2

#-----Couleurs
screen_color = ( 255 , 224 , 0)
dark_screen_color = (225, 200, 0)
light_effet = (252, 244, 164)
white = (255 , 255 , 255)
black = (0 , 0 , 0)
beige = (230, 215, 188)
gray = (200, 200, 200)
d_gray = (32, 32, 32)

#------Screen Initialisation
screen = pygame.display.set_mode((SIZE_X, SIZE_Y))#, pygame.RESIZABLE 
screen.fill(screen_color)

WIDTH_BUTTON = 500
HEIGHT_BUTTON = 100
MARGIN_TOP = 150 # MARGIN_TOP > HEIGHT_BUTTON
#--------Button

play_button = pygame.Rect((SIZE_X - WIDTH_BUTTON)/2, (SIZE_Y - HEIGHT_BUTTON)/2 - MARGIN_TOP, WIDTH_BUTTON , HEIGHT_BUTTON)
option_button = pygame.Rect((SIZE_X - WIDTH_BUTTON)/2,(SIZE_Y - HEIGHT_BUTTON)/2, WIDTH_BUTTON , HEIGHT_BUTTON)
quit_button = pygame.Rect((SIZE_X - WIDTH_BUTTON)/2, (SIZE_Y - HEIGHT_BUTTON)/2 + MARGIN_TOP, WIDTH_BUTTON , HEIGHT_BUTTON)

# BUTTON/2
play_button_2 = pygame.Rect((SIZE_X - WIDTH_BUTTON)/2, (SIZE_Y - HEIGHT_BUTTON)/2 - MARGIN_TOP, WIDTH_BUTTON , HEIGHT_BUTTON/2)
option_button_2 = pygame.Rect((SIZE_X - WIDTH_BUTTON)/2,(SIZE_Y - HEIGHT_BUTTON)/2, WIDTH_BUTTON , HEIGHT_BUTTON/2)
quit_button_2 = pygame.Rect((SIZE_X - WIDTH_BUTTON)/2, (SIZE_Y - HEIGHT_BUTTON)/2 + MARGIN_TOP, WIDTH_BUTTON , HEIGHT_BUTTON/2)
#BUTTON/4
play_button_4 = pygame.Rect((SIZE_X - WIDTH_BUTTON)/2 + 50, (SIZE_Y - HEIGHT_BUTTON)/2 - MARGIN_TOP, WIDTH_BUTTON-100 , HEIGHT_BUTTON/4)
option_button_4 = pygame.Rect((SIZE_X - WIDTH_BUTTON)/2 +50,(SIZE_Y - HEIGHT_BUTTON)/2, WIDTH_BUTTON -100 , HEIGHT_BUTTON/4)
quit_button_4 = pygame.Rect((SIZE_X - WIDTH_BUTTON)/2 + 50, (SIZE_Y - HEIGHT_BUTTON)/2 + MARGIN_TOP, WIDTH_BUTTON-100 , HEIGHT_BUTTON/4)


def main():
    """ The Main Menu """

    screen.fill(screen_color)
    title_font = switch_font(75, False, False)
    title = title_font.render(langues["hex_game"].get(LANG), True, (0 , 0 ,0))
    title_rect =title.get_rect(center=(SIZE_X/2, 50))
    screen.blit(title,title_rect)
    running = True
    click = False
    K = 0
    # DARK SCREEN COLOR
    pygame.draw.rect(screen, dark_screen_color, play_button, border_radius= 15)
    pygame.draw.rect(screen, dark_screen_color, option_button, border_radius= 15)
    pygame.draw.rect(screen, dark_screen_color, quit_button, border_radius= 15)
    #SCREEN COLOR
    pygame.draw.rect(screen, screen_color, play_button_2, border_radius= 15)
    pygame.draw.rect(screen, screen_color, option_button_2, border_radius= 15)
    pygame.draw.rect(screen, screen_color, quit_button_2, border_radius= 15)
    #LIGHT EFFECT
    pygame.draw.rect(screen, light_effet, play_button_4, border_radius= 15)
    pygame.draw.rect(screen, light_effet, option_button_4, border_radius= 15)
    pygame.draw.rect(screen, light_effet, quit_button_4, border_radius= 15)
    # Black BORDER
    pygame.draw.rect(screen, black, play_button, 5 ,border_radius= 15)
    pygame.draw.rect(screen, black, option_button, 5, border_radius= 15)
    pygame.draw.rect(screen, black, quit_button, 5, border_radius= 15)

    font = switch_font(50, False, False)
    play_text = font.render(langues["play"].get(LANG), True, (0 , 0 ,0))
    option_text =font.render(langues["option"].get(LANG), True, (0 , 0 ,0))
    quit_text = font.render(langues["quit"].get(LANG), True, (0 , 0 ,0))

    play_rect = play_text.get_rect(center=(SIZE_X/2, SIZE_Y/2 - MARGIN_TOP))
    option_rect = option_text.get_rect(center=(SIZE_X/2, SIZE_Y/2))
    quit_rect = quit_text.get_rect(center=(SIZE_X/2, SIZE_Y/2 + MARGIN_TOP))

    screen.blit(play_text, play_rect)
    screen.blit(option_text, option_rect)
    screen.blit(quit_text, quit_rect)

    while running:
        mouse_x , mouse_y = pygame.mouse.get_pos()

        if K == 8:
            pygame.draw.rect(screen, dark_screen_color, play_button, border_radius= 15)
            pygame.draw.rect(screen, screen_color, play_button_2, border_radius= 15)
            pygame.draw.rect(screen, light_effet, play_button_4, border_radius= 15)
            pygame.draw.rect(screen, black, play_button, 5 ,border_radius= 15)
            play_text = font.render(langues["p1ay"].get(LANG), True, (0 , 0 ,0))
            play_rect = play_text.get_rect(center=(SIZE_X/2, SIZE_Y/2 - MARGIN_TOP))
            screen.blit(play_text, play_rect)
            K=9

        #------Direction of a Button
        if play_button.collidepoint((mouse_x, mouse_y)) and click:
            choosing_lenght()
        if option_button.collidepoint((mouse_x, mouse_y)) and click:
            option()
        if quit_button.collidepoint((mouse_x, mouse_y)) and click:
            running = False
            sys.exit()

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                click = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and K in {0, 1}:
                    K+=1
                elif event.key == pygame.K_DOWN and K in {2, 3}:
                    K+=1
                elif event.key == pygame.K_LEFT and K in {4, 6}:
                    K+=1
                elif event.key == pygame.K_RIGHT and K in {5, 7}:
                    K+=1
                else:
                    K=0
        pygame.display.update()
        mainClock.tick_busy_loop(60)
  

def choosing_lenght():
    """ The Menu to change the lenght of the tray """
   
    screen.fill(screen_color)
    title_font = switch_font(75, False, False)

    #TITLE
    title = title_font.render(langues["hex_game"].get(LANG), True, (0 , 0 ,0))
    title_rect =title.get_rect(center=(SIZE_X/2, 50))
    screen.blit(title,title_rect)

    K=0

    #Back Button
    button_return = pygame.Rect(10, 10 , 200, 75)
    click_button = pygame.draw.rect(screen, screen_color, button_return)
    back_font = switch_font(50, False, True)
    back_text = back_font.render(" << "+langues["back"].get(LANG), True, black)

    back_center = back_text.get_rect(center=(105, 43))
    pygame.draw.rect(screen, black, button_return, 5)
    screen.blit(back_text, back_center)


    change_lenght_background = pygame.Rect(100, SIZE_Y/2 -50, SIZE_X - 200, 100 )
    change_lenght_frame = pygame.Rect(95, SIZE_Y/2 -55, SIZE_X - 190, 110 )

    pygame.draw.rect(screen, black, change_lenght_frame)
    pygame.draw.rect(screen, gray, change_lenght_background)

    _extracted_from_choosing_lenght_29(70, "tray_lenght", 100)
    # ctc <=> Click to change
    ctc_font = switch_font(20, False, False)
    ctc_text = ctc_font.render(langues["clic_to_change"].get(LANG), True, black)
    ctc_rect = ctc_text.get_rect(bottomright=(SIZE_X - 150, SIZE_Y/2 - 60))
    screen.blit(ctc_text, ctc_rect)

    arrow_file = pygame.image.load("Icon/arrow.png")
    arrow = pygame.transform.scale(arrow_file, (100, 100))
    #---Showing Images
    screen.blit(arrow, [SIZE_X - 150, SIZE_Y/2 - 100])

    #-------Let's GO Button

    WIDTH_BUTTON2 = 300
    HEIGHT_BUTTON2 = 100
    MARGIN_TOP2 = -200 # MARGIN_TOP > HEIGHT_BUTTON

    letsgo_button = pygame.Rect((SIZE_X - WIDTH_BUTTON2)/2, (SIZE_Y - HEIGHT_BUTTON2)/2 - MARGIN_TOP2, WIDTH_BUTTON2, HEIGHT_BUTTON2)
    letsgo_button_2 = pygame.Rect((SIZE_X - WIDTH_BUTTON2)/2, (SIZE_Y - HEIGHT_BUTTON2)/2 - MARGIN_TOP2, WIDTH_BUTTON2 , HEIGHT_BUTTON2/2)
    letsgo_button_4 = pygame.Rect((SIZE_X - WIDTH_BUTTON2)/2 + 50, (SIZE_Y - HEIGHT_BUTTON2)/2 - MARGIN_TOP2, WIDTH_BUTTON2-100 , HEIGHT_BUTTON2/4)

    pygame.draw.rect(screen, dark_screen_color, letsgo_button, border_radius= 5)
    pygame.draw.rect(screen, screen_color, letsgo_button_2, border_radius= 5)
    pygame.draw.rect(screen, light_effet, letsgo_button_4, border_radius= 5)
    pygame.draw.rect(screen, black, letsgo_button, 5 ,border_radius= 5)
    pygame.display.flip()

    _extracted_from_choosing_lenght_29(50, "letsgo", MARGIN_TOP2)
    running = True
    click = False
    while running:
        mouse_x , mouse_y = pygame.mouse.get_pos()

        if click_button.collidepoint((mouse_x, mouse_y)) and click:
            main()

        if change_lenght_background.collidepoint((mouse_x, mouse_y)) and click:
            lenght_plate = int(round((((mouse_x -100 )/( SIZE_X -100)) * 45) * (10/8.97)+5, 0))
            vol_text = back_font.render( str(lenght_plate) + "x" + str(lenght_plate), True, black)
            vol_rect = back_text.get_rect(center=(SIZE_X/2,SIZE_Y/2 +100))
            change_volume = pygame.Rect(100, SIZE_Y/2 -50, mouse_x-100, 100 )
            pygame.draw.rect(screen, gray, change_lenght_background)
            pygame.draw.rect(screen, white, change_volume)
            pygame.draw.rect(screen, screen_color, vol_rect)
            screen.blit(vol_text, vol_rect)

        if not change_lenght_background.collidepoint((mouse_x, mouse_y)):
            click = False


        if K==8:
            lenght_plate = 100
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                click = True
            if event.type == pygame.MOUSEBUTTONDOWN and letsgo_button.collidepoint((mouse_x, mouse_y)):
                try:
                    game(lenght_plate)
                except UnboundLocalError:
                    game(11)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and K in {0, 1}:
                    K+=1
                elif event.key == pygame.K_DOWN and K in {2, 3}:
                    K+=1
                elif event.key == pygame.K_LEFT and K in {4, 6}:
                    K+=1
                elif event.key == pygame.K_RIGHT and K in {5, 7}:
                    K+=1
                else:
                    K=0

        pygame.display.flip()

def _extracted_from_choosing_lenght_29(arg0, arg1, arg2):
    lenght_font = switch_font(arg0, False, False)
    lenght_text = lenght_font.render(langues[arg1].get(LANG), True, black)
    lenght_rect = lenght_text.get_rect(center=(SIZE_X/2, SIZE_Y/2 - arg2))
    screen.blit(lenght_text, lenght_rect)

def game(x):

    """ The Game """

    POSITION_FOUND2 = False
    screen.fill(screen_color)
    title_font = switch_font(75, False, False)
    title = title_font.render(langues["hex_game"].get(LANG), True, (0 , 0 ,0))
    title_rect =title.get_rect(center=(SIZE_X/2, 50))
    screen.blit(title,title_rect)


    #Back Button
    button_return = pygame.Rect(10, 10 , 200, 75)
    click_button = pygame.draw.rect(screen, screen_color, button_return)
    back_font = switch_font(50, False, True)
    back_text = back_font.render(" << "+langues["back"].get(LANG), True, black)

    back_center = back_text.get_rect(center=(105, 43))
    
    pygame.draw.rect(screen, black, button_return, 5)
    screen.blit(back_text, back_center)


    #-----Plateau
    #---------------Fond
    box  = [(LEFT_BOX, TOP_BOX),(RIGHT_BOX,TOP_BOX),(RIGHT_BOX,BOTTOM_BOX),(LEFT_BOX, BOTTOM_BOX)]
    bordures = [(SIZE_X/2, TOP_BOX),(RIGHT_BOX,MIDY_BOX),(SIZE_X/2,BOTTOM_BOX),(LEFT_BOX, MIDY_BOX)]
    phase_blanche  = [(SIZE_X/2, TOP_BOX),(SIZE_X/2,BOTTOM_BOX),(RIGHT_BOX,MIDY_BOX),(LEFT_BOX, MIDY_BOX)]

    pygame.draw.polygon(screen, screen_color, box)
    pygame.draw.polygon(screen, black, bordures)
    pygame.draw.polygon(screen, white, phase_blanche)
    #---------------Hexagones 
    lenght_plate = x
    border_plate_size = sqrt((BOTTOM_BOX-MIDY_BOX)**2+(RIGHT_BOX-BOX_X/2)**2)
    hex_border = ((border_plate_size)/2)/lenght_plate
    marge = 72.5
    Hexa_color = []
    #print(f"BotBox = {BOTTOM_BOX} / Mid Box = {MIDY_BOX} / border plate size = {border_plate_size}")
    for i in range(lenght_plate):
        for j in range(lenght_plate):
            hexagone = [(LEFT_BOX + marge + hex_border/2 + j*(3/2)*hex_border +i*(3/2)*hex_border , MIDY_BOX + sqrt(3)*hex_border/2 - (sqrt(3)*j/2)*hex_border + (sqrt(3)*i/2)*hex_border),
            (LEFT_BOX + marge + j*(3/2)*hex_border +i*(3/2)*hex_border,MIDY_BOX - (sqrt(3)*j/2)*hex_border+ (sqrt(3)*i/2)*hex_border),
            (LEFT_BOX + marge + hex_border/2 + j*(3/2)*hex_border+i*(3/2)*hex_border, MIDY_BOX - sqrt(3)*hex_border/2 - (sqrt(3)*j/2)*hex_border+ (sqrt(3)*i/2)*hex_border),
            (LEFT_BOX + marge + (3 * hex_border)/2 + j*(3/2)*hex_border+i*(3/2)*hex_border, MIDY_BOX - sqrt(3)*hex_border/2 - (sqrt(3)*j/2)*hex_border+ (sqrt(3)*i/2)*hex_border),
            (LEFT_BOX + marge + 2 * hex_border + j*(3/2)*hex_border+i*(3/2)*hex_border,MIDY_BOX - (sqrt(3)*j/2)*hex_border+ (sqrt(3)*i/2)*hex_border),
            (LEFT_BOX + marge + (3 * hex_border)/2+ j*(3/2)*hex_border+i*(3/2)*hex_border, MIDY_BOX + sqrt(3)*hex_border/2 - (sqrt(3)*j/2)*hex_border+ (sqrt(3)*i/2)*hex_border)]
            Hexa_color+=[beige]
            bounding_rect = pygame.draw.polygon(screen, Hexa_color[(lenght_plate*i)+j], hexagone)
            pygame.draw.polygon(screen, black, hexagone, round(50/lenght_plate))

    pygame.display.flip()
    running = True
    TURN = 'white'
    once_variable = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONUP and once_variable and click_button.collidepoint(pygame.mouse.get_pos()):
                choosing_lenght()
            elif event.type == pygame.MOUSEBUTTONUP and once_variable:
                click = True
                FOUND = False
                for i in range(lenght_plate):
                    for j in range(lenght_plate):
                        hexagone = [(LEFT_BOX + marge + hex_border/2 + j*(3/2)*hex_border +i*(3/2)*hex_border , MIDY_BOX + sqrt(3)*hex_border/2 - (sqrt(3)*j/2)*hex_border + (sqrt(3)*i/2)*hex_border),
                        (LEFT_BOX + marge + j*(3/2)*hex_border +i*(3/2)*hex_border,MIDY_BOX - (sqrt(3)*j/2)*hex_border+ (sqrt(3)*i/2)*hex_border),
                        (LEFT_BOX + marge + hex_border/2 + j*(3/2)*hex_border+i*(3/2)*hex_border, MIDY_BOX - sqrt(3)*hex_border/2 - (sqrt(3)*j/2)*hex_border+ (sqrt(3)*i/2)*hex_border),
                        (LEFT_BOX + marge + (3 * hex_border)/2 + j*(3/2)*hex_border+i*(3/2)*hex_border, MIDY_BOX - sqrt(3)*hex_border/2 - (sqrt(3)*j/2)*hex_border+ (sqrt(3)*i/2)*hex_border),
                        (LEFT_BOX + marge + 2 * hex_border + j*(3/2)*hex_border+i*(3/2)*hex_border,MIDY_BOX - (sqrt(3)*j/2)*hex_border+ (sqrt(3)*i/2)*hex_border),
                        (LEFT_BOX + marge + (3 * hex_border)/2+ j*(3/2)*hex_border+i*(3/2)*hex_border, MIDY_BOX + sqrt(3)*hex_border/2 - (sqrt(3)*j/2)*hex_border+ (sqrt(3)*i/2)*hex_border)]
                        bounding_rect = pygame.draw.polygon(screen, Hexa_color[(lenght_plate*i)+j], hexagone)
                        if x < 64:
                            pygame.draw.polygon(screen, d_gray, hexagone, round(50/lenght_plate))
                        else:
                            pass
                        if bounding_rect.collidepoint(pygame.mouse.get_pos()) and not FOUND:
                            if Hexa_color[(lenght_plate * i) + j] != beige:
                                continue
                            if TURN == 'white':
                                Hexa_color[(lenght_plate*i)+j]=white
                                pygame.draw.polygon(screen, white , hexagone)
                                TURN = "black"
                            else:
                                Hexa_color[(lenght_plate*i)+j]=black
                                pygame.draw.polygon(screen, black , hexagone)
                                TURN = "white"
                            pygame.draw.polygon(screen, d_gray, hexagone, round(50/lenght_plate))
                            pygame.display.flip()
                            FOUND = True
                pygame.display.flip()
            else:
                once_variable = True
                continue

            once_variable = True
        #========GAME

        turn_font = switch_font(50, False, False)
        white_text = turn_font.render(langues["white"].get(LANG), True, black)
        black_text = turn_font.render(langues["black"].get(LANG), True, black)
        screen.blit(white_text,[10, 100])
        black_rect = black_text.get_rect(topright=(SIZE_X-10,100))
        screen.blit(black_text, black_rect)

        if TURN == "white":
            arrow_left = turn_font.render("<", True, black)
            arrow_right = turn_font.render(">", True, screen_color)
        elif TURN == "black":
            arrow_left = turn_font.render("<", True, screen_color)
            arrow_right = turn_font.render(">", True, black)
        screen.blit(arrow_left,[120, 100])
        if LANG in {'jp', 'gr'}:
            screen.blit(arrow_right,[SIZE_X-200, 100])
        else:
            screen.blit(arrow_right,[SIZE_X-127, 100])
        pygame.display.flip()
        Z = 1
        WIN = True
        WHITE_WON = False
        for i in range(lenght_plate):
            if Z==0:
                WIN=False
            else:
                Z = 0
            for j in range(lenght_plate):
                if Hexa_color[(lenght_plate*i)+j]==white:
                    Z = 1
                else:
                    continue
        if Z == 0:
            WIN = False
        elif Z == 1 and WIN:
            solution = []
            next_solution = []
            for j in range(lenght_plate):
                if Hexa_color[j]==white:
                    solution.append(j)
                else:
                    continue
            passed = []
            solutionLoop = []
            CanWin = True
            SOL_AND_PASSE = False
            POSITION_FOUND2 = False
            def solw(x):
                if Hexa_color[VALUE_SOLUTION+x]==white:
                    next_solution.append(VALUE_SOLUTION  + x)

            while CanWin and not WHITE_WON:
                if next_solution != []:
                    solution = next_solution
                for sol in solution:
                    for passe in passed:
                        if sol == passe:
                            SOL_AND_PASSE = True
                        else:
                            x=0
                    if not SOL_AND_PASSE:
                        solutionLoop.append(sol)
                    else:
                        x=0
                    SOL_AND_PASSE = False
                solution = []
                next_solution = []
                solution = solutionLoop
                solutionLoop = []
                #print(f"WHITE \ \n Solution = {solution} \n \n Passed = {passed} \n \n \n")
                if solution == []:
                    CanWin = False
                else:
                    for k in solution:
                        VALUE_SOLUTION = k
                        POSITION_FOUND2 = False
                        if VALUE_SOLUTION >= lenght_plate ** 2 - lenght_plate:
                            WHITE_WON = True
                        elif not WHITE_WON:
                            #print(VALUE_SOLUTION)
                            solw(lenght_plate)
                            for x in range(lenght_plate):
                                if VALUE_SOLUTION >= lenght_plate and VALUE_SOLUTION == x * lenght_plate - 1: #Black Border-Right
                                    solw(-lenght_plate)
                                    solw(-1)
                                    solw(-lenght_plate-1)
                                    POSITION_FOUND2 = True
                                elif VALUE_SOLUTION >= lenght_plate and VALUE_SOLUTION == x * lenght_plate: #Black Border-Left
                                    solw(-lenght_plate)
                                    solw(-lenght_plate+1)
                                    solw(1)
                                    POSITION_FOUND2 = True
                            if VALUE_SOLUTION == lenght_plate - 1: #White Border and Black Border-Right
                                solw(-1)
                                solw(lenght_plate -1)
                                POSITION_FOUND2 = True
                            
                            elif VALUE_SOLUTION == "0": #White Border and Black Border-Left
                                solw(1)
                                POSITION_FOUND2 = True
                            elif VALUE_SOLUTION < lenght_plate:#White Border
                                if Hexa_color[VALUE_SOLUTION-1]==white:
                                    next_solution.append(VALUE_SOLUTION  - 1)
                                if Hexa_color[VALUE_SOLUTION+1]==white:
                                    next_solution.append(VALUE_SOLUTION + 1 )
                                if Hexa_color[VALUE_SOLUTION+lenght_plate-1]==white:
                                    next_solution.append(VALUE_SOLUTION  + lenght_plate - 1)
                                POSITION_FOUND2 = True

                            elif not POSITION_FOUND2:
                                if Hexa_color[VALUE_SOLUTION-lenght_plate]==white:
                                    next_solution.append(VALUE_SOLUTION  -lenght_plate)
                                if Hexa_color[VALUE_SOLUTION-lenght_plate+1]==white:
                                    next_solution.append(VALUE_SOLUTION  - lenght_plate + 1)
                                if Hexa_color[VALUE_SOLUTION-1]==white:
                                    next_solution.append(VALUE_SOLUTION  - 1)
                                if Hexa_color[VALUE_SOLUTION+1]==white:
                                    next_solution.append(VALUE_SOLUTION + 1 )
                                if Hexa_color[VALUE_SOLUTION+lenght_plate-1]==white:
                                    next_solution.append(VALUE_SOLUTION  + lenght_plate - 1)
                            passed.append(VALUE_SOLUTION)
                            #print("next solution of",k,":",next_solution)
        
        # BLACK
        if not WHITE_WON:
            Z=1
            WIN = True
            BLACK_WON = False
            for i in range(lenght_plate):
                if Z==0:
                    WIN=False
                else:
                    Z = 0
                for j in range(lenght_plate):
                    if Hexa_color[(lenght_plate*j)+i]==black:
                        Z = 1
                    else:
                        continue
            if Z == 0:
                WIN = False
            elif Z == 1 and WIN:
                solution = []
                next_solution = []
                for j in range(lenght_plate):
                    if Hexa_color[j*lenght_plate]==black:
                        solution.append(j*lenght_plate)
                    else:
                        continue
                passed = []
                solutionLoop = []
                CanWin = True
                SOL_AND_PASSE = False
                POSITION_FOUND = False
                def solb(x):
                    global POSITION_FOUND
                    if Hexa_color[VALUE_SOLUTION+x]==black:
                        next_solution.append(VALUE_SOLUTION  + x)
                        POSITION_FOUND = True
                while CanWin and not BLACK_WON:
                    if next_solution != []:
                        solution = next_solution
                    for sol in solution:
                        for passe in passed:
                            if sol == passe:
                                SOL_AND_PASSE = True
                            else:
                                x=0
                        if not SOL_AND_PASSE:
                            solutionLoop.append(sol)
                        else:
                            x=0
                        SOL_AND_PASSE = False
                    solution = []
                    solution = solutionLoop
                    solutionLoop = []
                    #print(f"BLACK/ \nSolution = {solution} \n \nPassed = {passed} \n \n \n")
                    if solution == []:
                        CanWin = False
                    else:
                        for k in solution:
                            VALUE_SOLUTION = k
                            POSITION_FOUND = False
                            for x in range(lenght_plate):
                                if VALUE_SOLUTION== x * (lenght_plate) - 1 :
                                    BLACK_WON = True

                            if not BLACK_WON:
                                if Hexa_color[VALUE_SOLUTION+1]==black:
                                    next_solution.append(VALUE_SOLUTION +1)
                                for x in range(lenght_plate):
                                    if VALUE_SOLUTION == x*lenght_plate and VALUE_SOLUTION!=0 and VALUE_SOLUTION != lenght_plate**2 - lenght_plate : #Black Border
                                        solb(lenght_plate)
                                        solb(-lenght_plate+1)
                                        solb(-lenght_plate)
                                        POSITION_FOUND =True
                                        
                                if VALUE_SOLUTION == lenght_plate**2 - lenght_plate: #Black Border and white Border-Bottom
                                    solb(-lenght_plate+1)
                                    solb(-lenght_plate)
                                elif VALUE_SOLUTION == 0: #Black Border and white Border-Top
                                    solb(lenght_plate)
                                elif VALUE_SOLUTION > lenght_plate**2 - lenght_plate: #White Border-Bottom
                                    solb(-1)
                                    solb(-lenght_plate +1)
                                    solb(-lenght_plate)
                                elif VALUE_SOLUTION <= (lenght_plate-1) : #WHite Border-Top
                                   solb(lenght_plate)
                                   solb(lenght_plate-1)
                                   solb(-1)
                                
                                elif not POSITION_FOUND:
                                    if Hexa_color[VALUE_SOLUTION-lenght_plate]==black:
                                        next_solution.append(VALUE_SOLUTION - lenght_plate)
                                    if Hexa_color[VALUE_SOLUTION-lenght_plate+1]==black:
                                        next_solution.append(VALUE_SOLUTION - lenght_plate+1)
                                    if Hexa_color[VALUE_SOLUTION-1]==black:
                                        next_solution.append(VALUE_SOLUTION - 1)
                                    if Hexa_color[VALUE_SOLUTION+lenght_plate-1]==black:
                                        next_solution.append(VALUE_SOLUTION + lenght_plate-1)
                                    if Hexa_color[VALUE_SOLUTION+lenght_plate]==black:
                                        next_solution.append(VALUE_SOLUTION + lenght_plate )
                                    
                                passed.append(VALUE_SOLUTION)

        else:
            X=0
        X=0
        title_font = switch_font(50, False, False)
        win_rect = pygame.Rect(325, 110, SIZE_X - 650, 75)
        if WHITE_WON:
            winmessage = title_font.render(langues["white_won"].get(LANG), True, (0 , 0 ,0))
            pygame.draw.rect(screen,white,win_rect)
        elif BLACK_WON:
            winmessage = title_font.render(langues["black_won"].get(LANG), True, (255 , 255 ,255))
            pygame.draw.rect(screen,black,win_rect)
        else:
            continue
        l = 50 
        restart = [(SIZE_X - 100, SIZE_Y-10),
        (SIZE_X - 100 - l*(sqrt(3)/2), SIZE_Y-10-l/2 ),
        (SIZE_X - 100 - l*(sqrt(3)/2), SIZE_Y-10-(3*l)/2 ),
        (SIZE_X - 100, SIZE_Y - 20 - (sqrt(3)*l)),
        (SIZE_X - 100 + l*(sqrt(3)/2), SIZE_Y-10-(3*l)/2 ),
        (SIZE_X - 100 + l*(sqrt(3)/2), SIZE_Y-10-l/2 )
         ]

         #---------ARRORW 
        res_polygon = pygame.draw.polygon(screen, dark_screen_color,restart)
        pygame.draw.polygon(screen, black,restart, 5)
        pygame.draw.line(screen, black,(SIZE_X - 100, SIZE_Y-30),(SIZE_X - 100 - l*(sqrt(3)/2)+20, SIZE_Y-10-l/2 -10),5)
        pygame.draw.line(screen, black,(SIZE_X - 100 - l*(sqrt(3)/2)+20, SIZE_Y-10-l/2 -10),(SIZE_X - 100 - l*(sqrt(3)/2)+20, SIZE_Y-10-(3*l)/2 +10),5)
        pygame.draw.line(screen,black,(SIZE_X - 100 - l*(sqrt(3)/2)+20, SIZE_Y-10-(3*l)/2 +10), (SIZE_X - 100, SIZE_Y - (sqrt(3)*l)),5)
        pygame.draw.line(screen, black, (SIZE_X - 100, SIZE_Y - (sqrt(3)*l)),(SIZE_X - 100 + l*(sqrt(3)/2) - 20, SIZE_Y-10-(3*l)/2 +10),5)
        pygame.draw.line(screen, black, (SIZE_X - 100 + l*(sqrt(3)/2) - 20, SIZE_Y-10-(3*l)/2 +10),(SIZE_X - 100 + l*(sqrt(3)/2)-20, SIZE_Y-10-l/2 -10),5)
        pygame.draw.line(screen, black, (SIZE_X - 100 + l*(sqrt(3)/2)-20, SIZE_Y-10-l/2 -10),(SIZE_X - 95+ (sqrt(3)/4) * 12 , SIZE_Y-25 - l/4),5)
        pygame.draw.line(screen, black,(SIZE_X - 95+ (sqrt(3)/4) * 12 , SIZE_Y-25 - l/4),(SIZE_X - 95+ (sqrt(3)/4) * 12 , SIZE_Y-25 - l/4 -20),5)
        pygame.draw.line(screen, black,(SIZE_X - 95+ (sqrt(3)/4) * 12 , SIZE_Y-25 - l/4),(SIZE_X - 95+ (sqrt(3)/4) * 12 +20 , SIZE_Y-25 - l/4),5)
        #-------------

        if res_polygon.collidepoint(pygame.mouse.get_pos()) and click:
            choosing_lenght()
      
        middle = winmessage.get_rect(center=(SIZE_X/2,147))
        screen.blit(winmessage,middle)
        pygame.display.flip()
        click = False
    

def option():

    """ The Menu Option """

    screen.fill(screen_color)
    title_font = switch_font(75, False, False)
    title = title_font.render(langues["hex_game"].get(LANG), True, (0 , 0 ,0))
    title_rect =title.get_rect(center=(SIZE_X/2, 50))
    screen.blit(title,title_rect)

    running = True
    click = False
    # DARK SCREEN COLOR
    pygame.draw.rect(screen, dark_screen_color, play_button, border_radius= 15)
    pygame.draw.rect(screen, dark_screen_color, option_button, border_radius= 15)
    pygame.draw.rect(screen, dark_screen_color, quit_button, border_radius= 15)
    #SCREEN COLOR
    pygame.draw.rect(screen, screen_color, play_button_2, border_radius= 15)
    pygame.draw.rect(screen, screen_color, option_button_2, border_radius= 15)
    pygame.draw.rect(screen, screen_color, quit_button_2, border_radius= 15)
    #LIGHT EFFECT
    pygame.draw.rect(screen, light_effet, play_button_4, border_radius= 15)
    pygame.draw.rect(screen, light_effet, option_button_4, border_radius= 15)
    pygame.draw.rect(screen, light_effet, quit_button_4, border_radius= 15)
    # Black BORDER
    pygame.draw.rect(screen, black, play_button, 5 ,border_radius= 15)
    pygame.draw.rect(screen, black, option_button, 5, border_radius= 15)
    pygame.draw.rect(screen, black, quit_button, 5, border_radius= 15)

    #TEXT
    font = switch_font(50, False, False)
    play_text = font.render(langues["background-color"].get(LANG), True, (0 , 0 ,0))
    option_text = font.render(langues["languages"].get(LANG), True, (0 , 0 ,0))
    quit_text = font.render(langues["music"].get(LANG), True, (0 , 0 ,0))



    play_rect = play_text.get_rect(center=(SIZE_X/2, SIZE_Y/2 - MARGIN_TOP))
    option_rect = option_text.get_rect(center=(SIZE_X/2, SIZE_Y/2))
    quit_rect = quit_text.get_rect(center=(SIZE_X/2, SIZE_Y/2 + MARGIN_TOP))


    screen.blit(play_text, play_rect)
    screen.blit(option_text, option_rect)
    screen.blit(quit_text, quit_rect)


    button_return = pygame.Rect(10, 10 , 200, 75)
    click_button = pygame.draw.rect(screen, screen_color, button_return)


    back_font = switch_font(50, False, True)
    back_text = back_font.render(" << "+langues["back"].get(LANG), True, black)


    back_center = back_text.get_rect(center=(105, 43))
    

    pygame.draw.rect(screen, black, button_return, 5)
    screen.blit(back_text, back_center)

    click = False
    while running:
        
        mouse_x , mouse_y = pygame.mouse.get_pos()
        if click_button.collidepoint((mouse_x, mouse_y)) and click:
            main()
        if play_button.collidepoint((mouse_x, mouse_y)) and click:
            background_color()
        if option_button.collidepoint((mouse_x, mouse_y)) and click:
            language()
        if quit_button.collidepoint((mouse_x, mouse_y)) and click:
            music_menu()
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                click = True
        pygame.display.flip()

def switch_font(size, bold, italic):
    if LANG in ['fr', 'en', 'gr']:
        font = pygame.font.SysFont(global_font,size, bold, italic)
    elif LANG == 'jp':
        font = pygame.font.Font("Fonts/RocknRollOne-Regular.ttf", size-10)
    elif LANG == 'kr':
        font = pygame.font.Font("Fonts/DoHyeon-Regular.ttf", size)

    return font

def language():
    
    """ Allow the user to change the Langage"""

    global global_font
    global LANG
    try:
        LANG = LANG
    except:
        LANG = "en"
    screen.fill(screen_color)
    title_font = switch_font(75, False, False)


    # --- Flag Images
    fr_flag = pygame.image.load("Flags/fr.svg")
    us_flag = pygame.image.load("Flags/us.png")
    jp_flag = pygame.image.load("Flags/jp.svg")
    kr_flag = pygame.image.load("Flags/kr.png")
    gr_flag = pygame.image.load("Flags/gr.svg")
    kr_flag.convert()
    #---Rescale
    HEIGHT_FLAG = 133
    WIDTH_FLAG = 200
    fr_flag = pygame.transform.scale(fr_flag, (WIDTH_FLAG, HEIGHT_FLAG))
    us_flag = pygame.transform.scale(us_flag, (WIDTH_FLAG, HEIGHT_FLAG))
    jp_flag = pygame.transform.scale(jp_flag, (WIDTH_FLAG, HEIGHT_FLAG))
    kr_flag = pygame.transform.scale(kr_flag, (WIDTH_FLAG, HEIGHT_FLAG))
    gr_flag = pygame.transform.scale(gr_flag, (WIDTH_FLAG, HEIGHT_FLAG))
    kr_flag.convert()
    #---Showing Images
    screen.blit(fr_flag, [SIZE_X/2 - WIDTH_FLAG - 12, 100])
    screen.blit(us_flag, [SIZE_X/2 + 12, 100])
    screen.blit(jp_flag, [SIZE_X/2 - WIDTH_FLAG - 12, 100 + HEIGHT_FLAG + 25])
    screen.blit(kr_flag, [SIZE_X/2 + 12, 100 + HEIGHT_FLAG + 25])
    screen.blit(gr_flag, [SIZE_X/2 - WIDTH_FLAG/2, 100 + HEIGHT_FLAG*2 + 50])

    fr_rect = pygame.Rect(SIZE_X/2 - WIDTH_FLAG - 12, 100, WIDTH_FLAG, HEIGHT_FLAG)
    en_rect = pygame.Rect(SIZE_X/2 + 12, 100, WIDTH_FLAG, HEIGHT_FLAG)
    jp_rect = pygame.Rect(SIZE_X/2 - WIDTH_FLAG - 12, 100 + HEIGHT_FLAG + 25, WIDTH_FLAG, HEIGHT_FLAG)
    kr_rect = pygame.Rect(SIZE_X/2 + 12, 100 + HEIGHT_FLAG + 25, WIDTH_FLAG, HEIGHT_FLAG)
    gr_rect = pygame.Rect(SIZE_X/2 - WIDTH_FLAG/2, 100 + HEIGHT_FLAG*2 + 50, WIDTH_FLAG, HEIGHT_FLAG)

    running = True
    click = False
    while running:
        #TITLE
        title = title_font.render(langues["hex_game"].get(LANG), True, (0 , 0 ,0))
        title_rect =title.get_rect(center=(SIZE_X/2, 50))
        screen.blit(title,title_rect)


        #Back Button
        button_return = pygame.Rect(10, 10 , 200, 75)
        click_button = pygame.draw.rect(screen, screen_color, button_return)
        back_font = switch_font(50, False, True)
        back_text = back_font.render(" << "+langues["back"].get(LANG), True, black)

        back_center = back_text.get_rect(center=(105, 43))
        
        pygame.draw.rect(screen, black, button_return, 5)
        screen.blit(back_text, back_center)

        mouse_x , mouse_y = pygame.mouse.get_pos()
        if click_button.collidepoint((mouse_x, mouse_y)) and click:
            option()
        if fr_rect.collidepoint((mouse_x, mouse_y)) and click:
            LANG = "fr"
            language()
        if en_rect.collidepoint((mouse_x, mouse_y)) and click:
            LANG = "en"
            language()
        if jp_rect.collidepoint((mouse_x, mouse_y)) and click:
            LANG = "jp"
            language()
        if kr_rect.collidepoint((mouse_x, mouse_y)) and click:
            LANG = "kr"
            language()
        if gr_rect.collidepoint((mouse_x, mouse_y)) and click:
            LANG = "gr"
            language()


        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                click = True
        pygame.display.flip()

def music_menu():

    """Allow the user to change the language"""

    screen.fill(screen_color)
    title_font = switch_font(75, False, False)

    #TITLE
    title = title_font.render(langues["hex_game"].get(LANG), True, (0 , 0 ,0))
    title_rect =title.get_rect(center=(SIZE_X/2, 50))
    screen.blit(title,title_rect)

    #Back Button
    button_return = pygame.Rect(10, 10 , 200, 75)
    click_button = pygame.draw.rect(screen, screen_color, button_return)
    back_font = switch_font(50, False, True)
    back_text = back_font.render(" << "+langues["back"].get(LANG), True, black)

    back_center = back_text.get_rect(center=(105, 43))
    
    pygame.draw.rect(screen, black, button_return, 5)
    screen.blit(back_text, back_center)

    volume = 100
    vol_text = back_font.render( str(volume) + "%", True, black)
    vol_rect = back_text.get_rect(center=(SIZE_X/2,SIZE_Y/2 +100))
    screen.blit(vol_text, vol_rect)

    sound_font = switch_font(70, False, False)
    sound_text = sound_font.render(langues["vol_music"].get(LANG), True, black)
    sound_rect =title.get_rect(center=(SIZE_X/2, SIZE_Y/2 -100))

    screen.blit(sound_text, sound_rect)

    change_volume_background = pygame.Rect(100, SIZE_Y/2 -50, SIZE_X - 200, 100 )
    change_volume_frame = pygame.Rect(95, SIZE_Y/2 -55, SIZE_X - 190, 110 )

    pygame.draw.rect(screen, black, change_volume_frame)
    pygame.draw.rect(screen, light_effet, change_volume_background)

    running = True
    click = False

    while running:
        pygame.display.flip()

        mouse_x , mouse_y = pygame.mouse.get_pos()


        if click_button.collidepoint((mouse_x, mouse_y)) and click:
            option()

        if change_volume_background.collidepoint((mouse_x, mouse_y)) and click:
            volume = round((((mouse_x -100 )/( SIZE_X -100)) * 100) * (10/8.97), 1)
            vol_text = back_font.render( str(volume) + "%", True, black)
            vol_rect = back_text.get_rect(center=(SIZE_X/2,SIZE_Y/2 +100))
            change_volume = pygame.Rect(100, SIZE_Y/2 -50, mouse_x-100, 100 )
            pygame.draw.rect(screen, gray, change_volume_background)
            pygame.draw.rect(screen, light_effet, change_volume)
            pygame.draw.rect(screen, screen_color, vol_rect)
            screen.blit(vol_text, vol_rect)
            music.set_volume(volume/100)

        if not change_volume_background.collidepoint((mouse_x, mouse_y)):
            click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                click = True
        pygame.display.flip()
        
def background_color():

    """ Allow the user to change the background color"""

    #-------------------------------
    #
    #          COLORS
    #
    #--------------------------------

    global screen_color
    global dark_screen_color
    global light_effet

    #----------------------------

    blue = (0, 215, 255)
    d_blue = (0, 185, 225)
    l_blue = ( 165, 245, 255)

    green = (0, 255, 0)
    d_green = (0, 225, 0)
    l_green = (165, 255, 165)

    red = ( 255, 0, 0 )
    d_red = ( 225, 0, 0 )
    l_red = ( 255, 165, 165 )


    #-------------------------------
    screen.fill(screen_color)
    title_font = switch_font(75, False, False)

    #TITLE
    title = title_font.render(langues["hex_game"].get(LANG), True, (0 , 0 ,0))
    title_rect =title.get_rect(center=(SIZE_X/2, 50))
    screen.blit(title,title_rect)

    #Back Button
    button_return = pygame.Rect(10, 10 , 200, 75)
    click_button = pygame.draw.rect(screen, screen_color, button_return)
    back_font = switch_font(50, False, True)
    back_text = back_font.render(" << "+langues["back"].get(LANG), True, black)

    back_center = back_text.get_rect(center=(105, 43))
    
    pygame.draw.rect(screen, black, button_return, 5)
    screen.blit(back_text, back_center)


    running = True
    click = False
    lenght_square = 200
    def button(color, x, y):
        button_color = pygame.Rect(x, y, lenght_square, lenght_square)
        button_color_frame = pygame.Rect(x-5, y-5 , lenght_square + 10, lenght_square + 10)
        return_rect = pygame.draw.rect(screen, black, button_color_frame)
        pygame.draw.rect(screen, color, button_color)
        return return_rect


    while running:
        pygame.display.flip()

        mouse_x , mouse_y = pygame.mouse.get_pos()

        blue_button = button(blue, SIZE_X/2 - 210, 100)
        green_button = button(green, SIZE_X/2 + 5, 100)
        main_button = button(( 255 , 224 , 0), SIZE_X/2 - 210, 315)
        red_button = button(red, SIZE_X/2 + 5, 315)

        if click_button.collidepoint((mouse_x, mouse_y)) and click:
            option()
        if blue_button.collidepoint((mouse_x, mouse_y)) and click:
            screen_color = blue
            dark_screen_color = d_blue
            light_effet = l_blue
        if green_button.collidepoint((mouse_x, mouse_y)) and click:
            screen_color = green
            dark_screen_color = d_green
            light_effet = l_green
        if main_button.collidepoint((mouse_x, mouse_y)) and click:
            screen_color = ( 255 , 224 , 0)
            dark_screen_color = (225, 200, 0)
            light_effet = (252, 244, 164)
        if red_button.collidepoint((mouse_x, mouse_y)) and click:
            screen_color = red
            dark_screen_color = d_red
            light_effet = l_red
        if click:
            screen.fill(screen_color)
            screen.blit(title,title_rect)
            pygame.draw.rect(screen, black, button_return, 5)
            screen.blit(back_text, back_center)




        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                click = True
        pygame.display.flip()

main()