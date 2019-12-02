import math
#### ROund 1
##def findFuel(mass):
##    return math.floor(mass/3)-2
##clean = open('day1.txt').read().replace('\n',',')
##list_to_find=clean.split(',')
##total = 0
##for i in list_to_find:
##    i = int(i)
##    total += findFuel(i)
##print(total)

##Round 2
def findFuel(mass):
    return math.floor(mass/3)-2

clean = open('day1.txt').read().replace('\n',',')
list_to_find=clean.split(',')
#list_to_find = [1969]
total = 0
for i in list_to_find:
    p = findFuel(int(i))
    total += p
    if p >= 3:
        while True:
            p = findFuel(p)
            if p > 0:
                total += p
            else:
                break
print(total)
