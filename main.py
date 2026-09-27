import os
import sys

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

#Importing of pygame and the project classes classes
import pygame as pg
from growthPoints import GrowthPoints
from button import Button
from root import Root
from camera import Camera
from upgrade import Upgrade

#Creating the various objects
gP = GrowthPoints()
btnPlay = Button(pg.image.load(resource_path("Sprites/Button_Background.png")), "Play", 330, 300, None)
btnClose = Button(pg.image.load(resource_path("Sprites/Button_Background.png")), "Quit", btnPlay.getX(), btnPlay.getY()+100, None)
btnUpgRoot = Button(pg.image.load(resource_path("Sprites/Button_Upgrade_Background.png")), "Upg root", 650, 50, 30)
btnUpgMult = Button(pg.image.load(resource_path("Sprites/Button_Upgrade_Background.png")), "Upg mult", btnUpgRoot.getX(), btnUpgRoot.getY()+66, 35)
btnUpgPPS = Button(pg.image.load(resource_path("Sprites/Button_Upgrade_Background.png")), "Upg PPS", btnUpgRoot.getX(), btnUpgMult.getY()+66, 32)
root = Root(340, 335)
camera = Camera()
upgrade = Upgrade()

#import the sprites for the game 
title = pg.image.load(resource_path("Sprites/Title.png"))
menuBackground = pg.image.load(resource_path("Sprites/Menu_Background.png"))
gameBackground = pg.image.load(resource_path("Sprites/Game_background.png"))
endingBackground = pg.image.load(resource_path("Sprites/Ending_Background.png"))

#Setting the window with size and name. 
pg.init()
screen = pg.display.set_mode((800, 600))
pg.display.set_caption("Coz 'till you FALL")

#Setting the variable for the game cycle continuation
running = True

#Setting the font as default and size as 36
font = pg.font.Font(None, 36)

#Importing the main menu themes
upgradeSound = pg.mixer.Sound(resource_path("Sounds/Upgrade.mp3"))
pg.mixer.music.load(resource_path("Sounds/Menu_theme.mp3"))
pg.mixer.music.play(-1)

#While cycle for the title screen
while running:
    #If the close button in window UI is pressed, the quit condition becomes true, running is set false to exit the cycle
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            quit = True

    screen.blit(menuBackground)

    #Getting the mouse position for the buttons
    mouseX, mouseY = pg.mouse.get_pos()

    #Various conditions for the left mouse click
    if event.type == pg.MOUSEBUTTONDOWN:

        #if the play button is pressed, the game starts and the 2 sendond timer is set
        if mouseX >= btnPlay.getX() and mouseX <= btnPlay.getX()+128 and mouseY >= btnPlay.getY() and mouseY <= btnPlay.getY()+64:
            running = False
            goal_time = 1000+pg.time.get_ticks()

        #if the close button is pressed, the the game closes as if you clicked the x in the window Ui
        if mouseX >= btnClose.getX() and mouseX <= btnClose.getX()+128 and mouseY >= btnClose.getY() and mouseY <= btnClose.getY()+64:
            running = False
            quit = True

    #Draws the title png
    screen.blit(title, (272, 100))

    #Drawing the play button with his background and text
    play = font.render(f"{btnPlay.getText()}", True, (0, 0, 0))
    screen.blit(btnPlay.getBackground(), (btnPlay.getX(), btnPlay.getY()))
    screen.blit(play, (btnPlay.getX()+36, btnPlay.getY()+20))

    #Drawing the exit button with his background and text
    exit = font.render(f"{btnClose.getText()}", True, (0, 0, 0))
    screen.blit(btnClose.getBackground(), (btnClose.getX(), btnClose.getY()))
    screen.blit(exit, (btnClose.getX()+36, btnClose.getY()+20))

    #Updating the screen
    pg.display.flip()
    

#If the quit condition is true the program closes right there, if not, the running continues
if quit == True:
     pg.quit()
else:          
    running = True
    pg.mixer.music.stop()

#Game cycle using while with the same condition as the one above
while running:

    #Code to permit the closure of the software
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            quit = True

    #Getting mouse position and saving it as two separated variables
    mouseX, mouseY = pg.mouse.get_pos()

    #Getting the ticks from the start
    current_time = pg.time.get_ticks()

    #Checking if 1 second has passed, if so the points are added and the doal is updated to 1000 tick from now
    if current_time >= goal_time:
        gP.add()
        goal_time = current_time + 1000

    #Drawing the backfround updating its position whith the camera
    screen.blit(gameBackground, (0, 0+camera.getY()))

    #Draw the root sprite, updating the position with the camera
    screen.blit(root.getSprite(), (root.getX(), root.getY()+camera.getY()))

    #Button to upgrade the root with a text that includes the price
    upgRoot = font.render(f"{btnUpgRoot.getText()}\n{btnUpgRoot.getUpgCost()}GP", True, (0, 0, 0))
    screen.blit(btnUpgRoot.getBackground(), (btnUpgRoot.getX(), btnUpgRoot.getY()))
    screen.blit(upgRoot, (btnUpgRoot.getX()+15, btnUpgRoot.getY()+5))

    #Button to upgrade the point multiplier
    upgMult = font.render(f"{btnUpgMult.getText()}\n{btnUpgMult.getUpgCost()}GP", True, (0,0,0))
    screen.blit(btnUpgMult.getBackground(), (btnUpgMult.getX(), btnUpgMult.getY()))
    screen.blit(upgMult, (btnUpgMult.getX()+13, btnUpgMult.getY()+5))

    upgPPS = font.render(f"{btnUpgPPS.getText()}\n{btnUpgPPS.getUpgCost()}GP", True, (0,0,0))
    screen.blit(btnUpgPPS.getBackground(), (btnUpgPPS.getX(), btnUpgPPS.getY()))
    screen.blit(upgPPS, (btnUpgPPS.getX()+13, btnUpgPPS.getY()+5))

    #Getting the string to display and printing it on the window
    points = font.render(f"Ground Point(s): {int(gP.getPoints())}", True, (0, 0, 0))
    screen.blit(points, (530, 20))

    #Controller for keyboard buttons
    if event.type == pg.KEYDOWN:
        if event.key== pg.K_UP:
            camera.moveDown()
        elif event.key == pg.K_DOWN:
            camera.moveUp()

    #Mouse controller for left click
    if event.type == pg.MOUSEBUTTONDOWN:

        #If teh click is between the root upgrade area and you have enough points, then the root is upgraded and becomes bigger
        if mouseX >= btnUpgRoot.getX() and mouseX <= btnUpgRoot.getX()+128 and mouseY >= btnUpgRoot.getY() and mouseY <= btnUpgRoot.getY()+64:
            if gP.getPoints() >= btnUpgRoot.getUpgCost():
                upgrade.upgRoot(btnUpgRoot, gP)
                root.bigger()
                upgradeSound.play()

        #If the click is in the multiplier upgrade button area and there are enough points the multiplier updates
        if mouseX >= btnUpgMult.getX() and mouseX <= btnUpgMult.getX()+128 and mouseY >= btnUpgMult.getY() and mouseY <= btnUpgMult.getY()+64:
            if gP.getPoints() >= btnUpgMult.getUpgCost():
                upgrade.upgMult(btnUpgMult, gP)
                upgradeSound.play()

        #If the click is in the PPS (Points Per Seconds) upgrade button and there are enough points, the numbrt of points given every second update
        if mouseX >= btnUpgPPS.getX() and mouseX <= btnUpgPPS.getX()+128 and mouseY >= btnUpgPPS.getY() and mouseY <= btnUpgPPS.getY()+64:
            if gP.getPoints() >= btnUpgPPS.getUpgCost():
                upgrade.upgPPS(btnUpgPPS, gP)
                upgradeSound.play()

    #When whe root reaches the soil, whe exit this cicle
    if root.getHeight()>=1605:
        running = False

    #Updates the screen
    pg.display.flip()

#Check if the player pressed the start button or wanted to exit
if quit == True:
     pg.quit()
else:          
    running = True

#While cicle for the ending screen
while running:

    #Checking if the close button in the window UI is pressed 
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            quit = True

    screen.blit(endingBackground)

    #Getting the mouse position for the buttons
    mouseX, mouseY = pg.mouse.get_pos()

    #Drawing the exit button with his background and text
    exit = font.render(f"{btnClose.getText()}", True, (0, 0, 0))
    screen.blit(btnClose.getBackground(), (btnClose.getX(), btnClose.getY()))
    screen.blit(exit, (btnClose.getX()+36, btnClose.getY()+20))

    if event.type == pg.MOUSEBUTTONDOWN:
         #if the close button is pressed, the the game closes as if you clicked the x in the window Ui
        if mouseX >= btnClose.getX() and mouseX <= btnClose.getX()+128 and mouseY >= btnClose.getY() and mouseY <= btnClose.getY()+64:
            running = False
        
    pg.display.flip()

pg.quit()