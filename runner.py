
import pygame
import sys
import random

class Runner(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.number = 10

    def update(self, value = 0):
        self.number += value

class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.value = random.randint(1, 5)

class Game:
    def __init__(self):
        pygame.init()
        self.width, self.height = 800, 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Number Runner")
        self.clock = pygame.time.Clock()
        self.all_sprites = pygame.sprite.Group()
        self.runner = Runner()
        self.obstacle = Obstacle()
        self.all_sprites.add(self.runner, self.obstacle)
        self.score = 0

    def run(self):
        while True:
            self.handle_events()
            self.update()
            self.render()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def update(self):
        choice_a = random.randint(1, 10)
        choice_b = random.randint(1, 10)

        # Simulate player making a choice (always choosing the greater number)
        player_choice = max(choice_a, choice_b)

        self.runner.update(player_choice)

        if player_choice >= self.obstacle.value:
            self.score += 1
            self.obstacle = Obstacle()
            self.all_sprites.add(self.obstacle)
        else:
            print("Game Over! Your score:", self.score)
            # pygame.quit()
            # sys.exit()

        # Update all sprites
        self.all_sprites.update()

        self.clock.tick(60)

    def render(self):
        self.screen.fill((0, 0, 0))

        font = pygame.font.Font(None, 36)
        text_a = font.render(f"Choose: {random.randint(1, 10)}", True, (255, 255, 255))
        text_b = font.render(f"or {random.randint(1, 10)}", True, (255, 255, 255))
        obstacle_text = font.render(f"Obstacle: -{self.obstacle.value}", True, (255, 0, 0))
        player_text = font.render(f"Your Number: {self.runner.number}", True, (255, 255, 255))
        score_text = font.render(f"Score: {self.score}", True, (255, 255, 255))

        self.screen.blit(text_a, (50, 50))
        self.screen.blit(text_b, (50, 100))
        self.screen.blit(obstacle_text, (50, 350))
        self.screen.blit(player_text, (50, 200))
        self.screen.blit(score_text, (50, 250))

        self.all_sprites.draw(self.screen)
        pygame.display.flip()

if __name__ == "__main__":
    game = Game()
    game.run()
