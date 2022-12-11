import pygame, sys
from pygame.locals import *
import random, time

# 게임화면 설정
FPS = 120 # 프레임
SCREENWIDTH = 1200 # 창 너비
SCREENHEIGHT = 800 # 창 높이

#색 설정
WHITE = (255,255,255)
YELLOW = (255,255,0)
CYAN = (0,238,238)
BLACK = (0, 0, 0)
GRAY = (128,128,128)
RED = (255, 0, 0)

def main():
    pygame.init()

    global FPSCLOCK, SCREEN, FONT
    
    FPSCLOCK = pygame.time.Clock()
    SCREEN = pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))
    FONT = pygame.font.SysFont('Verdana', 20) # 순서대로 글자 종류, 크기

    # 게임이 끝난후 표기될 문구
    global game_over, clear1, clear2, thanks, creator

    game_over = pygame.font.SysFont('Verdana', 60).render("GAME OVER", True, BLACK)
    clear1 = pygame.font.SysFont('Verdana', 60).render("ALL CLEAR!!", True, RED)
    clear2 = pygame.font.SysFont('Verdana', 40).render("Exellent!!!", True, RED)
    thanks = FONT.render("Thanks for Playing! :)", True, BLACK)
    creator = FONT.render("21101190 Seo Bo Seong", True, BLACK)

    pygame.display.set_caption('Growing Fish Game') # 창 이름 설정
    
    background = pygame.image.load('deepSea.jpg') # 화면 이미지 넣기
    SCREEN.blit(background, (0, 0)) #왼쪽 위 꼭지점좌표 기준 
    pygame.display.flip()

    gameStart() #시작화면 띄우기
    SCREEN.fill((0, 0, 0))

    #시작 화면의 텍스트를 없애고 게임 시작
    background = pygame.image.load('deepSea.jpg')
    SCREEN.blit(background, (0, 0))

    pygame.display.update()

    #게임 진행
    GrowingFishGame()


def terminateGame(): # 종료 함수
    pygame.quit()
    sys.exit()

def gameStart(): #시작 화면을 보여주면서 시작 (완료)
    #시작 화면에 띄워질 문구
    titleText = pygame.font.SysFont('Verdana', 80).render('Growing Fish Game', True, YELLOW, CYAN)
    toStart = pygame.font.SysFont('Verdana', 20).render('Press Any Key to Start', True, WHITE)
    exitGame = pygame.font.SysFont('Verdana', 20).render('Press Esc Key to Exit', True, GRAY)
    
    SCREEN.blit(titleText, (220, 200))
    SCREEN.blit(toStart, (470, 600))
    SCREEN.blit(exitGame, (0,0))
    while True:
        if KeyPress(): #Esc 키를 제외한 아무 키를 눌러 게임 시작
            pygame.event.get()
            return
        pygame.display.update()

def KeyPress(): # 게임 시작을 위한 함수
    if len(pygame.event.get(QUIT)) > 0:
        terminateGame()

    isPressed=pygame.event.get(KEYUP)
    if len(isPressed) == 0:
        return None
    if isPressed[0].key == K_ESCAPE:
        terminateGame()
    return isPressed[0].key
    

class Fish(pygame.sprite.Sprite): #플레이어와 적 클래스가 상속받을 물고기 클래스
    def __init__(self, img, level, score):
        super().__init__()
        # 이미지 불러오기
        self.img = pygame.image.load(img)
        # 이미지 모양의 직사각형 모양 불러오기
        self.rect = self.img.get_rect()
        self.rect.width *= 0.4
        self.rect.height *= 0.4
        self.level = level
        self.score = score # 점수, 플레이어는 점수를 얻고 적은 먹혔을 때 점수를 줌
        self.invincible = True

class Player(Fish): # 플레이어 클래스
    def __init__(self):
        self.levelImages = ["Level1playerFish.png", "Level2playerFish.png", "Level3playerFish.png", "Level4playerFish.png", "Level5playerFish.png",]
        super().__init__(self.levelImages[0], 1, 0)
        self.lives = 3
        self.items=[1, 1] # 생명 증가/무적(5초) 아이템
        self.target_scores = [1000, 3000, 5000, 7000, 10000, 0] #최대 5단계까지
        self.rect.center = (SCREENWIDTH/2, SCREENHEIGHT/2)
        self.invincible = True

    def move(self):
        pressedKeys = pygame.key.get_pressed()
        speed = 5
        # 방향키에 따라서 speed 만큼 이동
        if self.rect.left > 0:
            if pressedKeys[K_LEFT]:
                self.rect.move_ip(speed*(-1),0)
                position_player = self.rect.center
                return position_player
        
        if self.rect.right < SCREENWIDTH:
            if pressedKeys[K_RIGHT]:
                self.rect.move_ip(speed, 0)
                position_player = self.rect.center
                return position_player
        
        if self.rect.top > 0:
            if pressedKeys[K_UP]:
                self.rect.move_ip(0,speed*(-1))
                position_player = self.rect.center
                return position_player
        
        if self.rect.bottom < SCREENHEIGHT:
            if pressedKeys[K_DOWN]:
                self.rect.move_ip(0,speed)
                position_player = self.rect.center
                return position_player
        
    #무적 아이템 사용
    def InvincibleItem(self):
        if pygame.key.get_pressed()[K_1]:
            if self.items[0] > 0:
                return True
        return False

    # 생명추가 아이템 사용
    def LivesUPItem(self):
        if pygame.key.get_pressed()[K_2]:
            if self.items[1] > 0:
                return True
        return False

    def LevelUP(self): #레벨업
        if self.score >= self.target_scores[self.level-1]: # 목표 점수 돌파하면 레벨업
            self.level += 1 # 레벨 증가
            if self.level <=5:
                self.img = pygame.image.load(self.levelImages[self.level-1])
            # 이미지 모양의 직사각형 모양 불러오기
            self.rect = self.img.get_rect()
            self.rect.width *= 0.4
            self.rect.height *= 0.4
            #아이템 하나씩 추가로 증정
            self.items[0]+=1
            self.items[1]+=1

        
class Enemy(Fish):
    def __init__(self, level):
        enemyImg="Level1Fish.png"
        #레벨에 따라서 이미지가 설정됨(정확히는 크기가 커짐)
        if level == 1:
            enemyImg = "Level1Fish.png"
        elif level == 2:
            enemyImg = "Level2Fish.png"
        elif level == 3:
            enemyImg = "Level3Fish.png"
        elif level == 4:
            enemyImg = "Level4Fish.png"
        elif level == 5:
            enemyImg = "Level5Fish.png"
        super().__init__(enemyImg, level, level*100)
        # 랜덤 위치에서 적 생성
        self.rect.center = (random.randint(400,SCREENWIDTH-400), random.randint(40,SCREENHEIGHT-40))

    def move(self):
        speed = 3
        direction = random.randint(0,100)
        
        #위치 이동은 랜덤으로, 확률은 균일
        if self.rect.top > 0:
            if direction in range(0, 25): # 위쪽으로 이동
                self.rect.move_ip(0, speed*(-1))
                position_enemy = self.rect.center
                return position_enemy
        if self.rect.bottom < SCREENHEIGHT:
            if direction in range(25, 50): # 아래쪽으로 이동
                self.rect.move_ip(0, speed)
                position_enemy = self.rect.center
                return position_enemy

        if self.rect.left > 0:
            if direction in range(50, 75): # 왼쪽으로 이동
                self.rect.move_ip(speed*(-1), 0)
                position_enemy = self.rect.center
                return position_enemy
        
        if self.rect.right < SCREENWIDTH:
            if direction in range(75, 100): # 오른쪽으로 이동
                self.rect.move_ip(speed, 0)
                position_enemy = self.rect.center
                return position_enemy
        return self.rect.center

# 게임 진행
def GrowingFishGame():

    # 배경화면 설정
    background = pygame.image.load('deepSea.jpg')

    #객체 생성
    player = Player()
    enemy = Enemy(random.randint(1,player.level+3)) # 플레이어 레벨보다 2보다 큰 물고기까지만 생성

    #적 객체 그룹화
    Enemies = pygame.sprite.Group()
    Enemies.add(enemy)

    #전체 그룹
    All_groups = pygame.sprite.Group()
    All_groups.add(player)
    All_groups.add(enemy)

    #1초마다 적 1개씩 생성
    start = pygame.time.get_ticks()

    invincibleStart = pygame.time.get_ticks() # 플레이어의 무적시간, 처음에는 무적
    invincibleTime = pygame.time.get_ticks()

    #게임 루프
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminateGame()
            #if event.type == SPAWNENEMY:
                #pass
        now = pygame.time.get_ticks() #플레이 시간

        SCREEN.blit(background, (0,0))
        
        invincibleTime = pygame.time.get_ticks() # 무적시간
        if player.invincible: #플레이어가 무적일때
            if invincibleTime - invincibleStart > 5000:
                player.invincible = False
            
        
        if player.InvincibleItem(): # 무적 아이템 사용
            if player.items[0] > 0:
                player.items[0] -= 1
                player.invincible = True
                invincibleStart = pygame.time.get_ticks()

        if player.LivesUPItem(): # 생명 아이템 사용
            if player.items[1] > 0:
                player.items[1] -= 1
                player.lives += 1


        #레벨, 점수, 목표점수와 목숨 표시
        level = FONT.render("LEVEL" + str(player.level), True, YELLOW)
        lives = FONT.render("LIVES : " + str(player.lives), True, BLACK)
        scores = FONT.render("SCORE : " + str(player.score), True, BLACK)
        target = FONT.render("Target Score to Next Level : " + str(player.target_scores[player.level-1]), True, BLACK)
        invincibleCount = FONT.render("Invincible : " + str(player.items[0]), True, WHITE)
        # 무적 시간 표시
        if invincibleTime - invincibleStart > 5000: # 무적 아니면
            invincibleLimit = FONT.render("Invincible time : 0 ",True, YELLOW)
        else:
            invincibleLimit = FONT.render("Invincible time : " + str(5-(int((invincibleTime - invincibleStart)/1000))),True, YELLOW)
        livesUPCount = FONT.render("1UP : " + str(player.items[1]), True, WHITE)

        SCREEN.blit(level, (100, 0))
        SCREEN.blit(lives, (300, 0))
        SCREEN.blit(scores, (500, 0))
        SCREEN.blit(target, (700, 0))
        SCREEN.blit(invincibleCount, (200, SCREENHEIGHT-100))
        SCREEN.blit(invincibleLimit, (400, SCREENHEIGHT-100))
        SCREEN.blit(livesUPCount, (1000, SCREENHEIGHT-100))


        count2 = 0 #플레이어보다 레벨이 2 높은 물고기수
        count1 = 0 #플레이어보다 레벨이 1 높은 물고기수
        # 1초마다 적 생성(위치는 랜덤)
        if len(All_groups) < 20:
            if(now-start > 1000):
                start = now
                for k in All_groups: # 플레이어보다 레벨 높은 물고기수 제한
                    if k.level == player.level+2:
                        count2+=1
                    elif k.level == player.level+1:
                        count1+=1
                if count2 < 3 and count1 < 5:
                    newEnemy = Enemy(random.randint(1,player.level+2))
                elif count1 < 5:
                    newEnemy = Enemy(random.randint(1,player.level+1))
                else:
                    if player.level == 1:
                        newEnemy = Enemy(1)
                    newEnemy = Enemy(random.randint(1,player.level)) #플레이어 레벨까지의 물고기
                Enemies.add(newEnemy)
                All_groups.add(newEnemy)

        for i in All_groups:
            SCREEN.blit(i.img, i.rect)
            i.move()
        
        #물고기가 충돌할경우 (완료)
        for i in Enemies:
            if pygame.sprite.collide_rect(player, i): #플레이어와 적의 충돌
                if player.level >= i.level: 
                    Enemies.remove(i)
                    All_groups.remove(i)
                    player.score += i.score
                else:
                    if not player.invincible:
                        player.lives -= 1
                        player.invincible = True # 플레이어는 다시 생성되면 무적상태
                        invincibleStart = pygame.time.get_ticks()
                        player.rect.center = (SCREENWIDTH/2, SCREENHEIGHT/2)
            for j in Enemies: # 적과 적의 충돌
                if i != j: # 서로 다른 물고기간에 충돌
                    if pygame.sprite.collide_rect(i, j): #레벨 낮은쪽이 먹힘
                        if i.level > j.level:
                            Enemies.remove(j)
                            All_groups.remove(j)
                        elif i.level < j.level:
                            Enemies.remove(i)
                            All_groups.remove(i)
        
        # 레벨업
        player.LevelUP()

        # 게임 오버
        if player.lives <= 0:
            for i in All_groups:
                i.kill()
            SCREEN.fill(WHITE)
            SCREEN.blit(game_over, (390, 200))
            SCREEN.blit(thanks, (470, 600))
            SCREEN.blit(creator, (450, 700))
            time.sleep(1) #1초 정지후
            pygame.display.update()
            time.sleep(3)
            terminateGame()

        # 게임 5단계까지 클리어
        if player.score >= player.target_scores[4]:
            for i in All_groups:
                i.kill()
                SCREEN.fill(WHITE)
                SCREEN.blit(clear1, (390, 200))
                SCREEN.blit(clear2, (460, 300))
                SCREEN.blit(thanks, (470, 600))
                SCREEN.blit(creator, (450, 700))
                time.sleep(1) #1초 정지후
                pygame.display.update()
                time.sleep(3)
                terminateGame()

        pygame.display.update()
        FPSCLOCK.tick(FPS)


if __name__=="__main__":
    main()
