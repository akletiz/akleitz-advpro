llist = []
ssorted = []


def main():
    while len(llist) > 0:
        x = findmin(llist)
        y = llist.pop(x)
        ssorted.append(y)
        print ssorted

def findmin(llist):
    minimum = llist(0)
    iindex = 0
    for i in range(len(llist)):
        if llist[i] < minimum:
            minimum = llist[i]
            iindex = i
    return iindex

main()
