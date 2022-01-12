import random

KK_Teams=['Thomastown', 'Young Irelands', 'Fenians', 'O Loughlin Gales', 'Mooncoin', 'Rower Inistioge', 'Conahy Shamrocks', 'St Lachtains', 'Tullogher Rosbercon', 'Dunnamaggin', 'Carrickshock', 'St Martins']
KK_Teams.sort()

def championship_draw():
    print ("The 2022 Intermediate teams are", KK_Teams)
    random.shuffle(KK_Teams)
    

    print('\nFirst round games \n')       
    Relegation_1= ((KK_Teams[0:2]))
    print ('Relegation 1',Relegation_1)
    Relegation_2= ((KK_Teams[2:4]))
    print ('Relegation 2',Relegation_2)
    Match_3=((KK_Teams[4:6]))
    print ('Match 3',Match_3)
    Match_4= (KK_Teams[6:8])
    print ('Match 4',(Match_4))
    Byes= ((KK_Teams[8:]))
    print ('First round byes: ', Byes)
    
    
    print('\nFirst round Winners \n')
    Winner_game_1 = (KK_Teams[0])
    print (Winner_game_1)
    Winner_game_2 = (KK_Teams[3])
    print (Winner_game_2)
    Winner_game_3 = random.choice(KK_Teams[4:6])
    print (Winner_game_3)
    Winner_game_4 = random.choice(KK_Teams[6:8])
    print (Winner_game_4)
    
    print('\nQuarter final games \n')
    Quarter_final_1 = [KK_Teams[8],Winner_game_1]
    print (Quarter_final_1)
    Quarter_final_2 = [KK_Teams[9],Winner_game_2]
    print (Quarter_final_2)
    Quarter_final_3 = [KK_Teams[10],Winner_game_3]
    print (Quarter_final_3)
    Quarter_final_4 = [KK_Teams[11],Winner_game_4]
    print (Quarter_final_4)
    
    print('\nQuarter final winners \n')
    QF_Winner_1 = (random.choice(Quarter_final_1))
    print (QF_Winner_1)
    QF_Winner_2 = (random.choice(Quarter_final_2))
    print (QF_Winner_2)
    QF_Winner_3 = (random.choice(Quarter_final_3))
    print (QF_Winner_3)
    QF_Winner_4 = (random.choice(Quarter_final_4))
    print (QF_Winner_4)
    
    print('\nSemi final games \n')
    Semi_final_1 = [QF_Winner_1,QF_Winner_2]
    print (Semi_final_1 )
    Semi_final_2 = [QF_Winner_3,QF_Winner_4]
    print (Semi_final_2 )
    
    print('\nSemi final winners \n')
    SF_Winner_1 = (random.choice(Semi_final_1))
    print (SF_Winner_1)
    SF_Winner_2 = (random.choice(Semi_final_2))
    print (SF_Winner_2)
    
    print('\nCounty Finalists \n')
    Final= [SF_Winner_1,SF_Winner_2]
    print (Final)
    
    print('\nRelagation Final \n')
    Relagation_Final= [KK_Teams[1:3]]
    print (Relagation_Final)
    Relagation_loser = (random.choice(KK_Teams[1:3]))
    print ('\nTeam relagated in 2022:', Relagation_loser)
    
    
    print('\n2022 Kilkenny Intermediate Champions \n')
    Final_Winner = (random.choice(Final))
    print (Final_Winner)
    
    
championship_draw()