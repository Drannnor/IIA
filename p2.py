from peoesN import *

def outro_player(p) :
            return 'brancas' if p == 'pretas' else 'pretas'

def F1(state,player):
            return len(state[2][1][player]) - len(state[2][1][outro_player(player)])

def F2(state,player)
sum = 0
            for (x,y) in state[2][1][player]
                        sum = sum + y - 2 
st = input()
if st.isdigit():
            print (F1(teste(int(st)),input()))
else:
           print (F1(eval(st),input()))  
