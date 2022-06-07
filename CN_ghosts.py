print("How many ghosts from the original ghostbusters movie can you name?\nYou have 3 lives...\n")

ghosts=["ANSWER: SLIMER", "GOZER", "ZUUL", "STAY-PUFT", "VINZ", "THE GREY LADY", "IVO SHANDOR", "DREAM GHOST"]
i=0

def chars():
    global ghosts
    global i
    x=3
    y=8
    while x>0 and y>0:
        ans=input("ANSWER: ")
        if ans.capitalize in ghosts:
            i += 1
            y -= 1
            ghosts.remove(ans)
        else:
            x -= 1
    if x == 0:
        print(f"Unlucky, you ran out of lives!\nYou scored {i} points")
    elif y == 0:
        print("Congratulations, you got them all!\nYou scored 8 points!")


chars()