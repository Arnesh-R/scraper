import player1
import player2
import pandas as pd
#Main


display = pd.options.display
display.max_columns = 1000
display.max_rows = 1000
display.max_colwidth = 9
display.width = 250
format=input('''Enter format: 
         - Test
         - ODI
         - T20
         - All formats 
            ''').lower()
    

role=input('''Enter role:
       - Batting
       - Bowling
       - Allround  
       - Fielding
       ''').lower()

qparams={'class' : '1',
    'type' : 'allround'}
if format=="test":
    qparams['class']='1'
elif format=="odi":
    qparams['class']='2'
elif format=="t20":
    qparams['class']='3'
if role=='batting':
    qparams['type']='batting'
elif role=='bowling':
    qparams['type']='bowling'
elif role=='allround':
    qparams['type']='allround'
elif role=='fielding':
    qparams['type']='fielding'
    
    
pid=(int(input("Enter player id")))
sp=int(input('''Select:
         1. Quick search
         2. Full search 
         (Enter 1 or 2)'''))
if role=='batting':
    sq=int(input('''Select option:
             1. All stats
             2. Innings by innings list
             3. Match by match list
             4. Cumulative averages
             5. Series averages
             6. Ground averages
             7. Partnership summary
             8. List of partnerships
             9. Dismissal summary
             10. Bowler summary
             11. Fielder summary    
             12. List of dismissals    
             '''))
elif role=='bowling':
    sq=int(input('''Select option:
             1. All stats
             2. Innings by innings list
             3. Match by match list
             4. Cumulative averages
             5. Series averages
             6. Ground averages
             7. Wickets summary
             8. Batter summary
             9. Fielder summary    
             10. List of wickets    
             '''))
elif role=='allround':
    sq=int(input('''Select option:
             1. All stats
             2. Innings by innings list
             3. Match by match list
             4. Cumulative averages
             5. Series averages
             6. Ground averages
             7. Match results
             8. Match awards
             9. Series awards  
             '''))
elif role=='fielding':
    sq=int(input('''Select option:
             1. All stats
             2. Innings by innings list
             3. Match by match list
             4. Cumulative averages
             5. Series averages
             6. Ground averages
             7. Dismissal summary
             8. Batter dismissed
             9. Bowler summary    
             10. List of dismissals    
             '''))
    
if sp==1:
    p=player1.Player1(pid)
    if role=="batting":
        if sq==1:
            cricdata=player1.Player1.totalstats(p,qparams)
        elif sq==2:
            cricdata=player1.Player1.innlist(p,qparams)
        elif sq==3:
            cricdata=player1.Player1.matchlist(p,qparams)
        elif sq==4:
            cricdata=player1.Player1.cavg(p,qparams)
        elif sq==5:
            cricdata=player1.Player1.savg(p,qparams)
        elif sq==6:
            cricdata=player1.Player1.gavg(p,qparams)
        elif sq==7:
            cricdata=player1.Player1.pship_total(p,qparams)
        elif sq==8:
            cricdata=player1.Player1.pship_list(p,qparams)
        elif sq==9:
            cricdata=player1.Player1.dis_total(p,qparams)
        elif sq==10:
            cricdata=player1.Player1.bow_total(p,qparams)
        elif sq==11:
            cricdata=player1.Player1.fl_total(p,qparams)
        elif sq==12:
            cricdata=player1.Player1.dis_list(p,qparams)
    elif role=="bowling":
        if sq==1:
            cricdata=player1.Player1.totalstats(p,qparams)
        elif sq==2:
            cricdata=player1.Player1.innlist(p,qparams)
        elif sq==3:
            cricdata=player1.Player1.matchlist(p,qparams)
        elif sq==4:
            cricdata=player1.Player1.cavg(p,qparams)
        elif sq==5:
            cricdata=player1.Player1.savg(p,qparams)
        elif sq==6:
            cricdata=player1.Player1.gavg(p,qparams)
        elif sq==7:
            cricdata=player1.Player1.dis_sum(p,qparams)
        elif sq==8:
            cricdata=player1.Player1.b_sum(p,qparams)
        elif sq==9:
            cricdata=player1.Player1.f_sum(p,qparams)
        elif sq==10:
            cricdata=player1.Player1.wlist(p,qparams)
    elif role=="allround":
        if sq==1:
            cricdata=player1.Player1.totalstats(p,qparams)
        elif sq==2:
            cricdata=player1.Player1.innlist(p,qparams)
        elif sq==3:
            cricdata=player1.Player1.matchlist(p,qparams)
        elif sq==4:
            cricdata=player1.Player1.cavg(p,qparams)
        elif sq==5:
            cricdata=player1.Player1.savg(p,qparams)
        elif sq==6:
            cricdata=player1.Player1.gavg(p,qparams)
        elif sq==7:
            cricdata=player1.Player1.results(p,qparams)
        elif sq==8:
            cricdata=player1.Player1.maw(p,qparams)
        elif sq==9:
            cricdata=player1.Player1.saw(p,qparams)
    elif role=="fielding":
        if sq==1:
            cricdata=player1.Player1.totalstats(p,qparams)
        elif sq==2:
            cricdata=player1.Player1.innlist(p,qparams)
        elif sq==3:
            cricdata=player1.Player1.matchlist(p,qparams)
        elif sq==4:
            cricdata=player1.Player1.cavg(p,qparams)
        elif sq==5:
            cricdata=player1.Player1.savg(p,qparams)
        elif sq==6:
            cricdata=player1.Player1.gavg(p,qparams)
        elif sq==7:
            cricdata=player1.Player1.fdis_sum(p,qparams)
        elif sq==8:
            cricdata=player1.Player1.fdis_bat(p,qparams)
        elif sq==9:
            cricdata=player1.Player1.fdis_bow(p,qparams)
        elif sq==10:
            cricdata=player1.Player1.fdis_list(p,qparams)
    print(cricdata)
elif sp==2:
    p=player2.Player2(pid)
    if role=="batting":
        if sq==1:
            cricdata=player2.Player2.totalstats(p,qparams)
        elif sq==2:
            cricdata=player2.Player2.innlist(p,qparams)
        elif sq==3:
            cricdata=player2.Player2.matchlist(p,qparams)
        elif sq==4:
            cricdata=player2.Player2.cavg(p,qparams)
        elif sq==5:
            cricdata=player2.Player2.savg(p,qparams)
        elif sq==6:
            cricdata=player2.Player2.gavg(p,qparams)
        elif sq==7:
            cricdata=player2.Player2.pship_total(p,qparams)
        elif sq==8:
            cricdata=player2.Player2.pship_list(p,qparams)
        elif sq==9:
            cricdata=player2.Player2.dis_total(p,qparams)
        elif sq==10:
            cricdata=player2.Player2.bow_total(p,qparams)
        elif sq==11:
            cricdata=player2.Player2.fl_total(p,qparams)
        elif sq==12:
            cricdata=player2.Player2.dis_list(p,qparams)
    elif role=="bowling":
        if sq==1:
            cricdata=player2.Player2.totalstats(p,qparams)
        elif sq==2:
            cricdata=player2.Player2.innlist(p,qparams)
        elif sq==3:
            cricdata=player2.Player2.matchlist(p,qparams)
        elif sq==4:
            cricdata=player2.Player2.cavg(p,qparams)
        elif sq==5:
            cricdata=player2.Player2.savg(p,qparams)
        elif sq==6:
            cricdata=player2.Player2.gavg(p,qparams)
        elif sq==7:
            cricdata=player2.Player2.dis_sum(p,qparams)
        elif sq==8:
            cricdata=player2.Player2.b_sum(p,qparams)
        elif sq==9:
            cricdata=player2.Player2.f_sum(p,qparams)
        elif sq==10:
            cricdata=player2.Player2.wlist(p,qparams)
    elif role=="allround":
        if sq==1:
            cricdata=player2.Player2.totalstats(p,qparams)
        elif sq==2:
            cricdata=player2.Player2.innlist(p,qparams)
        elif sq==3:
            cricdata=player2.Player2.matchlist(p,qparams)
        elif sq==4:
            cricdata=player2.Player2.cavg(p,qparams)
        elif sq==5:
            cricdata=player2.Player2.savg(p,qparams)
        elif sq==6:
            cricdata=player2.Player2.gavg(p,qparams)
        elif sq==7:
            cricdata=player2.Player2.results(p,qparams)
        elif sq==8:
            cricdata=player2.Player2.maw(p,qparams)
        elif sq==9:
            cricdata=player2.Player2.saw(p,qparams)
    elif role=="fielding":
        if sq==1:
            cricdata=player2.Player2.totalstats(p,qparams)
        elif sq==2:
            cricdata=player2.Player2.innlist(p,qparams)
        elif sq==3:
            cricdata=player2.Player2.matchlist(p,qparams)
        elif sq==4:
            cricdata=player2.Player2.cavg(p,qparams)
        elif sq==5:
            cricdata=player2.Player2.savg(p,qparams)
        elif sq==6:
            cricdata=player2.Player2.gavg(p,qparams)
        elif sq==7:
            cricdata=player2.Player2.fdis_sum(p,qparams)
        elif sq==8:
            cricdata=player2.Player2.fdis_bat(p,qparams)
        elif sq==9:
            cricdata=player2.Player2.fdis_bow(p,qparams)
        elif sq==10:
            cricdata=player2.Player2.fdis_list(p,qparams)
    try:
        print(cricdata)
    except:
        print("Input error")
else:
    print("Input error")
    
