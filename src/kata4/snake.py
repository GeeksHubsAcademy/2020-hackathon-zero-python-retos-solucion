import pygame, sys, time, random
from pygame.locals import *

#pygame.init()
#play_surface = pygame.display.set_mode((500, 500))
#fps = pygame.time.Clock()

class Snake():
    position = [100,50]
    body = [[100,50], [90,50],[80,50]]
    direction = "RIGHT"
    change = direction

    def controller(self, event, pygame):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                self.change = "RIGHT"
            if event.key == pygame.K_LEFT:
                self.change = "LEFT"
            if event.key == pygame.K_UP:
                self.change = "UP"
            if event.key == pygame.K_DOWN:
                self.change = "DOWN"

    def changeDirection(self):
        if self.change == "RIGHT" and self.direction != "LEFT":
            self.direction = "RIGHT"
        if self.change == "LEFT" and self.direction != "RIGHT":
            self.direction = "LEFT"
        if self.change == "UP" and self.direction != "DOWN":
            self.direction = "UP"
        if self.change == "DOWN" and self.direction != "UP":
            self.direction = "DOWN"

        if self.direction == "RIGHT":
            self.position[0] += 10
        if self.direction == "LEFT":
            self.position[0] -= 10
        if self.direction == "UP":
            self.position[1] -= 10
        if self.direction == "DOWN":
            self.position[1] += 10

        self.body.insert(0, list(self.position))

class Game():
    run = True
    food_pos = 0
    score = 0

    def __init__(self):
        self.food_spawn()

    def exit(self, event, pygame):
        if event.type == pygame.QUIT:
            self.run = False

    def food_spawn(self):
        self.food_pos = [random.randint(0,49)*10, random.randint(0,49)*10]

    def eat(self, snake):
        if snake.position == self.food_pos:
            self.food_spawn()
            self.score += 1
        else:
            snake.body.pop()

    def dead(self, snake):
        if snake.position[0] >= 500 or snake.position[0] <=0:
            print(f"Game Over! Score: {self.score})")
            self.run = False
            
        if snake.position[1] >= 500 or snake.position[1] <=0:
            print(f"Game Over! Score: {self.score})")
            self.run = False

        if snake.position in snake.body[1:]:
            print(f"Game Over! Score: {self.score})")
            self.run = False

def main():
    snake = Snake()
    game = Game()

    while game.run:
        for event in pygame.event.get():
            game.exit(event, pygame)
            snake.controller(event, pygame)

        snake.changeDirection()

        game.eat(snake)

        # Dibujar Snake
        play_surface.fill((0,0,0))
        for pos in snake.body:
            pygame.draw.rect(play_surface, (200,200,200), pygame.Rect(pos[0], pos[1], 10, 10))

        pygame.draw.rect(play_surface, (255,160,60), pygame.Rect(game.food_pos[0], game.food_pos[1], 10, 10))

        game.dead(snake)

        pygame.display.flip()
        fps.tick(10)

#main()
#pygame.quit()