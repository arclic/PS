import sys, math

class Party:
    def __init__(self, inputData):
        self.name = inputData[0]
        self.chairs = int(inputData[1])
        self.votes = int(inputData[2])
        self.pi = 0
        self.si = 0
        self.ti = 0 
        self.valid = True   

    def isValid(self):
        return self.valid

    def setValid(self, valid):
        self.valid = valid

    def getVotes(self):
        return self.votes
    
    def getChairs(self):
        return self.chairs

    def setPi(self, pi):
        self.pi = pi

    def getPi(self):
        return self.pi

    def setSi(self, si):
        self.si = si

    def getSi(self):
        return self.si

    def setTi(self, ti):
        self.ti = ti

    def getTi(self):
        return self.ti

# 국회의원 정수
N = 300

# P: 정당수, V: 투표자
P, V = list(map(int, sys.stdin.readline().strip().split()))

# 정당들
parties = []

# 전체 투표수
totalValidVotes = 0

for i in range(P):
    parties.append(Party(sys.stdin.readline().strip().split()))
    totalValidVotes += parties[-1].getVotes()

# 의석할당정당의 전체 투표수
allocateVotes = 0
# 의석할당정당의 전체 의석수
allocateChairs = 0

# 의석할당정당인지 check
for party in parties:
    if (party.getVotes() / totalValidVotes) >= 0.03 or party.getChairs() >= 5:
        allocateVotes += party.getVotes()
        allocateChairs += party.getChairs()
        party.setValid(True)

    else:
        party.setValid(False)
    

# 1단게 수행
R = 253 - allocateChairs
totalSi = 0

for party in parties:
    if party.isValid():
        pi = (party.getVotes()/allocateVotes)
        si = ((N-R)*pi - party.getChairs())/2
        
        si = 0 if si < 1 else si 

        if si - math.floor(si) == 0.5:
            si += 0.1
        
        si = round(si)

        party.setPi(pi)
        party.setSi(si)

        totalSi += si
    
# 2 - 1 단계
if totalSi > 30:
    # 나머지 배치할 때 순서 
    order = []
    currentSi = 0

    for idx, party in enumerate(parties):
        if party.isValid():
            si = (30 * party.getSi()) / totalSi
            currentSi += math.floor(si)
            order.append((si-math.floor(si), idx))

            party.setSi(math.floor(si))
    
    order.sort(key=lambda x: x[1])
    order.sort(key=lambda x: x[0], reverse=True)
    cnt = 0

    while currentSi < 30:
        _, index = order[cnt]
        parties[index].setSi(parties[index].getSi() + 1)

        currentSi += 1
        cnt = (cnt + 1) % len(order)

elif totalSi < 30:

    # 나머지 배치할 때 순서 
    order = []
    currentSi = 0

    for idx, party in enumerate(parties):
        if party.isValid():
            si = party.getSi() + (30 - totalSi) * party.getPi()
            currentSi += math.floor(si)
            order.append((si-math.floor(si), idx))

            party.setSi(math.floor(si))
    
    order.sort(key=lambda x: x[1])
    order.sort(key=lambda x: x[0], reverse=True)
    cnt = 0

    while currentSi < 30:
        _, index = order[cnt]
        parties[index].setSi(parties[index].getSi() + 1)

        currentSi += 1
        cnt = (cnt + 1) % len(order)

# 나머지 배치할 때 순서 
order = []
currentTi = 0

for idx, party in enumerate(parties):
    if party.isValid():
        ti = 17 * party.getPi()
        currentTi += math.floor(ti)
        order.append((ti-math.floor(ti), idx))
        
        party.setTi(math.floor(ti))

order.sort(key=lambda x: x[1])
order.sort(key=lambda x: x[0], reverse=True)
cnt = 0

while currentTi < 17:
    _, index = order[cnt]
    parties[index].setTi(parties[index].getTi() + 1)

    currentTi += 1
    cnt = (cnt + 1) % len(order)

result = []

for idx, party in enumerate(parties):
    result.append((party.name, party.getChairs() + party.getSi() + party.getTi()))

result.sort(key=lambda x : x[0])
result.sort(key=lambda x : x[1], reverse=True)

for name, chair in result:
    print(name, chair)
