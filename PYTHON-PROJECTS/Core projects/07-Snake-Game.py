import pygame
import random
import time

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 600, 400
NAVBAR_HEIGHT = 50  # Height of the navbar
GAME_HEIGHT = HEIGHT - NAVBAR_HEIGHT  # Height of the game area
CELL_SIZE = 20

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
DARK_GREEN = (0, 100, 0)

# Fonts
font = pygame.font.SysFont(None, 35)
welcome_font = pygame.font.Font(None, 50)  # Stylish font for welcome message
game_over_font = pygame.font.Font(None, 40)  # Stylish font for game over message

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Realistic Snake Game")

# Clock
clock = pygame.time.Clock()

# Snake and food
snake = [(100, 100 + NAVBAR_HEIGHT), (80, 100 + NAVBAR_HEIGHT), (60, 100 + NAVBAR_HEIGHT)]
snake_dir = (CELL_SIZE, 0)
food = (random.randint(0, (WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE,
        random.randint(0, (GAME_HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE + NAVBAR_HEIGHT)
food_radius = CELL_SIZE // 2

# Game variables
score = 0
high_score = 0
start_time = time.time()
paused = False
game_over = False
wait_for_input = False  # Wait for direction key after resuming

# Button class
class Button:
    def __init__(self, x, y, width, height, text, color, hover_color, border_radius=10, shadow=True):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.border_radius = border_radius
        self.shadow = shadow

    def draw(self, screen):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            button_color = self.hover_color
        else:
            button_color = self.color

        # Draw shadow
        if self.shadow:
            shadow_rect = pygame.Rect(self.rect.x + 5, self.rect.y + 5, self.rect.width, self.rect.height)
            pygame.draw.rect(screen, (0, 0, 0, 100), shadow_rect, border_radius=self.border_radius)

        # Draw button
        pygame.draw.rect(screen, button_color, self.rect, border_radius=self.border_radius)

        # Draw text
        text_surf = font.render(self.text, True, WHITE)
        text_rect = text_surf.get_rect(center=self.rect.center)
        screen.blit(text_surf, text_rect)

    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                return True
        return False

# Start screen buttons
start_button = Button(WIDTH // 2 - 75, HEIGHT // 2 - 50, 150, 50, "Start", (0, 200, 0), (0, 255, 0), border_radius=15, shadow=True)
quit_button = Button(WIDTH // 2 - 75, HEIGHT // 2 + 20, 150, 50, "Quit", (200, 0, 0), (255, 0, 0), border_radius=15, shadow=True)

# Pause screen buttons
resume_button = Button(WIDTH // 2 - 75, HEIGHT // 2 - 50, 150, 50, "Resume", (0, 200, 0), (0, 255, 0), border_radius=15, shadow=True)
pause_quit_button = Button(WIDTH // 2 - 75, HEIGHT // 2 + 20, 150, 50, "Quit", (200, 0, 0), (255, 0, 0), border_radius=15, shadow=True)

# Game over screen buttons
play_again_button = Button(WIDTH // 2 - 100, HEIGHT // 2 - 50, 200, 50, "Play Again", (0, 200, 0), (0, 255, 0), border_radius=15, shadow=True)
game_over_quit_button = Button(WIDTH // 2 - 100, HEIGHT // 2 + 20, 200, 50, "Quit", (200, 0, 0), (255, 0, 0), border_radius=15, shadow=True)

def draw_navbar():
    """
    Draws the navbar at the top of the screen with score, time, and high score.
    """
    # Draw navbar background
    pygame.draw.rect(screen, BLUE, (0, 0, WIDTH, NAVBAR_HEIGHT))

    # Calculate elapsed time
    elapsed_time = int(time.time() - start_time)

    # Render text for score, time, and high score
    score_text = font.render(f"Score: {score}", True, WHITE)
    time_text = font.render(f"Time: {elapsed_time}", True, WHITE)
    high_score_text = font.render(f"High Score: {high_score}", True, WHITE)

    # Position text in the navbar
    screen.blit(score_text, (10, 10))
    screen.blit(time_text, (WIDTH // 2 - 50, 10))
    screen.blit(high_score_text, (WIDTH - 200, 10))

def draw_snake():
    """
    Draws the snake with a realistic head, body, and tail.
    """
    for i, segment in enumerate(snake):
        if i == 0:  # Draw the head
            pygame.draw.circle(screen, DARK_GREEN, (segment[0] + CELL_SIZE // 2, segment[1] + CELL_SIZE // 2), CELL_SIZE // 2)
            # Draw eyes
            eye_radius = 3
            eye_offset = 5
            pygame.draw.circle(screen, WHITE, (segment[0] + CELL_SIZE // 2 - eye_offset, segment[1] + CELL_SIZE // 2 - eye_offset), eye_radius)
            pygame.draw.circle(screen, WHITE, (segment[0] + CELL_SIZE // 2 + eye_offset, segment[1] + CELL_SIZE // 2 - eye_offset), eye_radius)
        else:  # Draw the body
            pygame.draw.circle(screen, GREEN, (segment[0] + CELL_SIZE // 2, segment[1] + CELL_SIZE // 2), CELL_SIZE // 2)

def draw_food():
    """
    Draws the food as a red circle.
    """
    pygame.draw.circle(screen, RED, (food[0] + CELL_SIZE // 2, food[1] + CELL_SIZE // 2), food_radius)

def check_collision():
    """
    Checks if the snake collides with the walls or itself.
    """
    if (snake[0][0] < 0 or snake[0][0] >= WIDTH or
        snake[0][1] < NAVBAR_HEIGHT or snake[0][1] >= HEIGHT or
        snake[0] in snake[1:]):
        return True
    return False

def generate_food():
    """
    Generates food at a random position not occupied by the snake.
    """
    while True:
        new_food = (random.randint(0, (WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE,
                    random.randint(0, (GAME_HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE + NAVBAR_HEIGHT)
        if new_food not in snake:
            return new_food

def start_screen():
    """
    Displays the start screen with a welcome message and Start/Quit buttons.
    """
    while True:
        screen.fill(BLACK)

        # Draw welcome message
        welcome_text = welcome_font.render("Welcome to Snake Game!", True, WHITE)
        welcome_rect = welcome_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 100))
        screen.blit(welcome_text, welcome_rect)

        # Draw buttons
        start_button.draw(screen)
        quit_button.draw(screen)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if start_button.is_clicked(event):
                return
            if quit_button.is_clicked(event):
                pygame.quit()
                return

def pause_screen():
    """
    Displays the pause screen with Resume and Quit buttons.
    """
    global paused, wait_for_input
    while paused:
        screen.fill(BLACK)
        resume_button.draw(screen)
        pause_quit_button.draw(screen)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if resume_button.is_clicked(event):
                paused = False
                wait_for_input = True  # Wait for direction key after resuming
            if pause_quit_button.is_clicked(event):
                pygame.quit()
                return

def game_over_screen():
    """
    Displays the game over screen with a "Well done" message and Play Again/Quit buttons.
    """
    global game_over
    while game_over:
        screen.fill(BLACK)

        # Draw "Well done" message
        well_done_text = game_over_font.render(f"Well done! Your score is {score}", True, WHITE)
        well_done_rect = well_done_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 100))
        screen.blit(well_done_text, well_done_rect)

        # Draw buttons
        play_again_button.draw(screen)
        game_over_quit_button.draw(screen)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if play_again_button.is_clicked(event):
                reset_game()
                return
            if game_over_quit_button.is_clicked(event):
                pygame.quit()
                return

def reset_game():
    """
    Resets the game to its initial state.
    """
    global snake, snake_dir, food, score, start_time, game_over, wait_for_input
    snake = [(100, 100 + NAVBAR_HEIGHT), (80, 100 + NAVBAR_HEIGHT), (60, 100 + NAVBAR_HEIGHT)]
    snake_dir = (CELL_SIZE, 0)
    food = generate_food()
    score = 0
    start_time = time.time()
    game_over = False
    wait_for_input = False

# Main game loop
def main():
    global snake, snake_dir, food, score, high_score, paused, game_over, wait_for_input

    start_screen()
    reset_game()

    while True:
        screen.fill(BLACK)

        # Draw the navbar
        draw_navbar()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    paused = not paused
                if not paused and not game_over:
                    if wait_for_input:
                        # Wait for a direction key to be pressed
                        if event.key in (pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT):
                            wait_for_input = False
                    if not wait_for_input:
                        if event.key == pygame.K_UP and snake_dir != (0, CELL_SIZE):
                            snake_dir = (0, -CELL_SIZE)
                        if event.key == pygame.K_DOWN and snake_dir != (0, -CELL_SIZE):
                            snake_dir = (0, CELL_SIZE)
                        if event.key == pygame.K_LEFT and snake_dir != (CELL_SIZE, 0):
                            snake_dir = (-CELL_SIZE, 0)
                        if event.key == pygame.K_RIGHT and snake_dir != (-CELL_SIZE, 0):
                            snake_dir = (CELL_SIZE, 0)

        if not paused and not game_over and not wait_for_input:
            new_head = (snake[0][0] + snake_dir[0], snake[0][1] + snake_dir[1])
            snake.insert(0, new_head)

            if snake[0] == food:
                score += 1
                if score > high_score:
                    high_score = score
                food = generate_food()
            else:
                snake.pop()

            if check_collision():
                game_over = True

        draw_snake()
        draw_food()

        if paused:
            pause_screen()
        if game_over:
            game_over_screen()

        pygame.display.flip()
        clock.tick(10)

if __name__ == "__main__":
    main()
