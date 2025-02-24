"""
Recycle Rush - A Sustainability Game, under the Sustainability project for the University of Exeter

This is a simple recycling-themed game built using Pygame. The player controls one of four different recycling bins 
that moves left and right to catch falling rubbish. The goal is to match the correct type of waste with the corresponding
bin to earn points. If the player catches the wrong type of waste or misses an item, they lose a life. 

Features:
- Four types of bins: plastic, battery, can, and paper.
- The player can switch bins using the 1, 2, 3, and 4 keys.
- The speed of falling rubbish increases after every 5 points.
- A leaderboard system that saves and displays the top 5 scores.

Controls:
- LEFT and RIGHT arrow keys to move the bin.
- Number keys (1-4) to change bin type.
- The game ends when the player loses all lives, displaying the leaderboard.

@author Rami Youhana
"""

import pygame
import random
import os

pygame.init()

# How big the screen will be, this size will be perfect for any laptop to run
WIDTH, HEIGHT = 1000, 650
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Recycle Rush")

WHITE = (255, 255, 255) 
RED = (255, 0, 0)
BLUE = (0, 0, 255)

#This is setting up a scoreboard with the 10 highest scores recorded
font = pygame.font.Font(None, 36)
leaderboard_file = "leaderboard.txt"

def save_score(score):
    #This function saves the scores of a player in order to place it into the leaderboard file
    scores = []
    if os.path.exists(leaderboard_file):
        with open(leaderboard_file, "r") as file:
            scores = [int(line.strip()) for line in file.readlines()]
    
    scores.append(score)
    scores = sorted(scores, reverse=True)[:10]  # Keep top 10 scores, having the higest one of the top
    
    with open(leaderboard_file, "w") as file:
        for s in scores:
            file.write(str(s) + "\n")

def display_leaderboard():
    #This function is used to show the leaderboard, after the game has concluded
    screen.fill(WHITE)
    title_text = font.render("Leaderboard", True, BLUE)
    screen.blit(title_text, (WIDTH//2 - 60, 50))
    
    if os.path.exists(leaderboard_file):
        with open(leaderboard_file, "r") as file:
            scores = [line.strip() for line in file.readlines()]
        
        for i, score in enumerate(scores):
            score_text = font.render(f"{i+1}. {score}", True, RED)
            screen.blit(score_text, (WIDTH//2 - 40, 100 + i * 30))
    
    pygame.display.update()
    pygame.time.delay(3000)

def welcome_screen():
    #This function shows the first screen the player gets once running the code.
    screen.fill(WHITE)
    title_text = font.render("Recycle Rush - Sustainability at University of Exeter", True, BLUE)
    instructions = [ 
        #This will show the instructions of the game for the player, giving them an idea of how to play.
        "Use LEFT and RIGHT arrows to move the bin.",
        "Press 1, 2, 3, or 4 to select a bin type.",
        "Catch the correct rubbish with the right bin to score points!",
        "Avoid catching the wrong type or you lose lives.",
        "Press SPACE to start!"
    ]
    screen.blit(title_text, (WIDTH//2 - 325, HEIGHT//4))
    for i, line in enumerate(instructions):
        text = font.render(line, True, RED)
        screen.blit(text, (WIDTH//2 - 325, HEIGHT//3 + i * 30))
    pygame.display.update()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                waiting = False
                #once player wants to start playing, 'waiting' goes to 'False' and the game starts. 

welcome_screen()

bin_images = {
    # This shows the different types of bin in the game, each of which having a differnt purpose.
    "plastic": pygame.image.load("Images/Recycle_Bin_Plastic.png"),
    "battery": pygame.image.load("Images/Recycle_Bin_Battery.png"),
    "can": pygame.image.load("Images/Recycle_Bin_Can.png"),
    "paper": pygame.image.load("Images/Recycle_Bin_Paper.png")
}

for key in bin_images:
    bin_images[key] = pygame.transform.scale(bin_images[key], (120, 120)) 
    #Scaling the bins size for better visibility while playing

rubbish_images = {
    # This shows the different types of recycleable rubbish in the game, each requiring a differnt bin.
    "plastic": pygame.image.load("Images/Recycle_PBottle.png"),
    "battery": pygame.image.load("Images/Recycle_Battery.png"),
    "can": pygame.image.load("Images/Recycle_can.png"),
    "paper": pygame.image.load("Images/Recycle_Paper.png")
}

for key in rubbish_images:
    rubbish_images[key] = pygame.transform.scale(rubbish_images[key], (120, 120))
    #Scaling the bins size for better visibility while playing


bins = {
    #This shows the bins on the side of the game, to show the different bins to alternate from.
    "plastic": (WIDTH - 150, HEIGHT // 5),
    "battery": (WIDTH - 150, HEIGHT // 5 * 2),
    "can": (WIDTH - 150, HEIGHT // 5 * 3),
    "paper": (WIDTH - 150, HEIGHT // 5 * 4)
}

#This section of code shows the random areas the rubbish will be falling from, with initial speed.
#It also shows the number of lives a player starts with, 3.
rubbish_type = random.choice(list(rubbish_images.keys()))
rubbish_x = random.randint(20, WIDTH - 200)
rubbish_y = 100
rubbish_speed = 5
score = 0
lives = 3

#Starts the game with the plastic bin, on the bottom of the page, and sets the player speed to 10.
player_bin_type = "plastic"
player_bin_x = WIDTH // 2 - 50
player_bin_y = HEIGHT - 140
player_speed = 10


running = True #Let's the game run(Start)
while running:
    pygame.time.delay(30)
    screen.fill(WHITE) #sets a white background
    
    for event in pygame.event.get():
        #Incase someone wants to quit, it will return 'running' to 'false'
        if event.type == pygame.QUIT:
            running = False
        #This for-loop shows how the player can alternate between the different bins
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1: #1
                player_bin_type = "plastic"
            elif event.key == pygame.K_2: #2
                player_bin_type = "battery"
            elif event.key == pygame.K_3: #3
                player_bin_type = "can"
            elif event.key == pygame.K_4: #4
                player_bin_type = "paper"
    
    #This shows how the player can move right and left
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_bin_x > 0:
        player_bin_x -= player_speed
    if keys[pygame.K_RIGHT] and player_bin_x < WIDTH - 140:
        player_bin_x += player_speed
    
    rubbish_y += rubbish_speed
    
    
    if rubbish_y + 120 >= player_bin_y and player_bin_x < rubbish_x < player_bin_x + 140:
        if player_bin_type == rubbish_type:
            score += 1
            if score % 5 == 0:
                rubbish_speed += 1
                #Whenever the player correctly disposes the recycleable into the right bin
                #There score will increase by one.
                #Every 5 points, the rubbish will Fall down a little faster
        else:
            lives -= 1
        rubbish_type = random.choice(list(rubbish_images.keys()))
        rubbish_x = random.randint(20, WIDTH - 200)
        rubbish_y = 0
    elif rubbish_y > HEIGHT:
        lives -= 1
        rubbish_type = random.choice(list(rubbish_images.keys()))
        rubbish_x = random.randint(20, WIDTH - 200)
        rubbish_y = 0
        #the else, and elif statements shows that a player loses points when they miss the rubbish completely 
        #or place them into the wrong bin type.
    
    for bin_type, (x, y) in bins.items():
        screen.blit(bin_images[bin_type], (x, y))
    
    screen.blit(rubbish_images[rubbish_type], (rubbish_x, rubbish_y))
    screen.blit(bin_images[player_bin_type], (player_bin_x, player_bin_y))
    
    score_text = font.render(f"Score: {score}", True, BLUE) #Shows the score the player currently has.
    lives_text = font.render(f"Lives: {lives}", True, RED) #Shows the number of lives the player currently has.
    screen.blit(score_text, (10, 10))
    screen.blit(lives_text, (10, 40))
    
    if lives == 0:
        save_score(score)
        display_leaderboard()
        running = False 
        #once a player loses all their lives, the game ends, displaying their score, and the leaderboard
    
    pygame.display.update() 

pygame.quit()
