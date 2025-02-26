import pygame
import sys
import __main__


def guide_window():
    SCREEN = __main__.SCREEN
    IMAGES = __main__.IMAGES
    GREEN = __main__.GREEN
    DARKBLUE = __main__.DARKBLUE
    floor_y = __main__.floor_y
    CLOCK = __main__.CLOCK
    FPS = 60
    WIDTH, HEIGHT = 640, 800

    player_x = WIDTH * 0.5
    player_y = 720
    player_x_vel = 1  # 帧与帧之间，人物移动1像素
    player_x_range = [player_x - 100, player_x + 100]
    #  idx 代表人物跑步的6个状态中的第idx个   frames 描述跑步时每个状态持续5帧
    idx = 0
    frames = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:  # 按下空格时进入下一界面
                return

        SCREEN.fill((160, 172, 248))
        SCREEN.blit(IMAGES['floor'], (0, floor_y))

        test_font = pygame.font.SysFont("隶书", 78)
        text_surface = test_font.render("游戏提示", True, GREEN)
        SCREEN.blit(text_surface, (40, 30))
        test_font = pygame.font.SysFont("华文中宋", 20)
        text_surface = test_font.render("1、本游戏是闯关游戏，玩家需要选择合适的人生路径以到达进入下", True, DARKBLUE)
        SCREEN.blit(text_surface, (30, 130))
        text_surface = test_font.render("一人生阶段的传送门。每个阶段都有时间限制，超时则需重新开始", True, DARKBLUE)
        SCREEN.blit(text_surface, (30, 160))
        text_surface = test_font.render("2、UP——跳跃  LEFT——左行  RIGHT——右行  ESC——退出", True, DARKBLUE)
        SCREEN.blit(text_surface, (30, 220))
        text_surface = test_font.render("3、闯完四个关卡，游戏即告结束。希望玩家在闯关过程中能找到", True, DARKBLUE)
        SCREEN.blit(text_surface, (30, 270))
        text_surface = test_font.render("属于自己的人生道路，回首过去的自己，继往开来。", True, DARKBLUE)
        SCREEN.blit(text_surface, (30, 300))
        text_surface = test_font.render("4、游戏在各阶段设置了不同的障碍，请玩家莫误入歧途。", True, DARKBLUE)
        SCREEN.blit(text_surface, (30, 350))
        text_surface = test_font.render("5、游戏没有唯一的通关路径，各关卡“死亡”的方式也各不相同。", True, DARKBLUE)
        SCREEN.blit(text_surface, (30, 400))
        text_surface = test_font.render("6、游戏特性：为模拟成人阶段的负担，游戏会有正常的掉帧卡顿。", True, DARKBLUE)
        SCREEN.blit(text_surface, (30, 450))
        text_surface = test_font.render("7、本游戏没有输赢，正如人生不能用成功失败来衡量。", True, DARKBLUE)
        SCREEN.blit(text_surface, (30, 500))
        text_surface = test_font.render("8、游戏只能顺序进行，进入下一关卡前必须通过当前关卡。", True, DARKBLUE)
        SCREEN.blit(text_surface, (30, 550))
        test_font = pygame.font.SysFont("幼圆", 40)
        text_surface = test_font.render("按下空格键，开启游戏人生！", True, (95, 10, 30))
        SCREEN.blit(text_surface, (70, 650))

        player_x += player_x_vel
        if player_x < player_x_range[0] or player_x > player_x_range[1]:
            player_x_vel *= -1
        if player_x_vel < 0:  # 如果人物往左走，要用到向左的素材图片
            SCREEN.blit(IMAGES['player'][frames[idx] + 6], (player_x, player_y))
        else:
            SCREEN.blit(IMAGES['player'][frames[idx]], (player_x, player_y))

        idx += 1
        idx %= len(frames)

        pygame.display.update()
        CLOCK.tick(FPS)
