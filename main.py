# Example file showing a circle moving on screen
import pygame
from constants import WINDOW_HEIGHT, WINDOW_WIDTH, FLOOR_Y, FPS, GAME_SPEED
from dino import Dino
from environment import Environment
import neat
pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

def eval_genomes(genomes, config):
    nets = []
    ge = []
    dinos = []

    for _, g in genomes:
        net = neat.nn.FeedForwardNetwork.create(g, config)
        nets.append(net)

        dinos.append(Dino(FLOOR_Y, 'assets/dino.png'))
        g.fitness = 0
        ge.append(g)


    clock = pygame.time.Clock()

    environment = Environment(screen, dinos, GAME_SPEED, ge, nets)

    dt = 0
    clock.tick(FPS)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

        environment.add_cactus()
        environment.update(dt)    
        environment.draw()
        environment.dino_collision()
        
        if len(environment.dinos) == 0:
            running = False
            print("---------------------------------no more dinos-------------")
            break
        
        dt = clock.tick(FPS) / 1000.0

    

def run(config_file):
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         config_file)

    # Create the population, which is the top-level object for a NEAT run.
    p = neat.Population(config)

    # Add a stdout reporter to show progress in the terminal.
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)
    #p.add_reporter(neat.Checkpointer(5))

    # Run for up to 50 generations.
    winner = p.run(eval_genomes, 50)

    # show final stats
    print('\nBest genome:\n{!s}'.format(winner))

if __name__ == '__main__':
    run("config-dino")