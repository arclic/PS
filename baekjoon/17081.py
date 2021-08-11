import sys, math

class Creature:
    def __init__(self, maxHp, attack, defense):
        self.maxHp = maxHp
        self.hp = maxHp
        self.attack = attack
        self.defense = defense
        
    # 죽었는지 확인
    def isDead(self):
        if self.hp > 0:
            return False
        
        else:
            self.hp = 0
            return True
        
    # 공격을 맞았을 때
    def hit(self, attackDamage):
        self.hp -= max(1, (attackDamage - self.getDefense()))
        
class Character(Creature):

    def __init__(self, maxHp, attack, defense):
        super().__init__(maxHp, attack, defense)
        self.lv = 1
        self.exp = 0
        
        # 위치
        self.x = 0
        self.y = 0
        
        # 시작위치
        self.startX = None
        self.startY = None
        
        # 무기, 방어구, 장신구
        self.weapon = 0
        self.armor = 0
        self.accessory = []
        
        self.directionDict = {
            "U" : (-1, 0),
            "D" : (1, 0),
            "R" : (0, 1),
            "L" : (0, -1)
        }
    
    # defense를 가져옴
    def getDefense(self):
        if self.armor:
            return self.defense + self.armor
        else:
            return self.defense
        
    # accessory를 가지고 있는지 확인
    def hasItem(self, item):
        return item in self.accessory
    
    # Character의 시작 위치설정
    def setStartPosition(self, x, y):
        self.startX = x
        self.startY = y
    
    # Character의 위치 설정
    def setPosition(self, x, y):
        self.x = x
        self.y = y
    
    # Character의 위치 정보 얻기
    def getPosition(self):
        return [self.x, self.y]
        
    # 부활가능하면 부활
    def survive(self):
        # 부활 가능한 경우
        if self.hasItem("RE"):
            self.accessory.remove("RE")
            self.hp = self.maxHp
            self.x = self.startX
            self.y = self.startY
            
            return True
        
        else:
            return False
        
    # 이동
    def move(self, direction, GRID, N, M):
        moveX = self.x + self.directionDict[direction][0]
        moveY = self.y + self.directionDict[direction][1]
        
        # 움직일 수 없는 명령
        if moveX < 0 or moveY < 0 or moveX >= N or moveY >= M or GRID[moveX][moveY] == "#":
            return self.x, self.y
        
        # 움직일 수 있을 경우 움직임
        self.setPosition(moveX, moveY)
        return moveX, moveY
    
    # 상자를 얻은 경우
    def getItemBox(self, itemBox):
        itemType, itemValue = itemBox.get()
        
        # 무기인경우
        if itemType == "W":
            self.weapon = int(itemValue)
        
        elif itemType == "A":
            self.armor = int(itemValue)
        
        # 장신구인 경우
        else:
            if len(self.accessory) < 4 and itemValue not in self.accessory:
                self.accessory.append(itemValue)
                
    # 가시 함정을 만난경우
    def thorn(self):
        # "Dexterity" 장비가 있는경우 1의 고정피해
        if self.hasItem("DX"):
            self.hp -= 1
        
        # 아닌경우 5의 피해
        else:
            self.hp -= 5
            
        return self.isDead()
    
    # 몬스터를 공격
    def hitMonster(self, monster, turn, monsterType):
        multiple = 1
        if turn == 1 and self.hasItem("CO"):
            if self.hasItem("DX"):
                multiple = 3
            else:
                multiple = 2
                
        # Boss 몬스터고, HU가 있을 때
        if turn == 1 and monsterType == "M" and self.hasItem("HU"):
            self.hp = self.maxHp
        
        if self.weapon:
            attackDamage = (self.attack + self.weapon) * multiple
        
        else:
            attackDamage = self.attack * multiple
        
        monster.hit(attackDamage)
        return monster.isDead()

    # RE 아이템 효과
    def regeneration(self):
        self.hp = self.maxHp if (self.hp + 3) >= self.maxHp else self.hp + 3
    
    # 경험치를 획득
    def getExp(self, exp):
        if self.hasItem("EX"):
            self.exp += math.floor(exp*1.2)
        else:
            self.exp += exp
        
        # 레벨업 조건
        if self.exp >= 5 * self.lv:
            self.lv += 1
            self.exp = 0
            
            self.maxHp += 5
            self.hp = self.maxHp
            self.attack += 2
            self.defense += 2
            
    # 결과를 출력
    def printResult(self):
        print("LV : %s" % self.lv)
        print("HP : %s/%s" % (self.hp, self.maxHp))
        print("ATT : %s+%s" % (self.attack, self.weapon))
        print("DEF : %s+%s" % (self.defense, self.armor))
        print("EXP : %s/%s" % (self.exp, self.lv * 5))
    
class Monster(Creature):
    def __init__(self, name, attack, defense, maxHp, exp):
        super().__init__(maxHp, attack, defense)
        self.name = name
        
        # 처치시 획득가능한 exp
        self.exp = exp
    
    # 이름을 가져옴
    def getName(self):
        return self.name
    
    # defense를 가져옴
    def getDefense(self):
        return self.defense
    
    # 사람을 공격
    def hitCharacter(self, character, turn, monsterType):
        if turn == 1 and monsterType == "M" and character.hasItem("HU"):
            pass
        else:
            character.hit(self.attack)
        return character.isDead()
    
    # 체력 회목
    def cureHp(self):
        self.hp = self.maxHp
        
    # 경험치
    def giveExp(self):
        return self.exp

class ItemBox:
    def __init__(self, itemType, itemValue):
        self.itemType = itemType
        self.itemValue = itemValue
    
    def get(self):
        return [self.itemType, self.itemValue]

    
# 그리드
GRID = []

# 움직임
directions = []

# 몬스터와 박스의 위치를 알려주는 dictionary
monsterDict = {}
itemBoxDict = {}

# 그리드 크기 N, M
N, M = list(map(int, sys.stdin.readline().strip().split()))

# 몬스터 수, 아이템 상자 수
K, B = 0, 0

# Character object 생성
character = Character(20, 2, 2)


for i in range(N):
    inputGrid = [ x for x in sys.stdin.readline().strip()]
    GRID.append(inputGrid)
    
    K += inputGrid.count('&')
    K += inputGrid.count('M') # 보스몬스터
    B += inputGrid.count('B')
    
    if "@" in inputGrid:
        character.setPosition(i, inputGrid.index("@"))
        # Character의 위치를 저장하는 변수
        curX, curY = i, inputGrid.index("@")
        character.setStartPosition(curX, curY)
        GRID[curX][curY] = "."
        
        
directions = sys.stdin.readline().strip()

for _ in range(K):
    R, C, S, W, A, H, E = sys.stdin.readline().strip().split()
    monsterDict[(int(R) - 1, int(C) - 1)] = Monster(S, int(W), int(A), int(H), int(E))
    
for _ in range(B):
    R, C, T, S = sys.stdin.readline().strip().split()
    itemBoxDict[(int(R) - 1, int(C) - 1)] = ItemBox(T, S)

# 진행한 턴수
T = 1
status = ""
deadReason = ""
    
for direction in directions:
    curX, curY = character.move(direction, GRID, N, M) # 이동한 위치
    
    # 아이템 상자를 만난경우
    if GRID[curX][curY] == "B":
        character.getItemBox(itemBoxDict[(curX, curY)])
        GRID[curX][curY] = "."
    
    # 가시를 만난경우
    elif GRID[curX][curY] == "^":
        dead = character.thorn()
        
        if dead:
            # GAME OVER
            if not character.survive():
                status = "dead"
                deadReason = "SPIKE TRAP"
                break
    
    # 몬스터를 만난경우
    elif GRID[curX][curY] == "&" or GRID[curX][curY] == "M":
        # 전투의 턴
        turn = 1
        monster = monsterDict[(curX, curY)]
        while True:
            # 주인공이 몬스터 공격
            if character.hitMonster(monster, turn, GRID[curX][curY]):
                character.getExp(monster.giveExp())
                if character.hasItem("HR"):
                    character.regeneration()
                if GRID[curX][curY] == "M":
                    status = "win"
                
                GRID[curX][curY] = "."
                break
            
            # 몬스터가 주인공 공격
            if monster.hitCharacter(character, turn, GRID[curX][curY]):
                # GAME OVER
                if not character.survive():
                    status = "dead"
                    deadReason = monster.getName()
                
                # 유저가 살아나면서 monster도 체력회복
                else:
                    monster.cureHp()
                    
                break
            
            turn += 1
            
        if status:
            break
    T += 1
    
if status != "dead":
    GRID[curX][curY] = "@"

if not status:
    T -= 1
    
for i in range(N):
    print("".join(GRID[i]))
print("Passed Turns : %d" % T)
character.printResult()
if status == "win":
    print("YOU WIN!")
    
elif status == "dead":
    print("YOU HAVE BEEN KILLED BY %s.." % deadReason)
    
else:
    print("Press any key to continue.")
