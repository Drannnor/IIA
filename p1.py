from peoesN import *

def outro_player(p) :
            return 'brancas' if p == 'pretas' else 'pretas'

def F1(state,player):
            return len(state[2][1][player]) - len(state[2][1][outro_player(player)])


st = input()
if st.isdigit():
            print (F1(teste(int(st)),input()))
else:
           print (F1(eval(st),input()))  
