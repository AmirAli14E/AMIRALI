# library
import pygame as pg
import time
import random 
import sys
import math
from maps import MAP 
from pygame.locals import *
# init pygame 
pg.init()
width_screen=550
height_screen=800
# screen meno
screen=pg.display.set_mode((height_screen,width_screen+50))
pg.display.set_caption('<<PAC|MAN>>')
icon=pg.image.load('pics/pacman_icon.jpg')
pg.display.set_icon(icon)
circle_smale=0
color_circle=(255,255,255)
def draw_meno():
    screen.fill((0,0,25))
    pg.draw.circle(screen,(2,100,160),(390,300),100)
    pg.draw.rect(screen,(7,110,169),(220,430,345,150))
    font_style = pg.font.SysFont(None, 69)
    font_style2 = pg.font.SysFont(None, 69)
    font_style3 = pg.font.SysFont(None, 110)
    m=font_style.set_underline(True)
    mesg = font_style.render('Start', True, (255,255,255))
    name_mesg = font_style2.render('<< PACMAN >>', True, (255,255,255))
    nd1 = font_style3.render('>  >  >', True, (255,255,255))
    nd2 = font_style3.render('<  <  <', True, (255,255,255))
    pac=pg.image.load('pics/pacman_meno.jpg')
    aa=pg.image.load('pics/AA.jpg')
    pac2=pg.image.load('pics/pacman_meno2.jpg')
    shabah=pg.image.load('pics/shabah_mano.jpg')
    shabah2=pg.image.load('pics/shabah_mano2.jpg')
    screen.blit(mesg,[340,280])
    screen.blit(nd1,[550,260])
    screen.blit(nd2,[30,260])
    screen.blit(name_mesg,[220,480])
    screen.blit(pac,[30,500])
    screen.blit(pac2,[700,500])
    screen.blit(aa,[374,5])
    screen.blit(shabah,[30,20])
    screen.blit(shabah2,[700,20])
    screen.blit(shabah,[220,100])
    screen.blit(shabah2,[500,100])
x=True
snd = pg. mixer. Sound('music/music_meno.mp3')
snd. play()
while x:
    draw_meno()
    for event in pg.event.get():
        #turn off
        if event.type == pg.QUIT:
            sys.exit()
        if event.type == pg.KEYUP:
                    x=False
    pg.display.update()
snd.stop()           
# screen game
time_game=0
time_game_big=0
scor=0
screen=pg.display.set_mode([height_screen-100,width_screen+75])
pg.display.set_caption('<<PAC|MAN>>')
icon=pg.image.load('pics/pacman_icon.jpg')
pg.display.set_icon(icon)
# Game_map
tt=True
s=0
mm=0
X,y=60,50
sc=0
def draw_map(x,yy):
    global sc
    global s
    global mm
    global tt
    global X 
    global y
    global scor
    global circle_smale
    global color_circle
    xx=1
    for index_x,line in enumerate(MAP):
        for index_y,colon in enumerate(line):
            width=width_screen//len(line)
            height=height_screen//len(MAP)
            rect=Rect(x,yy,16,16)
            if colon == 1:
                xcs=((index_y*height)+(height * 0.5),(index_x * width)+(width * 0.5))
                rect2=Rect(xcs[0],xcs[1],2,2)
                if rect.colliderect(rect2):
                    MAP[index_x][index_y]=10

                    scor+=1
                    sc+=1
                else:
                    pg.draw.circle(screen,(color_circle),xcs,2)
            elif colon == 2:
                xcb=((index_y*height)+(height * 0.5),(index_x * width)+(width * 0.5))
                rect2=Rect(xcb[0],xcb[1],5,5)
                if rect.colliderect(rect2):
                    MAP[index_x][index_y]=11
                    scor+=4
                    sc+=4
                else:
                    pg.draw.circle(screen,(230,210,50),xcb,6)
            elif colon == 3:
                l1=((index_y*height) + (height * 0.5),index_x*width+ height)
                l2=((index_y*height) + (height * 0.5),index_x * width)
                rect2=Rect(l1[0],l2[1],3,3)
                rect3=Rect(l1[0],l1[1],3,3)
                if rect.collidepoint(rect2.x,rect2.y) or rect.collidepoint(rect3.x,rect3.y):
                    X=60
                    y=50
                    s+=10

                else:
                    pg.draw.line(screen,(255,255,255),l1,l2,3)
                    s=0
            elif colon == 4:
                l1=(index_y*height ,(index_x * width) + (width * 0.5) )
                l2=((index_y*height) +   height,(index_x * width) + (width * 0.5))
                rect2=Rect(l1[0],l2[1],3,3)
                rect3=Rect(l1[0],l1[1],3,3)
                if rect.colliderect(rect2) or rect.colliderect(rect3):
                    X=60
                    y=50
                    s+=10
                else:
                    pg.draw.line(screen,(0,100,200),l1,l2,3) 
                    s=0  
            elif colon == 5:
                rec=((index_y * height-(height * 0.4))-2,(index_x*width+(0.5*width)))
                rect2=Rect(rec[0],rec[1],3,3)
                if rect.colliderect(rect2):
                    X=60
                    y=50
                else:
                    pg.draw.arc(screen,(10,200,180),[rec[0],rec[1],height,width],0,math.pi/2,3)
            elif colon == 6:
                rec=(index_y * height + (height * 0.5),index_x * width + (width * 0.5))
                rect2=Rect(rec[0],rec[1],3,3)
                if rect.colliderect(rect2):
                    X=60
                    y=50
                else:
                    pg.draw.arc(screen,(250,250,250),[rec[0],rec[1],height,width],math.pi/2,math.pi,3 )
            elif colon == 7:
                rec=((index_y*height+(height*.5)),(index_x*width-(.4 * width)))
                rect2=Rect(rec[0],rec[1],3,3)
                if rect.colliderect(rect2):
                    X=60
                    y=50 
                else:
                   pg.draw.arc(screen,(0,100,200),[rec[0],rec[1],height,width],math.pi,3 * math.pi / 2,3)
            elif colon == 8:
                rec=((index_y*height-(height*.4)) -2,(index_x*width-(.4 * width)))
                rect2=Rect(rec[0],rec[1],3,3)
                if rect.colliderect(rect2):
                    X=60
                    y=50
                else:
                     pg.draw.arc(screen,(0,0,100),[rec[0],rec[1],height,width],3 * math.pi / 2,2 * math.pi,3)
            elif colon ==9:
                pg.draw.line(screen,(250,250,0),(index_y*height ,(index_x * width) + (width * 0.5)),((index_y*height) +   height,(index_x * width) + (width * 0.5)),3)    
            # elif scor>=2:
            #     MAP[index_x][index_y]=1
            #     scor=0


# enemy , player , hole
player=pg.image.load('pics/pacman_R.jpg')
shabah=pg.image.load('pics/shabah.jpg')
shabah2=pg.image.load('pics/shabah.jpg')
shabah3=pg.image.load('pics/shabah.jpg')
shabah4=pg.image.load('pics/shabah.jpg')
shabah5=pg.image.load('pics/shabah.jpg')
blackhole=pg.image.load('pics/blsckhole.jpg')
x_change = 0
y_change = 0
clock = pg.time.Clock()
x=True
# gameloop
xs=330
ys=280
xs2=330
ys2=280
xs3=330
ys3=280
xs4=330
ys4=280
xs5=330
ys5=280
sh=0
snd = pg. mixer. Sound('music/M.mp3')
snd. play()
while x:
    rx=X+50
    ry=y+50
    time_game+=1
    ran=random.choice(['l','r','u','d'])
    ran2=random.choice(['l','r','u','d'])
    ran3=random.choice(['l','r','u','d'])
    ran4=random.choice(['l','r','u','d'])
    ran5=random.choice(['l','r','u','d'])
    if time_game == 99999999999999999999:
        time_game_big+=1
        time_game-=99999999999999999999
    if time_game_big==999999999999:
        scor+=10
        time_game_big-=999999999999
    clock.tick(10)
    for event in pg.event.get():
        #turn off
        if event.type == pg.QUIT:
            x=False
        # keybord
        if event.type == pg.KEYDOWN:
            snd = pg. mixer. Sound('music/pacman_music.mp3')
            snd. play()
            
            if event.key == pg.K_RIGHT:
                player=pg.image.load('pics/pacman_R.jpg')
                mm=4
                x_change = 10
                y_change = 0
                
                    
            elif event.key == pg.K_LEFT:
                player=pg.image.load('pics/pacman_L.jpg')
                mm=3
                x_change = -10
                y_change = 0
                
            elif event.key == pg.K_UP:
                player=pg.image.load('pics/pacman_U.jpg')
                mm=2
                x_change = 0
                y_change = -10
                
            elif event.key == pg.K_DOWN:
                player=pg.image.load('pics/pacman_D.jpg')
                mm=1
                x_change = 0
                y_change =10
                
    if ran == 'r':
            sh=1
            xs+=10
    elif ran =='l':
            sh=1
            xs-=10
    elif ran =='u':
            sh=2
            ys+=10
    elif ran =='d':
            sh=2
            ys-=10
    if ran2 == 'r':
            sh=1
            xs2+=10
    elif ran2 =='l':
            sh=1
            xs2-=10
    elif ran2 =='u':
            sh=2
            ys2+=10
    elif ran2 =='d':
            sh=2
            ys2-=10
    if ran3 == 'r':
            sh=1
            xs3+=10
    elif ran3 =='l':
            sh=1
            xs3-=10
    elif ran3 =='u':
            sh=2
            ys3+=10
    elif ran3 =='d':
            sh=2
            ys-=10
    if ran4 == 'r':
            sh=1
            xs4+=10
    elif ran4 =='l':
            sh=1
            xs4-=10
    elif ran4 =='u':
            sh=2
            ys4+=10
    elif ran4 =='d':
            sh=2
            ys4-=10
    if ran5 == 'r':
            sh=1
            xs5+=10
    elif ran5 =='l':
            sh=1
            xs5-=10
    elif ran5 =='u':
            sh=2
            ys5+=10
    elif ran5 =='d':
            sh=2
            ys5-=10
    # location
    o3=20
    o2=0
    o1=0
    screen.fill((o1,o2,o3))
    draw_map(X,y)
    o2+=100
    X += x_change
    y += y_change
    if x<0:
        X = height_screen
    screen.blit(player,[X,y])
    screen.blit(shabah,[xs,ys])
    screen.blit(shabah2,[xs2,ys2])
    screen.blit(shabah3,[xs3,ys3]) 
    screen.blit(shabah4,[xs4,ys4])
    screen.blit(shabah5,[xs5,ys5])
    pr=Rect(X,y,18,18)
    sr=Rect(xs,ys,25,25)
    sr2=Rect(xs2,ys2,25,25)
    sr3=Rect(xs3,ys3,25,25)
    sr4=Rect(xs4,ys4,25,25)
    sr5=Rect(xs5,ys5,25,25)
    if pr.colliderect(sr):
            x=False
    if pr.colliderect(sr2):
            x=False
    if pr.colliderect(sr3):
            x=False
    if pr.colliderect(sr4):
            x=False
    if pr.colliderect(sr5):
            x=False
    if ys>= width_screen or xs>=(height_screen-160):
        if sh==1:
            xs=rx
        if sh==2:
            ys=ry
    if ys<=30 or xs<=20:
        if sh==1:
            xs=rx
        if sh==2:
            ys=ry
    if ys2>= width_screen or xs2>=(height_screen-160):
        if sh==1:
            xs2=rx
        if sh==2:
            ys2=ry
    if ys2<=30 or xs2<=20:
        if sh==1:
            xs2=rx
        if sh==2:
            ys2=ry
    if ys3>= width_screen or xs3>=(height_screen-160):
        if sh==1:
            xs3=rx
        if sh==2:
            ys3=ry
    if ys3<=30 or xs3<=20:
        if sh==1:
            xs3=rx
        if sh==2:
            ys3=ry
    if ys4>= width_screen or xs4>=(height_screen-160):
        if sh==1:
            xs4=rx
        if sh==2:
            ys4=ry
    if ys4<=30 or xs4<=20:
        if sh==1:
            xs4=rx
        if sh==2:
            ys4=ry
    if ys5>= width_screen or xs5>=(height_screen-160):
        if sh==1:
            xs5=rx
        if sh==2:
            ys5=ry
    if ys5<=30 or xs5<=20:
        if sh==1:
            xs5=rx
        if sh==2:
            ys5=ry
    # SCORE,time
    font_style=pg.font.SysFont(None,20)
    mesg = font_style.render(f'time:{time_game}', True, (200,255,230))
    mesg2 = font_style.render(f'score:{scor}', True, (200,200,100))
    mesg3 = font_style.render(f'big time:{time_game_big}', True, (200,200,250))
    screen.blit(mesg3,(240,5))
    screen.blit(mesg,(40,5))
    screen.blit(mesg2,(400,5))
    screen.blit(blackhole,(0,285))
    screen.blit(blackhole,(675,285))
    pg.display.update()
    clock.tick_busy_loop(30)
    if X >= (height_screen-100):
        X=11
    if X <= 5:
        X=(height_screen-100)
    if x==False:
        # gameover_screen
        snd.stop()
        snd = pg. mixer. Sound('music/music_gameove.mp3')
        snd. play()
        time.sleep(0.5)
        font_style = pg.font.SysFont(None, 100)
        mesg = font_style.render('! game ovre !', True, (200,3,0))
        screen.fill((20,0,0))
        screen.blit(mesg,[100, 300])
        pg.display.update()
        time.sleep(1)
    if scor >= 9999999999999999999990887:
        #  wineer
        x=False
        winner=pg.image.load('pics/winner_game.png')
        screen.blit(winner,(0,0))
        pg.display.update()
        time.sleep(2)
        pg.quit()
        sys.exit()
pg.display.update()
# get out
pg.quit()
sys.exit()
