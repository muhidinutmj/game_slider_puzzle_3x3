import pygame
import sys

# Inisialisasi Pygame
pygame.init()

# Ukuran layar
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pilih Latar Belakang")

# Warna
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
# BLUE = (0, 100, 255)

# Font
font = pygame.font.SysFont(None, 40)

# Tombol
button_black = pygame.Rect(100, 150, 180, 60)
button_white = pygame.Rect(320, 150, 180, 60)

# Status latar belakang
background_color = WHITE

def draw_menu():
    screen.fill(background_color)

    # Tentukan warna teks berdasarkan latar belakang
    text_color = BLACK if background_color == WHITE else WHITE

    # Judul
    title = font.render("Pilih Warna Latar", True, text_color)
    screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 50))

    # Tombol Hitam
    pygame.draw.rect(screen, GRAY, button_black)
    text_black = font.render("Hitam", True, BLACK)
    screen.blit(text_black, (button_black.x + 40, button_black.y + 15))

    # Tombol Putih
    pygame.draw.rect(screen, GRAY, button_white)
    text_white = font.render("Putih", True, BLACK)
    screen.blit(text_white, (button_white.x + 40, button_white.y + 15))

    pygame.display.flip()

# Loop utama
running = True
while running:
    draw_menu()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button_black.collidepoint(event.pos):
                background_color = BLACK
            elif button_white.collidepoint(event.pos):
                background_color = WHITE

pygame.quit()
sys.exit()
