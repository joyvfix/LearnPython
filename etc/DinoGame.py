# import numpy as np
# import cv2
# import math
# import pyautogui

# #open camera
# capture = cv2.VideoCapture(0)

# while capture.isOpened():

#     dilation = cv2.dilate(mask2,kernel,iterations=1)
#     erosion = cv2.erode(dilation,kernel,iterations=1)

#     filtered = cv2.GaussianBlur(erosian(3,3)0)
#     ret,thresh = cv2.threshold(filtered,127,255,0)
#     contours,hierachy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

#     cv2.imshow("Gesture",frame)

#     if cv2.waitKey(1) == ord("q"):
#         capture.release()
#         cv2.destroyAllWindows
# {::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::}
# import numpy as np
# import cv2

# # Open camera
# capture = cv2.VideoCapture(0)

# while capture.isOpened():
#     ret, frame = capture.read()
#     if not ret:
#         break

#     # Convert the frame to grayscale for processing
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#     # Apply a Gaussian Blur to the grayscale frame
#     filtered = cv2.GaussianBlur(gray, (3, 3), 0)

#     # Threshold the filtered frame to create a binary image
#     ret, thresh = cv2.threshold(filtered, 127, 255, 0)

#     # Find contours in the binary image
#     contours, hierarchy = cv2.findContours(
#         thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

#     # Draw the contours on the original frame
#     cv2.drawContours(frame, contours, -1, (0, 255, 0), 3)

#     # Show the frame with contours
#     cv2.imshow("Gesture", frame)

#     if cv2.waitKey(1) == ord("q"):
#         break

# capture.release()
# cv2.destroyAllWindows()
# {:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::}
# import numpy as np
# import cv2
# import pyautogui

# # Open camera
# capture = cv2.VideoCapture(0)

# while capture.isOpened():
#     ret, frame = capture.read()
#     if not ret:
#         break

#     # Convert the frame to grayscale for processing
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#     # Apply a Gaussian Blur to the grayscale frame
#     filtered = cv2.GaussianBlur(gray, (3, 3), 0)

#     # Threshold the filtered frame to create a binary image
#     ret, thresh = cv2.threshold(filtered, 127, 255, 0)

#     # Find contours in the binary image
#     contours, hierarchy = cv2.findContours(
#         thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

#     # Draw the contours on the original frame
#     cv2.drawContours(frame, contours, -1, (0, 255, 0), 3)

#     # Show the frame with contours
#     cv2.imshow("Gesture", frame)

#     # Check for keyboard inputs to control volume
#     key = cv2.waitKey(1)
#     if key == ord("q"):
#         break
#     elif key == ord("+"):
#         # Simulate volume up key press
#         pyautogui.press("volumeup")
#     elif key == ord("-"):
#         # Simulate volume down key press
#         pyautogui.press("volumedown")

# capture.release()
# cv2.destroyAllWindows()
# {:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::}
import pygame
import random

# Initialize pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 300
GROUND_HEIGHT = 40
DINO_WIDTH, DINO_HEIGHT = 50, 50
CLOUD_WIDTH, CLOUD_HEIGHT = 50, 30
CACTUS_WIDTH, CACTUS_HEIGHT = 20, 50
JUMP_HEIGHT = 8

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Dino Game')

# Load images
dino_img = pygame.image.load('dino.png')
cloud_img = pygame.image.load('cloud.png')
cactus_img = pygame.image.load('cactus.png')

# Function to draw the ground


def draw_ground():
    pygame.draw.rect(screen, BLACK, (0, SCREEN_HEIGHT -
                     GROUND_HEIGHT, SCREEN_WIDTH, GROUND_HEIGHT))

# Function to create a new cactus obstacle


def create_cactus():
    return pygame.Rect(SCREEN_WIDTH, SCREEN_HEIGHT - GROUND_HEIGHT - CACTUS_HEIGHT, CACTUS_WIDTH, CACTUS_HEIGHT)

# Main game loop


def main():
    clock = pygame.time.Clock()

    # Dino variables
    dino_x = 100
    dino_y = SCREEN_HEIGHT - GROUND_HEIGHT - DINO_HEIGHT
    dino_dy = 0
    is_jumping = False

    # Obstacle variables
    obstacles = []
    obstacle_spawn_time = 0

    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not is_jumping:
                    is_jumping = True
                    dino_dy = -JUMP_HEIGHT

        # Gravity for dino
        if dino_y < SCREEN_HEIGHT - GROUND_HEIGHT - DINO_HEIGHT:
            dino_dy += 1
        else:
            dino_dy = 0
            is_jumping = False

        dino_y += dino_dy

        # Spawning obstacles
        if pygame.time.get_ticks() - obstacle_spawn_time > 1500:
            obstacles.append(create_cactus())
            obstacle_spawn_time = pygame.time.get_ticks()

        # Move and remove obstacles
        for obstacle in obstacles:
            obstacle.x -= 5
            if obstacle.x + CACTUS_WIDTH < 0:
                obstacles.remove(obstacle)

        # Check for collisions with obstacles
        for obstacle in obstacles:
            if dino_x + DINO_WIDTH > obstacle.x and dino_x < obstacle.x + CACTUS_WIDTH \
                    and dino_y + DINO_HEIGHT > obstacle.y:
                game_over = True

        # Draw everything
        screen.fill(WHITE)
        screen.blit(dino_img, (dino_x, dino_y))
        for obstacle in obstacles:
            screen.blit(cactus_img, (obstacle.x, obstacle.y))
        draw_ground()

        pygame.display.update()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
