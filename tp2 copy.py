# 15-112 Term Project

from tkinter import *
from PIL import Image
from cmu_112_graphics import *
import random

def gameDimensions():
    rows = 15
    cols = 10
    cellSize = 20
    margin = 25
    return (rows, cols, cellSize, margin)

def splashScreenMode_redrawAll(app, canvas):
    font = 'Arial 23 bold'
    #canvas.create_image(200, 200,image=ImageTk.PhotoImage(app.resizestartscreengif))
    photoImage = app.spritePhotoImages[app.gifspriteCounter]
    canvas.create_image(210,160,image=photoImage)
    
    canvas.create_text(app.width/2, 25, text='Welcome to SuperMario Bros',
                       font=font, fill='black')
    canvas.create_text(app.width/2, 65, text='Press h for help screen',
                       font=font, fill='black')
    canvas.create_text(app.width/2, 120, text='Choose your character!',
                       font=font, fill='black')
    canvas.create_text(app.width/1.5, 150, text='M',
                       font='Arial 19 bold', fill='red')
    canvas.create_text(app.width/2, 150, text='Y',
                       font='Arial 19 bold', fill='yellow')
    canvas.create_text(app.width/3.3, 150, text='G',
                       font='Arial 19 bold', fill='brown')

    canvas.create_text(app.width/2, 320, text='Press any key to play!',
                       font=font, fill='white')                                      

def splashScreenMode_timerFired(app):
    app.cx = 400
    app.gifspriteCounter = (1 + app.gifspriteCounter) % len(app.spritePhotoImages)

##########################################
# Help Mode
##########################################

def helpMode_redrawAll(app, canvas): #help screen display
    canvas.create_image(200, 150,image=ImageTk.PhotoImage(app.resizehelp))
    #'Arial 16 bold'
    canvas.create_text(app.width/2, 50, text='Instructions', 
                       font='Arial 20 bold', fill='black')

    canvas.create_text(app.width/2, 110, 
    text='* Use arrows [→←] keys to move Mario',
                       font='Arial 13 bold', fill='black')

    canvas.create_text(app.width/2, 130, 
    text='* To jump higher hold space',
                       font='Arial 13 bold', fill='black')

    canvas.create_text(app.width/2, 150, text=
    "* Jump on enemies to defeat them", font=
    'Arial 13 bold', fill='black')

    canvas.create_text(app.width/2, 170, text=
    "* Watch out for Goomba attacks!", font=
    'Arial 13 bold', fill='black')

    canvas.create_text(app.width/2, 190, text=
    "* Accumulate score by distance", font=
    'Arial 13 bold', fill='black')
    
    canvas.create_text(app.width/2, 210, text= "traveled and enemies hit!", font=
    'Arial 13 bold', fill='black')

    canvas.create_text(app.width/2, 230, text= "* Beat your high score", font=
    'Arial 13 bold', fill='black')

    canvas.create_text(app.width/2, 250, text= "* DONT fall off the map", font=
    'Arial 13 bold', fill='black')

    canvas.create_text(app.width/2, 330, text= "Ready to play?", font=
    'Arial 13 bold', fill='black')

    canvas.create_text(app.width/2, 350, text='Press any key to return to the game!',
                       font='Arial 13 bold', fill='black')

def helpMode_keyPressed(app, event):
    app.mode = 'gameMode'

##########################################
# Actual gameplay
##########################################
class Topscore:
    def __init__(self):
        self.high_score = 0
    def top_score(self, score):
        if score > self.high_score:
            self.high_score = score
        return self.high_score
topscore = Topscore()

def appStarted(app):
    (app.rows, app.cols, app.cellSize, app.margin) = gameDimensions()
    app.x0 = 200
    app.y0 = 200
#coordinates of enemy
    #app.cx = app.width/2
    app.cx = 400
    app.cy = 200
    app.r = 40

    app.cx1 = app.width/2
    app.cy1 = 200

    #app.enemyx0 = 0

    # app.startgameimage = app.loadImage('startgame3.png')
    # app.resizeStartGame = app.scaleImage(app.startgameimage, 10/6)
    app.spritePhotoImages = loadAnimatedGif('startscreengif.gif')
    #app.resizestartscreengif = app.scaleImage(app.startscreengif, 4/3)
    app.helpscreen = app.loadImage('help.jpeg')
    app.resizehelp = app.scaleImage(app.helpscreen, 4/3)

    app.pausescreen = app.loadImage('pausepic.png')
    app.resizepausescreen = app.scaleImage(app.pausescreen, 4/3)

    app.gameoverscreen = app.loadImage('gameover2.jpeg')
    app.gameoverscreen = app.scaleImage(app.gameoverscreen, 13/13)

#resizing the world to scale
    app.world1 = app.loadImage('World1.png')
    app.resizeworld1 = app.scaleImage(app.world1, 4/3) #world1 4/3 + 2/3 sprite

    app.blocks = app.loadImage('blocks.png')
    app.resizeblocks = app.scaleImage(app.blocks, 4/3)

    app.newblock = app.resizeblocks.crop((200,10,200,100))

#sprite
    url = 'http://www.cs.cmu.edu/~112/notes/sample-spritestrip.png'
    app.sprite = app.loadImage(url)
    app.resized = app.scaleImage(app.sprite, 2/5)
    spritestrip = app.loadImage(url)
    app.sprites = [ ]
    for i in range(6):
        sprite = spritestrip.crop((30+260*i, 30, 230+260*i, 250))
        app.sprites.append(sprite)
    app.spriteCounter = 0
    app.gifspriteCounter = 0

    for i in range(len(app.sprites)):
        app.sprites[i]= app.scaleImage(app.sprites[i], 1/4)
        
#mario sprite
    app.mariosprite = app.loadImage('mariosprite.png')
    app.marioresized = app.scaleImage(app.mariosprite, 10/3)
    mariospritestrip = app.loadImage('mariosprite.png')
    app.mariosprites = [ ]
    for i in range(6):
        #msprite = mariospritestrip.crop((30+260*i, 30, 230+260*i, 250))
        msprite = mariospritestrip.crop((50+90*i, 90, 70+100*i, 100))
        #tuple values are left, top, right, bottom of value cropping
        app.mariosprites.append(msprite)
    app.mariospriteCounter = 0

    for i in range(len(app.mariosprites)):
        app.mariosprites[i]= app.scaleImage(app.mariosprites[i], 1/4)


    app.scrollX = 0
    app.dots = [(random.randrange(app.width),
                  random.randrange(60, app.height)) for _ in range(50)]

    #goomba image
    app.goombaImage = app.loadImage('goomba2.png')
    app.goombaresized = app.scaleImage(app.goombaImage, 1/11)
    app.yoshiImage = app.loadImage('yoshi2.png')
    app.yoshiresized = app.scaleImage(app.yoshiImage, 1/7)

    app.mode = 'splashScreenMode'

def loadAnimatedGif(path): #code from course notes
    spritePhotoImages = [ PhotoImage(file=path, format='gif -index 0') ]
    i = 1
    while True:
        try:
            spritePhotoImages.append(PhotoImage(file=path,
                                                format=f'gif -index {i}'))
            i += 1
        except Exception as e:
            return spritePhotoImages

#character selection screen
def splashScreenMode_keyPressed(app, event):
    #make sure press on key for character
    if (event.key == 'h'):
        app.mode = 'helpMode'
    elif (event.key == 'm'):
        app.mode = 'mariogameMode'
    elif (event.key == 'y'):
        app.mode = 'yoshigameMode'   
    elif (event.key == 'g'):
        app.mode = 'goombagameMode'     
   
#**********************************************#
def pauseMode_redrawAll(app, canvas): #display a pause feature 
    canvas.create_image(200, 200,image=ImageTk.PhotoImage(app.resizepausescreen))

def pausemariogameMode_keyPressed(app, event):
    if (event.key == 'p'):
        app.mode = 'mariogameMode'
    elif (event.key == 'q'):
        app.mode = 'splashScreenMode'

def pausegoombagameMode_keyPressed(app, event):
    if (event.key == 'p'):
        app.mode = 'goombagameMode'
    elif (event.key == 'q'):
        app.mode = 'splashScreenMode'    

def pauseyoshigameMode_keyPressed(app, event):
    if (event.key == 'p'):
        app.mode = 'yoshigameMode'
    elif (event.key == 'q'):
        app.mode = 'splashScreenMode'            
#**********************************************#

def pausegoombagameMode_redrawAll(app, canvas): #display a pause feature and 
    canvas.create_image(200, 200,image=ImageTk.PhotoImage(app.resizepausescreen))

def pausemariogameMode_redrawAll(app, canvas): #display a pause feature and 
    canvas.create_image(200, 200,image=ImageTk.PhotoImage(app.resizepausescreen))

def pauseyoshigameMode_redrawAll(app, canvas): #display a pause feature and 
    canvas.create_image(200, 200,image=ImageTk.PhotoImage(app.resizepausescreen))
#***************************gameplay movements ***************************#

#isJump = False
def mariogameMode_keyPressed(app, event):
    #use sprite sheet according to movements made
    maxJump = 100
    if (event.key == "Left"):    app.scrollX -= 10
    elif (event.key == "Right"): app.scrollX += 10
    elif (event.key == "p"):
        app.mode = 'pausemariogameMode'
    elif ( event.key == 'Space'): #not working yet
        if 200-app.y0 <= 100:
            app.y0 -= 60
        #app.y0 -= (1/2)*2*(vel_y**2)
            
            # m = 10
            # # # calculate force (F). F = 1 / 2 * mass * velocity ^ 2.
            # F =(1 / 2)*m*(vel_y**2)  
            # # change in the y co-ordinate
            # vel_y-= F
            # # decreasing velocity while going up and become negative while coming down
            # vel_y = vel_y-1
            # # object reached its maximum height
            # if vel_y<0: 
            #     # negative sign is added to counter negative velocity
            #     m =-1
            # # objected reaches its original state
            # if vel_y ==-6:
            #     # making isjump equal to false 
            #     isjump = False
            #     # setting original values to v and m
            #     vel_y = 5
            #     m = 1

    keyHold[event.key]=True #for holding down a key

def yoshigameMode_keyPressed(app, event):
    vel_y = 10
    isJump = False
    if (event.key == "Left"):    app.scrollX -= 10
    elif (event.key == "Right"): app.scrollX += 10
    elif (event.key == "p"):
        app.mode = 'pauseyoshigameMode'
    elif ( event.key == 'Space'): 
        isJump = True
        if isJump is True:
            app.y0 -= vel_y * 9
            if vel_y < -10:
                isJump = False
                vel_y = 10
    keyHold[event.key]=True

def goombagameMode_keyPressed(app, event):
    vel_y = 10
    isJump = False
    if (event.key == "Left"):    app.scrollX -= 10
    elif (event.key == "Right"): app.scrollX += 10
    elif (event.key == "p"):
        app.mode = 'pausegoombagameMode'
    elif ( event.key == 'Space'): #not working yet
        isJump = True
        if isJump is True:
            app.y0 -= vel_y * 9
            if vel_y < -10:
                isJump = False
                vel_y = 10

    keyHold[event.key]=True
keyHold=dict()
def keyReleased(app, event):
	keyHold[event.key]=False


#make enemies for mario
def drawEnemies(app, canvas):
    #have them spawn in randomly
    # app.goombaImage = app.loadImage('goomba.png')
    # app.goombaresized = app.scaleImage(app.goombaImage, 1/20
    canvas.create_image(300, 200,image=ImageTk.PhotoImage(app.goombaresized))
    canvas.create_image(100, 200,image=ImageTk.PhotoImage(app.yoshiresized))
    #randomIndex = random.randint(0, len(app.goombaresized) - 1)

#have enemy as an square

def isCollision(app):
    #check if sprite sheet and enemies collide
    if (app.cx-30 == 200) and (app.y0 == app.cy):
        return True
    else:
        return False
#goomba radius is 51 and mario is 200


def mariogameMode_timerFired(app):
    #app.timerDelay = 500
    app.spriteCounter = (1 + app.spriteCounter) % len(app.sprites)   
    if app.y0 < 200:
        app.y0 += 10
        app.timerDelay = 750

    if isCollision(app) == True:
        app.mode = 'gameOverMode'  

#moving dot/enemy
    app.timerDelay = 200 
    app.cx -= 10
    if (app.cx + app.r <= 0):
        app.cx = 400 + app.r
        #app.timerDelay = 200

def yoshigameMode_timerFired(app): 
    while app.y0 < 200:
        app.y0 += .002

def goombagameMode_timerFired(app): 
    while app.y0 < 200:
        app.y0 += .002        

def mariogameMode_redrawAll(app, canvas):
    # draw the x and y axes
    x = app.width/2 - app.scrollX # <-- This is where we scroll the axis!
    y = app.height/2
    canvas.create_line(x, 0, x, app.height)
    canvas.create_line(0, y, app.width, y)
    #random.random(app.goombaresized)

#insert hardcoded world map here
    canvas.create_image(x, 270,image=ImageTk.PhotoImage(app.resizeworld1))
    #map = (300,270)
    # draw the instructions and the current scrollX
    canvas.create_text(200, 20, text=f'Score = {app.scrollX}',
                       fill='black')
#course notes sprite examples                      
    sprite = app.sprites[app.spriteCounter]
    canvas.create_image(app.x0, app.y0, image=ImageTk.PhotoImage(sprite))
    #APP.X0 AND APP.XY ARE 200 200
    canvas.create_image(200, 200, image=ImageTk.PhotoImage(app.newblock))
    #make an (blocks)
    
#mario sprite
    msprite = app.mariosprites[app.mariospriteCounter]
    canvas.create_image(200, 200, image=ImageTk.PhotoImage(msprite))


    # canvas.create_image(app.cx-app.r, app.cy-app.r,
    #                    image=ImageTk.PhotoImage(app.goombaresized))
#goomba enemy #cx and cy are 200 200
    canvas.create_image(app.cx, app.cy + 10,
                       image=ImageTk.PhotoImage(app.goombaresized))

#yoshi enemy
    #create a new timerFired for yoshi spawn in
    canvas.create_image(app.cx1, app.cy1,
                       image=ImageTk.PhotoImage(app.yoshiresized))                    

    #drawEnemies(app, canvas)






 
#******************* gameplay as other characters (save for last)**************#
def goombagameMode_redrawAll(app, canvas):
    x = app.width/2 - app.scrollX # <-- This is where we scroll the axis!
    y = app.height/2
    canvas.create_line(x, 0, x, app.height)
    canvas.create_line(0, y, app.width, y)
    canvas.create_image(x, 270,image=ImageTk.PhotoImage(app.resizeworld1))
    canvas.create_text(200, 20, text=f'Score = {app.scrollX}',
                       fill='black')
    canvas.create_image(200, 200, image=ImageTk.PhotoImage(app.goombaresized))

#the gameplay as yoshi character
def yoshigameMode_redrawAll(app, canvas):
    x = app.width/2 - app.scrollX # <-- This is where we scroll the axis!
    y = app.height/2
    canvas.create_line(x, 0, x, app.height)
    canvas.create_line(0, y, app.width, y)
    canvas.create_image(x, 270,image=ImageTk.PhotoImage(app.resizeworld1))
    canvas.create_text(200, 20, text=f'Score = {app.scrollX}',
                       fill='black')                     
    canvas.create_image(app.x0, app.y0, image=ImageTk.PhotoImage(app.yoshiresized))



def gameOverMode_redrawAll(app, canvas): 
    canvas.create_image(200, 200,image=ImageTk.PhotoImage(app.gameoverscreen))

def gameOverMode_keyPressed(app, event):
    if (event.key == 'r'):
        app.mode = 'splashScreenMode'


runApp(width=415, height=275)   #runApp(width = 415, height 385) -> perfect for start screen

  #width=415, height=275 = perfect for gameplay