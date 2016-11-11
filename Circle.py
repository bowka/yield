# author Bowka
'''Circle with hot potatoe
    you have just 10 hits until popatoe exlode
    last player who get potatoe wins.

'''
class Player:
    def __init__(self,N,S):
        self.name = N
        self.hit = S
        
    def __repr__(self):
        return 'Player '+repr(self.name)+' : ' + repr(self.hit)
    
class Circle:
    def __init__(self):
        self.game = []
        self.amount = 0
        
    def add(self,N):
        self.game.append(N)
        self.amount+=1

    def __iter__(self):
        for p in self.game:
            yield p 
            

    def __repr__(self):
        res = '--------Level 1---------\n'
        for player in self:
            res += repr(player)+'\n'  
        return res

    def start(self):
        pass
    
    def killPlayer(self,P):
        self.game.remove(P)
        
C = Circle()
C.add(Player('J',3))
C.add(Player('F',6))
C.add(Player('K',4))
C.add(Player('X',1))
C.add(Player('Y',2))

##print(C) # not generator just repr

for player in C:
    print(player)


