# 15-112 Term Project

from tkinter import *
from PIL import Image
from cmu_112_graphics import *
import random

def splashScreenMode_redrawAll(app, canvas):
    font = 'Arial 23 bold'
    #canvas.create_image(200, 200,image=ImageTk.PhotoImage(app.resizestartscreengif))
    photoImage = app.spritePhotoImages[app.gifspriteCounter]
    canvas.create_image(200,200,image=photoImage)

    # canvas.create_rectangle(10, 100, 350, 200, fill='green',
    #                                             outline='red', width=3)
    canvas.create_text(app.width/2, 70, text='Welcome to SuperMario Bros',
                       font=font, fill='black')
    canvas.create_text(app.width/2, 100, text='Press h for help screen',
                       font=font, fill='black')
    canvas.create_text(app.width/2, 160, text='Choose your character!',
                       font=font, fill='black')
    canvas.create_text(app.width/1.5, 190, text='M',
                       font='Arial 19 bold', fill='red')
    canvas.create_text(app.width/2, 190, text='Y',
                       font='Arial 19 bold', fill='yellow')
    canvas.create_text(app.width/3.3, 190, text='G',
                       font='Arial 19 bold', fill='brown')

    canvas.create_text(app.width/2, 320, text='Press any key to play!',
                       font=font, fill='white')                  

def splashScreenMode_timerFired(app):
    app.gifspriteCounter = (1 + app.gifspriteCounter) % len(app.spritePhotoImages)

##########################################
# Help Mode
##########################################

def helpMode_redrawAll(app, canvas): #help screen display
    canvas.create_image(200, 200,image=ImageTk.PhotoImage(app.resizehelp))
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
    # app.startgameimage = app.loadImage('startgame3.png')
    # app.resizeStartGame = app.scaleImage(app.startgameimage, 10/6)
    app.spritePhotoImages = loadAnimatedGif('startscreengif.gif')
    #app.resizestartscreengif = app.scaleImage(app.startscreengif, 4/3)
    app.helpscreen = app.loadImage('help.jpeg')
    app.resizehelp = app.scaleImage(app.helpscreen, 4/3)

    app.pausescreen = app.loadImage('pausepic.png')
    app.resizepausescreen = app.scaleImage(app.pausescreen, 4/3)


#resizing the world to scale
    app.world1 = app.loadImage('World1.png')
    app.resizeworld1 = app.scaleImage(app.world1, 4/3) #perfect size + 2/3 sprite

#sprite
    url = 'http://www.cs.cmu.edu/~112/notes/sample-spritestrip.png'
    app.sprite = app.loadImage(url)
    app.resized = app.scaleImage(app.sprite, 2/3)
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
    app.goombaImage = app.loadImage('goomba.png')
    app.goombaresized = app.scaleImage(app.goombaImage, 1/20)

    app.yoshiImage = app.loadImage('yoshipng.jpeg')
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

    # else:
    #     app.mode = 'gameMode'
   
#**********************************************#
def mousePressed(app, event):
    app.messages.append(f'mousePressed at {(event.x, event.y)}')

def mouseReleased(app, event):
    app.messages.append(f'mouseReleased at {(event.x, event.y)}')

def pauseMode_redrawAll(app, canvas): #display a pause feature 
    canvas.create_image(200, 200,image=ImageTk.PhotoImage(app.resizepausescreen)) #fix this mousepress for pause

def pauseMode_keyPressed(app, event):#finish working on later

    if mousePressed and mouseReleased == (100 < event.x and 100 < event.y):
        app.mode = 'gameMode'
    #implement mouse pressed on either resume or exit game to perform function
#**********************************************#


def pauseMode_redrawAll(app, canvas): #display a pause feature and 
    canvas.create_image(200, 200,image=ImageTk.PhotoImage(app.resizepausescreen))

#***************************gameplay movements ***************************#
isJump = False
def mariogameMode_keyPressed(app, event):
    #use sprite sheet according to movements made
    if (event.key == "Left"):    app.scrollX -= 10
    elif (event.key == "Right"): app.scrollX += 10
    elif (event.key == "p"):
        app.mode = 'pauseMode'

    elif (event.key == 'Space'): #not working yet
        # isJump = True
        # if isjump:
        #     # calculate force (F). F = 1 / 2 * mass * velocity ^ 2.
        #     F =(1 / 2)*m*(v**2)  
        #     # change in the y co-ordinate
        #     y-= F
        #     # decreasing velocity while going up and become negative while coming down
        #     v = v-1
        #     # object reached its maximum height
        #     if v<0: 
        #         # negative sign is added to counter negative velocity
        #         m =-1
        #     # objected reaches its original state
        #     if v ==-6:
        #         # making isjump equal to false 
        #         isjump = False
        #         # setting original values to v and m
        #         v = 5
        #         m = 1
        app.scrollX = (app, 0,+5)

    keyHold[event.key]=True #for holdimg down a key

keyHold=dict()
def keyReleased(app, event):
	keyHold[event.key]=False


#implement game options or levels of difficulties
# def mousePressed(app, event):
#     app.messages.append(f'mousePressed at {(event.x, event.y)}')

# def mouseReleased(app, event):
#     app.messages.append(f'mouseReleased at {(event.x, event.y)}')


def mariogameMode_timerFired(app):
    app.spriteCounter = (1 + app.spriteCounter) % len(app.sprites)    


def mariogameMode_redrawAll(app, canvas):
    # draw the player fixed to the center of the scrolled canvas
    # cx, cy, r = app.width/2, app.height/2, 10
    # canvas.create_oval(cx-r, cy-r, cx+r, cy+r, fill='cyan')

    # draw the blocks that mario needs to avoid
    # for (cx, cy) in app.dots:
    #     cx -= app.scrollX  # <-- This is where we scroll each dot!!!
    #     canvas.create_rectangle(cx-r, cy-r, cx+r, cy+r, fill='lightGreen')

    # draw the x and y axes
    x = app.width/2 - app.scrollX # <-- This is where we scroll the axis!
    y = app.height/2
    canvas.create_line(x, 0, x, app.height)
    canvas.create_line(0, y, app.width, y)

    #random.random(app.goombaresized)

#insert hardcoded world map here
    canvas.create_image(200, 200,image=ImageTk.PhotoImage(app.resizeworld1))

    # draw the instructions and the current scrollX
    canvas.create_text(x, 40, text=f'app.scrollX = {app.scrollX}',
                       fill='black')
#course notes sprite examples                      
    sprite = app.sprites[app.spriteCounter]
    canvas.create_image(200, 200, image=ImageTk.PhotoImage(sprite))
    
#mario sprite
    msprite = app.mariosprites[app.mariospriteCounter]
    canvas.create_image(200, 200, image=ImageTk.PhotoImage(msprite))
    

#What to work on:
#   jumping effect in keyPressed
#   import a hardcoded map
#   add different levels of difficulty accord to the speed of enemies spawned

#functionality of mario
class Mario():
    def __init__(self, sprite):
        sprite.__init__(self)
        self.movex = 0
        self.movey = 0
        self.frame = 0
        self.health = 10
        self.is_jumping = True
        self.is_falling = True

    def gravity(self):
        if self.is_jumping:
            self.movey += 3.2

    def jump(self):
        if self.is_jumping is False:
            self.is_falling = False
            self.is_jumping = True

    def gameMode_keyPressed(app, event): #doesnt work yet
    #use sprite sheet according to movements made
        if (event.key == "Left"):    app.scrollX -= 10
        elif (event.key == "Right"): app.scrollX += 10
        elif (event.key == "p"):
            app.mode = 'pauseMode'

 
#******************* gameplay as other characters (save for last)**************#
def goombagameMode_redrawAll(app, canvas):
    x = app.width/2 - app.scrollX # <-- This is where we scroll the axis!
    y = app.height/2
    canvas.create_line(x, 0, x, app.height)
    canvas.create_line(0, y, app.width, y)
    canvas.create_image(200, 200,image=ImageTk.PhotoImage(app.resizeworld1))
    canvas.create_text(x, 40, text=f'app.scrollX = {app.scrollX}',
                       fill='black')
    canvas.create_image(200, 200, image=ImageTk.PhotoImage(app.goombaresized))
   
def goombagameMode_keyPressed(app, event):
    if (event.key == "Left"):    app.scrollX -= 10
    elif (event.key == "Right"): app.scrollX += 10
    elif (event.key == "p"):
        app.mode = 'pauseMode'

#the gameplay as yoshi character
def yoshigameMode_redrawAll(app, canvas):
    x = app.width/2 - app.scrollX # <-- This is where we scroll the axis!
    y = app.height/2
    canvas.create_line(x, 0, x, app.height)
    canvas.create_line(0, y, app.width, y)
    canvas.create_image(200, 200,image=ImageTk.PhotoImage(app.resizeworld1))
    canvas.create_text(x, 40, text=f'app.scrollX = {app.scrollX}',
                       fill='black')                     
    canvas.create_image(200, 200, image=ImageTk.PhotoImage(app.yoshiresized))

def yoshigameMode_keyPressed(app, event):
    if (event.key == "Left"):    app.scrollX -= 10
    elif (event.key == "Right"): app.scrollX += 10
    elif (event.key == "p"):
        app.mode = 'pauseMode'


runApp(width=415, height=385)    