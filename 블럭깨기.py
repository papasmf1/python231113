import pygame
import sys
from pygame.locals import *

# 초기화
pygame.init()

# 화면 설정
width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("블록 깨기 게임")

# 색상 정의
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# 패들 설정
paddle_width, paddle_height = 400, 10
paddle_x, paddle_y = (width - paddle_width) // 2, height - 20

# 공 설정
ball_radius = 10
ball_x, ball_y = width // 2, height // 2
ball_speed_x, ball_speed_y = 5, 5

# 블록 설정
block_width, block_height = 50, 20
block_rows, block_cols = 4, 10
blocks = []

for row in range(block_rows):
    for col in range(block_cols):
        block_x = col * (block_width + 5)
        block_y = row * (block_height + 5)
        blocks.append(pygame.Rect(block_x, block_y, block_width, block_height))

# 게임 루프
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    paddle_x += (keys[K_RIGHT] - keys[K_LEFT]) * 5

    # 공 이동
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # 벽과의 충돌 처리
    if ball_x - ball_radius <= 0 or ball_x + ball_radius >= width:
        ball_speed_x = -ball_speed_x

    if ball_y - ball_radius <= 0:
        ball_speed_y = -ball_speed_y

    # 패들과의 충돌 처리
    if (
        paddle_x < ball_x < paddle_x + paddle_width
        and paddle_y < ball_y < paddle_y + paddle_height
    ):
        ball_speed_y = -ball_speed_y

    # 블록과의 충돌 처리
    for block in blocks:
        if block.colliderect(pygame.Rect(ball_x - ball_radius, ball_y - ball_radius, 2 * ball_radius, 2 * ball_radius)):
            ball_speed_y = -ball_speed_y
            blocks.remove(block)
            break

    # 화면 그리기
    screen.fill(black)
    pygame.draw.rect(screen, white, (paddle_x, paddle_y, paddle_width, paddle_height))
    pygame.draw.circle(screen, red, (int(ball_x), int(ball_y)), ball_radius)

    for block in blocks:
        pygame.draw.rect(screen, white, block)

    pygame.display.flip()

    # 초당 프레임 설정
    pygame.time.Clock().tick(60)
