#Eound 1
import gc
def OpCode(lis):
    pos = 0
    while pos < len(lis):
        try:
            pos1 = lis[pos + 1]
            pos2 = lis[pos + 2]
            pos3 = lis[pos + 3]
        except:
            break
        if lis[pos] == 1:
            lis[pos3]=lis[pos1]+lis[pos2]
            pos += 4
        elif lis[pos] == 2:
            lis[pos3]=lis[pos1]*lis[pos2]
            pos += 4
        else:
            pos = len(lis)+100
    return lis
testy = [1,1,1,4,99,5,6,0,99]

#print(OpCode(listy))
#Eound 2

for noun in range(100):
    for verb in range(100):
        listy=[1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,9,1,19,1,19,5,23,1,23,6,27,2,9,27,31,1,5,31,35,1,35,10,39,1,39,10,43,2,43,9,47,1,6,47,51,2,51,6,55,1,5,55,59,2,59,10,63,1,9,63,67,1,9,67,71,2,71,6,75,1,5,75,79,1,5,79,83,1,9,83,87,2,87,10,91,2,10,91,95,1,95,9,99,2,99,9,103,2,10,103,107,2,9,107,111,1,111,5,115,1,115,2,119,1,119,6,0,99,2,0,14,0]
        listy[1] = noun
        listy[2] = verb
        if OpCode(listy)[0] == 19690720:
            print(noun, verb)
