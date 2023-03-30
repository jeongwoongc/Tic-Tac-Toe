import pygame
from pygame.locals import *
import random
import numpy as np

class randnum(object):
    def __init__(self):
        self.playerList = []
        self.num = random.randint(0,1)
    
    def assign(self):
        if self.num == 1:
            self.playerList = [1, 0]
        else:
            self.playerList = [0, 1]

        return self.playerList
class players(object):
    def __init__(self):
        shapes = randnum()
        self.player1, self.player2 = shapes.assign()
        self.gameArray = np.zeros((3,3))
        self.color1 = None
        self.color2 = None
        self.turns = 0
        self.profile = {}
    def assign(self):
        self.player1 = 1
        self.player2 = 2
        self.color1 = (0,80,255)
        self.color2 = (255,80,0)
        
        self.profile = {
            "p1_color" : self.color1,
            "p1_number" : self.player1,
            "p2_color" : self.color2,
            "p2_number" : self.player2
        }

        return self.profile
    
    def turn(self):
        count = 0
        if self.turns == 0:
            self.turns = self.player1
            count += 1
        elif (self.turns == self.player1 and count <= 9):
            self.turns = self.player2
            count += 1
        elif (self.turns == self.player2 and count <= 9):
            self.turns = self.player1
            count += 1
        
        return self.turns    
class rectCollide(object):
    def __init__(self):
        qWidth = width // rows
        qh = 0
        self.rect_coords = []
        
        q_i = qWidth
        for l in range(rows):
            qw = 0
            if l == 0:
                qh = 0
            else:
                qh += q_i
            for n in range(rows):
                self.rect_coords.append(pygame.draw.rect(win, (0,0,0), (qw, qh, qWidth, qWidth)))
                qw += qWidth

def drawBoard(w, rows, surface):
    sizeBtwn = w // rows

    x = 0
    y = 0
    for l in range(rows):
        x = x + sizeBtwn
        y = y + sizeBtwn

        pygame.draw.line(surface, (255,255,255), (x+5,0),(x+5,w),width=2)
        pygame.draw.line(surface, (255,255,255), (0,y+5),(w,y+5),width=2)
def centerCoord(w, rows):
    qWidth = w // rows
    qh = 0
    quadrants = []
    
    for l in range(rows):
        qw = 0
        q_i = (qWidth+5)//2
        if l == 0:
            qh += q_i
        else:
            qh += q_i*2
        for n in range(rows):
            if n == 0:
                qw += q_i
            else:
                qw += q_i*2  
            quadrants.append((qw,qh))
    
    return quadrants
def draw(w, rows, gameboard, profile, q, turn):
    qWidth = w // rows
    rad = qWidth // 3
    xlen = 80
    coords = centerCoord(w, rows)
    p = 0
    quad = {}
    
    for i,n in enumerate(coords):
        quad[i+1] = n

    if q == 1:
        if gameboard[0,0] != 0:
            print(f"Already placed on q{q} please pick an empty q!") 
        elif turn == 1:
            gameboard[0,0] = turn
            pygame.draw.line(win, profile["p1_color"],(quad[1][0] - xlen,quad[1][1] - xlen), (quad[1][0] + xlen,quad[1][1] + xlen), rad//2)
            pygame.draw.line(win, profile["p1_color"],(quad[1][0] - xlen,quad[1][1] + xlen), (quad[1][1] + xlen,quad[1][0] - xlen), rad//2)
        else:
            gameboard[0,0] = turn
            pygame.draw.circle(win, profile["p2_color"],quad[1], rad)
    elif q == 2:
        if gameboard[0,1] != 0:
            print(f"Already placed on q{q} please pick an empty q!") 
        elif turn == 1:
            gameboard[0,1] = turn
            pygame.draw.line(win, profile["p1_color"],(quad[2][0] - xlen,quad[2][1] - xlen), (quad[2][0] + xlen,quad[2][1] + xlen), rad//2)
            pygame.draw.line(win, profile["p1_color"],(quad[2][0] - xlen,quad[2][1] + xlen), (quad[2][0] + xlen,quad[2][1] - xlen), rad//2)
        else:
            gameboard[0,1] = turn
            pygame.draw.circle(win, profile["p2_color"],quad[2], rad)
    elif q == 3:
        if gameboard[0,2] != 0:
            print(f"Already placed on q{q} please pick an empty q!") 
        elif turn == 1:
            gameboard[0,2] = turn
            pygame.draw.line(win, profile["p1_color"],(quad[3][0] - xlen,quad[3][1] - xlen), (quad[3][0] + xlen,quad[3][1] + xlen), rad//2)
            pygame.draw.line(win, profile["p1_color"],(quad[3][0] - xlen,quad[3][1] + xlen), (quad[3][0] + xlen,quad[3][1] - xlen), rad//2)
        else:
            gameboard[0,2] = turn
            pygame.draw.circle(win, profile["p2_color"],quad[3], rad)
    elif q == 4:
        if gameboard[1,0] != 0:
            print(f"Already placed on q{q} please pick an empty q!") 
        elif turn == 1:
            gameboard[1,0] = turn
            pygame.draw.line(win, profile["p1_color"],(quad[4][0] - xlen,quad[4][1] - xlen), (quad[4][0] + xlen,quad[4][1] + xlen), rad//2)
            pygame.draw.line(win, profile["p1_color"],(quad[4][0] - xlen,quad[4][1] + xlen), (quad[4][0] + xlen,quad[4][1] - xlen), rad//2)
        else:
            gameboard[1,0] = turn
            pygame.draw.circle(win, profile["p2_color"],quad[4], rad)
    elif q == 5:
        if gameboard[1,1] != 0:
            print(f"Already placed on q{q} please pick an empty q!") 
        elif turn == 1:
            gameboard[1,1] = turn
            pygame.draw.line(win, profile["p1_color"],(quad[5][0] - xlen,quad[5][1] - xlen), (quad[5][0] + xlen,quad[5][1] + xlen), rad//2)
            pygame.draw.line(win, profile["p1_color"],(quad[5][0] - xlen,quad[5][1] + xlen), (quad[5][0] + xlen,quad[5][1] - xlen), rad//2)
        else:
            gameboard[1,1] = turn
            pygame.draw.circle(win, profile["p2_color"],quad[5], rad)
    elif q == 6:
        if gameboard[1,2] != 0:
            print(f"Already placed on q{q} please pick an empty q!") 
        elif turn == 1:
            gameboard[1,2] = turn
            pygame.draw.line(win, profile["p1_color"],(quad[6][0] - xlen,quad[6][1] - xlen), (quad[6][0] + xlen,quad[6][1] + xlen), rad//2)
            pygame.draw.line(win, profile["p1_color"],(quad[6][0] - xlen,quad[6][1] + xlen), (quad[6][0] + xlen,quad[6][1] - xlen), rad//2)
        else:
            gameboard[1,2] = turn
            pygame.draw.circle(win, profile["p2_color"],quad[6], rad)
    elif q == 7:
        if gameboard[2,0] != 0:
            print(f"Already placed on q{q} please pick an empty q!") 
        elif turn == 1:
            gameboard[2,0] = turn
            pygame.draw.line(win, profile["p1_color"],(quad[7][0] - xlen,quad[7][1] - xlen), (quad[7][0] + xlen,quad[7][1] + xlen), rad//2)
            pygame.draw.line(win, profile["p1_color"],(quad[7][0] - xlen,quad[7][1] + xlen), (quad[7][0] + xlen,quad[7][1] - xlen), rad//2)
        else:
            gameboard[2,0] = turn
            pygame.draw.circle(win, profile["p2_color"],quad[7], rad)
    elif q == 8:
        if gameboard[2,1] != 0:
            print(f"Already placed on q{q} please pick an empty q!") 
        elif turn == 1:
            gameboard[2,1] = turn
            pygame.draw.line(win, profile["p1_color"],(quad[8][0] - xlen,quad[8][1] - xlen), (quad[8][0] + xlen,quad[8][1] + xlen), rad//2)
            pygame.draw.line(win, profile["p1_color"],(quad[8][0] - xlen,quad[8][1] + xlen), (quad[8][0] + xlen,quad[8][1] - xlen), rad//2)
        else:
            gameboard[2,1] = turn
            pygame.draw.circle(win, profile["p2_color"],quad[8], rad)
    elif q == 9:
        if gameboard[2,2] != 0:
            print(f"Already placed on q{q} please pick an empty q!") 
        elif turn == 1:
            gameboard[2,2] = turn
            pygame.draw.line(win, profile["p1_color"],(quad[9][0] - xlen,quad[9][1] - xlen), (quad[9][0] + xlen,quad[9][1] + xlen), rad//2)
            pygame.draw.line(win, profile["p1_color"],(quad[9][0] - xlen,quad[9][1] + xlen), (quad[9][0] + xlen,quad[9][1] - xlen), rad//2)
        else:
            gameboard[2,2] = turn
            pygame.draw.circle(win, profile["p2_color"],quad[9], rad)
    return quad
def displayWin(wplayer):
    if wplayer == 1:
        font = pygame.font.SysFont(None, 100)
        img = font.render('Player X Wins!', True, (57,255,0))
        win.blit(img, (70, 300))
    else:
        font = pygame.font.SysFont(None, 100)
        img = font.render('Player O Wins!', True, (57,255,0))
        win.blit(img, (70, 300))
def judge(gameboard, rst):
    # for m in gameboard: # This one's for 3 in a row, need a more efficient way to implement columns and diagonals also a case where nobody wins shows "draw" and reset button
    m, n = gameboard.shape
    g = gameboard
    wplayer = 2
    end = 0

    # Check rows
    for i in range(n):
        if (gameboard[i] == 1).all():
            print("Player X wins")
            end = 1
            wplayer = 1
            displayWin(wplayer)
        elif (gameboard[i] == 2).all():
            print("Player O wins")
            end = 1
            displayWin(wplayer)
    
    # Check columns (need to improve)
    if (gameboard[0,0] == 1 and gameboard[1,0] == 1 and gameboard[2,0] == 1):
        print("Player X wins")
        wplayer = 1
        end = 1
        displayWin(wplayer)
    elif (gameboard[0,1] == 1 and gameboard[1,1] == 1 and gameboard[2,1] == 1):
        print("Player X wins")
        wplayer = 1
        end = 1
        displayWin(wplayer)
    elif (gameboard[0,2] == 1 and gameboard[1,2] == 1 and gameboard[2,2] == 1):
        print("Player X wins")
        wplayer = 1
        end = 1
        displayWin(wplayer)
    elif (gameboard[0,0] == 2 and gameboard[1,0] == 2 and gameboard[2,0] == 2):
        print("Player O wins")
        end = 1
        displayWin(wplayer)
    elif (gameboard[0,1] == 2 and gameboard[1,1] == 2 and gameboard[2,1] == 2):
        print("Player O wins")
        end = 1
        displayWin(wplayer)
    elif (gameboard[0,2] == 2 and gameboard[1,2] == 2 and gameboard[2,2] == 2):
        print("Player O wins")
        end = 1
        displayWin(wplayer)

    # Check diagonals (need to improve)
    elif (gameboard[0,0] == 1 and gameboard[1,1] == 1 and gameboard[2,2] == 1):
        print("Player X wins")
        wplayer = 1
        end = 1
        displayWin(wplayer) 
    elif (gameboard[0,2] == 1 and gameboard[1,1] == 1 and gameboard[2,0] == 1):
        print("Player X wins")
        end = 1
        wplayer = 1
        displayWin(wplayer)
    elif (gameboard[0,0] == 2 and gameboard[1,1] == 2 and gameboard[2,2] == 2):
        print("Player O wins")
        end = 1
        displayWin(wplayer)
    elif (gameboard[0,2] == 2 and gameboard[1,1] == 2 and gameboard[2,0] == 2):
        print("Player O wins")
        end = 1
        displayWin(wplayer)
    elif (gameboard[:,:] > 0).all():
        print("Draw, please reset the game by clicking again on the screen")
        font = pygame.font.SysFont(None, 100)
        img = font.render('Draw, reset!', True, (57,255,0))
        win.blit(img, (190, 300))
        end = 1

    return end
def main():
    global width, rows, win
    pygame.init()
    end = 0
    width = 800
    rows = 3
    fps=30
    clock = pygame.time.Clock()
    win = pygame.display.set_mode((width,width))
    rectcollide = rectCollide()
    t = players()
    gameboard = t.gameArray
    profile = t.assign()
    pygame.display.set_caption('Tic Tac Toe')
    drawBoard(width,rows,win)
    game_over = False
    rst = False

    while not game_over:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over=True
            elif event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if end == 1:
                    game_over = True
                    main()
                for q, rect_c in enumerate(rectcollide.rect_coords):
                    rect = rect_c
                    if rect.collidepoint(pos) and end != 1 :
                        turn = t.turn()
                        draw(width, rows, gameboard, profile, q+1, turn)
                        end = judge(gameboard, rst)
        pygame.display.update()
    pygame.display.quit()
    pygame.quit()
    quit()

main()

