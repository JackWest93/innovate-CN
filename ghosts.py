print("How many ghosts from the original ghostbusters movie can you name?\nYou have 3 lives...\n")

ghosts=["SLIMER", "GOZER", "ZUUL", "STAY-PUFT", "VINZ", "THE GREY LADY", "IVO SHANDOR", "DREAM GHOST"]
points = 0

def chars():
    global ghosts
    global points
    lives = 3
    answers = 8
    while lives>0 and answers>0:
        ans=input("Answer: ")
        if ans.capitalize in ghosts:
            points += 1
            answers -= 1
            ghosts.remove(ans)
        else:
            lives -= 1
    if lives == 0:
        print(f"Unlucky, you ran out of lives!\nYou scored {points} points")
    elif answers == 0:
        print("Congratulations, you got them all!\nYou scored 8 points!")


chars()