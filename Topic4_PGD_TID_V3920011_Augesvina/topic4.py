import pygame
import sys  # mengimport semua library dari python
from pygame import rect
from pygame.locals import *
import time

WIDTH, HEIGHT = 400, 400
pygame.display.set_caption('Smooth Movement')

pygame.init()  # melakukan inisialisasi atau deklarasi variabel dan objek yang dibutuhkan
win = pygame.display.set_mode((WIDTH, HEIGHT))  # mengatur ukuran layar display
clock = pygame.time.Clock()  # membuat jam yang dapat digunakan untuk melacak waktu

BLACK = (0, 0, 0)  # membuat index kode warna yang digunakan
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PINK = (255, 0, 127)
YELLOW = (255, 255, 0)


class Player:
    # fungsi untuk operasi yang harus dilakukan sebelum object dibuat yaitu self
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)
        self.rect = pygame.Rect(self.x, self.y, 32, 32)
        self.color = (250, 120, 60)
        self.velX = 0
        self.velY = 0
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False
        self.speed = 4

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)

    def update(self):  # membuat batas titik yang akan dilalui gambar saat bergerak
        self.velX = 0
        self.velY = 0
        if self.left_pressed and not self.right_pressed:
            self.velX = -self.speed
        if self.right_pressed and not self.left_pressed:
            self.velX = self.speed
        if self.up_pressed and not self.down_pressed:
            self.velY = -self.speed
        if self.down_pressed and not self.up_pressed:
            self.velY = self.speed

        self.x += self.velX
        self.y += self.velY

        self.rect = pygame.Rect(int(self.x), int(self.y), 32, 32)


player = Player(WIDTH/2, HEIGHT/2)

font_color = (0, 0, 255)  # mengubah warna font
font_obj = pygame.font.Font("C:\Windows\Fonts\RAVIE.TTF", 25)
text = "AUGESVINA S. L"  # menambahkan text pada screen
img = font_obj.render(text, True, (BLUE))  # mengubah gaya font dan warna font

rect = img.get_rect()
rect.topleft = (20, 20)
cursor = Rect(rect.topright, (3, rect.height))

while True:

    for event in pygame.event.get():  # sintaks ini akan membantu mengosongkan antrean sebelum menambahkan yang baru
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:  # membuat kondisi baru untuk mengatur key sebagai yang menjalankan aksi ke kanan kiri atas bawah
            if event.key == pygame.K_LEFT:
                player.left_pressed = True
            if event.key == pygame.K_RIGHT:
                player.right_pressed = True
            if event.key == pygame.K_UP:
                player.up_pressed = True
            if event.key == pygame.K_DOWN:
                player.down_pressed = True
        if event.type == pygame.KEYUP:  # kondisi baru untuk mengatur key sebagai yang menjalankan aksi
            if event.key == pygame.K_LEFT:
                player.left_pressed = False
            if event.key == pygame.K_RIGHT:
                player.right_pressed = False
            if event.key == pygame.K_UP:
                player.up_pressed = False
            if event.key == pygame.K_DOWN:
                player.down_pressed = False

            if event.type == QUIT:
                running = False

            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    if len(text) > 0:
                        text = text[:-1]

                else:
                    text += event.unicode
                    img = font_obj.render(text, True, BLACK)
                    rect.size = img.get_size()
                    cursor.topleft = rect.topright

    win.fill((GREEN))  # mengubah warna background screen window
    pygame.draw.rect(win, (BLUE), player)  # mengubah warna player

    win.blit(img, rect)
    if time.time() % 1 > 0.5:  # kode ini merupakan kode untuk kursor pada kalimat
        pygame.draw.rect(win, BLACK, cursor)  # mengubah warna kursor
    pygame.display.update()  # untuk mengupdate tampilan pada layar

    player.update()
    # kode ini diperlukan agar pembaruan apa saja yang dilakukan pada layar game bisa terlihat
    pygame.display.flip()

    # untuk mengupdate tampilan pada layar dan juga untuk mengupdate waktu
    clock.tick(120)
    pygame.display.update()  # untuk mengupdate tampilan pada layar

pygame.quit()  # keluar dari program
