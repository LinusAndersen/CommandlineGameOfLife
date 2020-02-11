import random
board = [(x + 3, 9)for x in range(32)]
while True: #xS = 50, yS = 20, starting points = 250
    print('\n' + '\n'.join([''.join(['*' if (c,r) in board else '.' for c in range( 50 )]) for r in range( 20 )]))
    board = [(x,y) for x in range(50) for y in range(20) if (((sum([(a%50,b%20) in board for a,b in [(x-1,y-1), (x, y-1), (x+1, y-1), (x-1, y), (x+1, y), (x-1, y+1), (x, y+1), (x+1, y+1)]]) in [2,3]) and (x,y) in board) or (sum([(a%50,b%20) in board for a,b in [(x-1,y-1), (x, y-1), (x+1, y-1), (x-1, y), (x+1, y), (x-1, y+1), (x, y+1), (x+1, y+1)]]) in [3] and not (x,y) in board))] #(0-x) + size[0]+






#Programm by LinusAndersen
#random generation: list(set([(random.randint(1, 50 - 1), (random.randint(1, 20 - 1))) for i in range(250)]))
#glider: [(2,1), (3,2), (3,3), (2,3),(1,3)]
# straight: [(x + 3, 9)for x in range(10)] 3=xOffset, y=yOffset, 10=length
