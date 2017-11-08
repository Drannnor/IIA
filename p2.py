from peoesN import *

def outro_player(p) :
            return 'brancas' if p == 'pretas' else 'pretas'

def F1(state,player):
            return len(state[2][1][player]) - len(state[2][1][outro_player(player)])

def F2(state,player):

           distsPl = [pc[1] for pc in state[2][1][player]]
           distsAd = [pc[1] for pc in state[2][1][outro_player(player)]]
           print (distsAd)
           print(distsPl)
           if(player == 'brancas'):
                        f2Pl =  sum(map(lambda x: 2**(x - 2),distsPl)) / len( state[2][1][player])
                        f2Ad = sum(map(lambda x: 2**(7 - x),distsAd)) / len( state[2][1][player])
           else:
                        f2Pl = sum(map(lambda x: 2**(7 - x),distsPl)) / len( state[2][1][player])
                        f2Ad =  sum(map(lambda x: 2**(x - 2),distsAd)) / len( state[2][1][player])


           print (f2Pl)
           print (f2Ad)
           return f2Pl - f2Ad



st = input()
if st.isdigit():
            print (F2(teste(int(st)),input()))
else:
           print (F2(eval(st),input()))  
