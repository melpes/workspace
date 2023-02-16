import numpy as np

M = 10
N = M
BLANK, BLACK, WHITE, BLOCKED = 0, 1, 2, -1
ALPHA, BETA, CHARLIE, DELTA = 4, 3, 2, 1

def test(mapp):
    mapp[[2,4,6,4,5,6,3], [6,5,3,6,7,5,3]] = WHITE
    mapp[[6,4,2,2,2,5,6], [8,6,2,3,6,4,6]] = BLACK
    
    for i in range(mapp.shape[0]):
        for j in range(mapp.shape[1]):
            if mapp[i, j] == BLACK:
                print('°', end=' ')
            elif mapp[i, j] == WHITE:
                print('×', end=' ')
            else:
                print(mapp[i, j], end=' ')
        print()
    print()
    for line, string in line_range(mapp):
        if line.size == 0:
            continue
        for i in line:
            pass

def main():
    mapp = np.zeros((M, N), int)
    test(mapp)
    
    ai(mapp, BLACK)
    ai(mapp, WHITE)
    for line, dir in line_range(mapp):
        #print(line)
        pass

def ai(mapp, color):
    mapp_info = np.zeros((M, N), dtype={"names":('alpha', 'beta', 'charlie', 'delta', 'blocked', 'blanked'), "formats":('i1', 'i1', 'i1', 'i1', bool, 'i1')})
    dtype_names = list(mapp_info.dtype.names)
    for i, (line, dir) in enumerate(line_range(mapp)):
       #print(i)
        i %= M
        if line.size == 0:
            continue
        line_info = explore_line(line, color)
        for j, info in enumerate(line_info):
               if dir == 'x':
                   index = i, j
               elif dir == 'y':
                   index = j, i
               elif dir == 'xy1':
                   index = j, M+j - (i+1)
               elif dir == 'xy2':
                   index = i+j+1, j
               elif dir == '-xy1':
                   index = j, i-j
               elif dir == '-xy2':
                   index = i+1, M - (j+1)
               for dn in dtype_names:
                   mapp_info[index][dn] += info[dn]
       
    for i in range(mapp.shape[0]):
        for j in range(mapp.shape[1]):
            if mapp[i, j] == get_e_color(color):
                print('°', end=' ')
            elif mapp_info[i, j]["blocked"] == True:
                print('B', end=' ')
            elif mapp[i, j] == WHITE:
                print('×', end=' ')
            else:
                print(mapp_info[i, j]["charlie"], end=' ')
        print()
    print(color)
        
        
def explore_line(line, color):
        e_color = get_e_color(color)
        line_info = np.zeros(line.size, dtype={"names":('alpha', 'beta', 'charlie', 'delta', 'blocked', 'blanked'), "formats":('i1', 'i1', 'i1', 'i1', bool, 'i1')})
        line_info_rec = line_info.view(np.recarray)

        print(np.where(line == e_color))
        for idx in np.where(line == e_color)[0]:
            print(idx)
            check_blocked(line, idx, line_info_rec, 1, color)
            check_blocked(line, idx, line_info_rec, -1, color)
        
        set_info(line, line_info_rec, color)
    #	total_info(line_info_rec)
        return line_info
        
def check_out_of_range2(size, idx, k):
        if idx + k < size and idx + k >= 0:
            return False
        else:
            return True
        
def check_blocked(line, idx, line_info_rec, k, color):
    if k >1 or k < -1:
        print(idx, k)
    if idx.size == 0:
        return
    if check_out_of_range2(line.size, idx, k):
        return
    if line[idx + k] == color:
        line_info_rec[idx + k].blocked = True
        k = k+1 if k>0 else k - 1
        check_blocked(line, idx, line_info_rec, k, color)
        
def set_info(line, line_info_rec, color):
    stack = 0
    for i in range(line.size):
        if line[i] == color:
            stack += 1
        #	print(stack)

        elif True in is_blocked(line_info_rec, stack, i):
            for blank in range(2):
                if stack == ALPHA and blank == 1:
                    continue
                idx = check_out_of_range(line.size, i, stack, blank)
                if change_stack(stack) == None:
                    continue
                line_info_rec.field( change_stack(stack))[idx] += 1
                line_info_rec[idx].blocked = True
                line_info_rec[idx].blanked += blank
                #print(line_info_rec[idx], change_stack(stack))
                #print(line_info_rec[idx][change_stack(stack)])
            stack = 0
        else:
            for blank in range(2):
                if stack == ALPHA and blank == 1:
                    continue
                idx = check_out_of_range(line.size, i, stack, blank)
                if change_stack(stack) == None:
                    continue
                #print(stack, idx, line_info_rec[idx][ change_stack(stack)])
                line_info_rec.field(change_stack(stack))[idx] += 1
                line_info_rec[idx].blanked += blank
                #print(line_info_rec)
            stack = 0
                

def change_stack(stack):
    if stack == 4:
        return "alpha"
    elif stack == 3:
        return "beta"
    elif stack == 2:
        return "charlie"
    elif stack == 1:
        return "delta"
    else:
        return None

def check_out_of_range(size, i, stack, blank=0):
    output = []
    if i + blank < size:
        output.append(i+blank)
    if i - stack - 1 - blank >= 0:
        output.append(i - stack - 1)
        
    return output

            
def is_blocked(line_info_rec, stack, i):
    return line_info_rec[np.arange(i - stack, i)].blocked
    

def get_e_color(color):
    if color == BLACK:
        return WHITE
    else:
        return BLACK

def line_range(mapp) -> list:
    for v in mapp:
        yield v, 'x'
    
    for v in mapp.T:
        yield v, 'y'

    for i in np.arange(0, M):
        yield mapp[0:1+i, M-1-i:M].diagonal(), 'xy1'
    for i in np.arange(M-2, -1, -1):
        yield mapp.T[0:1+i, M-1-i:M].diagonal(), 'xy2'
    yield np.array([]), ''
        
    for i in np.arange(0, M):
        yield mapp[:,::-1][0:1+i, M-1-i:M].diagonal(), '-xy1'
    for i in np.arange(M-2, -1, -1):
        yield mapp.T[::-1][0:1+i, M-1-i:M].diagonal(), '-xy2'
    yield np.array([]), ''
        
        
main()