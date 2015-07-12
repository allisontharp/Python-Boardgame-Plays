from functs import add_scores, read_cell
from boardgamegeek import BoardGameGeek
from datetime import datetime
from connect import connect


bgg = BoardGameGeek()
al = bgg.plays('mad4hatter')
alplays = al.plays

entry, client, key = connect()

latestgame = read_cell(client,key)

print latestgame


for games in alplays:
    if games.date > latestgame:
            temp = games.players
            troytest = ['yes' for players in temp if players.name == 'Troy']
            
            
            if troytest == ['yes']:
                entry, client, key = connect()
                
                entry.set_value('date',games.date.strftime('%m/%d/%y'))
                entry.set_value('gamename',games.game_name)
                entry.set_value('duration', str(games.duration))
                

                winners = []
                win = '1'
                [winners.append(players.name) for players in games.players if players.win == win]
                winnersfinal = ", ".join(winners)
                entry.set_value('winners', winnersfinal)
                
                tind = [item for item in range(len(games.players)) if games.players[item].name == 'Troy']
                aind = [item for item in range(len(games.players)) if games.players[item].name == 'Allison']
                
                newplayers = ''
                if games.players[tind[0]].new == '1':
                    newplayers += ' troynew'
                if games.players[aind[0]].new == '1':
                    newplayers += ' alnew'
                
                newplayers += games.comment
                entry.set_value('comment', newplayers)
                
                
                if winners != []:
                    winscore = [float(players.score.replace(" ","")) for players in games.players if players.name == winners[0]]
                    
                    tscore = float(games.players[tind[0]].score.replace(" ",""))
                    ascore = float(games.players[aind[0]].score.replace(" ",""))
            

                    tdif = abs(tscore - winscore[0])
                    adif = abs(ascore - winscore[0])
                    
                    if (tdif < adif):
                        entry.set_value('troyvawinner', 'Troy')
                        print 'troy'
                    elif (tdif > adif):
                        entry.set_value('troyvawinner', 'Allison')
                        print 'allison'
                    elif (tdif == adif and tdif == winscore and not(winscore==0)):
                        entry.set_value('troyvawinner','Troy, Allison')
                        print 'both'
                
                for players in games.players:
                    entry.set_value(players.name.replace(' ','').lower(), players.score)
                
                client.add_list_entry(entry, key,'od6')

                
                print "Game added"
            else:
                print "Troy did not play this game with you"
    elif games.date == latestgame:
        print "Games on latest date need to be added"
    else:
        break
    
