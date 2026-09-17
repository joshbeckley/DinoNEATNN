import pygame
from constants import FLOOR_Y, CACTUS_FREQUENCY_SECS, BLACK, WHITE, GAME_SPEED_INCREASE
import random
from cactus import Cactus
from ground import Ground

class Environment:

    def __init__(self, screen, dinos, game_speed, ge, nets):
        self.screen = screen
        self.dinos = dinos
        self.game_speed = game_speed
        self.ge = ge
        self.nets = nets

        self.score = 0

        self.font = pygame.font.Font('freesansbold.ttf', 10)

        self.dino_group = pygame.sprite.Group()
        for dino in dinos:
            self.dino_group.add(dino)

        self.cactus_group = pygame.sprite.Group()

        self.ground = Ground(0, FLOOR_Y, "assets/ground.png")
        # TODO: could move in draw
        self.ground_group = pygame.sprite.Group()
        self.ground_group.add(self.ground)

        # self.last_cactus = pygame.time.get_ticks() - CACTUS_FREQUENCY
        self.elapsed_game_time = 0
        self.spawn_time_interval = CACTUS_FREQUENCY_SECS;
        self.spawn_time_interval_decrease = 0.03;
        self.next_spawn_time = self.spawn_time_interval;
        
        
    def add_cactus(self):
        if self.elapsed_game_time > self.next_spawn_time:
            random_x = random.randint(30,200)
            cactus = Cactus(self.screen.get_width() + 2 + random_x, FLOOR_Y, "assets/cactus.png")
            self.cactus_group.add(cactus)

            self.spawn_time_interval -= self.spawn_time_interval_decrease;
            self.next_spawn_time += self.spawn_time_interval;

    def dino_collision(self):
        for idx, dino in enumerate(self.dinos):
            if pygame.sprite.spritecollide(dino, self.cactus_group, False):
                self.ge[idx].fitness -= 1
                self.dinos.pop(idx)
                self.nets.pop(idx)
                self.ge.pop(idx)

                return dino

    def draw(self):
        self.screen.fill("white")

        # self.draw_info()

        self.dino_group.draw(self.screen)
        self.cactus_group.draw(self.screen)
        self.ground_group.draw(self.screen)

        pygame.display.update()

    def update(self, dt):
        self.dino_group.update(dt)

        for idx, dino in enumerate(self.dinos):
            # should i do this? since i update it anyway in a few lines
            # self.ge[x].fitness += 0.1

            output = self.nets[idx].activate((dino.grounded, dino.distance_to_cactus(self.cactus_group), self.game_speed * dt))
            if output[0] > 0.5:
                dino.jump()
            
            dino.update(dt)

        self.cactus_group.update(self.game_speed, dt)
        self.game_speed += GAME_SPEED_INCREASE * dt

        self.elapsed_game_time += 1 * dt
        self.score = self.elapsed_game_time * 10

        for g in self.ge:
            g.fitness += 5 * dt

    def draw_info(self):
        speed = self.font.render("Speed:".ljust(30) + f"{self.game_speed}", True, BLACK, WHITE)
        speedRect = speed.get_rect()
        speedRect.topleft = (10, 10)
        self.screen.blit(speed, speedRect)

        spawn = self.font.render(f"Spawn Interval:".ljust(24) + f"{self.spawn_time_interval}", True, BLACK, WHITE)
        spawnRect = spawn.get_rect()
        spawnRect.topleft = (10, 20)
        self.screen.blit(spawn, spawnRect)

        next = self.font.render(f"Next Spawn:".ljust(26) + f"{self.next_spawn_time}", True, BLACK, WHITE)
        nextRect = next.get_rect()
        nextRect.topleft = (10, 30)
        self.screen.blit(next, nextRect)

        elapsed = self.font.render(f"Elapsed Time:".ljust(25) + f"{self.elapsed_game_time}", True, BLACK, WHITE)
        elapsedRect = elapsed.get_rect()
        elapsedRect.topleft = (10, 40)
        self.screen.blit(elapsed, elapsedRect)

        score = self.font.render(f"Score:".ljust(31) + f"{self.score}", True, BLACK, WHITE)
        scoreRect = score.get_rect()
        scoreRect.topleft = (10, 50)
        self.screen.blit(score, scoreRect)

        distance = self.font.render(f"Distance:".ljust(29) + f"{self.dino.distance_to_cactus(self.cactus_group)}", True, BLACK, WHITE)
        distanceRect = distance.get_rect()
        distanceRect.topleft = (10, 60)
        self.screen.blit(distance, distanceRect)
        