states = []
states = input()
states = states.split(" ")
states.pop(0)
states.append('s')
symbols = []
symbols = input()
symbols = symbols.split(" ")
symbols.pop(0)

matrix = [['s' for j in range(len(symbols))] for i in range(len(states))]

if input() == "begin_rules":
    while True:
        rule = input()
        if rule != "end_rules":
            r_list =  []
            r_list = rule.split(" ") 
            c_st = r_list[0]
            n_st = r_list[2]
            sy = r_list[4]
            i_st = states.index(c_st)
            i_sy = symbols.index(sy)
            for i in range(len(states)):
                for j in range(len(symbols)):
                    if ((i is i_st) and (j is i_sy)):
                        matrix[i][j] = n_st
        else:
            break

def nextState(c_state, symbol):
    return matrix[states.index(c_state)][symbols.index(symbol)]
 
start = []
start = input()
start = start.split(" ")
start.pop(0)
s_i = states.index(start[0])
start = states[s_i]
final = []
final = input()
final = final.split(" ")
final.pop(0)

try:
    while True:
        start_s = start
        list = []
        check = input()
        for i in check:
            next = nextState(start_s, i)
            list.append(next)
            start_s = next
        if list[-1] in final:
            print('accepted')
        else:
            print('rejected')
except:
    pass

