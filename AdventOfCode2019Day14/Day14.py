def rec1(baglist,currentbag,bagcount,counter):
    for bag, contain in baglist.items():
        if currentbag in bag:
            print(counter)
            for c in contain:
                if 'ORE' not in c:
                    counter += bagcount * int(c.strip().split()[0])
                    counter = rec1(baglist,c.strip().split()[1],bagcount * int(c.strip().split()[0]),counter)
                else:
                    return counter
    return counter

def Part1():
    f = open("Day14Input.txt","r")
    lines = f.readlines()
    baglist = {}
    counter = 0
    for i in lines:
        baglist[i.split("=>")[1].replace("\n","").strip()] = i.split("=>")[0].split(",")
    print(baglist)
    counter =rec1(baglist,"FUEL",1,counter) 
    print(counter)

Part1()