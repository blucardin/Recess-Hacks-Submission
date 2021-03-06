import math

playersR = open("players.txt", "rt")
scoresR = open("scores.txt", "rt")

listplayers = playersR.read().split(" ")
listsscore = scoresR.read().split(" ")

print(listplayers)
print(listsscore)

playersR.close()
scoresR.close()

def retrivescore(player):
    if player in listplayers: 
        index = listplayers.index(player) 
        return listsscore[index]
    else:
        return "Player not in database"


def add_to_score(player, amount):
    if player in listplayers: 
        index = listplayers.index(player) 
        listsscore[index] = str(int(listsscore[index]) + int(math.floor(amount)))

    else:
        listplayers.append(player)
        listsscore.append(str( int(math.floor(amount))))

    separator = " "
    newscorelist = separator.join(listsscore)
    newplayerlist = separator.join(listplayers)


    playersW = open("players.txt", "wt")
    scoresW = open("scores.txt", "wt")


    playersW.write(newplayerlist)
    scoresW.write(newscorelist)

    playersW.close()
    scoresW.close()


def printrow(index): 
    return listplayers[index] + "    " + listsscore[index]

