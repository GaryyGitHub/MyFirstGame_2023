import pygame
import sys
import __main__


def menu_window():
    SCREEN = __main__.SCREEN
    IMAGES = __main__.IMAGES
    GREEN = __main__.GREEN
    DARKRED = __main__.DARKRED
    BLACK = __main__.BLACK
    CLOCK = __main__.CLOCK
    FPS = __main__.FPS

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:  # 按下空格时游戏开始
                return
        SCREEN.blit(IMAGES['guide'], (0, 0))

        test_font = pygame.font.SysFont("华文中宋", 78)
        text_surface = test_font.render("道阻且长，", True, GREEN)
        SCREEN.blit(text_surface, (40, 70))
        text_surface = test_font.render("行而不辍。", True, GREEN)
        SCREEN.blit(text_surface, (96, 200))
        test_font = pygame.font.SysFont("consolas", 18)
        text_surface = test_font.render("Life is but a Span Full of Choosing, ", True, DARKRED)
        SCREEN.blit(text_surface, (130, 400))
        text_surface = test_font.render("With Nothing Left in the End.", True, DARKRED)
        SCREEN.blit(text_surface, (180, 433))
        test_font = pygame.font.SysFont("bodoniblack", 30)
        text_surface = test_font.render("Press SPACE to continue", True, BLACK)
        SCREEN.blit(text_surface, (200, 580))
        pygame.display.update()
        CLOCK.tick(FPS)
