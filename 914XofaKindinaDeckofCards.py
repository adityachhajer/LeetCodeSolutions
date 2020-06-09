deck =[1,1,1,1,2,2,2,2,2,2]
d=0
for i in set(deck):
    if deck.count(i)>=2:
        if(d==0):
            d=deck.count(i)
        else:
            if (deck.count(i)==d) or (deck.count(i)%d==0)or((d%deck.count(i)==0)):
                continue
            else:
                print("False")
                break
    else:
        print("False")
        break
