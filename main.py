import os
import sys
import pygame
from components.player import Player, Youth, Adult, Old
from components.brick import Brick
from components.brick_long import BrickLong
from components.brick_vertical import BrickVert
from components.brick_longlong import BrickLL
from levels.menu_window import menu_window
from levels.guide_window import guide_window

# setup 设置
pygame.init()
SCREEN = pygame.display.set_mode((640, 800))
pygame.display.set_caption("道阻且长，行而不辍")  # title
CLOCK = pygame.time.Clock()

# materials dictionary 素材,利用字典存储
IMAGES = {}
for image in os.listdir('resources/picture'):
    name, extension = os.path.splitext(image)
    path = os.path.join('resources/picture', image)
    IMAGES[name] = pygame.image.load(path)

print(IMAGES)

# constants 常量
WIDTH, HEIGHT = 640, 800
FPS = 40
floor_y = HEIGHT - IMAGES['floor'].get_height()
dt = 0
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKRED = (120, 30, 70)
GREEN = (0, 80, 90)
DARKBLUE = (25, 10, 90)
BACKGROUND = (160, 172, 248)

IMAGES['player'] = [IMAGES['right1'], IMAGES['right2'], IMAGES['right3'], IMAGES['right4'], IMAGES['right5'], IMAGES['right6'],
                    IMAGES['left1'], IMAGES['left2'], IMAGES['left3'], IMAGES['left4'], IMAGES['left5'], IMAGES['left6']]
IMAGES['youth'] = [IMAGES['right11'], IMAGES['right12'], IMAGES['right13'], IMAGES['right14'], IMAGES['right15'], IMAGES['right16'],
                    IMAGES['left11'], IMAGES['left12'], IMAGES['left13'], IMAGES['left14'], IMAGES['left15'], IMAGES['left16']]
IMAGES['adult'] = [IMAGES['right21'], IMAGES['right22'], IMAGES['right23'], IMAGES['right24'],
                    IMAGES['left21'], IMAGES['left22'], IMAGES['left23'], IMAGES['left24']]
IMAGES['old'] = [IMAGES['right31'], IMAGES['right32'], IMAGES['right33'], IMAGES['right34'], IMAGES['right35'], IMAGES['right36'],
                    IMAGES['left31'], IMAGES['left32'], IMAGES['left33'], IMAGES['left34'], IMAGES['left35'], IMAGES['left36']]

# music 音乐
startMUSIC = pygame.mixer.Sound("resources/audio/menuBGM.mp3")
endMUSIC = pygame.mixer.Sound("resources/audio/endingBGM.mp3")
jumpSOUND = pygame.mixer.Sound("resources/audio/jump.wav")
dropSOUND = pygame.mixer.Sound("resources/audio/drop down.wav")
interestMUSIC = pygame.mixer.Sound("resources/audio/interestBGM.mp3")
youthMUSIC = pygame.mixer.Sound("resources/audio/youthBGM.flac")


def main():
    while True:
        startMUSIC.play()
        menu_window()
        guide_window()
        pygame.mixer.stop()
        youthMUSIC.play()
        child_window()


def child_window():
    #   计时器设定
    #   player 相关设定
    global dt
    counter, text = 45, '45'.rjust(3)
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    font = pygame.font.SysFont('华文中宋', 24)

    player = Player(WIDTH * 0.4, 739)  # 生成人物对象
    brick_group = pygame.sprite.Group()  # 建立brick精灵组，包含各类brick

    #  地图中的大平台
    brick_group.add(Brick(300, 715))
    # brick_group.add(Brick(200, 730))
    brick_group.add(Brick(400, 655))
    brick_group.add(Brick(500, 605))
    brick_group.add(Brick(380,555))
    brick_group.add(Brick(70, 365))
    brick_group.add(Brick(180, 300))
    brick_group.add(Brick(60, 262))
    brick_group.add(Brick(180, 220))
    brick_group.add(Brick(60, 175))
    brick_group.add(Brick(180, 140))
    brick_group.add(Brick(340, 343))
    brick_group.add(Brick(430, 295))
    brick_group.add(Brick(520, 247))
    brick_group.add(Brick(430, 185))
    brick_group.add(Brick(520, 130))

    brick_group.add(BrickLong(170, 505))
    brick_group.add(BrickLong(390, 470))
    brick_group.add(BrickLong(175, 410))

    jumping = False

    while True:
        # 创建舞台
        SCREEN.fill((160, 172, 248))
        SCREEN.blit(IMAGES['floor'], (0, floor_y))  # background

        SCREEN.blit(IMAGES['interest1'], (170, 435))
        SCREEN.blit(IMAGES['interest2'], (220, 455))
        SCREEN.blit(IMAGES['interest3'], (280, 455))
        SCREEN.blit(IMAGES['toy1'], (370, 400))
        SCREEN.blit(IMAGES['toy2'], (448, 400))
        SCREEN.blit(IMAGES['toy3'], (532, 400))
        SCREEN.blit(IMAGES['school'], (190, 360))
        SCREEN.blit(IMAGES['door'], (533, 70))
        SCREEN.blit(IMAGES['hospital'], (100, 684))

        test_font = pygame.font.SysFont("方正姚体", 40)
        text_surface = test_font.render("关卡一：童年        难度：简单", True, DARKBLUE)
        SCREEN.blit(text_surface, (10, 20))
        test_font = pygame.font.SysFont("华文中宋", 20)
        text_surface = test_font.render("跳到有插图的平台上会有特殊音效", True, DARKBLUE)
        SCREEN.blit(text_surface, (20, 70))
        text_surface = test_font.render("“恭喜，是个男孩儿！”", True, GREEN)
        SCREEN.blit(text_surface, (46, 645))
        text_surface = test_font.render("初次跳跃", True, BLACK)
        SCREEN.blit(text_surface, (372, 700))
        text_surface = test_font.render("一回生，二回熟↘", True, BLACK)
        SCREEN.blit(text_surface, (265, 625))
        text_surface = test_font.render("↙轻车熟路", True, BLACK)
        SCREEN.blit(text_surface, (535, 575))
        text_surface = test_font.render("开启你的童年时代！", True, BLACK)
        SCREEN.blit(text_surface, (330, 525))
        text_surface = test_font.render("你开始启蒙兴趣，学习乐器", True, BLACK)
        SCREEN.blit(text_surface, (30, 535))
        text_surface = test_font.render("同玩具作伴，乐在其中", True, BLACK)
        SCREEN.blit(text_surface, (420, 360))
        text_surface = test_font.render("该上学了！", True, BLACK)
        SCREEN.blit(text_surface, (210, 377))
        text_surface = test_font.render("不想上学啊！", True, BLACK)
        SCREEN.blit(text_surface, (55, 335))
        text_surface = test_font.render("厌学", True, BLACK)
        SCREEN.blit(text_surface, (70, 235))
        text_surface = test_font.render("不学无术", True, BLACK)
        SCREEN.blit(text_surface, (45, 150))
        test_font = pygame.font.SysFont("华文中宋", 17)
        text_surface = test_font.render("好好学习！", True, DARKBLUE)
        SCREEN.blit(text_surface, (335, 318))
        text_surface = test_font.render("认真完成作业", True, DARKBLUE)
        SCREEN.blit(text_surface, (410, 270))
        text_surface = test_font.render("读书做题", True, DARKBLUE)
        SCREEN.blit(text_surface, (520, 220))
        text_surface = test_font.render("通过考试", True, DARKBLUE)
        SCREEN.blit(text_surface, (430, 160))

        brick_group.draw(SCREEN)  # 画平台们

        #  实现跳跃，计时器
        if jumping:
            player.rect.y -= player.y_vel
            player.y_vel -= player.gravity  # 向上速度为正
            if player.rect.y == 740:
                jumping = False
                player.y_vel = 0  # 更新下次跳跃的初速度，否则在跳跃会继承之前的负速度
        else:
            player.y_vel = 15

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    jumping = True
                    jumpSOUND.play()
            if event.type == pygame.USEREVENT:
                counter -= 1
                if counter > 0:
                    text = str(counter).rjust(3)
                else:
                    fail_timeout(1)
                    break
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

        SCREEN.blit(font.render("你的童年阶段还剩余：" + text + "秒", True, (0, 0, 0)), (52, 100))  # 显示计时器

        #  实现左右移动
        LEFTMOVE = True
        RIGHTMOVE = True
        if player.rect.x < 2:  # 边界判断
            LEFTMOVE = False
        if player.rect.x > 620:
            RIGHTMOVE = False
        if 170 <= player.rect.x <= 320 and 460 <= player.rect.y <= 500:
            interestMUSIC.play()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and LEFTMOVE:
            player.rect.x -= 130 * dt
            player.idx += 1
            player.idx %= len(player.frames)
            player.image = IMAGES['player'][player.frames[player.idx] + 6]  # 向左走
        if keys[pygame.K_RIGHT] and RIGHTMOVE:
            player.rect.x += 130 * dt
            player.idx += 1
            player.idx %= len(player.frames)
            player.image = IMAGES['player'][player.frames[player.idx]]
        dt = CLOCK.tick(60) / 500
        SCREEN.blit(player.image, player.rect)

        #  碰撞检测
        collision = pygame.sprite.spritecollideany(player, brick_group)
        if collision:  # 如果碰撞了
            jumping = False
            if player.rect.bottom >= collision.rect.top and player.y_vel < 0:  # y方向,从上往下撞
                player.y_vel = 0
                player.rect.bottom = collision.rect.top

            elif player.rect.top <= collision.rect.bottom and player.y_vel > 0:  # y方向,从下往上撞
                player.y_vel = 0
                player.rect.y -= player.y_vel
                player.y_vel -= player.gravity
                player.rect.top = collision.rect.bottom
                jumping = True

            if player.rect.right >= collision.rect.left and player.x_vel > 0:  # x方向,从左往右撞
                player.rect.right = collision.rect.left

            elif player.rect.left <= collision.rect.right and player.x_vel < 0:  # x方向,从右往左撞
                player.rect.left = collision.rect.right

        player.rect.y += 1  # 控制玩家能够在平台上掉落
        collided = pygame.sprite.spritecollideany(player, brick_group)
        if not collided and not jumping and player.rect.y <= 738:
            player.y_vel = 0
            player.rect.y -= player.y_vel
            player.y_vel -= player.gravity
            jumping = True
        player.rect.y -= 1

        #  游戏失败判断
        if player.rect.y > 800:
            fail_serious(1)

        #  游戏通关判断
        if 570 >= player.rect.x >= 535 and 150 >= player.rect.y >= 90:
            return youth_window()

        # print(player.rect.left)
        # print(player.rect.right)
        # print(player.rect.top)
        # print(player.rect.bottom)
        print(player.y_vel)
        # print(player.rect.y)
        pygame.display.flip()
        pygame.display.update()
        CLOCK.tick(FPS)


def youth_window():

    buff1 = 0
    buff2 = 0
    buff3 = 0
    buff4 = 0
    buff5 = 0
    buff6 = 0
    buff7 = 0
    global dt
    counter, text = 45, '45'.rjust(3)
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    font = pygame.font.SysFont('华文中宋', 24)

    youth = Youth(WIDTH * 0.4, 739)
    brick_group = pygame.sprite.Group()  # 建立brick精灵组

    #  搭建游戏障碍平台
    brick_group.add(BrickLL(130, 690))

    brick_group.add(BrickLong(180, 620))
    brick_group.add(BrickLong(290, 620))
    brick_group.add(BrickVert(175, 505))
    brick_group.add(BrickVert(197, 505))

    brick_group.add(Brick(80, 575))
    brick_group.add(Brick(5, 535))
    brick_group.add(Brick(490, 575))
    brick_group.add(Brick(570, 530))
    brick_group.add(Brick(180, 535))

    jumping = False

    while True:
        SCREEN.fill((160, 172, 248))
        SCREEN.blit(IMAGES['floor'], (0, floor_y))  # background

        test_font = pygame.font.SysFont("方正姚体", 40)
        text_surface = test_font.render("关卡二：青年        难度：中等", True, DARKBLUE)
        SCREEN.blit(text_surface, (10, 20))
        test_font = pygame.font.SysFont("华文中宋", 17)
        text_surface = test_font.render("跳到问号箱会叠加不同的buff。人生没有第二条路，同一水平线的buff仅可选一个。", True, DARKBLUE)
        SCREEN.blit(text_surface, (10, 73))
        test_font = pygame.font.SysFont("华文中宋", 20)
        text_surface = test_font.render("人生的转折点：高考。向左向右，请选一边。", True, DARKBLUE)
        SCREEN.blit(text_surface, (120, 660))

        brick_group.draw(SCREEN)  # 画平台们

        SCREEN.blit(IMAGES['buff'], (22, 505))  # 22 < x < 52, 505 < y <535
        SCREEN.blit(IMAGES['buff'], (587, 500))  # 577 < x < 607, 505 < y < 535
        SCREEN.blit(IMAGES['buff'], (195, 505))  # 195 < x < 225, 505 < y < 535
        #  实现跳跃，计时器
        if jumping:
            youth.rect.y -= youth.y_vel
            youth.y_vel -= youth.gravity  # 向上速度为正
            if youth.rect.y == 740:
                jumping = False
                # youth.y_vel = 18  # 更新下次跳跃的初速度，否则在跳跃会继承之前的负速度
        else:
            youth.y_vel = 18

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    jumping = True
                    jumpSOUND.play()
            if event.type == pygame.USEREVENT:
                if buff3:
                    counter -= 10
                elif buff5:
                    counter -= 8
                elif buff7:
                    counter -= 5
                else:
                    counter -= 1
                if counter > 0:
                    text = str(counter).rjust(3)
                elif buff3 or buff5 or buff7:
                    fail_frustrate(2)
                    break
                else:
                    fail_timeout(2)
                    break
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

        SCREEN.blit(font.render("你的青年阶段还剩余：" + text + "秒", True, BLACK), (52, 100))  # 显示计时器

        #  实现左右移动
        LEFTMOVE = True
        RIGHTMOVE = True
        if youth.rect.x < 2:  # 边界判断
            LEFTMOVE = False
        if youth.rect.x > 620:
            RIGHTMOVE = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and LEFTMOVE:
            youth.rect.x -= 150 * dt
            youth.idx += 1
            youth.idx %= len(youth.frames)
            youth.image = IMAGES['youth'][youth.frames[youth.idx] + 6]  # 向左走
        if keys[pygame.K_RIGHT] and RIGHTMOVE:
            youth.rect.x += 150 * dt
            youth.idx += 1
            youth.idx %= len(youth.frames)
            youth.image = IMAGES['youth'][youth.frames[youth.idx]]
        dt = CLOCK.tick(60) / 500
        SCREEN.blit(youth.image, youth.rect)

        if 150 <= youth.rect.x <= 280 and 580 <= youth.rect.y <= 620:
            test_font = pygame.font.SysFont("华文中宋", 18)
            text_surface = test_font.render("很不幸，高考落榜", True, BLACK)
            SCREEN.blit(text_surface, (145, 595))
        if 320 <= youth.rect.x <= 430 and 580 <= youth.rect.y <= 620:
            test_font = pygame.font.SysFont("华文中宋", 18)
            text_surface = test_font.render("恭喜你，考入理想的大学", True, BLACK)
            SCREEN.blit(text_surface, (340, 595))

        #  buff 碰撞判断

        if 22 <= youth.rect.x <= 52 and 475 <= youth.rect.y <= 535:
            buff1 = 1
        if 587 <= youth.rect.x <= 617 and 475 <= youth.rect.y <= 535:
            buff2 = 1
        if 195 <= youth.rect.x <= 225 and 475 <= youth.rect.y <= 535:
            buff3 = 1

        if buff1 == 1:
            test_font = pygame.font.SysFont("华文中宋", 20)
            text_surface = test_font.render("buff1 已装载：实迷途其未远，整理心情，向未知发起挑战！", True, DARKBLUE)
            SCREEN.blit(text_surface, (20, 145))
            brick_group.add(Brick(90, 470))
            text_surface = test_font.render("努力学习，健康作息", True, BLACK)
            SCREEN.blit(text_surface, (50, 445))
            brick_group.add(Brick(180, 420))
            text_surface = test_font.render("学习遇挫，不可避免", True, BLACK)
            SCREEN.blit(text_surface, (140, 395))

            brick_group.add(Brick(270, 370))  # buff4 here
            SCREEN.blit(IMAGES['buff'], (290, 340))
            if 270 <= youth.rect.x <= 300 and 330 <= youth.rect.y <= 370:
                buff4 = 1

            brick_group.add(Brick(80, 370))  # buff5 here
            SCREEN.blit(IMAGES['buff'], (100, 340))
            if 80 <= youth.rect.x <= 110 and 330 <= youth.rect.y <= 370:
                buff5 = 1

        if buff2 == 1:
            test_font = pygame.font.SysFont("华文中宋", 20)
            text_surface = test_font.render("buff2 已装载：百尺竿头，更进一步。", True, DARKBLUE)
            SCREEN.blit(text_surface, (20, 175))
            brick_group.add(Brick(460, 474))
            text_surface = test_font.render("似乎一切都很顺利", True, BLACK)
            SCREEN.blit(text_surface, (440, 450))
            brick_group.add(Brick(550, 415))
            brick_group.add(Brick(460, 350))
            test_font = pygame.font.SysFont("华文中宋", 16)
            text_surface = test_font.render("但人生并不一帆风顺，总会有挫折", True, BLACK)
            SCREEN.blit(text_surface, (380, 325))

            brick_group.add(Brick(550, 290))  # buff6 here
            SCREEN.blit(IMAGES['buff'], (570, 260))
            if 550 <= youth.rect.x <= 580 and 220 <= youth.rect.y <= 260:
                buff6 = 1

            brick_group.add(Brick(370, 290))  # buff7 here
            SCREEN.blit(IMAGES['buff'], (390, 260))
            if 370 <= youth.rect.x <= 400 and 220 <= youth.rect.y <= 260:
                buff7 = 1

        if buff3 == 1:
            test_font = pygame.font.SysFont("华文中宋", 20)
            text_surface = test_font.render("buff3 已装载：失志胆寒，畏葸不前，无心进取，时间飞逝。", True, DARKBLUE)
            SCREEN.blit(text_surface, (20, 205))

        if buff4 == 1:
            test_font = pygame.font.SysFont("华文中宋", 20)
            text_surface = test_font.render("buff4 已装载：战胜挫折，迎接更坚强的自己", True, DARKBLUE)
            SCREEN.blit(text_surface, (20, 185))
            brick_group.add(Brick(360, 320))

            brick_group.add(Brick(440, 270))
            SCREEN.blit(IMAGES['door'], (450, 210))

        if buff5 == 1:
            test_font = pygame.font.SysFont("华文中宋", 20)
            text_surface = test_font.render("buff5 已装载：未能直面挫折，半途而废，意志仍需磨炼", True, DARKBLUE)
            SCREEN.blit(text_surface, (20, 215))

        if buff6 == 1:
            test_font = pygame.font.SysFont("华文中宋", 20)
            text_surface = test_font.render("buff6 已装载：成功应对艰难挑战，你已经变得愈发成熟", True, DARKBLUE)
            SCREEN.blit(text_surface, (20, 205))
            brick_group.add(Brick(455, 220))
            SCREEN.blit(IMAGES['door'],(465, 160))

        if buff7 == 1:
            test_font = pygame.font.SysFont("华文中宋", 20)
            text_surface = test_font.render("buff7 已装载：很遗憾，一帆风顺的人生使你并不能应对压力与挫折", True, DARKBLUE)
            SCREEN.blit(text_surface, (20, 235))
            brick_group.add(Brick(455, 120))
            SCREEN.blit(IMAGES['door'], (465, 60))

            #  碰撞检测
        collision = pygame.sprite.spritecollideany(youth, brick_group)
        if collision:  # 如果碰撞了
            jumping = False
            if youth.rect.bottom > collision.rect.top and youth.y_vel < 0:  # y方向,从上往下撞
                youth.y_vel = 0
                youth.rect.bottom = collision.rect.top

            elif youth.rect.top < collision.rect.bottom and youth.y_vel > 0:  # y方向,从下往上撞
                youth.y_vel = 0
                youth.rect.y -= youth.y_vel
                youth.y_vel -= youth.gravity
                youth.rect.top = collision.rect.bottom
                jumping = True

            if youth.rect.right > collision.rect.left and youth.x_vel > 0:  # x方向,从左往右撞
                youth.rect.right = collision.rect.left

            elif youth.rect.left < collision.rect.right and youth.x_vel < 0:  # x方向,从右往左撞
                youth.rect.left = collision.rect.right

        youth.rect.y += 1  # 控制玩家能够在平台上掉落
        collided = pygame.sprite.spritecollideany(youth, brick_group)
        if not collided and not jumping and youth.rect.y <= 738:
            youth.y_vel = 0
            youth.rect.y -= youth.y_vel
            youth.y_vel -= youth.gravity
            jumping = True
        youth.rect.y -= 1

        #  游戏失败判断
        if youth.rect.y > 800:
            fail_serious(2)

        #  游戏通关判断
        if buff4 == 1 and 210 <= youth.rect.y <= 272 and 450 <= youth.rect.x <= 488:
            return adult_window()
        if buff6 == 1 and 160 <= youth.rect.y <= 222 and 465 <= youth.rect.x <= 503:
            return adult_window()

        pygame.display.flip()
        pygame.display.update()
        CLOCK.tick(FPS)


def adult_window():
    proposal = 0
    marry = 0
    poison = 0
    house = 0
    car = 0
    pregnant = 0
    ham = 0
    sweet = 0
    drink = 0
    global dt
    counter, text = 75, '75'.rjust(3)
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    font = pygame.font.SysFont('华文中宋', 24)

    adult = Adult(WIDTH * 0.4, 739)
    brick_group = pygame.sprite.Group()  # 建立brick精灵组

    #  搭建游戏障碍平台

    brick_group.add(Brick(50, 705))
    brick_group.add(Brick(150, 650))
    # brick_group.add(Brick(50, 595))
    brick_group.add(Brick(150, 540))
    # brick_group.add(Brick(250, 485))
    # brick_group.add(Brick(50, 485))

    jumping = False

    while True:
        SCREEN.fill((160, 172, 248))
        SCREEN.blit(IMAGES['floor'], (0, floor_y))  # background

        test_font = pygame.font.SysFont("方正姚体", 40)
        text_surface = test_font.render("关卡三：中年        难度：困难", True, DARKBLUE)
        SCREEN.blit(text_surface, (10, 20))
        test_font = pygame.font.SysFont("华文中宋", 20)
        text_surface = test_font.render("成人的世界充满未知，请奋力往上跳吧，努力试错！", True, DARKBLUE)
        SCREEN.blit(text_surface, (20, 70))

        brick_group.draw(SCREEN)  # 画平台们

        SCREEN.blit(IMAGES['work'], (250, 585))
        SCREEN.blit(IMAGES['working'], (50, 655))

        if 50 <= adult.rect.x <= 115 and 550 <= adult.rect.y <= 595:  # 求婚
            brick_group.add(Brick(50, 595))
            proposal = 1
        if proposal == 1:
            SCREEN.blit(IMAGES['proposal'], (50, 550))

        if 50 <= adult.rect.x <= 115 and 430 <= adult.rect.y <= 485:  # 结婚
            brick_group.add(Brick(50, 485))
            brick_group.add(Brick(150, 430))
            marry = 1
        if marry == 1:
            SCREEN.blit(IMAGES['marry'], (50, 437))

        if 250 <= adult.rect.x <= 315 and 430 <= adult.rect.y <= 485:  # 吸毒
            brick_group.add(Brick(250, 485))
            poison = 1
        if poison == 1:
            SCREEN.blit((IMAGES['poison']), (250, 430))

        if 250 <= adult.rect.x <= 315 and 320 <= adult.rect.y <= 375:  # 买车
            brick_group.add(Brick(250, 375))
            car = 1
        if car == 1:
            SCREEN.blit(IMAGES['car'], (250, 335))

        if 50 <= adult.rect.x <= 115 and 320 <= adult.rect.y <= 375:  # 买房
            brick_group.add(Brick(50, 375))
            house = 1
        if house == 1:
            SCREEN.blit(IMAGES['house'], (50, 324))

        if house == 1 or car == 1:
            brick_group.add(Brick(150, 320))
            brick_group.add(Brick(50, 265))
            pregnant = 1
        if pregnant == 1:
            SCREEN.blit(IMAGES['pregnant'], (50, 219))
            test_font = pygame.font.SysFont("consolas", 18)
            text_surface = test_font.render("We 're having a baby!!", True, BLACK)
            SCREEN.blit(text_surface, (20, 190))
            brick_group.add(Brick(150, 215))
            brick_group.add(Brick(280, 215))
            test_font = pygame.font.SysFont("华文中宋", 20)
            text_surface = test_font.render("试着向右下方纵身而跃", True, BLACK)
            SCREEN.blit(text_surface, (266, 190))
            brick_group.add(Brick(400, 215))

        brick_group.add(Brick(520, 280))
        if 520 <= adult.rect.x <= 565 and 215 <= adult.rect.y <= 280:  # 不能吃汉堡
            ham = 1
        if ham == 1:
            SCREEN.blit(IMAGES['ham'], (520, 215))
            test_font = pygame.font.SysFont("consolas", 18)
            text_surface = test_font.render("No burger!!", True, BLACK)
            SCREEN.blit(text_surface, (530, 195))
        brick_group.add(Brick(440, 345))
        brick_group.add(Brick(520, 410))

        if 520 <= adult.rect.x <= 565 and 345 <= adult.rect.y <= 410:  # 不能吃甜食
            sweet = 1
        if sweet == 1:
            SCREEN.blit(IMAGES['sweet'], (520, 345))
            test_font = pygame.font.SysFont("consolas", 18)
            text_surface = test_font.render("No sweet!!", True, BLACK)
            SCREEN.blit(text_surface, (530, 325))
        brick_group.add(Brick(440, 475))
        brick_group.add(Brick(520, 540))

        if 520 <= adult.rect.x <= 565 and 475 <= adult.rect.y <= 540:  # 不能喝酒
            drink = 1
        if drink == 1:
            SCREEN.blit(IMAGES['drink'], (520, 475))
            test_font = pygame.font.SysFont("consolas", 18)
            text_surface = test_font.render("No drink!!", True, BLACK)
            SCREEN.blit(text_surface, (530, 455))
            brick_group.add(Brick(520, 670))
            SCREEN.blit(IMAGES['medicine'], (520, 645))
            brick_group.add(Brick(440, 735))
            SCREEN.blit(IMAGES['door'], (455, 673))

            if 440 <= adult.rect.x <= 505 and 673 <= adult.rect.y <= 735:  # 游戏通关判断
                return old_window()
        brick_group.add(Brick(440, 605))

        #  实现跳跃，计时器
        if jumping:
            adult.rect.y -= adult.y_vel
            adult.y_vel -= adult.gravity  # 向上速度为正
            if adult.rect.y == 740:
                jumping = False
                # adult.y_vel = 15  # 更新下次跳跃的初速度，否则在跳跃会继承之前的负速度
        else:
            adult.y_vel = 15

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    jumping = True
                    jumpSOUND.play()
            if event.type == pygame.USEREVENT:
                if not poison:
                    counter -= 1
                else:
                    counter -= 5
                if counter > 0:
                    text = str(counter).rjust(3)
                elif not poison:
                    fail_timeout(3)
                    break
                else:
                    fail_drug(3)
                    break
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

        SCREEN.blit(font.render("你的中年阶段还剩余：" + text + "秒", True, BLACK), (52, 100))  # 显示计时器

        #  实现左右移动
        LEFTMOVE = True
        RIGHTMOVE = True
        if adult.rect.x < 2:  # 边界判断
            LEFTMOVE = False
        if adult.rect.x > 620:
            RIGHTMOVE = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and LEFTMOVE:
            adult.rect.x -= 110 * dt
            adult.idx += 1
            adult.idx %= len(adult.frames)
            adult.image = IMAGES['adult'][adult.frames[adult.idx] + 4]  # 向左走
        if keys[pygame.K_RIGHT] and RIGHTMOVE:
            adult.rect.x += 110 * dt
            adult.idx += 1
            adult.idx %= len(adult.frames)  # 一个动作循环结束
            adult.image = IMAGES['adult'][adult.frames[adult.idx]]
        dt = CLOCK.tick(60) / 500
        SCREEN.blit(adult.image, adult.rect)

        #  碰撞检测
        collision = pygame.sprite.spritecollideany(adult, brick_group)
        if collision:  # 如果碰撞了
            jumping = False
            if adult.rect.bottom > collision.rect.top and adult.y_vel < 0:  # y方向,从上往下撞
                adult.y_vel = 0
                adult.rect.bottom = collision.rect.top

            elif adult.rect.top < collision.rect.bottom and adult.y_vel > 0:  # y方向,从下往上撞
                adult.y_vel = 0
                adult.rect.y -= adult.y_vel
                adult.y_vel -= adult.gravity
                adult.rect.top = collision.rect.bottom
                jumping = True

            if adult.rect.right > collision.rect.left and adult.x_vel > 0:  # x方向,从左往右撞
                adult.rect.right = collision.rect.left

            elif adult.rect.left < collision.rect.right and adult.x_vel < 0:  # x方向,从右往左撞
                adult.rect.left = collision.rect.right

        adult.rect.y += 1  # 控制玩家能够在平台上掉落
        collided = pygame.sprite.spritecollideany(adult, brick_group)
        if not collided and not jumping and adult.rect.y <= 738:
            adult.y_vel = 0
            adult.rect.y -= adult.y_vel
            adult.y_vel -= adult.gravity
            jumping = True
        adult.rect.y -= 1

        #  游戏失败判断
        if adult.rect.y > 800:
            fail_serious(3)

        #  游戏通关判断
        pygame.display.flip()
        pygame.display.update()
        CLOCK.tick(FPS)


def old_window():
    global dt
    counter, text = 60, '60'.rjust(3)
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    font = pygame.font.SysFont('华文中宋', 24)

    old = Old(30, 739)
    brick_group = pygame.sprite.Group()  # 建立brick精灵组

    #  搭建游戏障碍平台

    jumping = False

    while True:
        SCREEN.fill((160, 172, 248))
        SCREEN.blit(IMAGES['floor'], (0, floor_y))  # background
        #  TODO: 填充各种图案

        test_font = pygame.font.SysFont("方正姚体", 40)
        text_surface = test_font.render("关卡四：老年        难度：简单", True, DARKBLUE)
        SCREEN.blit(text_surface, (10, 20))
        test_font = pygame.font.SysFont("华文中宋", 20)
        text_surface = test_font.render("本关不再设置任何难以逾越的障碍，请安享晚年！", True, DARKBLUE)
        SCREEN.blit(text_surface, (20, 70))

        brick_group.draw(SCREEN)  # 画平台们

        brick_group.add(Brick(80, 740))
        brick_group.add(Brick(160, 710))
        SCREEN.blit(IMAGES['right1'], (170, 682))
        brick_group.add(Brick(240, 680))
        SCREEN.blit(IMAGES['right13'], (250, 648))
        brick_group.add(Brick(320, 650))
        SCREEN.blit(IMAGES['right22'], (330, 615))
        brick_group.add(Brick(400, 620))
        SCREEN.blit(IMAGES['right31'], (410, 588))
        brick_group.add(Brick(480, 590))
        SCREEN.blit(IMAGES['door'], (495, 530))

        if 160 <= old.rect.x <= 225 and 652 <= old.rect.y <= 710:  # 童年
            SCREEN.blit(IMAGES['hospital'], (100, 245))
            test_font = pygame.font.SysFont("华文中宋", 20)
            text_surface = test_font.render("“恭喜，是个男孩儿！”", True, GREEN)
            SCREEN.blit(text_surface, (46, 345))
            SCREEN.blit(IMAGES['interest1'], (300, 245))
            SCREEN.blit(IMAGES['interest2'], (350, 245))
            SCREEN.blit(IMAGES['interest3'], (420, 245))
            SCREEN.blit(IMAGES['toy1'], (300, 345))
            SCREEN.blit(IMAGES['toy2'], (390, 345))
            SCREEN.blit(IMAGES['toy3'], (480, 345))
            SCREEN.blit(IMAGES['study'], (100, 445))
            SCREEN.blit(IMAGES['school'], (330, 465))

        if 240 <= old.rect.x <= 305 and 622 <= old.rect.y <= 680:  # 青年
            SCREEN.blit(IMAGES['youthpage'], (50, 120))
            SCREEN.blit(IMAGES['youthpage2'], (200, 350))

        if 320 <= old.rect.x <= 385 and 592 <= old.rect.y <= 650:  # 中年
            SCREEN.blit(IMAGES['work'], (50, 150))
            SCREEN.blit(IMAGES['working'], (250, 150))
            SCREEN.blit(IMAGES['proposal'], (450, 150))
            SCREEN.blit(IMAGES['marry'], (310, 230))
            SCREEN.blit(IMAGES['car'], (250, 320))
            SCREEN.blit(IMAGES['house'], (460, 320))
            SCREEN.blit(IMAGES['pregnant'], (480, 230))

            SCREEN.blit(IMAGES['ham'], (100, 400))
            SCREEN.blit(IMAGES['sweet'], (200, 400))
            SCREEN.blit(IMAGES['drink'], (300, 400))

        if 400 <= old.rect.x <= 465 and 562 <= old.rect.y <= 620:  # 老年
            SCREEN.blit(IMAGES['wheelchair'],(200, 250))
            SCREEN.blit(IMAGES['death'], (150, 450))

        if 480 <= old.rect.x <= 545 and 532 <= old.rect.y <= 590:  # 游戏通关判断
            return end_window()

        #  实现跳跃，计时器
        if jumping:
            old.rect.y -= old.y_vel
            old.y_vel -= old.gravity  # 向上速度为正
            if old.rect.y == 740:
                jumping = False
        else:
            old.y_vel = 14  # 更新下次跳跃的初速度，否则在跳跃会继承之前的负速度

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    jumping = True
                    jumpSOUND.play()
            if event.type == pygame.USEREVENT:
                counter -= 1
                if counter > 0:
                    text = str(counter).rjust(3)
                else:
                    fail_timeout(4)
                    break
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

        SCREEN.blit(font.render("你的老年阶段还剩余：" + text + "秒", True, BLACK), (52, 100))  # 显示计时器

        #  实现左右移动
        LEFTMOVE = True
        RIGHTMOVE = True
        if old.rect.x < 2:  # 边界判断
            LEFTMOVE = False
        if old.rect.x > 620:
            RIGHTMOVE = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and LEFTMOVE:
            old.rect.x -= 60 * dt
            old.idx += 1
            old.idx %= len(old.frames)
            old.image = IMAGES['old'][old.frames[old.idx] + 6]  # 向左走
        if keys[pygame.K_RIGHT] and RIGHTMOVE:
            old.rect.x += 60 * dt
            old.idx += 1
            old.idx %= len(old.frames)
            old.image = IMAGES['old'][old.frames[old.idx]]
        dt = CLOCK.tick(60) / 500
        SCREEN.blit(old.image, old.rect)

        #  碰撞检测
        collision = pygame.sprite.spritecollideany(old, brick_group)
        if collision:  # 如果碰撞了
            jumping = False
            if old.rect.bottom > collision.rect.top and old.y_vel < 0:  # y方向,从上往下撞
                old.y_vel = 0
                old.rect.bottom = collision.rect.top

            elif old.rect.top < collision.rect.bottom and old.y_vel > 0:  # y方向,从下往上撞
                old.y_vel = 0
                old.rect.y -= old.y_vel
                old.y_vel -= old.gravity
                old.rect.top = collision.rect.bottom
                jumping = True

            if old.rect.right > collision.rect.left and old.x_vel > 0:  # x方向,从左往右撞
                old.rect.right = collision.rect.left

            elif old.rect.left < collision.rect.right and old.x_vel < 0:  # x方向,从右往左撞
                old.rect.left = collision.rect.right

        old.rect.y += 1  # 控制玩家能够在平台上掉落
        collided = pygame.sprite.spritecollideany(old, brick_group)
        if not collided and not jumping and old.rect.y <= 738:
            old.y_vel = 0
            old.rect.y -= old.y_vel
            old.y_vel -= old.gravity
            jumping = True
        old.rect.y -= 1

        #  游戏失败判断
        if old.rect.y > 800:
            fail_serious(4)

        pygame.display.flip()
        pygame.display.update()
        CLOCK.tick(FPS)


def end_window():
    pygame.mixer.stop()
    endMUSIC.play()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:  # 按下空格时游戏进入下一界面
                pygame.mixer.stop()
                youthMUSIC.play()
                return child_window()

        SCREEN.fill((160, 172, 248))
        SCREEN.blit(IMAGES['floor'], (0, floor_y))
        SCREEN.blit(IMAGES['gameover'], (220, 50))

        test_font = pygame.font.SysFont("华文中宋", 22)
        text_surface = test_font.render("童年的你，没有遇到太多困难，只是不断跳跃、探索。", True, BLACK)
        SCREEN.blit(text_surface, (55, 120))
        text_surface = test_font.render("即使误入歧途，代价也相对较小，还可以重回正轨。", True, BLACK)
        SCREEN.blit(text_surface, (60, 155))
        text_surface = test_font.render("高考固然重要，但成绩不能决定一切，无论如何你都有出路。", True, BLACK)
        SCREEN.blit(text_surface, (40, 220))
        text_surface = test_font.render("最重要的是，你能否在挫折中挺过来，使自己更加成熟。", True, BLACK)
        SCREEN.blit(text_surface, (55, 255))
        text_surface = test_font.render("沉浸在舒适区，亦或自暴自弃，只会蹉跎宝贵的青春年华。", True, BLACK)
        SCREEN.blit(text_surface, (45, 290))
        text_surface = test_font.render("来到充满未知的成人世界，没有人为你铺好前路，只有试错。", True, BLACK)
        SCREEN.blit(text_surface, (36, 355))
        text_surface = test_font.render("你开始工作、结婚、买房、买车。你只有向上攀登，别无他路。", True, BLACK)
        SCREEN.blit(text_surface, (26, 390))
        text_surface = test_font.render("人到中年，你的身体开始走下坡路。药不离手，老年将至。", True, BLACK)
        SCREEN.blit(text_surface, (50, 425))
        text_surface = test_font.render("步入老年，你的生活变得轻松，游戏也没有任何难度。", True, BLACK)
        SCREEN.blit(text_surface, (55, 490))
        text_surface = test_font.render("你开始回忆自己的这一生，往事一幕幕浮现眼前，感慨万千。", True, BLACK)
        SCREEN.blit(text_surface, (40, 525))
        text_surface = test_font.render("“道阻且长，行而不辍。”这不正是你笃行不怠的一生吗？", True, BLACK)
        SCREEN.blit(text_surface, (45, 560))

        test_font = pygame.font.SysFont("bodoniblack", 30)
        text_surface = test_font.render("Press SPACE: Play Again", True, BLACK)
        SCREEN.blit(text_surface, (130, 620))
        text_surface = test_font.render("Press ESC: Exit", True, BLACK)
        SCREEN.blit(text_surface, (205, 670))


        pygame.display.update()
        CLOCK.tick(FPS)


def fail_serious(index):  # 游戏失败，按空格键重新开始
    while True:
        SCREEN.fill((160, 172, 248))
        SCREEN.blit(IMAGES['floor'], (0, floor_y))  # background
        test_font = pygame.font.SysFont("华文中宋", 40)
        text_surface = test_font.render("你堕入了无底深渊，回天乏术。", True, (170, 10, 25))
        SCREEN.blit(text_surface, (50, 150))
        test_font = pygame.font.SysFont("华文中宋", 26)
        text_surface = test_font.render("谨记：游戏可以重来，人生只有一次！请珍爱生命。", True, (70, 0, 0))
        SCREEN.blit(text_surface, (35, 250))
        test_font = pygame.font.SysFont("bodoniblack", 40)
        text_surface = test_font.render("Press SPACE to try again.", True, BLACK)
        SCREEN.blit(text_surface, (45, 350))
        pygame.display.update()
        CLOCK.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if index == 1:
                        return child_window()
                    elif index == 2:
                        return youth_window()
                    elif index == 3:
                        return adult_window()
                    elif index == 4:
                        return old_window()


def fail_timeout(index):  # 游戏失败，按空格键重新开始
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if index == 1:
                        return child_window()
                    elif index == 2:
                        return youth_window()
                    elif index == 3:
                        return adult_window()
                    elif index == 4:
                        return old_window()
        SCREEN.fill((160, 172, 248))
        SCREEN.blit(IMAGES['floor'], (0, floor_y))  # background
        test_font = pygame.font.SysFont("华文中宋", 30)
        text_surface = test_font.render("你在此阶段的生命已耗尽，无法继续前行。", True, (170, 10, 25))
        SCREEN.blit(text_surface, (35, 150))
        test_font = pygame.font.SysFont("华文中宋", 26)
        text_surface = test_font.render("谨记：盛年不重来，一日难再晨。", True, (70, 0, 0))
        SCREEN.blit(text_surface, (85, 280))
        text_surface = test_font.render("及时当勉励，岁月不待人。", True, (70, 0, 0))
        SCREEN.blit(text_surface, (160, 330))
        test_font = pygame.font.SysFont("bodoniblack", 40)
        text_surface = test_font.render("Press SPACE to try again.", True, BLACK)
        SCREEN.blit(text_surface, (45, 480))
        pygame.display.update()
        CLOCK.tick(FPS)


def fail_drug(index):  # 游戏失败，按空格键重新开始
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                if event.key == pygame.K_SPACE:
                    if index == 1:
                        return child_window()
                    elif index == 2:
                        return youth_window()
                    elif index == 3:
                        return adult_window()
                    elif index == 4:
                        return old_window()
        SCREEN.fill((160, 172, 248))
        SCREEN.blit(IMAGES['floor'], (0, floor_y))  # background
        test_font = pygame.font.SysFont("华文中宋", 35)
        text_surface = test_font.render("你沾染上了毒品，生命逐渐凋零。", True, (170, 10, 25))
        SCREEN.blit(text_surface, (35, 150))
        test_font = pygame.font.SysFont("华文中宋", 28)
        text_surface = test_font.render("谨记：珍爱生命，远离毒品！", True, (70, 0, 0))
        SCREEN.blit(text_surface, (85, 300))
        text_surface = test_font.render("拒绝黄赌毒，人人有责。", True, (70, 0, 0))
        SCREEN.blit(text_surface, (150, 350))
        test_font = pygame.font.SysFont("bodoniblack", 40)
        text_surface = test_font.render("Press SPACE to try again.", True, BLACK)
        SCREEN.blit(text_surface, (45, 480))
        pygame.display.update()
        CLOCK.tick(FPS)


def fail_frustrate(index):  # 游戏失败，按空格键重新开始
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                if event.key == pygame.K_SPACE:
                    if index == 1:
                        return child_window()
                    elif index == 2:
                        return youth_window()
                    elif index == 3:
                        return adult_window()
                    elif index == 4:
                        return old_window()
        SCREEN.fill((160, 172, 248))
        SCREEN.blit(IMAGES['floor'], (0, floor_y))  # background
        test_font = pygame.font.SysFont("华文中宋", 35)
        text_surface = test_font.render("你一直沉浸在过去的挫折中，无法自拔。", True, (170, 10, 25))
        SCREEN.blit(text_surface, (15, 150))
        test_font = pygame.font.SysFont("华文中宋", 28)
        text_surface = test_font.render("谨记：抱怨身处黑暗，不如提灯前行。", True, (70, 0, 0))
        SCREEN.blit(text_surface, (85, 300))
        text_surface = test_font.render("心态决定高度，细节决定成败。", True, (70, 0, 0))
        SCREEN.blit(text_surface, (150, 350))
        test_font = pygame.font.SysFont("bodoniblack", 40)
        text_surface = test_font.render("Press SPACE to try again.", True, BLACK)
        SCREEN.blit(text_surface, (45, 480))
        pygame.display.update()
        CLOCK.tick(FPS)

main()
