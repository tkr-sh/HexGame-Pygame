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
sound = pygame.mixer.Sound("Music/button_hover.mp3")

mainClock = pygame.time.Clock()


#-----Restoration of data
cookie = open("info.txt",'r')
all_txt = cookie.readlines()
for i in range(len(all_txt)):
    all_txt[i] = all_txt[i].replace("\n","")
r, g, b, LANG, global_font, volume = all_txt
music.set_volume(int(volume)/100)
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
#-----------Colors

var_red = var_green = var_blue = False

if int(r) > 235 and int(g) > 235 and int(b) > 235:
    screen_color = (235,235,235)
elif int(r) < 50 and int(g) < 50 and int(b) < 50:
    screen_color = (50, 50, 50)
else:
    screen_color = ( int(r) , int(g) , int(b)) #255 , 224 , 0
print(screen_color)

dark_screen_color = (int(round(float(r)/1.13,0)) , int(round(float(g)/1.13,0)) , int(round(float(b)/1.13,0))) #225, 200, 0

def light_color(x):
    y = int(165.0 + float(90/255)*float(x))
    y = min(y, 255)
    return y

light_effet = (light_color(r), light_color(g), light_color(b)) #252, 244, 164
darker_color = ( max( int(r) - 50 , 0),max( int(g) - 50 , 0),max( int(b) - 50 , 0))
white = (255 , 255 , 255)
black = (0 , 0 , 0)
beige = (230, 215, 188)
gray = (200, 200, 200)
d_gray = (32, 32, 32)
l_gray = (230, 230, 230)


# ----- Screen
screen = pygame.display.set_mode((SIZE_X, SIZE_Y), pygame.RESIZABLE )#, pygame.RESIZABLE
screen.fill(screen_color)
pygame.display.flip()


#---Button 
def switch_font(size, bold, italic):
    # --- Roboto
    if LANG in ['fr', 'en', 'gr', 'sw']:
        font =  pygame.font.SysFont(global_font,size, bold, italic)

    # --- Japanese
    elif LANG == 'jp':
        font = pygame.font.Font("Fonts/MPLUSRounded1c-Medium.ttf", size-10)

    # --- Korean
    elif LANG == 'kr':
        font = pygame.font.Font("Fonts/DoHyeon-Regular.ttf", size)
    a_file = open("info.txt", "r")
    list_of_lines = a_file.readlines()
    list_of_lines[4] = str(font)+"\n"

    with open("info.txt", "w") as a_file:
        a_file.writelines(list_of_lines)

    return font

def text(txt,x,y,z,color,bold, italic):
    font = switch_font(z, bold, italic)
    text2 = font.render(langues[txt].get(LANG), True, color)
    screen.blit(text2, (x,y))

def main_button(txt,x,y,color):
    font = switch_font(75,False,False)
    play_text = font.render("> "+langues[txt].get(LANG), True, color)
    rect = pygame.Rect(x, y , SIZE_X/2.5, 80)
    f_rect = pygame.draw.rect(screen, screen_color, rect )
    screen.blit(play_text, (x, y))
    return  f_rect

def exit_sys(event):
    if event.type == pygame.QUIT:
        sys.exit()
'''
def animation(button, text,y ):

    mouse_x , mouse_y = pygame.mouse.get_pos()
    if not button.collidepoint((mouse_x, mouse_y)):
        button = main_button(text,SIZE_X/15,y,black)
        var = True 
    try:
        if button.collidepoint((mouse_x, mouse_y)) and var:
            for _ in range(50):
                button = main_button(text,SIZE_X/15+_,y,(int(5.1 * _),int(5.1 * _),int(5.1 * _)))
                pygame.display.flip()
            var = False
    except UnboundLocalError:
        if button.collidepoint((mouse_x, mouse_y)):
            for _ in range(50):
                button = main_button(text,SIZE_X/15+_,y,(int(5.1 * _),int(5.1 * _),int(5.1 * _)))
                pygame.display.flip()
            var = False
'''
def menu():
    screen.fill(screen_color)
    running = True
    click = True
    var_time = 0
    previousClock = 0
    time_loop = 0
    play_button = main_button("play",SIZE_X/15,2*SIZE_Y/5 ,black)
    option_button = main_button("option",SIZE_X/15,3*SIZE_Y/5 - 30,black)
    quit_button = main_button("quit",SIZE_X/15,4*SIZE_Y/5 - 60,black)
    if LANG == 'jp':
        text("hex_game",SIZE_X/20,SIZE_Y/5 - 30, 100, black, False, False)
    else:
        text("hex_game",SIZE_X/20,SIZE_Y/5 - 30, 150, black, False, False)
    text("v",SIZE_X- 75,SIZE_Y - 30, 25, black, False, False)
    rect = pygame.Rect(SIZE_X/15, 2*SIZE_Y/5 , 30, SIZE_Y/2)
    pygame.draw.rect(screen, screen_color, rect )
    while running:

        #-----Play Button
        mouse_x , mouse_y = pygame.mouse.get_pos()

        if not play_button.collidepoint((mouse_x, mouse_y)):
            play_button = main_button("play",SIZE_X/15,2*SIZE_Y/5,black)
            var = True 
        if play_button.collidepoint((mouse_x, mouse_y)) and var:
            for _ in range(20):
                play_button = main_button("play",SIZE_X/15+_*2,2*SIZE_Y/5,(int(12.75 * _),int(12.75 * _),int(12.75 * _)))
                pygame.draw.rect(screen, screen_color, rect )
                pygame.display.flip()
            sound.play()
            var = False
        if play_button.collidepoint((mouse_x, mouse_y)) and click:
            game_menu()

        #-------Option Button
        if not option_button.collidepoint((mouse_x, mouse_y)):
            option_button = main_button("option",SIZE_X/15,3*SIZE_Y/5 - 30,black)
            var_opt = True 
        if option_button.collidepoint((mouse_x, mouse_y)) and var_opt:
            for _ in range(20):
                option_button = main_button("option",SIZE_X/15+_*2,3*SIZE_Y/5 -30,(int(12.75 * _),int(12.75 * _),int(12.75 * _)))
                pygame.draw.rect(screen, screen_color, rect )
                pygame.display.flip()
            sound.play()

            var_opt = False
        if option_button.collidepoint((mouse_x, mouse_y)) and click:
            langue(0)

        #-------Quit Button
        if not quit_button.collidepoint((mouse_x, mouse_y)):
            quit_button = main_button("quit",SIZE_X/15,4*SIZE_Y/5 - 60,black)
            var_qt = True 
        if quit_button.collidepoint((mouse_x, mouse_y)) and var_qt:
            for _ in range(20):
                quit_button = main_button("quit",SIZE_X/15+_*2,4*SIZE_Y/5 - 60,(int(12.75 * _),int(12.75 * _),int(12.75 * _)))
                pygame.draw.rect(screen, screen_color, rect )
                pygame.display.flip()
            sound.play()
            var_qt = False
        if quit_button.collidepoint((mouse_x, mouse_y)) and click:
            sys.exit()
        var_time += pygame.time.get_ticks() - previousClock
        previousClock = pygame.time.get_ticks()
        #print(pygame.time.get_ticks())
        if var_time > 15000:
            var_time = 0
            time_loop += 1
            if time_loop == 4:
                time_loop = 0
            def load_image(x,img_name,img_txt, img_txt2):
                if time_loop == x:
                    #For text bg
                    bg_rect = pygame.Rect(SIZE_X/2, 4*SIZE_Y/5 , SIZE_X/2, 90)
                    pygame.draw.rect(screen, screen_color, bg_rect )
                    # For Image bf
                    SIZE_IMG = 400
                    bg_rect_img = pygame.Rect(4*SIZE_X/5 - 200,4*SIZE_Y/5 - 400,SIZE_IMG,SIZE_IMG)
                    #Image
                    pygame.draw.rect(screen, screen_color, bg_rect_img )
                    image = pygame.image.load("Icon/"+img_name+".png")
                    image = pygame.transform.scale(image, (SIZE_IMG, SIZE_IMG))
                    screen.blit(image, [4*SIZE_X/5 - 200,4*SIZE_Y/5 - 400])
                    #Text to describe image
                    font = switch_font(30, False, False)
                    text_img = font.render(langues[img_txt].get(LANG), True, black)
                    text_rect = text_img.get_rect(center=(4*SIZE_X/5,4*SIZE_Y/5 + 30))
                    text_img2 = font.render(langues[img_txt2].get(LANG), True, black)
                    text_rect2 = text_img2.get_rect(center=(4*SIZE_X/5,4*SIZE_Y/5 + 60))
                    screen.blit(text_img, text_rect)
                    screen.blit(text_img2, text_rect2)
            load_image(0,"github","github","github2")
            load_image(1,"paint","custom_color","custom_color2")
            load_image(2,"logo_menu","mode","mode2")
            load_image(3,"flags","flags"," ")

        click = False
        for event in pygame.event.get():
            exit_sys(event)
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                click = True
        pygame.draw.rect(screen, screen_color, rect )
        pygame.display.flip()


def play(x, img, ico, txt,des,des2):

    #---Rect
    play_rect = pygame.Rect(x,SIZE_Y/3,SIZE_X/5,SIZE_Y/2)
    header_rect = pygame.Rect(x,SIZE_Y/3,SIZE_X/5,SIZE_Y/15)
    text_rect = pygame.Rect(x,SIZE_Y/3 + 0.3 *SIZE_Y,SIZE_X/5,3*SIZE_Y/15)
    pygame.draw.rect(screen, d_gray, header_rect)
    pygame.draw.rect(screen, gray, text_rect)
    
    #---Image
    image = pygame.image.load("Icon/"+img+".png")
    image = pygame.transform.scale(image, (int(SIZE_X/5), int(SIZE_X/5)))
    screen.blit(image, [x,SIZE_Y/3 + SIZE_Y/15])

    #---icon
    icon = pygame.image.load("Icon/"+ico+".png")
    icon = pygame.transform.scale(icon, (30, 30))
    rect_icon = icon.get_rect(center=(x + SIZE_X/10,SIZE_Y/3 + 0.3 *SIZE_Y+60))
    screen.blit(icon, rect_icon)

    #---Title
    font = switch_font(47, False, False)
    title_header = font.render(langues[txt].get(LANG), True, white)
    header_text = title_header.get_rect(center = ( x + SIZE_X/10 , SIZE_Y/3 + SIZE_Y/30))
    screen.blit(title_header, header_text)

    #---Description
    if LANG == 'gr':
        font_des = switch_font(15, False, False)
    else:
        font_des = switch_font(20, False, False)
    des = font_des.render(langues[des].get(LANG), True, black)
    des_text = des.get_rect(center = ( x + SIZE_X/10 , SIZE_Y/3 + SIZE_Y/2.4))
    screen.blit(des, des_text)

    des2 = font_des.render(langues[des2].get(LANG), True, black)
    des_text2 = des2.get_rect(center = ( x + SIZE_X/10 , SIZE_Y/3 + SIZE_Y/2.25))
    screen.blit(des2, des_text2)


    return play_rect

def play_hover(button,x,y,z, img, ico, txt,des,des2,click,function,para):
    if not button.collidepoint((x,y)):
        pygame.draw.rect(screen, screen_color, pygame.Rect(z - 5 ,SIZE_Y/3 - 5 ,SIZE_X/5 +10 ,SIZE_Y/2 + 10))
    elif button.collidepoint((x,y)) and click:
        if para =="":
            function()
        else: 
            function(para)
    elif button.collidepoint((x,y)):
        pygame.draw.rect(screen, white, pygame.Rect(z - 5 ,SIZE_Y/3 - 5 ,SIZE_X/5 +10 ,SIZE_Y/2 + 10))
    play(z,img,ico,txt,des,des2)


bool_hover = False
def back_button(mx,my, click):
    global bool_hover
    x=100
    arrow = [ (x,75), 
    (x+20,30),
    (x+40,30),
    (x+20,75),
    (x+40,120),
    (x+20,120)
    ]
    anti_arrow = [ (0,28),
    (x+18,28),
    (x-2,75),
    (x+18,122),
    (0,122)
    ]
    anti_anti_arrow = [ (x+42,30),
    (x+22,75),
    (x+42,120),
    (300,120),
    (300,30)
    ]


    s = pygame.Surface((40,90))  # the size of your rect
    s.set_alpha(0)                # alpha level
    s.fill((255,255,255))           # this fills the entire surface
    screen.blit(s, (100,30))
    if not screen.blit(s, (100,30)).collidepoint((mx,my)):
        _extracted_from_back_button_30(arrow, anti_arrow)
        pygame.draw.polygon(screen, dark_screen_color, anti_anti_arrow)
        bool_hover = False
    elif screen.blit(s, (100,30)).collidepoint((mx,my)) and not bool_hover:
        for _ in range(15):
            pygame.draw.polygon(screen, dark_screen_color, arrow)
            pygame.draw.polygon(screen, dark_screen_color, arrow,4)
            x -= 4
            text_rectt = pygame.Rect(x+20,40,-3.5 * (x-100),70)
            pygame.draw.rect(screen, light_effet, text_rectt)
            if LANG in {'jp','kr'}:
                back_font = switch_font(50, False, False)
            else:
                back_font = switch_font(75, False, False)
            text_back = back_font.render(langues["back"].get(LANG), True, black)
            screen.blit(text_back, (70, 53))
            arrow = [ (x,75), (x+20,30),(x+40,30),(x+20,75),(x+40,120),(x+20,120)]
            anti_arrow = [ (0,28),(x+18,28),(x-2,75),(x+18,122),(0,122)]
            _extracted_from_back_button_30(arrow, anti_arrow)
            pygame.display.flip()
        bool_hover = True
    elif screen.blit(s, (100,30)).collidepoint((mx,my)) and click:
        menu()

    return arrow

def _extracted_from_back_button_30(arrow, anti_arrow):
    pygame.draw.polygon(screen, white, arrow)
    pygame.draw.polygon(screen, black, arrow,4)
    pygame.draw.polygon(screen, dark_screen_color, anti_arrow)

def game_menu():

    screen.fill(screen_color)

    #Header
    Header = pygame.Rect(0,0,SIZE_X, 150)
    pygame.draw.rect(screen, dark_screen_color, Header)
    
    #-----Title
    font = switch_font(100, False, False)

    title = font.render(langues["play"].get(LANG), True, white)
    title_border = font.render(langues["play"].get(LANG), True, black )

    rect_title = title.get_rect(center=(SIZE_X/2,75))
    rect_title_bl = title.get_rect(center=(SIZE_X/2-2,73))
    rect_title_br = title.get_rect(center=(SIZE_X/2+2,73))
    rect_title_tl = title.get_rect(center=(SIZE_X/2-2,77))
    rect_title_tr = title.get_rect(center=(SIZE_X/2+2,77))
    screen.blit(title_border, rect_title_bl)
    screen.blit(title_border, rect_title_br)
    screen.blit(title_border, rect_title_tr)
    screen.blit(title_border, rect_title_tl)
    screen.blit(title, rect_title)
    
    local_button = play(SIZE_X/25,"local","house","local","des_local","des_local2")
    online_button = play(SIZE_X/5 + (SIZE_X/25)*2,"online","WWW","online","des_online","des_online2")
    ia_button = play(2*(SIZE_X/5)+ (SIZE_X/25)*3,"IA","ai","Computer","des_ia","des_ia2")
    _button = play(3*(SIZE_X/5)+ (SIZE_X/25)*4,"?","?2","?"," ", " ")

    #-------
    
    click = False
    pygame.display.flip()
    while 1:
        mouse_x , mouse_y = pygame.mouse.get_pos()
        back_button(mouse_x,mouse_y,click)
        play_hover(local_button,mouse_x,mouse_y,SIZE_X/25, "local","house","local","des_local","des_local2",click,choosing_lenght,"")
        play_hover(online_button,mouse_x,mouse_y,SIZE_X/5 + (SIZE_X/25)*2,"online","WWW","online","des_online","des_online2",click,menu,"")
        play_hover(ia_button,mouse_x,mouse_y,2*(SIZE_X/5)+ (SIZE_X/25)*3,"IA","ai","Computer","des_ia","des_ia2",click,menu,"")
        play_hover(_button,mouse_x,mouse_y,3*(SIZE_X/5)+ (SIZE_X/25)*4,"?","?2","?"," ", " ",click,menu,"")




        click = False
        for event in pygame.event.get():
            exit_sys(event)
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                click = True
        pygame.display.flip()


def flag_icon(flag,color,nb,txt,x,y,click,page):
    global LANG
    flag = pygame.image.load(f"Flags/{flag}.png")
    flag.convert()
    #---Rescale
    HEIGHT_FLAG = 33
    WIDTH_FLAG = 50
    flag = pygame.transform.scale(flag, (WIDTH_FLAG, HEIGHT_FLAG))
    margin = 50
    # --- Main
    flag_rect = pygame.Rect(margin,300+nb*80,SIZE_X - 2*margin, 60)
    pygame.draw.rect(screen, l_gray, flag_rect, border_radius= 5)
    # --- Left-border
    flag_rect_lborder = pygame.Rect(margin,300+nb*80,10, 60)
    flag_rect_lborder2 = pygame.Rect(margin+5,300+nb*80,10, 60)
    pygame.draw.rect(screen, color, flag_rect_lborder, border_radius= 5)
    pygame.draw.rect(screen, color, flag_rect_lborder2)
    screen.blit(flag, [margin + 20, 310+nb*80])
    # --- txt 
    if LANG in {'jp', 'kr'}:
        flag_font =  switch_font(45, False, False)
    else:
        flag_font =  switch_font(60, False, False)
    flag_txt = flag_font.render(langues[txt].get(LANG), True, black)
    screen.blit(flag_txt,(margin + WIDTH_FLAG + 20,310+nb*80))

    if flag_rect.collidepoint((x,y)) and click:
        LANG = txt
        a_file = open("info.txt", "r")
        list_of_lines = a_file.readlines()
        list_of_lines[3] = str(txt)+"\n"

        with open("info.txt", "w") as a_file:
            a_file.writelines(list_of_lines)

        langue(page)

    
def underHeaderButton(x,y,nb,txt,click):
    if LANG =='gr':
        under_font =  switch_font(45, False, False)
    else:
        under_font =  switch_font(60, False, False)
    under_rect = pygame.Rect(nb * SIZE_X/3,150,SIZE_X/3,100 )
    under_txt = under_font.render(langues[txt].get(LANG), True, black)
    under_center = under_txt.get_rect(center=( (2*nb+1) * SIZE_X / 6,200))
    if pygame.draw.rect(screen, screen_color,under_rect).collidepoint((x,y)) and click:
        if txt=='languages':
            langue(0)
        elif txt == 'background-color':
            background_color()
        else:
            sound_menu()
    if pygame.draw.rect(screen, screen_color,under_rect).collidepoint((x,y)):
        pygame.draw.rect(screen, darker_color,under_rect)
    screen.blit(under_txt, under_center)

def triangle_back(x,y,click):
    arrow = [(100,30), (100, 120) , (33,75)]
    arrow_rect = pygame.draw.polygon(screen,white,arrow)
    if arrow_rect.collidepoint((x,y)) and click:
        menu()


def langue(page):
    #Header
    screen.fill(light_effet)
    Header = pygame.Rect(0,0,SIZE_X, 150)
    pygame.draw.rect(screen, dark_screen_color, Header)
    underHeader = pygame.Rect(0,150,SIZE_X, 100)
    pygame.draw.rect(screen, screen_color, underHeader)
    #-----Title
    font = switch_font(110, False, False)
    #---LAnguage

    title = font.render(langues["option"].get(LANG), True, white)
    rect_title = title.get_rect(center=(SIZE_X/2,75))
    screen.blit(title, rect_title)
    click = False

    # --- Switch Page

    arrow = font.render(">", True, black)
    rect_arrow = arrow.get_rect(center=(SIZE_X - 25, 490))
    screen.blit(arrow, rect_arrow)


    while 1:

        mouse_x, mouse_y = pygame.mouse.get_pos()

        triangle_back(mouse_x,mouse_y,click)
        underHeaderButton(mouse_x,mouse_y,0,"languages",click)
        underHeaderButton(mouse_x,mouse_y,1,"background-color",click)
        underHeaderButton(mouse_x,mouse_y,2,"music",click)


        if rect_arrow.collidepoint((mouse_x,mouse_y)) and click:
            next_page = page + 1
            if next_page > 1:
                next_page = 0
            langue(next_page)

        if page == 0:
            flag_icon('fr',(0, 85, 164),0,'fr',mouse_x,mouse_y,click,page)
            flag_icon('us',(178, 34, 52),1,'en',mouse_x,mouse_y,click,page)
            flag_icon('jp',(188, 0, 45),2,'jp',mouse_x,mouse_y,click,page)
            flag_icon('kr',(0,0,0),3,'kr',mouse_x,mouse_y,click,page)
            flag_icon('gr',(13, 94, 175),4,'gr',mouse_x,mouse_y,click,page)
        else:
            flag_icon('sw',(0, 106, 168),0,'sw',mouse_x,mouse_y,click,page)
        click = False
        for event in pygame.event.get():
            exit_sys(event)
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                click = True
        pygame.display.flip()


def slider(x,y,nb,color,realcolor):
    global var_red, var_green, var_blue
    change_volume_frame = pygame.Rect(95, SIZE_Y/2 -55+ nb * SIZE_Y/5, SIZE_X - 190, 110 )
    pygame.draw.rect(screen, black, change_volume_frame)
    change_volume_background = pygame.Rect(100, SIZE_Y/2 -50 + nb * SIZE_Y/5 , SIZE_X - 200, 100 )
    pygame.draw.rect(screen, gray, change_volume_background)
    change_volume_basic = pygame.Rect(100, SIZE_Y/2 -50 + nb * SIZE_Y/5, (SIZE_X-100)*int(realcolor)/255-100, 100 )
    if color == 'r':
        pygame.draw.rect(screen, (int(realcolor),0,0), change_volume_basic)
        varf = var_red
    elif color == 'g':
        pygame.draw.rect(screen, (0,int(realcolor),0), change_volume_basic)
        varf = var_green
    else:
        pygame.draw.rect(screen, (0,0,int(realcolor)), change_volume_basic)
        varf = var_blue
    if change_volume_background.collidepoint((x,y)) and varf:
        degre = _extracted_from_slider_18(x, nb, color, change_volume_background)
    if not change_volume_background.collidepoint((x,y)):
        if color == 'r':
            var_red = False
        elif color == 'g':
            var_green = False
        else:
            var_blue = False
    try:
        if degre is None:
            degre = realcolor
    except UnboundLocalError:
        degre = realcolor
    return degre

def _extracted_from_slider_18(x, nb, color, change_volume_background):
    result = int(round((((x -100 )/( SIZE_X -100)) * 100) * (10/8.97), 0))*2.55
    result = min(result, 255)
    result = max(result, 0)
    change_volume = pygame.Rect(100, SIZE_Y/2 -50 + nb * SIZE_Y/5, x-100, 100 )
    a_file = open("info.txt", "r")
    list_of_lines = a_file.readlines()
    if color == 'r':
        color2 = result, 0, 0
        list_of_lines[0] = str(int(result)) + "\n"

    elif color == 'g':
        color2 = 0, result, 0
        list_of_lines[1] = str(int(result)) + "\n"
    else:
        color2 = 0, 0, result
        list_of_lines[2] = str(int(result)) + "\n"

    with open("info.txt", "w") as a_file:
        a_file.writelines(list_of_lines)
    pygame.draw.rect(screen, gray, change_volume_background)
    pygame.draw.rect(screen, color2, change_volume)
    return result


def background_color():
    global var_red, var_green, var_blue
    global r, g, b , screen_color, light_effet, dark_screen_color, darker_color
    Header = pygame.Rect(0,0,SIZE_X, 150)
    underHeader = pygame.Rect(0,150,SIZE_X, 100)
    #-----Title
    font = switch_font(110, False, False)
    #---LAnguage

    title = font.render(langues["option"].get(LANG), True, white)
    rect_title = title.get_rect(center=(SIZE_X/2,75))
    click = False
    while 1:
        screen.fill(light_effet)
        pygame.draw.rect(screen, dark_screen_color, Header)
        pygame.draw.rect(screen, screen_color, underHeader)
        screen.blit(title, rect_title)
        mouse_x, mouse_y = pygame.mouse.get_pos()#54654865424654868
        r = slider(mouse_x,mouse_y,0,'r',r)
        g = slider(mouse_x,mouse_y,1,'g',g)
        b = slider(mouse_x,mouse_y,2,'b',b)

        triangle_back(mouse_x,mouse_y,click)
        underHeaderButton(mouse_x,mouse_y,0,"languages",click)
        underHeaderButton(mouse_x,mouse_y,1,"background-color",click)
        underHeaderButton(mouse_x,mouse_y,2,"music",click)


        # ---- CHanging COLORS

        if int(r) > 235 and int(g) > 235 and int(b) > 235:
            screen_color = (235,235,235)
        elif int(r) < 50 and int(g) < 50 and int(b) < 50:
            screen_color = (50, 50, 50)
        else:
            screen_color = ( int(r) , int(g) , int(b)) #255 , 224 , 0

        dark_screen_color = (int(round(float(r)/1.13,0)) , int(round(float(g)/1.13,0)) , int(round(float(b)/1.13,0))) #225, 200, 0

        light_effet = (light_color(r), light_color(g), light_color(b)) #252, 244, 164
        darker_color = ( max( int(r) - 50 , 0),max( int(g) - 50 , 0),max( int(b) - 50 , 0))

        # -----------

        if click:
            var_red = not var_red
            var_green = not var_green
            var_blue = not var_blue
            
        click = False
        for event in pygame.event.get():
            exit_sys(event)
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                click = True
        pygame.display.flip()

def sound_menu():

    global volume

    Header = pygame.Rect(0,0,SIZE_X, 150)
    underHeader = pygame.Rect(0,150,SIZE_X, 100)
    #-----Title
    font = switch_font(110, False, False)
    #---LAnguage

    title = font.render(langues["option"].get(LANG), True, white)
    rect_title = title.get_rect(center=(SIZE_X/2,75))

    screen.fill(light_effet)
    pygame.draw.rect(screen, dark_screen_color, Header)
    pygame.draw.rect(screen, screen_color, underHeader)
    screen.blit(title, rect_title)

    back_font = switch_font(50, False, True)
    vol_text = back_font.render( str(volume) + "%", True, black)
    vol_rect = vol_text.get_rect(center=(SIZE_X/2,SIZE_Y/1.75 +100))
    screen.blit(vol_text, vol_rect)

    sound_font = switch_font(70, False, False)
    sound_text = sound_font.render(langues["vol_music"].get(LANG), True, black)
    sound_rect = sound_text.get_rect(center=(SIZE_X/2, SIZE_Y/1.75 -100))

    screen.blit(sound_text, sound_rect)

    change_volume_background = pygame.Rect(100, SIZE_Y/1.75 -50, SIZE_X - 200, 100 )
    change_volume_frame = pygame.Rect(95, SIZE_Y/1.75 -55, SIZE_X - 190, 110 )

    pygame.draw.rect(screen, black, change_volume_frame)
    pygame.draw.rect(screen, screen_color, change_volume_background)


    click = False
    click_slider = False
    while 1:

        mouse_x, mouse_y = pygame.mouse.get_pos()

        triangle_back(mouse_x,mouse_y,click)

        if change_volume_background.collidepoint((mouse_x, mouse_y)) and click_slider:
            volume = round((((mouse_x -100 )/( SIZE_X -100)) * 100) * (10/8.97), 1)
            vol_text = back_font.render( str(volume) + "%", True, black)
            vol_rect = vol_text.get_rect(center=(SIZE_X/2,SIZE_Y/1.75 +100))
            vol_rect2 = pygame.Rect(100,SIZE_Y/1.75 + 55,SIZE_X - 190, 110)
            change_volume = pygame.Rect(100, SIZE_Y/1.75 -50, mouse_x-100, 100 )
            pygame.draw.rect(screen, gray, change_volume_background)
            pygame.draw.rect(screen, screen_color, change_volume)
            pygame.draw.rect(screen, light_effet, vol_rect2)
            screen.blit(vol_text, vol_rect)
            music.set_volume(volume/100)
            a_file = open("info.txt", "r")
            list_of_lines = a_file.readlines()
            list_of_lines[5] = str(int(volume)) + "\n"

            with open("info.txt", "w") as a_file:
                a_file.writelines(list_of_lines)

        if not change_volume_background.collidepoint((mouse_x, mouse_y)):
            click_slider = False

        underHeaderButton(mouse_x,mouse_y,0,"languages",click)
        underHeaderButton(mouse_x,mouse_y,1,"background-color",click)
        underHeaderButton(mouse_x,mouse_y,2,"music",click)

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                click_slider = True
                click = True
        pygame.display.flip()


def choosing_lenght():
    """ The Menu to change the lenght of the tray """
   
    screen.fill(screen_color)
    title_font = switch_font(75, False, False)

    #TITLE
    title = title_font.render(langues["local"].get(LANG), True, (0 , 0 ,0))
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
            vol_rect = vol_text.get_rect(center=(SIZE_X/2,SIZE_Y/2 +100))
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
    title = title_font.render(langues["local"].get(LANG), True, (0 , 0 ,0))
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
                game_menu()
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

menu()
