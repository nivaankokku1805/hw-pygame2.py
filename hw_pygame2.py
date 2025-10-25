import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Circle and Text Controlled by Arrow Keys")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Circle properties
circle_x, circle_y = WIDTH // 2, HEIGHT // 2
circle_radius = 30
circle_speed = 5

# Font for text
font = pygame.font.Font(None, 36)
text = "Move me with arrow keys!"

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get keys pressed
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        circle_y -= circle_speed
    if keys[pygame.K_DOWN]:
        circle_y += circle_speed
    if keys[pygame.K_LEFT]:
        circle_x -= circle_speed
    if keys[pygame.K_RIGHT]:
        circle_x += circle_speed

    # Prevent circle from going out of bounds
    circle_x = max(circle_radius, min(WIDTH - circle_radius, circle_x))
    circle_y = max(circle_radius, min(HEIGHT - circle_radius, circle_y))

    # Draw everything
    screen.fill(WHITE)  # Clear screen
    pygame.draw.circle(screen, BLUE, (circle_x, circle_y), circle_radius)  # Draw circle
    text_surface = font.render(text, True, BLACK)  # Render text
    screen.blit(text_surface, (20, 20))  # Draw text

    pygame.display.flip()  # Update display
    pygame.time.Clock().tick(60)  # Limit FPS to 60

# Quit Pygame
pygame.quit()
sys.exit()