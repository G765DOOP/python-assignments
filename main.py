import pygame
import time
import random

WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("IDK")

def main():
    run = True

    while run:
        for event in pygame. event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            b = myint(2,3)
            print(b)
    pygame.quit

if __name__ == "__main__":
    main()


    def myint(x,y):
        s = x+y 
        return s




       