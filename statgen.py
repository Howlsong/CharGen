import random
def gen_stat():
    xlist =[]
    for b in range(4):
        xlist.append(random.randint(1,6))
    xlist.sort()
    xlist.pop(0)
    return (int(xlist[0])+int(xlist[1])+int(xlist[2]))