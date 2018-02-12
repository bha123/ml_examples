#Library for games in python
import pygame

# Which direction our ball is going
import random


#Variables for game

# frame rate 
FPS = 60

#size of our window
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400


# size of our paddle

PADDLE_WIDTH = 10
PADDLE_HEIGHT = 60

#size of the ball
BALL_WIDTH = 10
BALL_HEIGHT = 10

#Speed of our paddle & ball
PADDLE_SPEED = 2
BALL_X_SPEED = 3
BALL_Y_SPEED = 2

#RGB Colors paddle and ball
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

#Initialize our screen

screen = pygame.display.set_mode(WINDOW_WIDTH, WINDOW_HEIGHT)

def drawBall(ballXpos, ballYpos):

    ball = pygame.rect(ballXpos, ballYpos, BALL_WIDTH, BALL_HEIGHT)    
    pygame.draw.rect(screen, WHITE, ball)


def drawPaddle1(paddle1YPos):

    paddle1 = pygame.rect(PADDLE_BUFFER, paddle1YPos, PADDLE_WIDTH, PADDLE_HEIGHT)
    pygame.draw.rect(screen, WHITE, paddle1)


def drawPaddle2(paddle2YPos):

    paddle2 = pygame.rect(WINDOW_WIDTH - PADDLE_BUFFER - PADDLE_WIDTH, paddle2YPos, PADDLE_WIDTH, PADDLE_HEIGHT)
    pygame.draw.rect(screen, WHITE, paddle2)


def updateBall(paddle1YPos, paddle2YPos, ballXpos, ballYpos, ballXDirection, ballYDirection):

    #update x and y position

    ballXPos = ballXPos + ballXDirection * BALL_X_SPEED
    ballYPos = ballYPos + ballYDirection * BALL_Y_SPEED
    score = 0

    # Check for collision , if the ball hits the left side
    # then we swithch direction
    if(ballXPos <= PADDLE_BUFFER  + PADDLE_WIDTH and ballYPos + BALL_HEIGHT >= paddle1YPos and ballYPos - BALL_HEIGHT <= paddle1YPos + PADDLE_HEIGHT):
        ballXDirection = 1
    elif (ballXPos <= 0):
        ballXDirection = 1
        score = -1
        return [score, paddle1YPos, paddle2YPos, ballXpos, ballYPos, ballXDirection,ballYDirection] 

    
    if(ballXPos >= WINDOW_WIDTH - PADDLE_WIDTH - PADDLE_BUFFER and ballYPos + 
    
