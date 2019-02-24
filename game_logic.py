from spaceship import *
from aliens import *
from settings import *
s = spaceship()
missiles = []
alist = []
flag = 0
score = 0


def run():
    while True:
        global flag
        global score
        x_change = 0
        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    x_change = -25
                if event.key == pygame.K_d:
                    x_change = 25
                if event.key == pygame.K_s:
                    mis = missile2(s.x, s.y - 25, time() / 1000)
                    missiles.append(mis)
                if event.key == pygame.K_SPACE:
                    mis = missile1(s.x, s.y - 25, time() / 1000)
                    missiles.append(mis)
                if event.key == pygame.K_q:
                    pygame.quit()
                    print("Your final score is " + str(score))
                    quit()
        s.x += x_change
        if s.x < 25:
            s.x = 25
        elif s.x > (dis_width - 25):
            s.x = dis_width - 25

        gameDisplay.fill(black)

        seconds = int(time() / 1000)
        for m in missiles:
            for al in alist:
                if m.ty == 1:
                    if abs(
                            m.x -
                            al.x) <= 25 and abs(
                            m.y -
                            al.y) <= 25 and m.destroy == False and al.destroy == False:
                        al.first()
                        m.destroy = True
                        score += 1
                        print(score)
                if m.ty == 2:
                    if abs(
                            m.x -
                            al.x) <= 25 and abs(
                            m.y -
                            al.y) <= 25 and m.destroy == False and al.destroy == False and al.hit == False:
                        al.second(seconds)
                        m.destroy = True
                        score += 1
                        print(score)

        s.draw()
        for m in missiles:
            if not m.destroy:
                m.draw()
        if seconds % freq == 0 and flag == 0:
            new = alien(seconds)
            alist.append(new)
            flag = 1
        elif seconds % freq != 0:
            flag = 0

        for x in alist:
            if not x.hit:
                x.timer = 8 - (seconds - x.start)
            elif x.hit:
                x.timer = 5 - (seconds - x.hit_time)
            if x.timer == 0:
                x.destroy = True
        for x in alist:
            if x.destroy is False:
                x.draw()
        pygame.display.update()
        clock.tick(60)
