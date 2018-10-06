#TicTacToe with minimax
player='x'
opponent='o'
def movesLeft(m):
    for i in range(9):
        if m[i]=='-':
            return True
    return False

def evalFunction(m):
    
    #checking row for victory of o or x
    i=0
    while i<=6:
        if m[i]==m[i+1] and m[i+1]==m[i+2]:
            if m[i]=='x':
                return 10
            elif m[i]=='o': 
                return -10
              
        i=i+3
    
     #checking column for victory of o or x
    for i in range(3): 
        if m[i]==m[i+3] and m[i+3]==m[i+6]:
            if m[i]=='x':
                return 10
            elif m[i]=='o': 
                return -10
              
     #checking diagonal for victory of o or x
    if m[0]==m[4] and m[4]==m[8]:
            if m[0]=='x':
                return 10
            elif m[0]=='o':
                return -10
              
    if m[2]==m[4] and m[4]==m[6]:
            if m[0]=='x':
                return 10
            elif m[0]=='o':  
                return -10
    #no one wins
    return 0

def minimax(m,depth,ismax):
    ej=evalFunction(m)
    #max wins
    if ej==10:
        return ej
    #min wins
    if ej==-10:
        return ej
    #no block left to move or draw
    if movesLeft(m)==False:
        return 0
    #if it is max's move
    if ismax==True:
        best=-1000
        for i in range(9):
            if m[i]=='-':
                m[i]=player
                best=max(best,minimax(m,depth+1,not ismax))
                #undo move
                m[i]='-'
                
        return best
    else:
        best=1000
        for i in range(9):
            if m[i]=='-':
                m[i]=opponent
                best=min(best,minimax(m,depth+1,not ismax))
                #undo move
                m[i]='-'
        return best
def findBestmove(m):
    bestval=-1000
    p=-1
    for i in range(9):
        if m[i]=='-':
            m[i]=player
            curmove=minimax(m,0,False)
            #undo move
            m[i]='-'
            if curmove>bestval:
                p=i
                bestval=curmove
                
    return p

    
def printmat(m):
    i=0
    while i<=6:
        print (m[i]+''+m[i+1]+''+m[i+2])
        i=i+3
    return
    
        
#driving example
m=["-","-","-","-","-","-","-","-","-"]
print ("make a move")
n = int(input())
m[n]=opponent
turn=1
while turn<=9:
    print ("after opponents turn")
    printmat(m)
    best=findBestmove(m)
    print ("best move is at position"+str(best)+"of the column major")
    m[best]=player
    print ("after players turn")
    printmat(m)
    turn=turn+1
    if turn==9:
        print ("draw")
        break
    print ("make a move")
    n = int(input())
    m[n]=opponent
    turn=turn+1
    if turn==9:
        print ("draw")
        break
