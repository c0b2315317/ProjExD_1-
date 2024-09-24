import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    kk_img = pg.image.load("fig/3.png")  #練習２
    kk_img = pg.transform.flip(kk_img,True,False) #練習２
    kk_rct = kk_img.get_rect() #練習８
    kk_rct.center = 300, 200
    re_bg_img = pg.transform.flip(bg_img,True,False)
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        key_lst = pg.key.get_pressed() #練習８－３
        kk_move = [-1, 0]
        if key_lst[pg.K_UP]:
            kk_move[1] -= 1
        if key_lst[pg.K_DOWN]:
            kk_move[1] += 1
        if key_lst[pg.K_LEFT]:
            kk_move[0] -= 1
        if key_lst[pg.K_RIGHT]:
            kk_move[0] += 2
        kk_rct.move_ip(kk_move)
        x = -(tmr%3200)
        screen.blit(bg_img, [x, 0])
        screen.blit(re_bg_img, [x+1600, 0])
        screen.blit(bg_img, [x+3200, 0])
        screen.blit(re_bg_img, [x+4800, 0])
        screen.blit(kk_img, kk_rct) #練習４,8-5
        pg.display.update()
        tmr += 1        
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()