import pygame

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("First try")

running = True

white = (255, 255, 255)
red = (255, 0, 0)

ball_radius = 25
ball_x = 600 // 2
ball_y = 400 // 2
move_distance = 20

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running =  False
        elif event.type == pygame.KEYDOWN:
            new_x = ball_x
            new_y = ball_y  
            
            if event.key == pygame.K_UP: 
                new_y -= move_distance  
            elif event.key == pygame.K_DOWN:
                new_y += move_distance
            elif event.key == pygame.K_LEFT:
                new_x -= move_distance
            elif event.key == pygame.K_RIGHT:
                new_x += move_distance
                
            if (ball_radius <= new_x <= 600 - ball_radius and 
                ball_radius <= new_y <= 400 - ball_radius):
                
                ball_x = new_y
                ball_y = new_y
                
    screen.fill(white)
    
    pygame.draw.circle(screen, red, (ball_x,  ball_y), ball_radius)
    pygame.display.flip()
    
    clock.tick(60)
    
pygame.quit()



