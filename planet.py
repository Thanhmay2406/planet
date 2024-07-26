import pygame
import math

pygame.init()

# create window
WIDTH, HEIGHT = 800, 800
WINDOW = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("PLANET SIMULATOR")

# create the planet class
class planet:
    # astronomocal unit
    AU = 149.6e6 * 1000
    G = 6.67428e-11
    SCALE = 250 / AU # 1 AU = 100 pixel
    TIMESTEP = 3600 * 24 # 1 day

    def __init__ (self , x , y , radius, color , mass):
        # define simple variable create the planet
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.mass = mass
        
        self.orbit = []
        self.sun = False #check if this planet is the sun?
        self.distance_to_sun = 0 #distance from the planet to the sun

        # make x,y vel
        self.x_vel = 0
        self.y_vel = 0

    def draw(self , win):
        x = self.x * self.SCALE + WIDTH/2
        y = self.y * self.SCALE + HEIGHT/2
        pygame.draw.circle(win , self.color,(x,y),self.radius)

# main funtion
def main():
    ok = True
    clock = pygame.time.Clock()
    
    while (ok):
        clock.tick(60)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ok = False

    pygame.quit()


# run =)))
main()