def main():
    status=["0","1","2","3","4","5","6","7","8",0]
    turn=True
    game=True
    position=9
    while(game):
        print("")
        display(status)
        print("")
        if(turn):
            position=eval(input("Enter position for X: "))
            status[position]="X"
            turn=False
        else:
            position=eval(input("Enter position for O: "))
            status[position]="O"
            turn=True
        status[9]=status[9]+1
        game=check(status)

def display(status):
    for i in range(3):
        for j in range(3):
            print(status[(i*3)+j],end="    ")
        print("")

def check(status):
    if(status[0]==status[1]==status[2]):
        display(status)
        print("Game won by "+status[0])
        return False
    elif(status[3]==status[4]==status[5]):
        display(status)
        print("Game won by "+status[3])
        return False
    elif(status[6]==status[7]==status[8]):
        display(status)
        print("Game won by "+status[6])
        return False
    elif(status[0]==status[3]==status[6]):
        display(status)
        print("Game won by "+status[0])
        return False
    elif(status[1]==status[4]==status[7]):
        display(status)
        print("Game won by "+status[1])
        return False
    elif(status[2]==status[5]==status[8]):
        display(status)
        print("Game won by "+status[2])
        return False
    elif(status[0]==status[4]==status[8]):
        display(status)
        print("Game won by "+status[0])
        return False
    elif(status[2]==status[4]==status[6]):
        display(status)
        print("Game won by "+status[2])
        return False
    elif(status[9]==9):
        display(status)
        print("Game Drawn.")
        return False
    else:
        return True

main()
