# #15-112 term project
# #jorge gracia - Jgraciav
# from cmu_112_graphics import *
# import math
# import random
# import sys
# pygame.init()
# import sys
# # print(f'sudo "{sys.executable}" -m pip install pillow')
# # print(f'sudo "{sys.executable}" -m pip install requests')
# WINDOW_WIDTH = 1000
# WINDOW_HEIGHT = 500
# FPS = 20
# BLUE = (0, 0, 0)
# GREEN = (0, 255, 0)
# goomba = pygame.image.load('goomba.png')
# goomba_rect = goomba.get_rect()
# goomba_rect.left = 0
# world1 = pygame.image.load('world1.png')

# enemies = [] #make list and a class of different enemies (e.g goomba) and
# #account use it to collide with mario 

# #the movements of mario. later implement jumping and physics
# def keyPressed(app, event):#accounts for left, right, down, up, harddrop input
#     if event.key == "r":
#         appStarted(app)
#     if app.isGameOver == False:
#         drow, dcol = 0,0 
#         if event.key == "Space":  
#             pass 
#             #hardDrop(app)
#         elif event.key == "Up":
#             pass
#             #rotateFallingPiece(app)
#         elif event.key == "Down":
#             drow, dcol = +1, 0 
#         elif event.key == "Left":
#             drow, dcol = 0,-1 
#         elif event.key == "Right":
#             drow, dcol = 0,1 

#         #moveFallingPiece(app,drow,dcol) 



# #import sprite sheet

# def appStarted(app): #testing out
#     app.scrollX = 0
#     app.dots = [(random.randrange(app.width),
#                   random.randrange(60, app.height)) for _ in range(50)]

# def start_game():
#     canvas.fill(BLUE)
#     start_img = pygame.image.load('startgame.png')
#     start_img_rect = start_img.get_rect()
#     start_img_rect.center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2)
#     canvas.blit(start_img, start_img_rect)

#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_ESCAPE:
#                     pygame.quit()
#                     sys.exit()
#                 game_loop()
#         pygame.display.update()


# def game_loop(): #create Mario class for mario later
#     while True:
#         #mario = Mario() create mario class
#         global SCORE
#         SCORE = 0
#         global HIGH_SCORE
#         while True:
#             canvas.fill(BLUE)
#             #check_level(SCORE)
# #mario movements
#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     pygame.quit()
#                     sys.exit()
#                 if event.type == pygame.KEYDOWN:
#                     if event.key == pygame.K_UP:
#                         mario.up = True
#                         mario.down = False
#                     elif event.key == pygame.K_DOWN:
#                         mario.down = True
#                         mario.up = False
#                 if event.type == pygame.KEYUP:
#                     if event.key == pygame.K_UP:
#                         mario.up = False
#                         mario.down = True
#                     elif event.key == pygame.K_DOWN:
#                         mario.down = True
#                         mario.up = False

#             score_font = font.render('Score:'+str(SCORE), True, GREEN)
#             score_font_rect = score_font.get_rect()
#             canvas.blit(score_font, score_font_rect)

#             level_font = font.render('Level:'+str(LEVEL), True, GREEN)
#             level_font_rect = level_font.get_rect()
#             canvas.blit(level_font, level_font_rect)

#             top_score_font = font.render('Top Score:'+str(topscore.high_score),True,GREEN)
#             top_score_font_rect = top_score_font.get_rect()
#             canvas.blit(top_score_font, top_score_font_rect)

#             mario.update()
#             for hit in enemies_list: #will create
#                 if hit.enemies_img_rect.colliderect(mario.mario_img_rect):
#                     game_over() #create game over later
#                     if SCORE > mario.mario_score:
#                         mario.mario_score = SCORE
#             pygame.display.update()

# def movePlayer(app, dx, dy):
#     app.playerX += dx
#     app.playerY += dy
#     #checkForNewWallHit(app) create function to detect blocks

# def keyPressed(app, event):
#     if event.key == "Left":
#         movePlayer(app, -5, 0)
#     elif event.key == "Right":
#         movePlayer(app, +5, 0)
#     elif event.key == "Up":
#         movePlayer(app, 0, +5)
#     elif event.key == "Down":
#         movePlayer(app, 0, -5)



# class Mario:
   

#     def __init__(self):
#         self.mario_img = pygame.image.load('mariocharacter.png')
#         self.mario_img_rect = self.mario_img.get_rect()
#         self.mario_img_rect.left = 20
#         self.mario_img_rect.top = WINDOW_HEIGHT/2 - 100
#         self.down = True
#         self.up = False
#         self.left = True
#         self.right = True

#     def update(self):
#         canvas.blit(self.mario_img, self.mario_img_rect)
#         if self.mario_img_rect.top <= goomba.bottom:
#             game_over()
#             if SCORE > self.mario_score:
#                 self.mario_score = SCORE
#             if SCORE > self.mario_score:
#                 self.mario_score = SCORE
#         if self.up:
#             self.mario_img_rect.top -= 10
#         if self.down:
#             self.mario_img_rect.bottom += 10
#         if self.right:
#             self.mario_img_rect.right #fill out later
#         if self.left:
#             self.mario_img_rect.left #fill out later


# class Topscore: #score tracker
#     def __init__(self):
#         self.high_score = 0
#     def top_score(self, score):
#         if score > self.high_score:
#             self.high_score = score
#         return self.high_score

# topscore = Topscore()


# start_game()
# #figure out how to import sprite sheet


# # currently is displaying the main screeen of the game. however, it does not load
# # the game. 

# testing side scroller for Super Mario

# from tkinter import *
from PIL import Image
from cmu_112_graphics import *
# def appStarted(app):
#     app.scrollX = 0
#     app.dots = [(random.randrange(app.width),
#                   random.randrange(60, app.height)) for _ in range(50)]

# def keyPressed(app, event):
#     if (event.key == "Left"):    app.scrollX -= 5
#     elif (event.key == "Right"): app.scrollX += 5
#     keyHold[event.key]=True #for hpldimg down a key

# keyHold=dict()
# def keyReleased(app,event):
# 	keyHold[event.key]=False

# def redrawAll(app, canvas):
#     # draw the player fixed to the center of the scrolled canvas
#     cx, cy, r = app.width/2, app.height/2, 10
#     canvas.create_oval(cx-r, cy-r, cx+r, cy+r, fill='cyan')

#     # draw the dots, shifted by the scrollX offset
#     for (cx, cy) in app.dots:
#         cx -= app.scrollX  # <-- This is where we scroll each dot!!!
#         canvas.create_oval(cx-r, cy-r, cx+r, cy+r, fill='lightGreen')

#     # draw the x and y axes
#     x = app.width/2 - app.scrollX # <-- This is where we scroll the axis!
#     y = app.height/2
#     canvas.create_line(x, 0, x, app.height)
#     canvas.create_line(0, y, app.width, y)

#     # draw the instructions and the current scrollX
#     x = app.width/2
#     canvas.create_text(x, 20, text='Use arrows to move left or right',
#                        fill='black')
#     canvas.create_text(x, 40, text=f'app.scrollX = {app.scrollX}',
#                        fill='black')

# runApp(width=300, height=300)

# This demos sprites using Pillow/PIL images
# See here for more details:
# https://pillow.readthedocs.io/en/stable/reference/Image.html

# This uses a spritestrip from this tutorial:
# https://www.codeandweb.com/texturepacker/tutorials/how-to-create-a-sprite-sheet


def appStarted(app):
    url = 'http://www.cs.cmu.edu/~112/notes/sample-spritestrip.png'
    spritestrip = app.loadImage(url)
    app.sprites = [ ]
    for i in range(6):
        sprite = spritestrip.crop((30+260*i, 30, 230+260*i, 250))
        app.sprites.append(sprite)
    app.spriteCounter = 0

def timerFired(app):
    app.spriteCounter = (1 + app.spriteCounter) % len(app.sprites)

def redrawAll(app, canvas):
    sprite = app.sprites[app.spriteCounter]
    canvas.create_image(200, 200, image=ImageTk.PhotoImage(sprite))

runApp(width=400, height=400)

#What I currently have: 
# a side-scroller to move mario left and right
# a sprite sheet of mario (not working)
